 #!/usr/bin/env python

import time, serial, glob, sys, os


def listSerialPorts():
	

	if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this is to exclude your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty[A-Za-z]*')
		print "OS Detected: Linux"

	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')
		print "OS Detected: Darwin"

	elif sys.platform.startswith('win'):
		ports = ['COM' + str(i + 1) for i in range(256)]
		print "OS Detected: Windows"

	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		if "usb" in port:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)
			except (OSError, serial.SerialException):
				print "OSError"
				pass

	print "found ports:", ports, "using port:", result
	return result

class UnknownSerialPortException(Exception):
	pass

def findPort():
	serialPorts = listSerialPorts()
	if len(serialPorts) > 0:
		port = serialPorts[0]
		return port
	return

def readInput(port, deleteData=True):
	if not os.path.exists(port):
		raise UnknownSerialPortException("Port " + port + " does not exist")
	else:
		# configure the serial connections (the parameters differs on the device you are connecting to)
		ser = serial.Serial(
			port=port,
			baudrate=9600,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS
		)


		if ser.isOpen():
			print "Port already open..."
		else:
			print "Opening port..."
			ser.open()


		ser.flush()


		ser.write("r")

		end = time.time() + 2
		print "reading data...."
		
		data = ""
		while time.time() < end:
			while ser.inWaiting():
				addition = ser.read(ser.inWaiting())
				data += addition
				print 'Receieved \t' + str(len(addition)) + " bytes"
				end = time.time() + 2.0
			time.sleep(0.5)
		#print data
		if deleteData:
			print "Erasing data on device..."
			ser.write("d")
			print "Done."

		ser.close()
		return data

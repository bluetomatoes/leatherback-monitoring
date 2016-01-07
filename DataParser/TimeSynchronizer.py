import time, datetime
with open("timetest.txt","r") as f:
	# read a list of lines into data
	data = f.readlines()


seconds = 7776220
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print str(time.strftime('%Y %m months %d days %H:%M:%S', time.gmtime(seconds)))
print "%d days %d:%02d:%02d" % (d, h, m, s)
#newformat = time.format("%Y-%m-%d %H:%M")
# now change the 2nd line, note that you have to add a newline
lastTime = 0
count = 0
for i in data:
	#converts minutes to seconds
	data[count] = str(int(round(int(i),-3)/1000))+"\n"
	if int(i) < lastTime:
		newTime = 1+ lastTime
		
		data[count] = str(newTime) + "\n"
		lastTime = newTime
	else:
		lastTime = int(i)
	count+=1
	

# and write everything back
with open("timetest.txt","w") as f:
	f.writelines(data)
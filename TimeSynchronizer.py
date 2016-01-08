import time, datetime
from datetime import timedelta

with open("timetest.txt","r") as f:
	# read a list of lines into data
	data = f.readlines()



def parseTime(seconds):
	minute, second = divmod(seconds, 60)
	hour, minute = divmod(minute, 60)
	day, hour = divmod(hour, 24)

	month = time.gmtime[1] - seconds 
	return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

print str(time.strftime('%Y %m months %d days %H:%M:%S', time.gmtime()))
print time.gmtime()[0]
#newformat = time.format("%Y-%m-%d %H:%M")
# now change the 2nd line, note that you have to add a newline
lastTime = 0
count = 0
seconds = 0

for i in data:
	#converts minutes to seconds
	if int(i) > 1000:
		i = str(int(i)/1000)
		data[count] = i+"\n"
		if int(i) < lastTime:
			newTime = 1 + lastTime
			
			data[count] = str(newTime) + "\n"
			lastTime = newTime
		else:
			lastTime = int(i)
	count+=1

seconds = timedelta(seconds=int(data[len(data)-1]))
startDate = datetime.datetime.now() - seconds
print startDate
	
# and write everything back
with open("timetest.txt","w") as f:
	f.writelines(data)
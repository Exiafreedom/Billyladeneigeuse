from megapi import *

def read(d):
	print("distance: "+str(d))
	if d > 20:
		bot.motorRun(M1, -100)
		bot.motorRun(M2, -100)
	else:
		bot.motorRun(M1, 200)
		bot.motorRun(M2, -200)
		sleep(1)
		bot.motorRun(M1, -100)
		bot.motorRun(M2, -100)
		sleep(2)
		bot.motorRun(M2, 200)
		bot.motorRun(M1, -200)
		sleep(1)
		bot.motorRun(M1, -100)
	    bot.motorRun(M2, -100)


bot = MegaPi()
bot.start()
while 1:
    bot.ultrasonicSensorRead(4, read)
from megapi import *


def read(d):
    print("Distance:", d)
    if d > 10:
        bot.motorRun(M1, 100)
        bot.motorRun(M2, 100)
    else:
        bot.motorRun(M1, 0)
        bot.motorRun(M2, 0)


bot = MegaPi()
bot.start('/dev/ttyUSB0')

while 1:
    bot.ultrasonicSensorRead(4, read)



#!/usr/bin/env python


file=open("/sys/class/thermal/thermal_zone0/temp")

temp=float(file.read())/1000

file.close()

print"temp:%.1f"%temp
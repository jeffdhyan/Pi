import httplib, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time


file = open("/sys/class/thermal/thermal_zone0/temp") 

 
def doit():
	temp = float(file.read()) / 1000
                 	
	params = urllib.urlencode({'field1':temp,'key':'IJB2LXXDPCNGU1E2'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("192.168.1.70:3000")
	
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print "temp : %.1f" %temp
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"	

file.close() 
print "temp : %.1f" %temp
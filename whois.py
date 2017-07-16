import pythonwhois
import sys
import json

url=sys.argv[1]

rf=open(url, 'r')
d=rf.readline()
data=pythonwhois.get_whois(d)

def data_handler(obj):#this funciton in order to catch timeerror
	if hasattr(obj, 'isoformat'):
		return obj.isoformat()
	else:
		raise TypeError

#data=pythonwhois.get_whois(d)

jsonString=json.dumps(data, default=data_handler)

print jsonString

wf=open(WriteFile, 'w')
wf.write(jsonString)

rf.close()
wf.close()





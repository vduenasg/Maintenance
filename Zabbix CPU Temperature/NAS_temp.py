from gpiozero import CPUTemperature
import requests
import socket
from datetime import datetime

website = "www.ifttt.com"
iftttkey = "puTcw4njSAV1yRYAOyk6poxRwJV3uiyQhbC7SLMLhln"
alarm_high = "RP4_TEMP_HIGH"
alarm_low = "RP4_TEMP_LOW"
temp_high = 50
temp_low = 45
temp = 0


def get_temp():
	cpu = CPUTemperature()
	return (cpu.temperature)


def alarm(event):
	r = requests.post("https://maker.ifttt.com/trigger/" + event + "/with/key/" + iftttkey, params={"value1":"none","value2":"none","value3":"none"})
	return r


def is_connected(hostname):
	try:
		host = socket.gethostbyname(hostname)
		s = socket.create_connection((host, 80), 2)
		s.close()
		return True
	except:
		pass
		return False

now = datetime.now()

temp = get_temp()

print('************************')
print(now.strftime("%H:%M:%S"))
print(temp)

if is_connected(website):

	print('Connected to Internet')

	if temp >= temp_high:
		print('Turning On')
		alarm(alarm_high)

	if temp <= temp_low:
		print('Turning Off')
		alarm(alarm_low)

print('************************')

#!/bin/sh
#IP ZABBIX SERVER
ip_zabbix="172.16.10.22"
#LOCAL HOSTNAME
host_local="Home-NAS"

#GET TEMPERATURE
RPrawtemp=`cat /sys/class/thermal/thermal_zone0/temp`
RPtemp="$((RPrawtemp))"

#SEND TO ZABBIX SERVER
zabbix_sender -z $ip_zabbix -p 10051 -s $host_local -k "rpi.cpuTemperature" -o $RPtemp

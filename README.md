# AmbientWx-Zabbix
Python script to pull Ambient Weather API data into Zabbix. The Python script can be used either as an agent external script or as a just an external check. The template xml will need to be modified once imported if you want to use it as an external check.

# Agent Setup
1. Copy ZabbixWxDist.py to /usr/lib/zabbix/externalscripts on the machine running the Zabbix Agent
1. Create file /etc/zabbix/zabbix_agentd.d/AmbientWx.conf containing the following line.
   1. UserParameter=AmbientTemp.wx[*],/usr/lib/zabbix/externalscripts/ZabbixWxDist.py $1 $2 $3
1. Restart the Zabbix Agent
1. Import AmbientWx_ZabbixTemplate.xml into Zabbix
1. Open Template with in Zabbix, modify the macros to be your own app and api keys.
1. Apply template to host with script installed

## Requirements
* Zabbix Server
* Zabbix Agent
* Ambient Weather API

## Tested With
* Ambient Weather Station 2902a
* Ambient Weather API
* Ubuntu 18.0.4
* Python 3

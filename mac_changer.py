#!/usr/bin/env python

import subprocess

interface="eth0"
mac="00:00:00:00:00:11"

print("[+] Changing MAC address in %s to %s"%(interface,mac))

subprocess.call("ifconfig %s down"%(interface),shell=True)
subprocess.call("ifconfig %s hw ether %s"%(interface,mac),shell=True)
subprocess.call("ifconfig %s up"%(interface),shell=True)

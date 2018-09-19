#!/usr/bin/env python

import subprocess

interface=raw_input("Which interface? >")
mac=raw_input("Insert new MAC >")

print("[+] Changing MAC address in %s to %s"%(interface,mac))

subprocess.call("ifconfig %s down"%(interface),shell=True)
subprocess.call("ifconfig %s hw ether %s"%(interface,mac),shell=True)
subprocess.call("ifconfig %s up"%(interface),shell=True)

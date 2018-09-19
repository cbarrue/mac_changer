#!/usr/bin/env python

import subprocess

interface=raw_input("Which interface? >")
mac=raw_input("Insert new MAC >")

print("[+] Changing MAC address in %s to %s"%(interface,mac))

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])

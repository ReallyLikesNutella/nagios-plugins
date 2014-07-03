#!/usr/bin/env python
#Dan Cottam - 20140702
#Check VNXe for hardware faults
#Requires Navisphere CLI
 
import sys,subprocess
 
cmd = subprocess.Popen("/opt/Navisphere/bin/naviseccli -User <username> -Password <password> -Address <address> -Scope 0 faults -list", shell=True, stdout=subprocess.PIPE)
rawquery = cmd.communicate()[0]
faultsquery = rawquery.strip()
 
if faultsquery == 'The array is operating normally.':
    print  faultsquery
    sys.exit(0)
elif faultsquery != expectedfaultquery:
    print  "Error, query returned: " + faultsquery
    sys.exit(2)
else:
    print "Error code 0 (Something went wrong)"
    sys.exit(3)

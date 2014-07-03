#!/usr/bin/env python
#Dan Cottam - 20140703
#Check VNXe for hardware faults in customer replaceable units
 
import sys,subprocess
 
cmd = subprocess.Popen("/opt/Navisphere/bin/naviseccli -User <username> -Password <password> -Address <address> -Scope 0 getcrus", shell=True, stdout=subprocess.PIPE)
rawquery = cmd.communicate()[0]
nowhitespace = rawquery.replace(' ', '')
crusquery = nowhitespace.rstrip()
 
expectedhardwareresult1 = """DPE9 Bus 0 Enclosure 0
SP A State:                 Present
SP B State:                 Present
Bus 0 Enclosure 0 Fan A0 State: Present
Bus 0 Enclosure 0 Fan A1 State: Present
Bus 0 Enclosure 0 Fan B0 State: Present
Bus 0 Enclosure 0 Fan B1 State: Present
Bus 0 Enclosure 0 Power A State: Present
Bus 0 Enclosure 0 Power B State: Present
Bus 0 Enclosure 0 BBU A State: Present
Bus 0 Enclosure 0 BBU B State: Present
 
DAE5S Bus 0 Enclosure 1
Bus 0 Enclosure 1 Power A State: Present
Bus 0 Enclosure 1 Power B State: Present
Bus 0 Enclosure 1 LCC A State: Present
Bus 0 Enclosure 1 LCC B State: Present
Bus 0 Enclosure 1 LCC A Revision: 1.47
Bus 0 Enclosure 1 LCC B Revision: 1.47
Bus 0 Enclosure 1 LCC A Serial #: JWXEL140501470
Bus 0 Enclosure 1 LCC B Serial #: JWXEL140501545"""
 
expectedhardwareresult = expectedhardwareresult1.replace(' ', '')
 
if crusquery == expectedhardwareresult:
    print "No faults detected:\n" + rawquery.rstrip()
    sys.exit(0)
elif crusquery != expectedhardwareresult:
    print "Error, query returned: " + rawquery.rstrip()
    sys.exit(2)
else:
    print "Error code 0 (Something went wrong)"
    sys.exit(3)

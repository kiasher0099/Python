'''********** Date: 2020.03.18    Author: Ke Wang ***************
*  This script designed for acquiring the status of the device.
*  include: 
*  - WiFi
*  - BT
*  - GPS
*  - Airplane mode
*  - NFC
*  (extra module can be added here if needed)
***************************************************************'''

import subprocess
import os
import time

# Wait-for-devices
os.system('adb wait-for-device')

# Get DUT serial number
output=os.popen('adb devices')
print(output.read())

# Get WiFi status, "1" is on, "0" is off
wifi_stat = os.popen('adb shell settings get global wifi_on')
print(wifi_stat.read())



# ls = subprocess.Popen(["ls","-l"], shell=True, stdout=subprocess.PIPE)
# print (ls.stdout.read())


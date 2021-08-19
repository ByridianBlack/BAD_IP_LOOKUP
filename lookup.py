import sys
import os
import requests
import re
import time

output_file = ""
if len(sys.argv) < 3:
    print("3 Argumnets are required: Ex - python3 lookup.py (IP | inputfile) <email>")
    exit(0)
ARGUMENT = str(sys.argv[1])
EMAIL = str(sys.argv[2])
IP_ADDRESS_SEARCH = re.search("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ARGUMENT)


def check_bad_ip(IP_ADDRESS):
    json_output = requests.get("http://check.getipintel.net/check.php?ip=" + IP_ADDRESS + "&contact=" + str(EMAIL) + "&format=json&flags=b&oflags=c")
    # print("StATUS: " + str(json_output.status_code))
    if json_output.status_code == 429:
        time.sleep(15)
        json_output = requests.get("http://check.getipintel.net/check.php?ip=" + IP_ADDRESS + "&contact=" + str(EMAIL) + "&format=json&flags=b&oflags=c")
    requested_data = json_output.json()

    results = 0.0
    country = ""
    for key, value in requested_data.items():
        if key == "result":
            results = value
        elif key == "Country":
            country = str(value)


    if(float(results) < 0.5):
        if country == "":
            print("IP: " + str(IP_ADDRESS) + " is harmless. Location not known ")
        else:   
            print("IP: " + str(IP_ADDRESS) + " is harmless. Location is: " + str(country))
    else:
        if country == "":
            print("IP: " + str(IP_ADDRESS) + " has been reported as bad. Location not known ")
        else:
            print("IP: " + str(IP_ADDRESS) + " has been reported as bad. Is from " + country)



if IP_ADDRESS_SEARCH:
   check_bad_ip(ARGUMENT)
else:
    if os.path.exists(ARGUMENT):
        if os.path.isfile(ARGUMENT):
            with open(r""+ARGUMENT, "r") as NFILE:
                for line in NFILE.readlines():
                    line = line[:-1]
                    check_bad_ip(line)

                

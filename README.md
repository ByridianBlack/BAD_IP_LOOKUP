# BAD_IP_LOOKUP
This tool looks up IPS supplied to it  either through command line or a file. Lets you know if they have been reported and there known location. Uses the API: https://getipintel.net/free-proxy-vpn-tor-detection-api/


Usage: python3 lookup.py (IP_ADDRESS | LIST_OF_IPS) <email address>
  
This tool as of now will not be sending an emails but that can be an option in the future. The API I am using requires a valid email to be used.
Becaue of the nature of IP reporting false positives may occure. 

Please let me know of any bugs or problems.

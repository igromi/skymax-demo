import os
import json
import requests

os.system("/home/pi/poller/inverter_poller -1 > /home/pi/poller/vars.json")

with open('/home/pi/poller/vars.json') as json_file:
    data_json = json.load(json_file)
    print(data_json['Battery_voltage'])
    
    
   # defining the api-endpoint  
    API_ENDPOINT = "http://66.85.77.14:8080/api/v1/4vS8SuInT0Do49kvmhjL/telemetry"
         
    # data to be sent to api 
    data_request = "{\"Battery_voltage\": "+str(data_json['Battery_voltage'])+"}"
    
    print(data_request)
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data_request) 
      
    # extracting response text  
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url)     

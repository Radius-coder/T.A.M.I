import logging
from tuya_connector import TuyaOpenAPI
import numpy as np

a = np.arange(1, 1000)

ACCESS_ID = 'ytt5fnxnb3vmvxlvd2di'
ACCESS_KEY ='8c908190d8524a30bfaef8f06701d3eb'

ENDPOINT = "https://openapi.tuyaeu.com"
MQ_ENDPOINT = "wss://mqe.tuyaeu.com:8285/"

#turn the light brightness to 400
DEVICE_ID = 'bfc3c03743f5d5300agxew'

colour = ["red", "orange", "pink" "green", "blue", "yellow", "purple", "colour"]
mode = ["rainbow", "normal", "white", "reset", "night"]
brightness = ["brightness", "bright", "brightness up", "brightness down"]
temperature = ["warmth", "temperature", "temp", "cold"]
switch = ["on", "off"]

def Lights(string):
    commands = {'commands': [{'code': 'switch_led', 'value': True}]}
    global a
    global ENDPOINT
    global ACCESS_ID
    global ACCESS_KEY
    global MQ_ENDPOINT
    global DEVICE_ID
    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)	
    openapi.connect()


    response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID))

    response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(DEVICE_ID))
    splitstring = string.split()
    for x in splitstring:
        if x in switch:
            if x == "on":
                #turn light on
                commands = {'commands': [{'code': 'switch_led', 'value': True}]}
                break
            if x == "off":
                #turn light off
                commands = {'commands': [{'code': 'switch_led', 'value': False}]}
                break
            
            else:
                print("Do you want to turn it on or off")
            
        if x in colour:
            for z in splitstring:
                if z == "orange":
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 40, "s": 1000, "v":700}'}]}
                #lightgreen
                #[{"code":"colour_data_v2","value": '{"h": 40, "s": 1000, "v":700}'}]
                #lightblue
                #[{"code":"colour_data_v2","value": '{"h": 140, "s": 1000, "v":700}'}]
                #darkblue
                #[{"code":"colour_data_v2","value": '{"h": 230, "s": 1000, "v":700}'}]
                if z == "pink":
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 290, "s": 1000, "v":700}'}]}
                if z == 'red':
                    print("red")
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 10, "s": 1000, "v":700}'}]}
                if z == 'green':
                    print("green")
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 120, "s": 1000, "v":700}'}]}
                if z == 'blue': 
                    print("b")
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 200, "s": 800, "v":700}'}]}
                if z == 'yellow':
                    print("y")
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 90, "s": 1000, "v":700}'}]}
                if z == 'purple':
                    commands = {'commands':[{"code":"colour_data_v2","value": '{"h": 255, "s": 1000, "v":700}'}]}
                else:
                    print("What colour do you want")
        if x in mode:
            if x == "rainbow":
                commands = {'commands': [{"code":"work_mode","value":"scene"}]}
            if x == "night":
                commands = {'commands': [{"code":"bright_value_v2","value":30}]}
            if x == "normal" or x == "white" or x == "reset":
                #normal mode
                commands = {'commands':[{"code":"work_mode","value":"white"}]}
            else:
                print("what mode do you want to set it to")
        
        if x in brightness:
            for z in splitstring:
                if z in np.array_str(a):
                    z = int(z)
                    commands = {'commands': [{"code":"bright_value_v2","value":z}]}
                    break
                else:
                    print("how bright do you want it")
                    
        if x in temperature:
            for z in splitstring:
                if z in np.array_str(a):
                    z = int(z)
                    commands = {'commands': [{"code":"temp_value_v2","value":z}]}
                    break
                else:
                    print("how warm do u want it")

    request = openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)	
    print(request)
    
    response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))

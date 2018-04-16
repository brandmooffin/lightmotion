import requests
import json

LIFX_TOKEN = '<LIFX API KEY>'

def lambda_handler(event, context):
    if event['request']['intent']['name'] == 'ToggleLightOffIntent':
        lights = json.loads(getLifxLights())
        toggleLifxLights(lights[0]['id'], "off")
        return 'Toggle off'
    if event['request']['intent']['name'] == 'ToggleLightOnIntent':
        lights = json.loads(getLifxLights())
        toggleLifxLights(lights[0]['id'], "on")
        return 'Toggle on'
    return 'Hello from Lambda'
    
    
def getLifxLights():
    url = 'https://api.lifx.com/v1/lights/'
    headers = {
        'Authorization': 'Bearer ' + LIFX_TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.content


def toggleLifxLights(lightId, toggle):
    url = 'https://api.lifx.com/v1/lights/id:'+lightId+'/state'
    data = '{ "power": "'+toggle+'" }'
    headers = {
        'Authorization': 'Bearer ' + LIFX_TOKEN,
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.put(url, data=data, headers=headers)
    return response
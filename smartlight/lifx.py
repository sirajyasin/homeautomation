import requests
import sys

# Syntax
# python lifx.py on 
# python lifx.py off
# python lifx.py on green/red/blue

token = "[REPLCAE_TOKEN_HERE]"
headers = {
    "Authorization": "Bearer %s" % token,
}

state = sys.argv[1]
color = 'green'
if len(sys.argv) > 2:
  color = sys.argv[2]

payload = {
    "power": state,
    "color": color
}

response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


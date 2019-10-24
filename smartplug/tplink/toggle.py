#git clone https://github.com/vrachieru/tplink-smartplug-api.git
#pip3 install ./tplink-smartplug-api
from tplink_smartplug import SmartPlug

plug = SmartPlug('192.168.1.9')

if plug.is_on:
    plug.turn_off()
    print('Plug turned off')
else:
    plug.turn_on()
    print('Plug turned on')

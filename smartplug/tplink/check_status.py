from tplink_smartplug import SmartPlug

plug = SmartPlug('192.168.1.9')

print('Name:      %s' % plug.name)
print('Model:     %s' % plug.model)
print('Mac:       %s' % plug.mac)
print('Time:      %s' % plug.time)

print('Is on:     %s' % plug.is_on)
print('Nightmode: %s' % (not plug.led))
print('RSSI:      %s' % plug.rssi)

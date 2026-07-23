#Smart thermostat alert system

device_status = input('Enter device status')

temprature = float(input('Enter temprature'))



if device_status == 'active':
    if temprature > 35:
        print('High temperature alert!')
    else:
        print('Temprature is normal')
else:
    print('Device is offline')
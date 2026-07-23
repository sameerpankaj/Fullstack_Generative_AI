#ticket info sytem

seat_type = input("select your seat type: 'sleeper/AC/general/luxury' ").lower()

match seat_type:
    case 'sleeper':
        print('Sleeper- No AC, no beds available')
    case 'ac':
        print("AC: Air conditioned', comfy ride")
    case 'general':
        print('General: cheapest option: no reservation')
    case 'luxury':
        print('Luxury- Premium seats with meals')
    case _:
        print('Invalid seat type')



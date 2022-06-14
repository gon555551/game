import keyboard, sys

while True:
    event = keyboard.read_event()
    match event.name + event.event_type:
        case 'wdown':
            print(event)
        case 'qdown':
            print(event)
        case 'hdown':
            print(event)
        case 'escdown':
            sys.exit()

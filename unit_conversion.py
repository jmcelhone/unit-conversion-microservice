import zmq

def get_unit(unit, value):
    if "centimeter" in unit:
        value /= 2.54
        unit = "inch(es)"
    elif "inch" in unit:
        value *= 2.54
        unit = "centimeter(s)"
    elif "kilogram" in unit:
        value *= 2.205
        unit = "pound(s)"
    elif "pound" in unit:
        value /= 2.205
        unit = "kilogram(s)"
    elif "celsius" in unit:
        value = (value * 1.8) + 32
        unit = "fahrenheit"
    elif "fahrenheit" in unit:
        value = (value / 1.8) - 32
        unit = "celsius"
    elif "liter" in unit:
        value *= 0.264
        unit = "gallon(s)"
    elif "gallon" in unit:
        value *= 3.79
        unit = "liter(s)"
    elif "mile" in unit:
        value *= 1.61
        unit = "kilometer(s)"
    elif "kilometers" in unit:
        value *= 0.62
        unit = "mile(s)"
    elif "feet" in unit:
        value *= 0.304
        unit = "meter(s)"
    elif "meter" in unit:
        value *= 3.28
        unit = "feet"
    elif "mph" in unit:
        value *= 1.609
        unit = "kph"
    else:
        value *= 0.621
        unit = "mph"


    return f"{value} {unit}"
    
def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("ASCII Service Listening on Port 5555")

    

    while True:
        message = socket.recv_string()

        if len(message) > 0:
            split_message = message.decode().split()
            value = split_message[0]
            unit = split_message[1].lower()
            new_unit = get_unit(unit, value)
            socket.send_string(new_unit)

if __name__ == "__main__":
    main()
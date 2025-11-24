import zmq
import time
context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def get_unit(quantity, category):
    time.sleep(1)
    socket.send_string(f"{quantity} {category}")
    new_unit = socket.recv()
    return new_unit

while True:
    q = input("choose quantity of unit: ")
    c = input("choose type of unit: ")
    noun = get_unit(q, c)
    print(noun)
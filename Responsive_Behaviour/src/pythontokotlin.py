import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gesture = "Dorsal Fist"
s.connect(('localhost', 9999))
s.send(bytes(gesture,'ascii'))
s.close()
print ('Done')


"""
Simple socket client, Just send one of these: Open Palm, Dorsal Palm, Open Fist
Dorsal Fist, Open Three Fingers, Dorsal Three Fingers.
break can also be sent if you need to exit server loop.
"""

import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectHeader = "CONNECT furhat MyClassName\n"
sendEventHeader = "EVENT action.speech "
sampleSayEvent ="{\"class\" : \"iristk.system.Event\", " + "\"event_name\" : \"action.speech\", " + "\"event_id\" : \"my_unique_id_123\", " + "\"text\" : \"Hello there\"}"
s.connect(('localhost', 1932))
s.send(bytes(connectHeader, 'ascii'))
time.sleep(2)
data = s.recv(1024)
print('recieved', repr(data))
s.send(bytes(sendEventHeader + str(len(sampleSayEvent.encode('ascii'))) + '\n', 'ascii'))
s.send(bytes(sampleSayEvent,'ascii'))
time.sleep(5)
s.close()
print ('Done')

## Simple Port Scanner
import socket
from queue import Queue
import threading 

queue = Queue()
openPorts = []

def Scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        None

def fillQueue(portList):
    for port in portList:
        queue.put(port)

def workerFunction():
    while not queue.empty():
        port = queue.get()
        if Scan(target, port) == True:
            print('Port Open: ', str(port))
            openPorts.append(port)

target = str(input('Target IP: '))


portList = range(1, int(input('How many ports do you want to scan?: ')))
fillQueue(portList)

threadList = []

for t in range(100):
    thread = threading.Thread(target=workerFunction)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print('Open Ports are: ', openPorts)

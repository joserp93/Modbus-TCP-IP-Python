from threading import Thread
import time
import analog
import screen

'''
hilo1 = analog.get_analog_1()
hilo1.start()
hilo2 = analog.get_analog_2()
hilo2.start()
'''
hilo3 = screen.display()
hilo3.start()
hilo4 = analog.get_modbustcp_arduinoM()
hilo4.start()

'''
read("Thread-2");
while 1:
    pass
'''
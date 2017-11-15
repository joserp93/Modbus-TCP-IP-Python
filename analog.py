import time
from random import randint
from threading import Thread
from pymodbus3.client.sync import ModbusTcpClient as ModbusClient


current_time_1 = time.time();
current_time_2 = time.time();
current_time_3 = time.time();
read_ok_1 = 0
read_ok_2 = 0
read_ok_3 = 0
analog_1 = 0
analog_2 = 0
rh=0
rc=0

class get_modbustcp_arduinoM(Thread):
    def run(self):
        global rh,current_time_3,read_ok_3
        client = ModbusClient('192.168.0.100', port=502)
        client.connect()
        while True:
            if((time.time() - current_time_3) > 1):
                if(0 == read_ok_3):
                    current_time_3 = time.time();
                    read_ok_3=1
                    rh = client.read_holding_registers(0,13)
                    print(rh.registers)
                    rc = client.read_coils(0,1)
            
def read_update_sensores():
    global read_ok_3,rh,rc
    data3 = 0;
    val3=0;
    estado=0;
    if(1 == read_ok_3):
        read_ok_3 = 0;
        data3 = 1;
        val3 = rh;
        print(val3)
        estado = rc;
        
    return data3,val3,estado     

def rearranque():
    client.write_coil(0, False)

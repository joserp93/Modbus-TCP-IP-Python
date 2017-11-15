from tkinter import *
import analog
import time
from threading import Thread
from pymodbus3.client.sync import ModbusTcpClient as ModbusClient

class App():
    
    def __init__(self, master):
        self.master = master

        frame = Frame(master)
        frame.pack()

      #  canvas = Canvas(master)
      # imagen1=PhotoImage(file='tren-128x64.png')
      #  canvas.create_image(0,0,image=imagen1)
        
      # canvas=Canvas(width=128,height=200,bg="yellow")
      # canvas.pack(expand=YES,fill=BOTH)
      #  gif1=PhotoImage(file='tren-128x64.png')
      #  canvas.create_image(150,100,image=gif1,anchor=NW)


        label = Label(frame , text = "SISTEMA DE SUPERVISION DE LOS SENSORES DE TRANCA DEL TREN LAMINADOR PROPERZI EN CORPAL C.A" , font = ("Helvetica",12))
        label.grid(row = 0,column=4)

        se = Label(frame, text= "Sensor N:",font=("Helvetica",10), fg= "green")
        se.grid(row=1,column=1, sticky=W)

        va = Label(frame, text= "valor actual",font=("Helvetica",10), fg= "green")
        va.grid(row=1,column=2, sticky=W)

        ret = Label(frame, text= "Referencia",font=("Helvetica",10), fg= "green")
        ret.grid(row=1,column=3, sticky=W)

        boton1=Button(frame,text="Rearranque del Laminador",bg="blue")
        boton1.grid(row=1,column=4)
        self.reading_estadoL = Label(frame, text = "Estado del Laminador: " , font = ("Helvetica",14))
        self.reading_estadoL.grid(row = 2, column= 4)
        boton1=Button(frame,text="Cambiar Valor de Referencia",bg="green")
        boton1.grid(row=4,column=4)

        self.reading_referencia1 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia1.grid(row = 2, column= 3)
        self.reading_referencia2 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia2.grid(row = 3, column= 3)
        self.reading_referencia3 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia3.grid(row = 4, column= 3)
        self.reading_referencia4 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia4.grid(row = 5, column= 3)
        self.reading_referencia5 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia5.grid(row = 6, column= 3)
        self.reading_referencia6 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia6.grid(row = 7, column= 3)
        self.reading_referencia7 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia7.grid(row = 8, column= 3)
        self.reading_referencia8 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia8.grid(row = 9, column= 3)
        self.reading_referencia9 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia9.grid(row = 10, column= 3)
        self.reading_referencia10 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia10.grid(row = 11, column= 3)
        self.reading_referencia11 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia11.grid(row = 12, column= 3)
        self.reading_referencia12 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_referencia12.grid(row = 13, column= 3)
       
        self.et1 = Label(frame, text= "estado",font=("Helvetica",10), fg= "green")
        self.et1.grid(row=1,column=4, sticky=W)

        s1 = Label(frame, text= "S1:",font=("Helvetica",14), fg= "green")
        s1.grid(row=2,column=1, sticky=W)

        self.e1 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e1.grid(row=2,column=4, sticky=W)

        s2 = Label(frame, text= "S2:",font=("Helvetica",14), fg= "green")
        s2.grid(row=3,column=1,sticky=W)

        self.e2 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e2.grid(row=3,column=4, sticky=W)

        s3 = Label(frame, text= "S3:",font=("Helvetica",14), fg= "green")
        s3.grid(row=4,column=1,sticky=W)

        self.e3 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e3.grid(row=4,column=4, sticky=W)

        s4 = Label(frame, text= "S4:",font=("Helvetica",14), fg= "green")
        s4.grid(row=5,column=1,sticky=W)

        self.e4 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e4.grid(row=5,column=4, sticky=W)

        s5 = Label(frame, text= "S5:",font=("Helvetica",14), fg= "green")
        s5.grid(row=6,column=1,sticky=W)

        self.e5 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e5.grid(row=6,column=4, sticky=W)

        s6 = Label(frame, text= "S6:",font=("Helvetica",14), fg= "green")
        s6.grid(row=7,column=1,sticky=W)

        self.e6 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e6.grid(row=7,column=4, sticky=W)

        s7 = Label(frame, text= "S7:",font=("Helvetica",14), fg= "green")
        s7.grid(row=8,column=1,sticky=W)

        self.e7 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e7.grid(row=8,column=4, sticky=W)

        s8 = Label(frame, text= "S8:",font=("Helvetica",14), fg= "green")
        s8.grid(row=9,column=1,sticky=W)

        self.e8 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e8.grid(row=9,column=4, sticky=W)

        s9 = Label(frame, text= "S9:",font=("Helvetica",14), fg= "green")
        s9.grid(row=10,column=1,sticky=W)

        self.e9 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e9.grid(row=10,column=4, sticky=W)

        s10 = Label(frame, text= "S10:",font=("Helvetica",14), fg= "green")
        s10.grid(row=11,column=1,sticky=W)

        self.e10 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e10.grid(row=11,column=4, sticky=W)

        s11 = Label(frame, text= "S11:",font=("Helvetica",14), fg= "green")
        s11.grid(row=12,column=1,sticky=W)

        self.e11 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e11.grid(row=12,column=4, sticky=W)

        s12 = Label(frame, text= "S12:",font=("Helvetica",14), fg= "green")
        s12.grid(row=13,column=1,sticky=W)

        self.e12 = Label(frame, text= "",font=("Helvetica",14), fg= "green")
        self.e12.grid(row=13,column=4, sticky=W)

        self.reading_label1 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label1.grid(row = 2, column= 2)

        self.reading_label2 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label2.grid(row = 3, column=2)

        self.reading_label3 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label3.grid(row = 4, column=2)  

        self.reading_label4 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label4.grid(row = 5, column=2)

        self.reading_label5 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label5.grid(row = 6, column=2)   

        self.reading_label6 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label6.grid(row = 7, column=2)   

        self.reading_label7 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label7.grid(row = 8, column=2)  

        self.reading_label8 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label8.grid(row = 9, column=2) 

        self.reading_label9 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label9.grid(row = 10, column=2)   

        self.reading_label10 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label10.grid(row = 11, column=2) 

        self.reading_label11 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label11.grid(row = 12, column=2)   

        self.reading_label12 = Label(frame, text = '0.0' , font = ("Helvetica",14))
        self.reading_label12.grid(row = 13, column=2)   

        self.update_reading()

        

    def update_reading(self):
        data3,val3,estado = analog.read_update_sensores()
        if(1 == data3):
           # reading_str = "{:.1f}".format(val3.registers[0])
           # k=int(val3.registers[0])
            reading_str = str(val3.registers[0])
            self.reading_label1.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[1])
            reading_str = str(val3.registers[1])
            self.reading_label2.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[2])
            reading_str = str(val3.registers[2])
            self.reading_label3.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[3])
            reading_str = str(val3.registers[3])
            self.reading_label4.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[4])
            reading_str = str(val3.registers[4])
            self.reading_label5.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[5])
            reading_str = str(val3.registers[5])
            self.reading_label6.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[6])
            reading_str = str(val3.registers[6])
            self.reading_label7.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[7])
            reading_str = str(val3.registers[7])
            self.reading_label8.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[8])
            reading_str = str(val3.registers[8])
            self.reading_label9.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[9])
            reading_str = str(val3.registers[9])
            self.reading_label10.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[10])
            reading_str = str(val3.registers[10])
            self.reading_label11.configure(text = reading_str)
           # reading_str = "{:.1f}".format(val3.registers[11])
            reading_str = str(val3.registers[11])
            self.reading_label12.configure(text = reading_str)
            referencia=val3.registers[12];
            reading_str = str(val3.registers[12])

            if(estado.bits[0]==False):
            	self.reading_estadoL.configure(text="Estado del Laminador: Encendido",fg= "green")
            else:
            	self.reading_estadoL.configure(text="Estado del Laminador: Apagado",fg= "green")

            self.reading_referencia1.configure(text = reading_str)
            self.reading_referencia2.configure(text = reading_str)
            self.reading_referencia3.configure(text = reading_str)
            self.reading_referencia4.configure(text = reading_str)
            self.reading_referencia5.configure(text = reading_str)
            self.reading_referencia6.configure(text = reading_str)
            self.reading_referencia7.configure(text = reading_str)
            self.reading_referencia8.configure(text = reading_str)
            self.reading_referencia9.configure(text = reading_str)
            self.reading_referencia10.configure(text = reading_str)
            self.reading_referencia11.configure(text = reading_str)
            self.reading_referencia12.configure(text = reading_str)            

            if(val3.registers[0]<referencia):
            	self.e1.configure(text="OK",fg= "green")
            else:
            	self.e1.configure(text="Error",fg= "red")
            if(val3.registers[1]<referencia):
            	self.e2.configure(text="OK",fg= "green")
            else:
            	self.e2.configure(text="Error",fg= "red")
            if(val3.registers[2]<referencia):
            	self.e3.configure(text="OK",fg= "green")
            else:
            	self.e3.configure(text="Error",fg= "red")
            if(val3.registers[3]<referencia):
            	self.e4.configure(text="OK",fg= "green")
            else:
            	self.e4.configure(text="Error",fg= "red")
            if(val3.registers[4]<referencia):
            	self.e5.configure(text="OK",fg= "green")
            else:
            	self.e5.configure(text="Error",fg= "red")
            if(val3.registers[5]<referencia):
            	self.e6.configure(text="OK",fg= "green")
            else:
            	self.e6.configure(text="Error",fg= "red")
            if(val3.registers[6]<referencia):
            	self.e7.configure(text="OK",fg= "green")
            else:
            	self.e7.configure(text="Error",fg= "red")
            if(val3.registers[7]<referencia):
            	self.e8.configure(text="OK",fg= "green")
            else:
            	self.e8.configure(text="Error",fg= "red")
            if(val3.registers[8]<referencia):
            	self.e9.configure(text="OK",fg= "green")
            else:
            	self.e9.configure(text="Error",fg= "red")
            if(val3.registers[9]<referencia):
            	self.e10.configure(text="OK",fg= "green")
            else:
            	self.e10.configure(text="Error",fg= "red")
            if(val3.registers[10]<referencia):
            	self.e11.configure(text="OK",fg= "green")
            else:
            	self.e11.configure(text="Error",fg= "red")
            if(val3.registers[11]<referencia):
            	self.e12.configure(text="OK",fg= "green")
            else:
            	self.e12.configure(text="Error",fg= "red")
        
              
            
        self.master.after(100 , self.update_reading)


class display(Thread): 
    def run(self):
        #print threadName
        root = Tk()
        root.wm_title("Ammeter")
        app = App(root)
        root.geometry("1200x480")
        root.mainloop()

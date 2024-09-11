from machine import Pin
import time

class LOW_SPEED_SPI:
    def __init__(self,cs_pin,clk_pin,miso_pin):
        self.clk=Pin(clk_pin,Pin.OUT)
        self.miso=Pin(miso_pin,Pin.OUT)
        self.cs=Pin(cs_pin,Pin.OUT)

    def delay(self,t):
        time.sleep_us(t)
    
    def senddata(self,data):
        for i in range(0,8):
            if (data&0x80):
                self.miso.value(1)
            else:
                self.miso.value(0)
            data=data<<1
            
            self.clk.value(0)
            self.delay(1)
            self.clk.value(1)
            self.delay(1)
    
    def write_cmd(self,data):   #9bit
        self.cs.value(0)
        self.miso.value(0)
        self.clk.value(0)
        self.delay(1)
        self.clk.value(1)
        self.delay(1)
        
        self.senddata(data)
        self.cs.value(1)
    
    def write_data(self,data):
        self.cs.value(0)
        self.miso.value(1)
        self.clk.value(0)
        self.delay(1)
        self.clk.value(1)
        self.delay(1)
        
        self.senddata(data)
        self.cs.value(1)
        
    def init_st7701_spi(self):
        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x13)

        self.write_cmd(0xEF)
        self.write_data(0x08)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x10)

        self.write_cmd(0xC0)
        self.write_data(0x4F)
        self.write_data(0x00)

        self.write_cmd(0xC1)
        self.write_data(0x10)
        self.write_data(0x02)

        self.write_cmd(0xC2)
        self.write_data(0x07)
        self.write_data(0x02)

        self.write_cmd(0xCC)
        self.write_data(0x10)

        self.write_cmd(0xB0)
        self.write_data(0x00)
        self.write_data(0x10)
        self.write_data(0x17)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x06)
        self.write_data(0x05)
        self.write_data(0x08)
        self.write_data(0x07)
        self.write_data(0x1F)
        self.write_data(0x04)
        self.write_data(0x11)
        self.write_data(0x0E)
        self.write_data(0x29)
        self.write_data(0x30)
        self.write_data(0x1F)

        self.write_cmd(0xB1)
        self.write_data(0x00)
        self.write_data(0x0D)
        self.write_data(0x14)
        self.write_data(0x0E)
        self.write_data(0x11)
        self.write_data(0x06)
        self.write_data(0x04)
        self.write_data(0x08)
        self.write_data(0x08)
        self.write_data(0x20)
        self.write_data(0x05)
        self.write_data(0x13)
        self.write_data(0x13)
        self.write_data(0x26)
        self.write_data(0x30)
        self.write_data(0x1F)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x11)

        self.write_cmd(0xB0)
        self.write_data(0x65)

        self.write_cmd(0xB1)
        self.write_data(0x71)

        self.write_cmd(0xB2)
        self.write_data(0x87)

        self.write_cmd(0xB3)
        self.write_data(0x80)

        self.write_cmd(0xB5)
        self.write_data(0x4D)

        self.write_cmd(0xB7)
        self.write_data(0x85)

        self.write_cmd(0xB8)
        self.write_data(0x20)

        self.write_cmd(0xC1)
        self.write_data(0x78)

        self.write_cmd(0xC2)
        self.write_data(0x78)

        self.write_cmd(0xD0)
        self.write_data(0x88)

        self.write_cmd(0xEE)
        self.write_data(0x42)

        self.write_cmd(0xE0)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x02)

        self.write_cmd(0xE1)
        self.write_data(0x04)
        self.write_data(0xA0)
        self.write_data(0x06)
        self.write_data(0xA0)
        self.write_data(0x05)
        self.write_data(0xA0)
        self.write_data(0x07)
        self.write_data(0xA0)
        self.write_data(0x00)
        self.write_data(0x44)
        self.write_data(0x44)

        self.write_cmd(0xE2)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)

        self.write_cmd(0xE3)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x22)
        self.write_data(0x22)

        self.write_cmd(0xE4)
        self.write_data(0x44)
        self.write_data(0x44)

        self.write_cmd(0xE5)
        self.write_data(0x0C)
        self.write_data(0x90)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x0E)
        self.write_data(0x92)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x08)
        self.write_data(0x8C)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x0A)
        self.write_data(0x8E)
        self.write_data(0xA0)
        self.write_data(0xA0)

        self.write_cmd(0xE6)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x22)
        self.write_data(0x22)

        self.write_cmd(0xE7)
        self.write_data(0x44)
        self.write_data(0x44)

        self.write_cmd(0xE8)
        self.write_data(0x0D)
        self.write_data(0x91)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x0F)
        self.write_data(0x93)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x09)
        self.write_data(0x8D)
        self.write_data(0xA0)
        self.write_data(0xA0)
        self.write_data(0x0B)
        self.write_data(0x8F)
        self.write_data(0xA0)
        self.write_data(0xA0)

        self.write_cmd(0xEB)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0xE4)
        self.write_data(0xE4)
        self.write_data(0x44)
        self.write_data(0x00)
        self.write_data(0x40)

        self.write_cmd(0xED)
        self.write_data(0xFF)
        self.write_data(0xF5)
        self.write_data(0x47)
        self.write_data(0x6F)
        self.write_data(0x0B)
        self.write_data(0xA1)
        self.write_data(0xAB)
        self.write_data(0xFF)
        self.write_data(0xFF)
        self.write_data(0xBA)
        self.write_data(0x1A)
        self.write_data(0xB0)
        self.write_data(0xF6)
        self.write_data(0x74)
        self.write_data(0x5F)
        self.write_data(0xFF)

        self.write_cmd(0xEF)
        self.write_data(0x08)
        self.write_data(0x08)
        self.write_data(0x08)
        self.write_data(0x45)
        self.write_data(0x3F)
        self.write_data(0x54)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x13)

        self.write_cmd(0xE6)
        self.write_data(0x16)

        self.write_cmd(0xE8)
        self.write_data(0x00)
        self.write_data(0x0E)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)

        self.write_cmd(0x11)
        self.delay(12)
        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x13)

        self.write_cmd(0xE8)
        self.write_data(0x00)
        self.write_data(0x0C)
        
        self.delay(1)
        self.write_cmd(0xE8)
        self.write_data(0x00)
        self.write_data(0x00)

        self.write_cmd(0xFF)
        self.write_data(0x77)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)

        self.write_cmd(0x29)

        self.write_cmd(0x3A)
        self.write_data(0x77)
        self.write_cmd(0x29)

        self.write_cmd(0x36)
        self.write_data(0x08)
        


myspi=LOW_SPEED_SPI(cs_pin=38,clk_pin=46,miso_pin=45)
myspi.init_st7701_spi()
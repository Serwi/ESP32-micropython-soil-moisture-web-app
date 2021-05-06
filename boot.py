import network
import gc
import esp
import ssd1306
import machine

i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    

    
esp.osdebug(None)

gc.collect()

ssid = my_ssid
password = my_password

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

def display_ip():
    ip = station.ifconfig()[0]
    oled.text(ip, 0, 0)

    oled.show()

def display_off():
    oled.fill(0)
    oled.show()
    
def delete_index():
    import os
    os.remove("/templates/index_html.py")

# esp32-plant-soil-moisture-webapp

## General info
  This is code for esp32 to use it as wireless plant soil moisture sensor and view it in your browser

## Technologies

### Project is created with:

  #### Hardware:
  
    ESP32-DevKitC V4 ESP32-WROOM-32D
    OLED 0,96 SSD1306 SPI I2C
    Hw-390 Capacitive Soil Moisture Sensor
  #### Software:
  
    Micropython
    Picoweb
    Utemplate
    
## Setup
  
  To install this project you should first flash your ESP32 with micropython, then you can just put all files and folders into it. <br>
  Alternatively you can install picoweb and utemplate by using **upip.install("")**. <br>
  You should also alter **boot.py** with your wifi id and password. <br>
  In main there is list of soil sensors which you can alter, function **soil_moisture.show_readings(Pin)** reads sensor value in range of 0-100% where **Pin** is pin number
  where your sensor is connected to board
  
## Links
  Micropthon: https://micropython.org/ <br>
  Picoweb: https://github.com/pfalcon/picoweb <br>
  Utemplate: https://github.com/pfalcon/utemplate <br>

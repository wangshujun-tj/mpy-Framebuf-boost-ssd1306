import time
from machine import Pin, SPI
spi = SPI(2,baudrate=16_000_000)

from SSD1306_12864 import SSD1306_SPI
dc = Pin('B2', Pin.OUT_PP)
cs = Pin('B12', Pin.OUT_PP)
res= Pin('B14', Pin.OUT_PP)
oled = SSD1306_SPI(128, 64, spi,dc,res,cs, rot = 0)

oled.font_load("GB2312-24.fon")
for i in range(4):
    oled.fill(0)
    oled.font_set(0x24,i,1,0)
    oled.text("中文显示",0,16,1)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.font_set(0x24,i,1,1)
    oled.text("中文显示",0,16,1)
    oled.show()
    time.sleep(1)
for count in range(10):
    oled.fill(0)
    oled.font_set(0x11,0,1,0)
    oled.text("micro中文迤=%d"%count,0,0,1)
    oled.font_set(0x31,0,1,0)
    oled.text("micro中文迤=%d"%count,0,13,1)
    oled.text("micro中文迤=%d"%count,0,26,1)
    oled.font_set(0x41,0,1,0)
    oled.text("micro中文迤=%d"%count,0,39,1)
    oled.text("micro中文迤=%d"%count,0,51,1)
    oled.show()
for count in range(10):
    oled.fill(0)
    oled.font_set(0x12,0,1,0)
    oled.text("MicRo中文=%d"%count,0,0,1)
    oled.font_set(0x22,0,1,0)
    oled.text("MicRo中文=%d"%count,0,16,1)
    oled.font_set(0x32,0,1,0)
    oled.text("MicRo中文=%d"%count,0,32,1)
    oled.font_set(0x42,0,1,0)
    oled.text("micro中文=%d"%count,0,48,1)
    oled.show()
oled.save_bmp("b.bmp")
for count in range(10):
    oled.fill(0)
    oled.font_set(0x13,0,1,0)
    oled.text("MRo中文=%d"%count,0,0,1)
    oled.font_set(0x33,0,1,0)
    oled.text("MRo中文=%d"%count,0,32,1)
    oled.show()
for count in range(10):
    oled.fill(0)
    oled.font_set(0x14,0,1,0)
    oled.text("MR文=%d"%count,0,0,1)
    oled.font_set(0x34,0,1,0)
    oled.text("Mo中=%d"%count,0,32,1)
    oled.show()
for count in range(65):
    oled.fill(0)
    oled.show_bmp("logo-1.bmp",count*3-64,count*2-64)
    oled.show()
for count in range(65):
    oled.fill(0)
    oled.show_bmp("logo-1.bmp",count*3-64,0)
    oled.show()
for count in range(65):
    oled.fill(0)
    oled.show_bmp("logo-1.bmp",32,count*2-64)
    oled.show()


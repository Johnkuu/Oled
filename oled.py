#!/usr/bin/env python3

from board import SCL, SDA
import busio
from oled_text import OledText

#kello
from datetime import datetime

now =datetime.now()
paiva = now.strftime("%m-%d-%Y")
aika = now.strftime("%H:%M:%S")
#paiva = now.strftime("%m%d%Y %H:%M:%S") 

i2c = busio.I2C(SCL, SDA)

# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32)

# Write to the oled
oled.text("Tallennettu", 1)  # Line 1
oled.text(paiva, 2)  # Line 2
oled.text(aika, 3)  # Line 2
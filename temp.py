import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0x03
spi.max_speed_hz = 1000000
time.sleep(0.01)

spi.xfer2([0x08,0x80])

time.sleep(0.1)

spi.xfer2([0x54])

time.sleep(0.25)

adc = spi.xfer2([0xff,0xff])
temp = (adc[0] << 8) | adc[1]

temp = temp >> 3

if(temp >= 4096):
    temp = temp - 8192

print(temp / 16.0)

spi.close()
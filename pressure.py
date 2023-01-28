import smbus
from time import sleep

i2c = smbus.SMBus(1)

SA0_LOW_ADDRESS = 0x5c
address = SA0_LOW_ADDRESS

WHO_AM_I = 0x0F

LPS25H_WHO_ID = 0xBD

device_25H = 0
device = device_25H

CTRL_REG1 = 0x20

def LPS_init():
    if(detectDevice() == False):
        return False
    
def testWhoAmI():
    return i2c.read_i2c_block_data(address,WHO_AM_I,1)

def detectDevice():
    id = testWhoAmI()
    if(id[0] == LPS25H_WHO_ID):
        return True
    return False

def writeReg(reg, value):
    i2c.write_byte_data(address,reg,value)

def enableDefault():
    if(device == device_25H):
        writeReg(CTRL_REG1, 0xB0)

def readPressurRaw():
    pxl = i2c.read_byte_data(address, 0x28)
    pl = i2c.read_byte_data(address, 0x29)
    ph = i2c.read_byte_data(address, 0x2A)

    return ph << 16 | pl << 8 | pxl


def readPressureMillivars():
    return readPressurRaw() / 4096

def readTemperatureRaw():
    ol = i2c.read_byte_data(address, 0x2B)
    oh = i2c.read_byte_data(address, 0x2C)

    temptemp =  oh << 8 | ol

    if temptemp >= 32768:
        temptemp -= 65536

    return temptemp

def readTemperatureC():
    return 42.5 + readTemperatureRaw() / 480

sleep(0.1)

if(LPS_init() == False):
    print("Fail!!")

enableDefault()

pressure = readPressureMillivars()
temperature = readTemperatureC()

print(pressure)
print(temperature)


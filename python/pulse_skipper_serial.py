from __future__ import print_function
import serial
import time

class PulseSkipperSerial(serial.Serial):

    def __init__(self,port='/dev/ttyUSB8'):
        super(PulseSkipperSerial,self).__init__(port=port,baudrate=9600,timeout=5.0)
        time.sleep(2.0)

    def skipPulse(self,n):
        assert (n>=1 and n<=9), 'pulse number must be in range [1,9]'
        self.write('{0}'.format(n))

    def resetCount(self):
        self.write('r')

    def getCount(self):
        self.write('c')
        value = self.readline()
        value = value.split(',')
        value = int(value[0])
        return value 

    def setDisplayBinary(self):
        self.write('b')

    def setDisplayNumber(self):
        self.write('n')


# ---------------------------------------------------------------
if __name__ == '__main__':

    dev = PulseSkipperSerial(port='/dev/ttyUSB8')
    for i in range(5):
        count = dev.getCount()
        print('{0} count: {1}'.format(i, count))
        time.sleep(2)





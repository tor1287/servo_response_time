#Servo response time project, version 1.0

from machine import UART
from time import sleep

uart0 = UART(0, 9600)
uart0.init(baudrate=9600, bits=8, parity=None, stop=1, tx=0, rx=1)

def main():
    while True:
        uart0.write('hello, Tor.\n')
        sleep(1)

if __name__ == '__main__':
    main()
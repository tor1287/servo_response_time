#Servo response time project, version 1.0

from machine import UART
from time import time_ns, sleep_ms

uart0 = UART(0, 9600)
uart0.init(baudrate=9600, bits=8, parity=None, stop=1, tx=0, rx=1)
start_time = time_ns() #start time value

def check_time():
    current_time = time_ns() - start_time
    current_time_ms = current_time/1_000_000 #convert nano to milli
    time_message = "running time: " + str(current_time_ms) +" milliseconds\n"
    uart0.write(time_message)

def main():
    uart0.write("Program begin, version 1.0\n")
    sleep_ms(1500)
    while True:
        check_time()
        sleep_ms(50)

if __name__ == '__main__':
    main()
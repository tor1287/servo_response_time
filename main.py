#Servo response time project, version 1.0
import adc_time_uart as ATU
from machine import UART
from time import time_ns, sleep_ms

servo_position = True
start_time = time_ns() #start time value

def main():
    ATU.uart0.write("Program begin, version 1.0\n")
    sleep_ms(1000)
    ATU.uart0.write("TIME/POT VALUE     milleseonds/65535(16bit)\n")
    sleep_ms(1000)
    while True:
        print_time = ATU.check_time()
        print_pot = ATU.check_pot()
        ATU.uart0.write(print_time + " / " + print_pot + "\n")
        sleep_ms(4)

if __name__ == '__main__':
    main()
#Servo response time project, version 1.0

from machine import UART, ADC, Pin
from time import time_ns, sleep_ms


uart0 = UART(0, 9600)
uart0.init(baudrate=9600, bits=8, parity=None, stop=1, tx=0, rx=1)
start_time = time_ns() #start time value

ADC_pin = Pin(26, Pin.IN)
pot_pin = ADC(ADC_pin)

def check_time():
    current_time = time_ns() - start_time
    current_time_ms = current_time/1_000_000 #convert nano to milli
    time_message = str(current_time_ms)
    return time_message

def check_pot():
    pot_value = str(pot_pin.read_u16())
    return pot_value

def main():
    uart0.write("Program begin, version 1.0\n")
    sleep_ms(2000)
    uart0.write("TIME/POT VALUE     milleseonds/65535(16bit)\n")
    sleep_ms(1000)
    while True:
        print_time = check_time()
        print_pot = check_pot()
        uart0.write(print_time + print_pot + "\n")
        sleep_ms(40)

if __name__ == '__main__':
    main()
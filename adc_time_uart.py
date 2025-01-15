#Function support Maker Nano RP2040: ADC read, UART,Runtime function for servo response time

from machine import UART, ADC, Pin
from time import time_ns, sleep_ms
from main import start_time

#UART to usb display
uart0 = UART(0, 9600)
uart0.init(baudrate=9600, bits=8, parity=None, stop=1, tx=0, rx=1)

#ADC pin connect potentiometer join with servo shaft
ADC_pin = Pin(27, Pin.IN)
pot_pin = ADC(ADC_pin)

#return time since start in millisecond
def check_time():
    current_time = time_ns() - start_time
    current_time_ms = int(current_time/1000000) #convert nano to milli
    time_message = str(current_time_ms)
    return time_message

#return raw analog value in 16 bits
def check_pot():
    pot_value = str(int(pot_pin.read_u16()))
    return pot_value
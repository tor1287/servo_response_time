#Function support Maker Nano RP2040: ADC read, UART,Runtime function for servo response time

from machine import UART, ADC, Pin, PWM
from time import time_ns, sleep_ms
from main import start_time, servo_position
button = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)
#UART to usb display
uart0 = UART(0, 115200)
uart0.init(baudrate=115200, bits=8, parity=None, stop=1, tx=0, rx=1)

#ADC pin connect potentiometer join with servo shaft
ADC_pin = Pin(27, Pin.IN)
pot_pin = ADC(ADC_pin)

#PWM resolution 65535
position_L = 3276
position_M = 4914
position_H = 6552

servo_pin = Pin(3)
servo = PWM(servo_pin) 
servo.freq(50)  # Set the frequency to 50 Hz

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

#button handler: toggle servo position
def button_handler(button):
    global servo_position
    if servo_position == True:
        uart0.write("Button position 1\n")
        servo.duty_u16(position_M)
        servo_position = not servo_position
    else:
        uart0.write("Button position 2\n")
        servo.duty_u16(position_L)
        servo_position = not servo_position

button.irq(button_handler, trigger=button.IRQ_FALLING)
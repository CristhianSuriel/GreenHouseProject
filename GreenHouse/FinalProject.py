from gpiozero import LightSensor
from time import sleep
import RPi.GPIO as GPIO

ldr = LightSensor(4)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(0)


#function to assign angle
def SetAngle(angle):
    duty = angle/18+2 #this is to calculate the duty cycle
    GPIO.output(18, True) #turns the pin for output
    pwm.ChangeDutyCycle(duty) #changes the duty cycle to match what's calculated
    sleep(1) #waits 1 second
    GPIO.output(18, False) #turns the pin for output
    # changes the duty back to 0 so we aren't continuously sending inputs to the servo
    pwm.ChangeDutyCycle(0)

while True:
    print(ldr.value)
    if (ldr.value > 0.5):
        GPIO.output(26,GPIO.LOW)
        sleep(1)
        SetAngle(0)
    else:
        SetAngle(180)
        GPIO.output(26,GPIO.HIGH)
        sleep(1)

import RPi.GPIO as GPIO
import time

# define pinout
led_green_gpio = 17
led_red_gpio = 27
switch_gpio = 22

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_green_gpio,GPIO.OUT)
GPIO.setup(led_red_gpio,GPIO.OUT)
GPIO.setup(switch_gpio,GPIO.IN)

# setup PWM
pwm_red = GPIO.PWM(led_red_gpio, 100)
pwm_red.start(0)

# main loop
try:
        while True:
                if (GPIO.input(switch_gpio) == False):
                        GPIO.output(led_green_gpio,GPIO.LOW)
                        pwm_red.ChangeDutyCycle(40)
                else:
                        GPIO.output(led_green_gpio,GPIO.HIGH)
                        pwm_red.ChangeDutyCycle(0)

                time.sleep(0.1)

except KeyboardInterrupt:
        pass

# cleanup GPIO before closing
GPIO.output(led_green_gpio,GPIO.LOW)
pwm_red.stop()
GPIO.cleanup()

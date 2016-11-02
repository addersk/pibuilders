import RPi.GPIO as GPIO
import time

# define pinout
led_green_gpio = 17
led_red_gpio = 27

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_green_gpio,GPIO.OUT)
GPIO.setup(led_red_gpio,GPIO.OUT)

# blink the LED forever
try:
	while True:
		GPIO.output(led_green_gpio,GPIO.HIGH)
		GPIO.output(led_red_gpio,GPIO.LOW)
		time.sleep(1)
		GPIO.output(led_green_gpio,GPIO.LOW)
		GPIO.output(led_red_gpio,GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	pass

# cleanup GPIO before closing
GPIO.output(led_green_gpio,GPIO.LOW)
GPIO.output(led_red_gpio,GPIO.LOW)
GPIO.cleanup()

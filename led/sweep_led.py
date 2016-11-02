import RPi.GPIO as GPIO
import time

# define pinout
led_green_gpio = 17
led_red_gpio = 27

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_green_gpio,GPIO.OUT)
GPIO.setup(led_red_gpio,GPIO.OUT)

# setup PWMs
pwm_green = GPIO.PWM(led_green_gpio, 100)
pwm_red = GPIO.PWM(led_red_gpio, 100)

pwm_green.start(0)
pwm_red.start(0)

# sweep PWM on LEDs forever
try:
	while True:
		for dc in range (0, 26, 1):
			pwm_green.ChangeDutyCycle(dc)
			time.sleep(0.05)
		for dc in range (25, -1, -1):
			pwm_green.ChangeDutyCycle(dc)
			time.sleep(0.05)
		for dc in range (0, 26, 1):
			pwm_red.ChangeDutyCycle(dc)
			time.sleep(0.05)
		for dc in range (25, -1, -1):
			pwm_red.ChangeDutyCycle(dc)
			time.sleep(0.05)
except KeyboardInterrupt:
	pass

# cleanup GPIO before closing
pwm_green.stop()
pwm_red.stop()
GPIO.cleanup()

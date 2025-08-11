import RPi.GPIO as GPIO
import time

#Use BCM pin numbering
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Blinking LED on GPIO 17. Press Ctrl + C t0 stop.")

try:
	while True:
		GPIO.output(LED_PIN, GPIO.HIGH) #LED on
		time.sleep(10)
		GPIO.output(LED_PIN, GPIO.LOW) #LED off
		time.sleep(1)
except KeyboardInterrupt:
	print("\nExiting...")
finally:
	GPIO.cleanup()


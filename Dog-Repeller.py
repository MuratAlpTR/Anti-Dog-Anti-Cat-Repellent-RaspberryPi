                                                      //  “The project was written by MuratAlpTR” // 

# Using an ultrasonic sensor to detect animals

import RPi.GPIO as GPIO
import time

trigPin = 9  # Ultrasonic sensor's trigger pin
echoPin = 10  # Ultrasonic sensor's echo pin
buzzerPin = 11  # Buzzer pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)

def measure_distance():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)

    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()

    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")

        if dist < 50:  # If an animal is closer than 50 cm
            GPIO.output(buzzerPin, GPIO.HIGH)  # Activate the buzzer
            time.sleep(1)  # Wait for 1 second
            GPIO.output(buzzerPin, GPIO.LOW)  # Turn off the buzzer

except KeyboardInterrupt:
    GPIO.cleanup()

                                                      //  “The project was written by MuratAlpTR” // 

#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_MQ = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_MQ, GPIO.IN)

if __name__ == '__main__':
    try:
        while True:
            print("Safe..." if GPIO.input(GPIO_MQ)==1 else "Alarm!")
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

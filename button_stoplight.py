from gpiozero import Button,TrafficLights
from time import sleep 

red_led_pin=5
yellow_led_pin=19
green_led_pin=20
button_pin=21

lights=TrafficLights(red_led_pin, yellow_led_pin,green_led_pin)
button=Button(button_pin)

def traffic_sequence():
    lights.green.on()
    sleep(5)
    lights.green.off()
    lights.yellow.on()
    sleep(1)
    lights.yellow.off()
    lights.red.on()
    sleep(4)
    lights.red.off()

print("Traffic light system ready, press the button to start the sequence")
xwhile True:
    button.wait_for_press()
    print("Button touched!")
    traffic_sequence()
    print("Button not touched!")
    sleep(0.1)

import RPi.GPIO as GPIO
import time
import random
import signal
import sys
import pygame
from pygame import mixer


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(6, GPIO.IN)

leds = []
leds_left = []
leds_right = []
pygame.mixer.init()
Slumber = pygame.mixer.Sound('Slumber.wav')
Choose = pygame.mixer.Sound('Choose.wav')
Remember = pygame.mixer.Sound('Remember 2.wav')
Greedy = pygame.mixer.Sound('Greedy.wav')

class LEDRight:
    def __init__(self, pin):
        self.pin = pin
        leds_right.append(self)
        leds.append(self)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)
        
    def off(self):
        GPIO.output(self.pin, False)

class LEDLeft:
    def __init__(self, pin):
        self.pin = pin
        leds_left.append(self)
        leds.append(self)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)
        
    def off(self):
        GPIO.output(self.pin, False)

RedLED = LEDRight(17)
YellowLED = LEDRight(27)
GreenLED = LEDRight(22)
RedLED2 = LEDLeft(18)
YellowLED2 = LEDLeft(23)
GreenLED2 = LEDLeft(24)

def PowerOn():
    for i in range(len(leds_right)):
                   leds_right[i].on()
    time.sleep(5)
    for i in range(len(leds_right)):
                   leds_right[i].off()
                   leds_left[i].on()
    time.sleep(5)
    for i in range(len(leds_left)):
                   leds_left[i].off()

    
def BOO():
    RedLED.on()
    RedLED2.on()
    time.sleep(3)
    RedLED.off()
    RedLED2.off()

def Scare(s):
    x = 0
    while x<s*5:
        for i in range(len(leds_right)):
            leds_right[i].on()
            leds_left[i].on()
            time.sleep(0.2)
            leds_right[i].off()
            leds_left[i].off()
        x=x+1

def TalkingLeft(s):
    YellowLED.on()
    x = 0
    while x < s:
        leds_left[x % 3].on()
        time.sleep(1)
        leds_left[x % 3].off()
        x = x+1
        YellowLED.off()

def TalkingRight(s):
    x = 0
    YellowLED2.on()
    while x < s:
        leds_right[x % 3].on()
        time.sleep(1)
        leds_right[x % 3].off()
        x = x+1
    YellowLED2.off()
    
def TalkingBoth(s):
    x = 0
    while x < s:
        leds_left[x % 3].on()
        leds_right[x % 3].on()
        time.sleep(1)
        leds_left[x % 3].off()
        leds_right[x % 3].off()
        x = x+1
        
def Resting(s):
    YellowLED.on()
    YellowLED2.on()
    time.sleep(s)
    YellowLED.off()
    YellowLED2.off()

def Laughing(s):
    x=0
    while x<s*5:
        RedLED.on()
        RedLED2.on()
        time.sleep(0.1)
        RedLED.off()
        RedLED2.off()
        GreenLED.on()
        GreenLED2.on()
        time.sleep(0.1)
        GreenLED.off()
        GreenLED2.off()
        x=x+1

PowerOn()

while True:
    if GPIO.input(6):
        print "Trick or Treat"
        Slumber.play()
        time.sleep(1)
        Laughing(2)
        Scare(1.5)
        Resting(5)
        Choose.play()
        Resting(1)
        Scare(3.5)
        Resting(0.5)
        Scare(1)
        Resting(1)
        TalkingBoth(3)
        Resting(2)
        Remember.play()
        Resting(1)
        TalkingBoth(6)
        Greedy.play()
        Resting(1.5)
        Scare(1)
        Laughing(10)

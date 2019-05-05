#!/usr/bin/python3
import datetime
import sys
import pygame
import time

try:
    pygame.init()

    bell = pygame.mixer.Sound("bell.wav")

    help = "Usage: [HOUR] [MINUTE] [AM/PM]"

    x = int(sys.argv[2])

    z = sys.argv[3].lower()

    if z == "am":
        y = int(sys.argv[1])
    elif z == "pm":
        y = int(sys.argv[1]) + 12
        pm = True

    while True:
        try:
            timern = datetime.datetime.now()

            if timern.minute == x and timern.hour == y:
                if pm:
                    y = y - 12
                    a = "pm"
                else:
                    a = ""

                if x <= 9:
                    addzero = "0"
                else:
                    addzero = ""

                print("Wake up!")
                print("The time is {}:{}{} {}".format(y, addzero, x, a))
                bell.play()
                time.sleep(3)
                bell.play()
                time.sleep(3)
                bell.play()
                time.sleep(3)
                break
                
        except KeyboardInterrupt:
            print("\nBye!")
            sys.exit()
except IndexError:
    print(help)
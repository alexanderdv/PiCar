import pygame,time
from BrickPi import *

BrickPiSetup()  # setup the serial port for communication
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B - Move Target
BrickPi.MotorEnable[PORT_C] = 1 #Enable the Motor C - Shoot Balls
BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

screen = pygame.display.set_mode((800, 400))
old = pygame.mouse.get_pos()[0]
while True:
    try:
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN :
            BrickPi.MotorSpeed[PORT_C]= 250
            BrickPiUpdateValues()
            time.sleep(.1)
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[PORT_C]= 0
        if event.type == pygame.MOUSEMOTION:
            new = pygame.mouse.get_pos()[0]
            pygame.event.clear(pygame.MOUSEMOTION)
            speed = old-new
            BrickPi.MotorSpeed[PORT_B]= speed*2
            BrickPiUpdateValues()
            old = new
        time.sleep(.2)
    except KeyboardInterrupt:
        pygame.quit()

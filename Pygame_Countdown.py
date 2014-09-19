#!/usr/bin/env python

# Harry Beadle
# Pygame Countdown

import pygame, time

# Get the total time in the format [Hours, Minutes, Seconds]
TotalTime = str(raw_input("Timer length (HH:MM:SS):\n")).split(':')

# Convert to Integers
try:
    for i in [0, 1, 2]:
        TotalTime[i] = int(TotalTime[i])
except:
    print "The Input wasn't Valid!"
    quit()
    
# Get the total time in seconds
TotalTimeSeconds = (TotalTime[2]) + (TotalTime[1] * 60) + (TotalTime[0] * (60 ** 2))

# Define a function Generate_String() that takes the time in seconds and makes it pretty
def Generate_String(Time_In_Seconds):
    Hours = Time_In_Seconds / (60 ** 2)
    Minutes = (Time_In_Seconds / 60) % 60
    Seconds = Time_In_Seconds % 60
    return "%i Hours, %i Minutes and %i Seconds" % (Hours, Minutes, Seconds)

# Wait for the user's input to start the countdown
raw_input("Press [Enter] to begin the countdown!\n")

# Initalise Pygame
pygame.init()
Screen_X = 1280 ; Screen_Y = 720
stdscr = pygame.display.set_mode((Screen_X, Screen_Y), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Countdown")
pygame.mouse.set_visible(0)

# Define a function that checks to see if the user has tried to quit
def Check_for_Quit():
    Events = pygame.event.get()
    for Event in Events:
        if Event.type == pygame.QUIT or (Event.type == pygame.KEYDOWN and Event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

# Setup Font or Custom Font
try:
    Font = pygame.font.Font('font.ttf', 40)
except:
    Font = pygame.font.SysFont('monospace', 40)

# Run the Timer
while TotalTimeSeconds > 0:
    Check_for_Quit()
    if TotalTimeSeconds <= 30:
        stdscr.fill((255,4.25*TotalTimeSeconds,4.25*TotalTimeSeconds))
    else:
        stdscr.fill((255,255,255))
    String = Generate_String(TotalTimeSeconds)
    Font_Position = (
        (0.5 * Screen_X) - (0.5 * Font.size(String)[0]),
        (0.5 * Screen_Y) - (0.5 * Font.size(String)[1])
    )
    Rendered_Font = Font.render(String, 1, (0,0,0))
    stdscr.blit(Rendered_Font, Font_Position)
    pygame.display.flip()
    pygame.time.wait(1000)
    TotalTimeSeconds -= 1

pygame.quit()
print "The Countdown Finished!"
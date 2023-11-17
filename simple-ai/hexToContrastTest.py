#By Julian Barwig 
#Color Contrast Checker. 
#Will now programm it to black and white text choosing relative to the backround.

import random

#hexWertHintergund = input("Hintergrundfarbe zum Testen #")

coloriterations = 5
red = []
green = []
blue = []

result = []

for i in range(coloriterations):
   red.append(random.randint(0, 255))
   green.append(random.randint(0,255))
   blue.append(random.randint(0, 255))
print(red, green, blue)


def hexToRgb(hexWert):
    #roten Wert berechnen
    red = int(hexWert[0:2], 16)
    print(f"red = {red}")
    
    #gruenen Wert berechnen
    green = int(hexWert[2:4], 16)
    print(f"green = {green}")
    
    #blauen Wert berechnen
    blue = int(hexWert[4:], 16)
    print(f"blue = {blue}")
    

    return red, green, blue

#use formula to calculate the relative luminicance 
#to later use the result to determin if white or black text should be used 
def relativeLuminicance(red, green, blue):
    l = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    print(l)
    result.append(l)
    return l 

def wOrBTextChoose(l):
    if l < 140:
        print("White text")
    else:
        print("Black text")

#Calculate all the relative Luminicance and look if white or black text should be used
for i in range(coloriterations):
    l = relativeLuminicance(red[i], green[i], blue[i])
    wOrBTextChoose(l)

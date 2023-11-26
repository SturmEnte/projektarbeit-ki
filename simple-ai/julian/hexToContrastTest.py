#By Julian Barwig | Jb2k5
#Color checker if White or Black text should be used. 

import random

colorIterations = 6 #how many files should be created

red = []
green = []
blue = []

result = []
wOrB = []

#create random rgb values
for i in range(colorIterations):
   red.append(random.randint(0, 255))
   green.append(random.randint(0,255))
   blue.append(random.randint(0, 255))
print(red, green, blue)


#hexToRgb Is not used! Is a remnent to older days... aka when the programm was manuel!
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
#Can break... Jk it can't
def relativeLuminicance(red, green, blue):
    l = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    print(l)
    result.append(l)
    return l 

#check if black or white text should be used. 
#wOrB = whiteOrBlack. in this case the color of the text. 
#return 0 if white text should be used and 1(one) if black text should be used
def wOrBTextChoose(l):
    if l < 140:
        print("White text")
        a = 0
        wOrB.append(a)
        return a
    else:
        print("Black text")
        a = 1
        wOrB.append(a)
        return a
        
#Write everything that could be usefull with for the ai and or the website in a textfile.
#returns rgb-values, the relative-Luminicance and 0 || 1 if white or black text is used. 

#needs to be reworked to be all in one textfile. For now it will work!
def resultOutData(red, green, blue, l, a):
        learningData = open(f"results{i}.txt","w")
        learningData.write(f"{red, green, blue}" " | " f"{l}" " | " f"{a}")
        learningData.close

#Calculate all the relative Luminicance's and look if white or black text should be used. 
#and also creates textfiles with resulst of one single(!) itteration. 
for i in range(colorIterations):
    l = relativeLuminicance(red[i], green[i], blue[i])
    wOrBTextChoose(l)
    resultOutData(red[i], green[i], blue[i], l, wOrB[i])
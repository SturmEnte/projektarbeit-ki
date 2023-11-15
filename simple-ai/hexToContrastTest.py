hexWert1 = input("Textfarbe zum Testen #")
hexWert2 = input("Hintergrundfarbe zum Testen #")

def hexToRgb(hexWert):
    #roten Wert berechnen
    red = int(hexWert[0:2], 16)
    print(f"Red = {red}")
    
    #gruenen Wert berechnen
    green = int(hexWert[2:4], 16)
    print(f"green = {green}")
    
    #blauen Wert berechnen
    blue = int(hexWert[4:], 16)
    print(f"blue = {blue}")
    

    return red, green, blue

def relativeLuminicance(red, green, blue):
    l = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    print(l)
    return l 

def calculateContrast():
    if l1 > l2:
        contrast = (l1 + 0.05) / (l2 + 0.05)
    else:
        contrast = (l2 + 0.05) / (l1 + 0.05)
    
    print(f"Kontrast ist {contrast}:1")

red, green, blue = hexToRgb(hexWert1)
l1 = relativeLuminicance(red, green, blue)
red, green, blue = hexToRgb(hexWert2)
l2 = relativeLuminicance(red, green, blue)

calculateContrast()

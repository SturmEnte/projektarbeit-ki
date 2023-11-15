hexWert1 = input("Hintergrundfarbe zum Testen #")

def hexToRgb1():
    red1 = tuple(int(hexWert1[i:i+2], 16) for i in (0,))
    print(f"Red1 = {red1}")
    blue1 = tuple(int(hexWert1[i:i+2], 16) for i in (2,))
    print(f"blue1 = {blue1}")
    green1 = tuple(int(hexWert1[i:i+2], 16) for i in (4,))
    print(f"green1 = {green1}")

hexToRgb1()

# Variablen
# Globale Zähler
height = None
number = None
color = None
red_block_count = 0
green_block_count = 0
blue_block_count = 0

# Farboffsets, wird inkrementiert
offsetR = 0
offsetG = 0
offsetB = 0

characterStartHeight = -56 # Höhe, auf die der Roboter verfahren muss, damit der Stift das Papier berührt
characterSafetyHeight = -40 # Sicherheitshöhe, in die der Roboter vor dem Malen verfährt
characterStart = (220, -50) # Startposition für die Zeichnung, wird mit den offsets oben verrechnet
waitBeforeWrite = 90  # 90 Leermessungen warten bis ergebnis geschrieben wird
numberDistanceX = 5 # Abstand zwischen den Zeichen (x)
numberDistanceY = 5 # Abstand zwischen den Zeichen (y)
characterScale = 5 # Zeichenskalierung in Millimetern
belt_timeout = 3 # Zeit in Sekunden bis der das Band anhält und die Zahlen aufgemalt werden

# Konstanten
STEP_PER_CIRCLE = 360.0 / 1.8 * 10.0 * 16.0 # Schritte pro Zirklischer Anordnung (Rotationsweite) als Berechnungshilfskonstante
MM_PER_CIRCLE = 3.1415926535898 * 36.0 # Millimeter auf einem kreis als Berechnungshilfskonstante

characters = { # Ein Character set (Schriftart) in relativen Koordinaten, start oben rechts
    "0": [
        (0, 0),
        (2, 0),
        (0, 1),
        (-2, 0),
        (0, -1)
    ],
    "1": [
        (0, 1),
        (2, 0)
    ],
    "2": [
        (0, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    ],
    "3": [
        (0, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        (0, -1)
    ],
    "4": [
        (0, 0),
        (1, 0),
        (0, 1),
        (-1, 0),
        (2, 0),
    ],
    "5": [
        (0, 1),
        (0, -1),
        (1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ],
    "6": [
        (0, 1),
        (0, -1),
        (2, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ],
    "7": [
        (0, 0),
        (0, 1),
        (2, 0)
    ],
    "8": [
        (1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (-2, 0),
        (0, 1),
        (1, 0),
    ],
    "9": [
        (1, 1),
        (0, -1),
        (-1, 0),
        (0, 1),
        (2, 0),
        (0, -1)
    ],
    "a": [
        (2, 0),
        (-1.75, 0),
        (-0.25, 0.25),
        (0, 0.5),
        (0.25, 0.25),
        (0.75, 0),
        (0, -1),
        (0, 1),
        (1, 0)
    ],
    "b": [
        (0, 0),
        (2, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (-0.25, 1),
        (-0.75, 0),
        (0, -1)
    ],
    "c": [
        (0, 1),
        (0, -0.75),
        (0.25, -0.25),
        (1.5, 0),
        (0.25, 0.25),
        (0, 0.75),
    ],
    "d": [
        (0, 0),
        (2, 0),
        (0, 0.75),
        (-0.25, 0.25),
        (-1.5, 0),
        (-0.25, -0.25),
        (0, -0.75)
    ],
    "e": [
        (0, 1),
        (0, -1),
        (1, 0),
        (0, 1),
        (0, -1),
        (1, 0),
        (0, 1)
    ],
    "f": [
        (0, 1),
        (0, -1),
        (1, 0),
        (0, 1),
        (0, -1),
        (1, 0)
    ],
    "g": [
        (0, 1),
        (0, -1),
        (2, 0),
        (0, 1),
        (-1, 0),
        (0, -0.5),
    ],
    "h": [
        (0, 0),
        (2, 0),
        (-1, 0),
        (0, 1),
        (1, 0),
        (-2, 0)
    ],
    "i": [
        (0, 0),
        (0, 1),
        (0, -0.5),
        (2, 0),
        (0, 0.5),
        (0, -1)
    ],
    "j": [
        (0, 0),
        (0, 1),
        (1.75, 0),
        (0.25, -0.25),
        (0, -0.75)
    ],
    "k": [
        (0, 0),
        (1, 0),
        (-1, 1),
        (0.75, -0.75),
        (0.75, 0.75),
        (0.5, 0),
        (-0.5, 0),
        (-0.75, -0.75),
        (0.25, -0.25),
        (1, 0)
    ],
    "l": [
        (0, 0),
        (2, 0),
        (0, 1)
    ],
    "m": [
        (2, 0),
        (-2, 0),
        (1, 0.5),
        (-1, 0.5),
        (2, 0)
    ],
    "n": [
        (2, 0),
        (-2, 0),
        (2, 1),
        (-2, 0)
    ],
    "o": [
        (0.25, 0),
        (1.5, 0),
        (0.25, 0.25),
        (0, 0.5),
        (-0.25, 0.25),
        (-1.5, 0),
        (-0.25, -0.25),
        (0, -0.5),
        (0.25, -0.25)
    ],
    "p": [
        (2, 0),
        (-2, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ],
    "q": [
        (2, 1),
        (-2, 0),
        (0, -1),
        (2, 0),
        (0, 1),
        (-0.2, 0),
        (-0.3, -0.3),
        (0.6, 0.6)
    ],
    "r": [
        (2, 0),
        (-2, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (0, 0.5),
        (1, 0.5)
    ],
    "s": [
        (0, 1),
        (0, -0.75),
        (0.25, -0.25),
        (0.5, 0),
        (0.25, 0.25),
        (0, 0.5),
        (0.25, 0.25),
        (0.5, 0),
        (0.25, -0.25),
        (0, -0.75)
    ],
    "t": [
        (0, 0),
        (0, 1),
        (0, -0.5),
        (2, 0)
    ],
    "u": [
        (0, 0),
        (1.75, 0),
        (0.25, 0.25),
        (0, 0.5),
        (-0.25, 0.25),
        (-1.75, 0)
    ],
    "v": [
        (0, 0),
        (2, 0.5),
        (-2, 0.5)
    ],
    "w": [
        (0, 0),
        (2, 0),
        (-1, 0.5),
        (1, 0.5),
        (-2, 0)
    ],
    "x": [
        (0, 0),
        (2, 1),
        (-1, -0.5),
        (-1, 0.5),
        (2, -1)
    ],
    "x": [
        (0, 0),
        (1, 0.5),
        (-1, 0.5),
        (1, -0.5),
        (1, 0)
    ],
    "z": [
        (0, 0),
        (0, 1),
        (2, -1),
        (0, 1)
    ],
    "ö": [
        (0.25, 0),
        (1.5, 0),
        (0.25, 0.25),
        (0, 0.5),
        (-0.25, 0.25),
        (-1.5, 0),
        (-0.25, -0.25),
        (0, -0.5),
        (0.25, -0.25),
        (-0.5, 0, 0),
        (0, 0.25),
        (0, 0.5, 0),
        (0, 0.25)
    ],
    "ä": [
        (2, 0),
        (-1.75, 0),
        (-0.25, 0.25),
        (0, 0.5),
        (0.25, 0.25),
        (0.75, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        (-2.25, -1, 0),
        (0, 0.25),
        (0, 0.5, 0),
        (0, 0.25)
    ],
    "ü": [
        (0, 0),
        (1.75, 0),
        (0.25, 0.25),
        (0, 0.5),
        (-0.25, 0.25),
        (-1.75, 0),
        (-0.25, -1, 0),
        (0, 0.25),
        (0, 0.5, 0),
        (0, 0.25)
    ],
    " ": [
        (0, 0, 0)
    ],
    ":": [
        (0, 0),
        (0.5, 0),
        (1, 0, 0),
        (0.5, 0)
    ]
}

# Funktionen


def setBeltSpeed(velocity_t): # laufbandgeschwindigkeit auf velocity_t setzen
    vel = float(velocity_t) * STEP_PER_CIRCLE / MM_PER_CIRCLE
    dType.SetEMotorEx(api, 0, 1, int(vel), 1)

def robotSleep(ms): # Roboter für x ms schlafen lassen
    dType.dSleep(ms)


def jumpTo(x, y, z): # Zu x|y|z springen
    dType.SetPTPCmdEx(api, 0, x,  y,  z, 0, 1)


def moveDiff(x, y, z): # Relativ um x|y|z bewegen
    dType.SetPTPCmdEx(api, 7, x, y, z, 0, 1)


def initRobot(): # Roboter inintialisieren
    dType.SetPTPJointParamsEx(api, 300, 50, 300, 50, 300, 50, 300, 50, 1)
    dType.SetInfraredSensor(api, 1, 1, 1)
    dType.SetColorSensor(api, 1, 0, 1)
    jumpTo(200, 0, 60)


def getColorSensor(): # Farbe vom Farbsensor holen
    dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)  # ?
    return ([dType.GetColorSensorEx(api, 0), dType.GetColorSensorEx(api, 1), dType.GetColorSensorEx(api, 2)])


def recal(): # Genaueres verfahren zum endpunkt eines Blocks
    while (dType.GetInfraredSensor(api, 1)[0]) == 1:
        setBeltSpeed(-20)
    while (dType.GetInfraredSensor(api, 1)[0]) == 0:
        setBeltSpeed(10)
    setBeltSpeed(10)
    robotSleep(2400)


def measure_color(): # global mapping wrapper für getColorSensor
    global color
    color = getColorSensor()
    return color


def draw_character(character, offsetX, offsetY): # Buchstaben mit dem Zeichensatz in characters und den jeweiligen offsets malen
    char = characters[character]

    jumpTo((characterStart[0] + offsetY),
           (characterStart[1] + offsetX),  characterSafetyHeight)
    moveDiff(char[0][0]*characterScale, char[0][1]*characterScale, 0)
    # Zur Sicherungsposition verfahren
    moveDiff(0, 0, characterStartHeight - characterSafetyHeight)
    # Zum Startpunkt verfahren
    isDrawing = True
    for xy in char[1:]: # Für jede relative koordinate im character array
        if (len(xy) > 2 and isDrawing == True):
            moveDiff(0, 0, 3)
            isDrawing = False
        if (len(xy) == 2 and isDrawing == False):
            moveDiff(0, 0, -3)
            isDrawing = True
        moveDiff(xy[0]*characterScale, xy[1]*characterScale, 0)
    moveDiff(0, 0, characterSafetyHeight - characterStartHeight) # Zurück zur Sicherungsposition verfahren

def draw_string(text, offsetX, offsetY): # String durch Roboter malen
    offset = offsetY
    charArr = []
    for char in text:
        charArr.append(char)
    for c in charArr: # jeden Buchstaben mit einem sich erhöhenden Offset zeichnen
        draw_character(c, offset, offsetX)
        offset += characterScale + numberDistanceY
    return offset # Offset für weitere berechnungen zurückgeben


# def draw_number(number, offsetX, offsetY): # alias für draw_character
#     drawCharacter(str(number), offsetX, offsetY)


def draw_number_color(number, color): # Farbzählerdaten malen
    global offsetR
    global offsetG
    global offsetB

    if color == "red":
        draw_string("rot:" + str(number), 0, 0)
    if color == "green":
        draw_string("grün:" + str(number), -
                    (characterScale*2 + numberDistanceX)*1, 0)
    if color == "blue":
        draw_string("blau:" + str(number),  -
                    (characterScale*2 + numberDistanceX)*2, 0)

# Ausführungslogik


def main():
    # Globale Variablen für die Farbzähler initialisieren
    global red_block_count
    global green_block_count
    global blue_block_count

    initRobot() # Roboter initialisieren
    while False: # Testmodus
        print(dType.GetInfraredSensor(api, 1)[0])
    i = 0
    while True and i < 20*belt_timeout: # Tue so lange bis der Infrarotsensor für mehr als 3 Sekunden nichts erkannt hat 
        i += 1
        if (dType.GetInfraredSensor(api, 1)[0]) == 0:
            setBeltSpeed(50)
        else:
            i = 0
            setBeltSpeed(0) # Band anhalten
            recal()
            block_color = measure_color() # Farbe ist encodiert in einem 1D Array, im Format [wert_rot, wert_grün, wert_blau]
            if block_color[0]:
                red_block_count = red_block_count + 1
            elif block_color[1]:
                green_block_count = green_block_count + 1
            else:
                blue_block_count = blue_block_count + 1
            print(["results:",red_block_count,green_block_count,blue_block_count]) # Zur Kontrolle immer auch die Zähler ausgeben
    setBeltSpeed(0) # Band anhalten

    # Blockzähler malen lassen
    draw_number_color(red_block_count, "red")
    draw_number_color(green_block_count, "green")
    draw_number_color(blue_block_count, "blue")
    # ende

main() # Programmstart

# Gruppenarbeit von Felix Steppeler, Lars Belmann, Malte Stork und Moritz Becker, 
# Abgabe 05.06.2023
# Doc ID: de783e_rev_0.4.1

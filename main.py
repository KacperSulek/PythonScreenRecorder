from PIL import ImageGrab
import cv2
import numpy as np
from tkinter import *

def recScreen():
    image = ImageGrab.grab()
    imgNpArr = np.array(image)
    shape = imgNpArr.shape
    print(shape)

    screenCapWriter = cv2.VideoWriter("screen_recorded.mp4", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 24, (shape[1], shape[0]))
    scaleByPercent = 50
    width = int(shape[1] * scaleByPercent / 100)
    height = int(shape[0] * scaleByPercent / 100)
    newDim = (width, height)

    while True:
        image = ImageGrab.grab()
        imgNpArr = np.array(image)
        finalImg = cv2.cvtColor(imgNpArr, cv2.COLOR_RGB2BGR)

        screenCapWriter.write(finalImg)

        image = cv2.resize(finalImg, (newDim))

        cv2.imshow("image", image)

        if(cv2.waitKey(1) == ord("e")):
            break

    screenCapWriter.release()
    cv2.destroyAllWindows()

screenRec = Tk()
screenRec.geometry("340x220")
screenRec.title("Flender Screen Recorder")

label1 = Label(screenRec, bd=0)
label1.pack()

titleLabel = Label(screenRec, text = "Flender Screen Recorder", font = ("Ubuntu Mono", 16), bg="#02b9e5")
titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
infoLabel = Label(screenRec, text = "Enter 'e' to exit screen recording", bg = "#02b9e5")
screenButton = Button(screenRec, text = "Record Screen", command = recScreen, relief = RAISED)
screenButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)

screenRec.mainloop()


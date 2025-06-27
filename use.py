#!/bin/python3

import cv2 as cv

def rescale(frame, scale):
    height = int(scale * img.shape[0])
    width = int(scale * img.shape[1])
    return cv.resize(frame,(width,height))

#reading video
video = cv.VideoCapture('video.mp4')

while True:
    is_okay, frame = video.read()
    if is_okay != True:
        break

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame,(3,3), cv.BORDER_DEFAULT)
    #frame = cv.Canny(frame,100,100)

    cv.imshow("video", frame)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

#reading image
img = cv.imread("screen.png")

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#gausian blur
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)

#edge cascade - Canny
edges = cv.Canny(img, 125, 175)

#rescaling
scaled = rescale(img, 0.5)

#rectangle
cv.rectangle(img,(25,25),(100,200),(255,255,255))



cv.imshow("image", img)



video.release()
cv.destroyAllWindows()

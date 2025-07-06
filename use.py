#!/bin/python3

import cv2 as cv
import numpy as np



def rescale(frame, scale):
    height = int(scale * img.shape[0])
    width = int(scale * img.shape[1])
    return cv.resize(frame,(width,height))

def translate(img, x, y):
    translation_matrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, dimensions)

def rotate(img, angle, rotation_point=None):
    (height,width)=img.shape[:2]

    if rotation_point == None:
        rotation_point = (width//2,height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

#reading video
video = cv.VideoCapture('video.mp4')

video = cv.VideoCapture(0)

while True:
    is_okay, frame = video.read()
    if is_okay != True:
        break



    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame,(7,7), cv.BORDER_DEFAULT)
    frame = cv.Canny(frame,100,100)
    #frame = translate(frame, 100,100)
    #frame = rotate(frame, 90)

    contours, hierarchies = cv.findContours(frame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


    blank = np.zeros(frame.shape,dtype='uint8')
    cv.drawContours(blank, contours, -1,(255,0,0),3)

    cv.imshow("Contours", blank)


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

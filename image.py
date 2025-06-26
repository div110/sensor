import cv2 as cv

def rescale(frame, scale):
    height = int(scale * img.shape[0])
    width = int(scale * img.shape[1])
    return cv.resize(frame,(width,height))



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


cv.waitKey(0)

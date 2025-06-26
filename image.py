import cv2 as cv

def rescale(frame, scale):
    height = int(scale * img.shape[0])
    width = int(scale * img.shape[1])
    return cv.resize(frame,(width,height))



img = cv.imread("screen.png")

img = rescale(img, 0.5)

cv.rectangle(img,(25,25),(100,200),(255,255,255))


cv.imshow("image", img)


cv.waitKey(0)

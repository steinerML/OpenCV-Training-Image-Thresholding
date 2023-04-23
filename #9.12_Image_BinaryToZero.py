import cv2

'''Binary Thresholding'''
#Read image
image = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)

#Set threshold and maxValue
thresh = 127
maxValue = 255

# #Threshold rule (still don't get this!)
# if image(x,y) > thresh:
#     dst(x,y) = maxValue
# else:
#     dst(x,y) = 0

# Basic threshold example
th, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO)

cv2.imshow('Thresholding', th)
cv2.imshow('Thresholding', dst)
 
cv2.waitKey(0)
cv2.imwrite("binary-tozero-threshold.jpg", dst)
cv2.destroyAllWindows()
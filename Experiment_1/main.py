import cv2 as cv
import numpy as np

#reading the main image
whole_image = cv.imread('all_chars_img.jpg',cv.IMREAD_UNCHANGED)

#reading roger's face image
needle_image = cv.imread('roger_img.jpg',cv.IMREAD_UNCHANGED)

#print(whole_image.shape)
#print(needle_image.shape)

#using matchTemplate function to find the needle_image in the whole_image with the help of Enumerator called TM_CCOEFF_NORMED
result =cv.matchTemplate(whole_image,needle_image,cv.TM_CCOEFF_NORMED)


min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s'%str(max_loc))
print('Best match confidence: %s'%max_val)

print('Best match bottom right position: %s'%str(min_loc))
print('Best match confidence: %s'%min_val)

threshold = 0.95
if max_val >= threshold:
    print('found needle.')

    needle_w = needle_image.shape[1]
    needle_h = needle_image.shape[0]
    top_left = max_loc
    bottom_right = (top_left[0]+needle_w, top_left[1]+needle_h)
    cv.rectangle(whole_image,top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv.LINE_4)


    #cv.imshow('Result',result)
    #cv.waitKey()
    cv.imwrite('result.jpg',whole_image)
else:
    print('needle not found.')
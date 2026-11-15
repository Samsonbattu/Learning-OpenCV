This is my journery of learning OpenCV from scratch. 
Date of start 15-11-2026

# Experiment_1
Every image is a structure with lots of pixels in it. OpenCV uses NumPy to convert those pixels into numbers. We use matchTemplate to match a particular template to the image and find out where the template is hidden within the image. There are lots of enumerators, and we used an enumerator called cv.TM_CCOEFF_NORMED.
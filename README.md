# OpenCV_Various
Variety of OpenCV Codes, scripts, and snippets I made 

# The Directories
## accessAndIndexAllCameras
This directory contains a file called **showAllCameras.py**. This file shows you and your users all cameras that the program can access. It shows you the actual live feed and all associated indices simultaneously. Most importantly it shows the index for each. You know that 0 in cv2.VideoCapture(0)? It shows that. Lets even your users figure out index of each camera with no code, they can find the appropriate index for themselves that you can have them write into a txt file that you call from. Far more convenient than having them reset default webcam or adjusting it in code each time.  

### To Run 
in terminal:

_pip install requirements.txt_    (skip this step if you already have recent versions of numpy and opencv-python, its just those 2 libraries. Works on current versions of those librearies as of May 2021)

_python showAllCameras.py_

And that's it! You can adjust parameters such as font used and image size (in resized_dimensions variable). Lines 187-189 let you choose the display option between vertical, horizontal, and square (see demo pics below). 

square display with pic1.jpg as filler, can replace with a logo or whatever or just leave blank. Square mostly usefule for large sets of cameras. ie if you have 100 camera feeds you can cram it into a 10x10. 
![img_Source](accessAndIndexAllCameras/showAllCameras_square_demo_output.jpg)


Vertical & Horizontal
![img_Source](accessAndIndexAllCameras/showAllCameras_vertical_demo_output.jpg) ![img_Source](accessAndIndexAllCameras/showAllCameras_horizontal_demo_output.jpg)

### Notes 
Obviously programs accessing all your cameras is a bit of a no-no so your antivirus may block access. Use responsibly. 

If you have a lot of cameras you may get FPS drops and lag. 

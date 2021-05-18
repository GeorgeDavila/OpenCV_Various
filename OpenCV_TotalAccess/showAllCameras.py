#Algorithm to show feed of all available cameras 
#Label each with its number that would go into cv2.VideoCapture(0) function 
#maybe a try: except on video cams over indexes until you get a 'no image' error
#or if static feed like just a black screen maybe show that too let user sort out 

import numpy as np
import cv2

'''
Structure:
1) first while loop basically look for working cameras and their indices. 
Exploits the fact that cv2.imshow gives error if active feed is found in a try/except method 

2) Returns a list of active idices, final_camIndexList. Should have length = Number of cameras your device is accessing

3) Create a function cap2img_andimgprocessing(), which turns an i-indexed video feed into a capture. Does the associated image processing. 

4) Last while loop creates list of images - imgList - from these captures, 
which we then horizontally concatenate using cv2.hconcat( imgList ) (just use cv2.vconcat for a vertical concatenation instead)

5) Finally we get a row of all the video feeds your device can access



if you have lots you may want to split imgList and concatenate accordingly. 
For instance for 25 camera feeds you might do a 5x5 split, first 5 in first row, 2nd 5 in 2nd, etc:

rowsOfImagesList = [None] * 5  #such that rowsOfImages[0] = 1st row combined into single image, rowsOfImages[1] = 2nd row, etc

for k in range(5): #iter over list [0,1,2,3,4]
    rowsOfImages[k] = cv2.hconcat( imgList[ k*5 : (k+1)*5 ] )

#Now have a list of lists that contains all rows of images. So rowsOfImages[k] should all be horizontal row of 5 images
#Recall we resize them all to same size, so in the 300x300 resizing we now have a width=1500, height=300 set of 5 images
#Now we just vertically concatenate this to get a square image:

finalSquareMatrixOfImages = cv2.vconcat( rowOfImages )

return finalSquareMatrixOfImages

cv2.imshow( "All 25 camera feeds 5x5", finalSquareMatrixOfImages)



And done! Obviously thats the square image case. concat functions require identically sized image inputs, so if you have 23 you cantjust leave the last 2 out and use this same method. 
What you CAN do is append identically sized (so in this case 300x300) placeholder images to imgList to get a square matrix. 
Then just use this sqaure matrix code. Can even just resize your logo or something to 300x300 and put that in imgList like so:

# path
path1 = "image_folder/my_logo.jpg"
path2 = "image_folder/picture_of_my_dog.jpg"
  
# Using cv2.imread() method
imported_img1 = cv2.imread(path1)
imported_img2 = cv2.imread(path2)

imported_img1 = cv2.resize(imported_img1, resized_dimensions, interpolation = cv2.INTER_AREA)
imported_img2 = cv2.resize(imported_img2, resized_dimensions, interpolation = cv2.INTER_AREA)
  
# Append them to imgList
imgList.append(imported_img1)
imgList.append(imported_img2)

Done! Even turned this into a bit more general of a function getSquareMatrixOfImages() below! I'll leave it up here 
as well as it shows nicely how you can make a concatenation of any size. Can even do it with arbitrary number of 
rows in a square matrix and just crop out excess 

'''

# ================== START ALL PARAMETERS ================== 
#all the parameters are defined in this section
#Font stuff:
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30) #pixel value text placed at 
font_color = (0, 0, 255)
thickness = 2
font_scale = 1

#Resizing:
width = 300
height = 300
resized_dimensions = (width, height) #(width, height) the size we make the images for the concatenation in the final while loop 

open("mainCameraIndex.txt", "r")

#^make bigger if you want bigger display, smaller if you want it smaller (maybe you have 100 cams and want to queeze them in)
#WARNING: PNG's have transparency layer, so can't concatenate those to jpg's without either removing those layers from pngs or dding to jpg. 
#Generally similar cams should use same format, but definitely some wierd camera setups out there. 
#So if you're getting a 'must be similar size' error on concatenation functions a wierd setup like that is probably why 
# ================== END ALL PARAMETERS ================== 


#WHEN i try cv2.VideoCapture( 2 ) I get erro message and no feed, since i only have 2 cams on this device (indexed 0 & 1)
#SO ill try a try/except method, where exception throws all found cams into list and goes from there
#SPECIFICALLY it fails at cv2.imshow function, so might need to alter if you alter what function you use for that 

#get list of indexes that work (should be same number as number of cams the software can access on your device )
camIndexList = []
camera_feed_index = 0

while 1:
    cap = cv2.VideoCapture( camera_feed_index )
    #print(camera_feed_index)
    
    # Get individual frame
    ret, img = cap.read()
    img = cv2.flip(img,1)
    try:
        cv2.imshow("try except while loop image (press Esc to exit)", img)
        camIndexList.append(camera_feed_index)
    except:
        final_camIndexList = camIndexList
        print("Hit last camera! Here's the indices that work: " + str( final_camIndexList ))
        break 
    camera_feed_index += 1
#^Close these windows, generated to test during the try except method 
cap.release()
cv2.destroyAllWindows()
#^will see gray screen this imshow function uses. That function generates the error which we exploit in the try except method, so acceptable 

print("final_camIndexList = " + str( final_camIndexList ) + "This should equal number of cameras the software can access on your device. Number of accessible cameras = " + str( len(final_camIndexList) ) + " <--- If this number is wrong check permissions and that nothing is blocking camera access.")
#Note: obviously software accessing cams is big no no so antivirus or something might block some cams from being accessed, keep in mind act accordingly. 

#resized_dimensions = (300,300) #(width, height)
#NEED images to be same size for concatenation. So if different feeds give different size this will fix it. 
#Although if one is png those have transparency layer. Convert to jpg or add empty transparency layer to jpgs
#Make smaller if you have lots of cams 

capList = [ cv2.VideoCapture( i ) for i in final_camIndexList] 
#^NEED to generate this before while loop, otherwise will redefined cap each time, thus turning off camera and greatly reducing FPS, increasing lag 
#dont want to update cap or capList, hence we leave out of while loop  

#see how its called in while loop for example of usage 
def cap2img_andimgprocessing( capture, index ):
    '''can put in a pure capture, as denoted.
    Here index used for labelling only (rather than calling the capture). This is so we dont need a list of captures. 
    index = name of capture, effectively. Call it index to align with usage below 
    '''
    ret, img = capture.read()
    img = cv2.flip(img,1)
    cv2.putText(img, "camera capture source: " + str(index), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    img = cv2.resize(img, resized_dimensions, interpolation = cv2.INTER_AREA)

    return img

def makePlaceholderImage(path=None):#specify local path to image as string. If none found we'll make one using OpenCV, None is default
    path = str( path )
    try:
        imported_img = cv2.imread( path )
        imported_img = cv2.resize(imported_img, resized_dimensions, interpolation = cv2.INTER_AREA)
        placeholder_img = imported_img
    except: #if it cant read an image from your specified path
        blank_image = np.zeros((height,width,3), np.uint8) 
        blank_image = cv2.resize(blank_image, resized_dimensions, interpolation = cv2.INTER_AREA)
        placeholder_img = blank_image

    return placeholder_img
    

def getSquareMatrixOfImages(imgList, path2pic=None): #can specify path here too, default is None
    #ie if its not an integer or empty it then defaults to nearest square larger than len(imgList)
    import math
    numberOfRows = math.ceil( math.sqrt( len(imgList) ) )
    numImagesToAppend = numberOfRows**2 - len( imgList )  #ie square matrix needs to be size of next perfect square 
    for i in range(numImagesToAppend):
        imgList.append( makePlaceholderImage(path2pic) )

    rowsOfImages = [None] * numberOfRows
    for k in range(numberOfRows): #iter over list [0,1,2,3,..., numberOfRows]
        rowsOfImages[k] = cv2.hconcat( imgList[ k*numberOfRows : (k+1)*numberOfRows ] )

    #Now have a list of lists that contains all rows of images. So rowsOfImages[k] should all be horizontal row of 5 images
    #Recall we resize them all to same size, so in the 300x300 resizing we now have a width=1500, height=300 set of 5 images
    #Now we just vertically concatenate this to get a square image:

    finalSquareMatrixOfImages = cv2.vconcat( rowsOfImages )

    return finalSquareMatrixOfImages

while 1:
    # Update images 
    imgList = [None]*len(final_camIndexList) #get this one since concatenation function takes list of images anyway 

    for i in final_camIndexList:
        imgList[i] = cap2img_andimgprocessing( capture=capList[i] , index=i )
    
    #OPTIONS - uncomment whichever one of these 3 you want to use, only 1 though 
    combinedCameraFeeds = cv2.vconcat( imgList ) #vertical concatenation
    #combinedCameraFeeds = cv2.hconcat( imgList ) #horizontal concatenation
    #combinedCameraFeeds = getSquareMatrixOfImages(imgList, path2pic='pic1.jpg') #square 

    #i like horizontal personally. Square not really needed unless you have lots of camera feeds 

    #cv2.imshow("Video from cameras (press Esc to exit)", img_vertical_concatenation)
    cv2.imshow("Video from cameras combined (press Esc to exit)", combinedCameraFeeds)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release video
cap.release()
cv2.destroyAllWindows()

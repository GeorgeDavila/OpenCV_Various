#Collection of random functions used during program creation. Most works and does something, not necessarily everything desired, hence why they are here.
#Everything below this line, including comments, are as-is old stuff. Might be of some help with something or another. 
#--------------------------------------------------------------------------------------------

#Algorithm to show feed of all available cameras 
#Label each with its number that would go into cv2.VideoCapture(0) function 
#maybe a try: except on video cams over indexes until you get a 'no image' error
#or if static feed like just a black screen maybe show that too let user sort out 

import numpy as np
import cv2

#for i in 
#camera_feed_index = 1



#font stuff
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30) #pixel value text placed at 
font_color = (0, 0, 255)
thickness = 2
font_scale = 1


'''def showcamerafeed(camIndex): 
    camIndex = int(camIndex)
    cap = cv2.VideoCapture( camIndex )

    while 1:
        # Get individual frame
        ret, img = cap.read()
        img = cv2.flip(img,1)

        cv2.putText(img, "camera_feed_index = " + str(camIndex), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
        
        cv2.imshow("Video from camera feed number " + str(camIndex) + " (press Esc to exit)", img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release video
    cap.release()
    cv2.destroyAllWindows()


showcamerafeed( camIndex=0 )
showcamerafeed( camIndex=1 )
'''

#Concatenate 2 cams: 
'''
cap1 = cv2.VideoCapture( 0 )
cap2 = cv2.VideoCapture( 1 )

while 1:
    # Get individual frames
    ret1, img1 = cap1.read()
    img1 = cv2.flip(img1,1)

    ret2, img2 = cap2.read()
    img2 = cv2.flip(img2,1)

    cv2.putText(img1, "camera_feed_index = " + str(0), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    cv2.putText(img2, "camera_feed_index = " + str(1), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    
    resized_dimensions = (300,300) #(width, height)
    img1 = cv2.resize(img1, resized_dimensions, interpolation = cv2.INTER_AREA)
    img2 = cv2.resize(img2, resized_dimensions, interpolation = cv2.INTER_AREA)
    #NEED to be resized to same dimensions for concatenation to work 
    
    #img_vertical_concatenation = cv2.vconcat([img1, img2])
    img_horizontal_concatenation = cv2.hconcat([img1, img2])

    #cv2.imshow("Video from cameras (press Esc to exit)", img_vertical_concatenation)
    cv2.imshow("Video from cameras (press Esc to exit)", img_horizontal_concatenation)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release video
cap.release()
cv2.destroyAllWindows()
'''

#WHEN i try cv2.VideoCapture( 2 ) I get erro message and no feed, since i only have 2 cams on this device (indexed 0 & 1)
#SO ill try a try/except method, where exception throws all found cams into list and goes from there
#SPECIFICALLY it fails at cv2.imshow function, so might need to alter if you alter what function you use for that 

#get list of indexes that work (should be same number as number of cams the software can access on your device )
camIndexList = []
camera_feed_index = 0

while 1:
    cap = cv2.VideoCapture( camera_feed_index )
    print(camera_feed_index)
    
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
cap.release()
cv2.destroyAllWindows()

print("final_camIndexList = " + str( final_camIndexList ) + "This should equal number of cameras the software can access on your device. Number of accessible cameras = " + str( len(final_camIndexList) ) + " <--- If this number is wrong check permissions and that nothing is blocking camera access.")
#Note: obviously software accessing cams is big no no so antivirus or something might block some cams from being accessed, keep in mind act accordingly. 

#Fulfills basic purpose, shows all cams at once. Just slower since flashes on/off. Want to fix that 
'''
camIndexList = []
camera_feed_index = 0

while 1:
    cap = cv2.VideoCapture( camera_feed_index )
    print(camera_feed_index)
    
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

while 1:
    # Get individual frames
    #capList = [None]*len(final_camIndexList)
    imgList = [None]*len(final_camIndexList) #get this one since concatenation function takes list of images anyway 

    for i in final_camIndexList:
        #capList[i] = cv2.VideoCapture( i )
        cap_i = cv2.VideoCapture( i )
        ret, img = cap_i.read()
        img = cv2.flip(img,1)

        cv2.putText(img, "camera_feed_index = " + str(i), org, font, font_scale, font_color, thickness, cv2.LINE_AA)

        resized_dimensions = (300,300) #(width, height) 
        #NEED to be resized to same dimensions for concatenation to work, one cam puts in diff size some reason this will fix that 
        img = cv2.resize(img, resized_dimensions, interpolation = cv2.INTER_AREA)

        imgList[i] = img
    
    #img_vertical_concatenation = cv2.vconcat( imgList )
    img_horizontal_concatenation = cv2.hconcat( imgList )

    #cv2.imshow("Video from cameras (press Esc to exit)", img_vertical_concatenation)
    cv2.imshow("Video from cameras combined (press Esc to exit)", img_horizontal_concatenation)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release video
cap.release()
cv2.destroyAllWindows()
'''

resized_dimensions = (300,300) #(width, height) 
'''
def image_processing_func( captureIndex ): 
    captureIndex = int(captureIndex)
    cap_i = cv2.VideoCapture( captureIndex )
    ret, img = cap_i.read()
    img = cv2.flip(img,1)
    cv2.putText(img, "camera_feed_index = " + str(captureIndex), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    img = cv2.resize(img, resized_dimensions, interpolation = cv2.INTER_AREA)

    return img

#alt method 
def image_processing_func( captureIndex ): 
    captureIndex = int(captureIndex)
    cap_i = cv2.VideoCapture( captureIndex )
    ret, img = cap_i.read()
    img = cv2.flip(img,1)
    cv2.putText(img, "camera_feed_index = " + str(captureIndex), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    img = cv2.resize(img, resized_dimensions, interpolation = cv2.INTER_AREA)

    return img

def cap2image_andimgprocessing( capture ):
    ret, img = capture.read()
    img = cv2.flip(img,1)
    cv2.putText(img, "camera capture source: " + str(capture), org, font, font_scale, font_color, thickness, cv2.LINE_AA)
    img = cv2.resize(img, resized_dimensions, interpolation = cv2.INTER_AREA)

    return img
#capList = [cv2.VideoCapture( j ) for j in final_camIndexList ]
'''
'''
#iter structure causing collapses in OpenCV display and thus massive FPS drop
#So lets remove iter by contructing imgList as sting then only do eval() once all for loops have been done 

imgList = str( ["eval(" + "image_processing_func(" +  str(i) + ") )" for i in final_camIndexList] )
print(imgList)
#imgList = eval(imgList_string)

while 1:
    # Get individual frames
    #capList = [None]*len(final_camIndexList)
    #imgList = [None]*len(final_camIndexList) #get this one since concatenation function takes list of images anyway 
    
    #img_vertical_concatenation = cv2.vconcat( imgList )
    img_horizontal_concatenation = cv2.hconcat( imgList )

    #cv2.imshow("Video from cameras (press Esc to exit)", img_vertical_concatenation)
    cv2.imshow("Video from cameras combined (press Esc to exit)", img_horizontal_concatenation)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release video
cap.release()
cv2.destroyAllWindows()
'''


'''while 1:
    capList = [None]*len(final_camIndexList)
    imgList = [None]*len(final_camIndexList)
    # Get individual frames
    print("step 1")
    #capList = [cv2.VideoCapture( j ) for j in final_camIndexList ]
    print("step 2")


    imgList = [cap2image_andimgprocessing( myCapture )  for myCapture in capList ]
    
    #img_vertical_concatenation = cv2.vconcat( imgList )
    img_horizontal_concatenation = cv2.hconcat( [cap2image_andimgprocessing( myCapture )  for myCapture in [cv2.VideoCapture( 0 ), cv2.VideoCapture( 1 )] ] )
    print("step 3")
    #cv2.imshow("Video from cameras (press Esc to exit)", img_vertical_concatenation)
    cv2.imshow("Video from cameras combined (press Esc to exit)", img_horizontal_concatenation)
    print("step 4")
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release video
cap.release()
cv2.destroyAllWindows()
'''



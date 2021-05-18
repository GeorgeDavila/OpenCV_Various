#Show Selected Camera feed indexed via the tkinter app and label stored in selectedCameraIndex.txt
import cv2


def sample_function(img_input):
    '''
    Example/Placeholder Operation. Just replace with whatever function you want to apply.
    Here we just make it gray.
    '''
    gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
    return gray


#If some error is retrieved it defaults to default camera index 0
#Entire file open operation included since in real app might have txt file displaced or otherwise producing error. Want to avoid that error. Modify according to your needs. 
try: 
    selectedCameraIndex_file = open("selectedCameraIndex.txt", "r")
    selectedCameraIndex = selectedCameraIndex_file.read()
    selectedCameraIndex_file.close
    selectedCameraIndex = int(selectedCameraIndex)
except:
    selectedCameraIndex = 0 


cap = cv2.VideoCapture( selectedCameraIndex )

while 1:
    ret, img = cap.read()
    img = cv2.flip(img,1)

    img = sample_function(img) #Just comment this function out to remove it
    
    cv2.putText(img, "Index of Camera Shown = " + str(selectedCameraIndex), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (3, 252, 252), 2, cv2.LINE_AA)

    cv2.imshow('The Camera You Selected (Esc to exit)', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break





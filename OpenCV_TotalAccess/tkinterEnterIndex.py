#Tkinter app to change selected index in selectedCameraIndex.txt 

from tkinter import *

window = Tk()
window.title("Put index of Camera here")
#window.iconphoto(False, tk.PhotoImage(file='icons/mn.png'))
window.geometry('800x400')


text1 = Label(window, text= "Enter Index of Camera you want to view as number. (0, 1, 2, etc.)")
text1.grid(column=0, row=0) 

index_input = Entry(window,width=30, bd =5)  
index_input.grid(column=0, row=1) 

def writeindex2file():
    indexfile_write = open("selectedCameraIndex.txt" , "w") #write only will replace whatever is in file 
    index_write = indexfile_write .write( str( index_input.get() ) )
    indexfile_write.close()
    text2 = Label(window, text= "Index = " + str( index_input.get() ) + "  Was written to the file!")
    text2.grid(column=0, row=3) 

btn2 = Button(window, text="PUSH THIS to write index to File selectedCameraIndex.txt", bg="red", command=writeindex2file )
btn2.grid(column=0, row=2)  

window.mainloop()
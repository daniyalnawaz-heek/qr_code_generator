
#importing module PIL(pillow qrcode)
import PIL 
import qrcode

#taking input of data
information=input("enter the info:\t")

#taking input of file name
name=input("enter the file name in which you have to store:\t")

#finalizing file name as png
file_name =  name+".png"

#creating qrcode for info
image=qrcode.make(information)

#storing the qrcode in the input filename
image.save(file_name)



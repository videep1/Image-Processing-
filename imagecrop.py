from PIL import Image
left=int(input("pixels left:"))
upper=int(input("pixels upper:"))
right=int(input("pixels right:"))
lower=int(input("pixels lower:"))
img_path=str(input("enter image adress:"))
open_img =Image.open(img_path)
crop_image=open_img.crop((left,upper,right,lower)) 
crop_image.show()
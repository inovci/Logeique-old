import os
from PIL import Image
resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


max_height= 1200
max_width= 1200
extensions= ['PNG','JPG']

path= os.path.abspath("C:/Users/XC-DEV-3/Documents/projet soutenance/logeique2/media/img/houses")
print(path)

def adjusted_size(width,height):
    if width>max_width or height>max_height:
        if width>height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width,height

	
if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].upper()
            if f_ext in extensions:
                print (f)
                image = Image.open(os.path.join(path,f))
                width, height= image.size
                image = image.resize(adjusted_size(540, 304))
                image.save(os.path.join(path,f))
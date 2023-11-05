from PIL import Image
import os
import time

# Script extrects aplha channel and saves it to separate file as mask.


def create_mask():
   for f in os.listdir('.'):
     if f.endswith('.png'):
        i = Image.open(f).convert('RGBA')
        alpha = i.getchannel("A")
        fn, text = os.path.splitext(f)
        alpha.save('masks/{}_mask.png'.format(fn))

        print(f+" is done")
       
     elif  0==f.endswith('.png'):
        continue
    
     else:
        print("no files found")
        
if  not os.path.exists("./masks"):
    os.mkdir("./masks")
    create_mask()

else:
    create_mask()
print("Done!")
time.sleep(4)
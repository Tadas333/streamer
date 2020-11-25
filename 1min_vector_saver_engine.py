import cv2
import numpy as np 
import glob, os 
import time
import shutil 

path1 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/outputs/vid1.mp4'

path2 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/vectordir/video0.mp4'
f = 0


while(1):
    video = path1
    
    

    path2 = list(path2)

    f += 1
    

    path2[65] = f   
    #path2 = str(path2) 
    #path3 = "".join(path2)
    path3 = ''.join(map(str, path2))
    
    shutil.copy2(video, path3)
    time.sleep(60)
    

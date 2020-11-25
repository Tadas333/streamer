import cv2
import numpy as np 
import glob, os 
import time
import shutil 
from pathlib import Path
import pathlib
from os import listdir
from os.path import isfile, join

path13 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/vectordir'
path2 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/streamer'
path3 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/recordings'
path4 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/recordings/video1.mp4'
f = 0
count = 0
while(1):
    
    path1 = 'C:/Users/tadas/Desktop/Jenop_soft_pit/Apache_site/vectordir'
    for vinput in glob.glob(os.path.join(path1, '*.mp4')):
        path11 = pathlib.PurePath(vinput)
        video = vinput
        #print("path11 =", path11.name)
        double = False

        for vinput2 in glob.glob(os.path.join(path3, '*.mp4')):
            path33 = pathlib.PurePath(vinput2)
            #print("path33 =",path33.name)
            

            if path33.name == path11.name:                
                #print("skip")
                #continue
                double = True
            

        if double == True:
            print("skip")
            continue
        else:
            shutil.copy2(video, path2)
            print('no skip')

            time.sleep(60)    
            for vinputt in glob.glob(os.path.join(path2, '*.mp4')):
                streamervid = vinputt
                shutil.move(streamervid, path3)

    recs = [f for f in listdir(path3) if isfile(join(path3, f))]
    print("files in recodings", len(recs))
    if (len(recs)) % 10 == 0:
        
            

    
        


            


    

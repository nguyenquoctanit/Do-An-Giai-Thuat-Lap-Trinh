mytime = 3

import glob
from datetime import datetime, timedelta
import cv2
import shutil
import os
from TOAN import Test

path = Test.getPath('Thu muc Cam1 NG') + '*.jpg'
path_1 = Test.getPath('Thu muc Cam2 OK')
path_2 = Test.getPath('Thu muc SAVE')

for i in glob.glob(path):
    print(i)


    for b in reversed(range(len(i))):
        if i[b] == "\\":
            position = b
            break 
    
    name = i[(position+1):]

    group = name[11:].split("-")

    string_date = ":".join(group[:-2])

    mydate = datetime.strptime(string_date, "%H:%M:%S" )
    for t in range(mytime+1):
        abc = i[(position+1):(position+12)] + (mydate + timedelta(seconds=t)).strftime('%H-%M-%S')
        n_path = path_1+ abc
        format_data = "%y/%m/%d %H:%M:%S"
        all_path_1 = glob.glob(path_1+"*.jpg")

        for o in all_path_1:

            if n_path[-19:] == o[-34:-15]:
                print('ok')
                shutil.copy(o, path_2 + abc + o[-15:])

                
            # c_path = "/".join((" ".join(n_path[-19:].split("_"))).split("-"))[-17:-8] + ":".join((" ".join(n_path[-19:].split("_"))).split("-"))[-8:]
            # g_path = "/".join((" ".join(o[-34:-15].split("_"))).split("-"))[-17:-8] + ":".join((" ".join(o[-34:-15].split("_"))).split("-"))[-8:]
            # print(g_path," ", c_path)


            # if datetime.strptime(c_path, format_data) + timedelta(seconds=4) > datetime.strptime(g_path, format_data) :
            #     print('break')
            #     break
  
        


import glob
import os
import shutil
import os
import datetime
import time
path = "D:/20.NQCOMI_RS656/New folder/FILE LABEL/ADD NHAM/ok/*.txt"
time_to_name = lambda: str(datetime.datetime.now()).replace(':', '-').replace(' ', '_').replace('.', '-')

for i in glob.glob(path):
    dir = os.path.dirname(i)
    name_new = time_to_name()
    os.rename(i, dir + '/'+ name_new + '.txt')
    if os.path.exists(i[:-3] + 'jpg'):
        os.rename(i[:-3] + 'jpg', dir + '/'+ name_new + '.jpg')
    time.sleep(0.01)


                    
 

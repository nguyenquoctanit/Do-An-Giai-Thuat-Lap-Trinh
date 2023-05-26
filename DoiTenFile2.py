from glob import glob                                                           
import os
from TOAN import Test
from time import sleep

TM = Test.getPath('Thu muc chua .jpg')
        
fname = glob(TM + '*.jpg')
cnt=0
for filename in fname:
    tenf = Test.time_to_string()
    while os.path.exists(TM + tenf + '.jpg'):
        sleep(0.1)
        tenf = Test.time_to_string()
    os.rename(filename, TM + tenf + '.jpg')
    os.rename(filename[:-3]+'txt', TM + tenf + '.txt')
    cnt += 1
    print(cnt)

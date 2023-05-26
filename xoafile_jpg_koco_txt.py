from glob import glob                                                           
import os
import shutil 
from TOAN import Test
TM = Test.getPath1() 
TM_save = Test.getPath2()  
def xoa_jpg_ko_co_txt(TM):
    txt = glob(TM + '*.jpg')
    c = 0
    for filename in txt:
        tenf = os.path.basename(filename)
        if not os.path.isfile(filename[:-3] +'txt') :
            c+=1
            # os.remove(filename)
            shutil.move(filename,TM_save + tenf)
            print(c , tenf) 
            #break
    print('completed')

def xoa_txt_ko_co_jpg(TM):
    txt = glob(TM + '*.txt')
    c = 0
    for filename in txt:
        tenf = os.path.basename(filename)
        if not os.path.exists(filename[:-3] +'jpg'):
            c+=1
            # os.remove(filename)
            shutil.move(filename,TM_save + tenf)
            #print(tenf) 
            print(c , tenf) 
    print('completed')
    
xoa_jpg_ko_co_txt(TM)
xoa_txt_ko_co_jpg(TM)
        

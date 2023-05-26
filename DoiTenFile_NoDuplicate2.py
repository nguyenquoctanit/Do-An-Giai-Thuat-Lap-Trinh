from glob import glob                                                           
import os
from TOAN import Test

TM1 = Test.getPath('CHON THU MUC DATA')
TM2 = Test.getPath('CHON THU MUC REVIEW')
fname = glob(TM2 + '*.jpg')

for filename in fname:
    tenf = os.path.basename(filename)[:30] + '.jpg'
    cnt = 0
    chk = False
    while os.path.exists(TM1 + tenf):
        cnt += 1
        chk = True
        tenf = tenf[:27] + str(cnt) + 'CD.jpg'
    
    os.rename(filename, TM1 + tenf)
    os.rename(filename[:-3]+'txt', TM1 + tenf[:-3]+'txt')
    print('changed', tenf)
    

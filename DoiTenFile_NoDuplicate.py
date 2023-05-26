from glob import glob                                                           
import os
from TOAN import Test

TM1 = Test.getPath('CHON THU MUC DATA')
TM2 = Test.getPath('CHON THU MUC REVIEW')
fname = glob(TM2 + '*.jpg')

for filename in fname:
    tenf = os.path.basename(filename)
    cnt = 0
    chk = False
    while os.path.exists(TM1 + tenf):
        cnt += 1
        chk = True
        tenf = tenf[:27] + str(cnt) + 'CD.jpg'
        while os.path.exists(TM2 + tenf):
            cnt += 1
            tenf = tenf[:27] + str(cnt) + 'CD.jpg'
    if chk:
        os.rename(filename, TM2 + tenf)
        print('changed', tenf)
    

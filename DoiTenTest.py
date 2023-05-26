from glob import glob                                                           
import os, shutil
from TOAN import Test

TM2 = Test.getPath('CHON THU MUC REVIEW')
fname = glob(TM2 + '*.txt')
os.makedirs(TM2 + 'TEMP', exist_ok=True)
for filename in fname:
    tenf = os.path.basename(filename)
    if len(tenf)>34:
        shutil.move(filename, TM2 + 'TEMP/' + tenf)
        print('moved', tenf)

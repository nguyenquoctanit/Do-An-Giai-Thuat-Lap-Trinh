from glob import glob                                                           
import os
from TOAN import Test

TM = Test.getPath("")
txt = glob(TM + '*.txt')
cnt = len(txt)
os.makedirs(TM + 'TEMP',exist_ok=True)
out = open(TM + 'TEMP/gom.txt','a')
for filename in txt:
    if 'classes' in filename:
        continue   
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0]) == 1:
                out.writelines(line) 
    f.close()
    cnt -= 1
    print(cnt)

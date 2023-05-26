from glob import glob                                                           
import os
from TOAN import Test

TM = Test.getPath('Chua TXT')
txt = glob(TM + '*.txt')
cnt = 0
os.makedirs(TM + 'TEMP', exist_ok=True)
out_dir = TM + 'TEMP/'
for filename in txt:
    tenf = os.path.basename(filename)
    dem = 0
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0]) == 4:
                dem += 1
    f.close()
    #Thay the file
    if dem < 2:
        os.replace(filename, out_dir + tenf)
        os.replace(filename[:-3] + 'jpg', out_dir + tenf[:-3] + 'jpg')
        cnt += 1
        print(cnt)

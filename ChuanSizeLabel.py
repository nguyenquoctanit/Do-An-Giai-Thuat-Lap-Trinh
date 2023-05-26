from glob import glob                                                           
import os
from TOAN import Test

TM = Test.getPath('Chon thu muc chua txt')     
txt = glob(TM + '*.txt')
os.makedirs(TM + 'TEMP', exist_ok=True)
out_dir = TM + 'TEMP/'
cnt = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            # if tmp[0] in ['0','1','2','3','4','5']:
            if int(tmp[0]) == 0:
            # if len(line)<40:
                out.writelines('0 ' + tmp[1] + ' ' + tmp[2] + ' 0.286250 0.154167\n')
            else:
                out.writelines(line)
    f.close() 
    out.close()
    #Thay the file
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt)

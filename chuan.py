from glob import glob                                                           
import os
TM = 'D:/TAN/A17_C1_10_12_2022/'
txt = glob(TM + '*.txt')

os.mkdir(TM + 'TUAN')

out_dir = TM + 'TUAN/'
cnt = len(txt)
c = 0
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            #if float((tmp[0])) >= 1.0 or float((tmp[0])) == 0.0:
            if int((tmp[0])) != 13:
                out.writelines(line)
            #else:
                #out.writelines('16' + line)
                #print('da xoa', tenf)
    f.close()
    c+=1
    print('da xoa nhan', c)

#shutil.rmtree(out_dir)

               
            


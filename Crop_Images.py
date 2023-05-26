from glob import glob                                                           
import shutil, os, cv2
from TOAN import Test
 
TM = Test.getPath('C:/Users/Admin/Desktop/CAM2')
os.makedirs(TM + '/TEMP',exist_ok=True)
img = glob(TM +'*.jpg')
cnt=0
for i in img:

    tenf  = os.path.basename(i)
    image = cv2.imread(i, 1)
    h, w, c = image.shape
    if w == 1600 and h == 1200:
        ROI = image[100:1200, :]
        cv2.imwrite(TM + 'TEMP/' + tenf, ROI)
        out = open(TM + 'TEMP/' + tenf[:-3]+'txt','w')
        with open(i[:-3]+'txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                tmp = line.split()
                y = round(float(tmp[2])*1200/1100 - 100/1100,6)
                h = round(float(tmp[4])*1200/1100,6)
                out.writelines(tmp[0] + ' ' + tmp[1] + ' ' + str(y) + ' ' + tmp[3] + ' ' + str(h) + '\n') 
        f.close()
        out.close()
        cnt += 1
        print(cnt)
print('Completed!')

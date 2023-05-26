from glob import glob
import os
from TOAN import Test

TM = Test.getPath('Chon Thu mua chua JPG')
img = glob(TM + "*.jpg")

for filename in img:
    tenf = os.path.basename(filename)
    if not os.path.exists(filename[:-3] + "txt"):
        print(tenf)
print("Finished!")

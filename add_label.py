import glob
for i in glob.glob('D:/20.NQCOMI_RS656/CAM2/413/*.jpg'):
    path = i[:-4] + '.txt'
    with open(path,'a') as f:
        f.write('4 0.465313 0.640417 0.794375 0.322500')
        f.write('\n')
      
  






# 8 0.515625 0.454583 0.570000 0.777500
# 9 0.513437 0.880833 0.580625 0.073333

















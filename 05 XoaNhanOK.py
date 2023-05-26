# import glob
# path = '//D8810421/a47-a19-a02-09_09_2022/A47_A19/A47_A19_C2_12_09_2022/vu/v2/A47_A19_C2_27_10_2022/*.txt'
# list_coordinates = []

# for path_i in glob.glob(path):
#     print(path_i)

#     with open(path_i, 'r') as file :
#         Lines = file.readlines()
#     list_num = []
#     for line in Lines:
#         list_num.append(line.strip().split()[0])
#     if '3' not in list_num:
#         with open(path_i,'a') as f:
#             f.write('3 0.489844 0.451042 0.664062 0.618750')
#             f.write('\n')



# import glob
# path = '//D8810421/a47-a19-a02-09_09_2022/A47_A19/A47_A19_C2_12_09_2022/vu/v2/A47_A19_C2_27_10_2022/*.txt'
# for path_i in glob.glob(path):


#     with open(path_i,'a') as f:
#         f.write('9 0.184375 0.753125 0.056250 0.447917')
#         f.write('\n')
#         f.write('9 0.795312 0.776042 0.056250 0.447917')
#         f.write('\n')
#         f.write('7 0.492969 0.755208 0.314063 0.231250')
#         f.write('\n')
#         f.write('8 0.489844 0.936458 0.251563 0.1270830')
#         f.write('\n')
        # f.write('12 0.492969 0.652083 0.351562 0.212500')
        # f.write('\n')


# 9 0.184375 0.753125 0.056250 0.447917
# 9 0.795312 0.776042 0.056250 0.447917
# 7 0.492969 0.755208 0.314063 0.231250
# 8 0.489844 0.936458 0.251563 0.127083



# path = '//D8810421/a47-a19-a02-09_09_2022/A47_A19/A47_A19_C2_12_09_2022/vu/v2/A47_A19_C2_27_10_2022/*.txt'

# C:/10005TOAN/X75/TRANG/C1/BC3
from TOAN import Test
import os
path = Test.getPath1()  + '*.txt'
cnt = 0
import glob 
for i in glob.glob(path):
    tenf = os.path.basename(i)
    if tenf == 'classes.txt' and tenf == 'lastclasses.txt':
        continue
    #print(i)
    file = open(i, 'r')
    Lines = file.readlines()
    names = []
    files = []
    for line in Lines:
        num = line.split()[0]
        names.append(num)
        #print(names)
    
    outers =  ['4','5','6','7']  
    inners = ['0','1','2','3']

    for inner in inners: 
        for outer in outers:
            if inner in names and outer in names:
                for index,line in enumerate(Lines):      
                    if line.strip().split()[0] == outer:
                        myindex =0
                        x4 = float(line.strip().split()[1])
                        y4 = float(line.strip().split()[2])
                        w4 = float(line.strip().split()[3])
                        h4 = float(line.strip().split()[4])
                        xmin = x4 - w4/2
                        xmax = x4 + w4/2
                        ymin = y4 - h4/2
                        ymax = y4 + h4/2
                        myindex = index 
                        #print(myindex)
                        break
                for line in Lines:   
                    if line.strip().split()[0] == inner:
                        x0 = float(line.strip().split()[1])
                        y0 = float(line.strip().split()[2])
                        w0 = float(line.strip().split()[3])
                        h0 = float(line.strip().split()[4])
                        #bui chi 0.013750 0.018333
                        #divat 0.025000 0.033333
                        if w0 > 0.200/3 or h0 > 0.323/3:
                            if xmin < x0 < xmax  and ymin < y0 < ymax:
                                for index,line in enumerate(Lines):  
                                    if line.strip().split()[0] == outer and index == myindex:
                                        files.append(line)
                with open(i, 'w') as f:
                    for line in Lines:
                        if line not in files:
                            #print('HAHA')
                            f.write(line)
                        else:
                            cnt += 1 
                            print('HAHA', cnt)

            if inner in names and outer in names:
                for index,line in enumerate(Lines):      
                    if line.strip().split()[0] == outer:
                        myindex =0
                        x4 = float(line.strip().split()[1])
                        y4 = float(line.strip().split()[2])
                        w4 = float(line.strip().split()[3])
                        h4 = float(line.strip().split()[4])
                        xmin = x4 - w4/2
                        xmax = x4 + w4/2
                        ymin = y4 - h4/2
                        ymax = y4 + h4/2
                        myindex = index 
                        #print(myindex)
        
                for line in Lines:   
                    if line.strip().split()[0] == inner:
                        x0 = float(line.strip().split()[1])
                        y0 = float(line.strip().split()[2])

                        w0 = float(line.strip().split()[3])
                        h0 = float(line.strip().split()[4])
                        #bui chi 0.142375 0.1896666
                        #divat 0.025000 0.033333
                        if w0 > 0.200/3 or h0 > 0.323/3:
                            if xmin < x0 < xmax  and ymin < y0 < ymax:
                                for index,line in enumerate(Lines):  
                                    if line.strip().split()[0] == outer and index == myindex:
                                        files.append(line)
                with open(i, 'w') as f:
                    for line in Lines:
                        if line not in files:
                            #print('HAHA')
                            f.write(line)
                        else:
                            cnt += 1 
                            print('HAHA', cnt)              

# cacbon 0
# buichi 1 
# divat 2
# chaudien 3
# taychoi 4
# 2 5
# 3 6
# 4 7
# 6 8
# 7 9
# 9 10
# 10 11


# me_duoi   0
# divat     1 
# me        2
# nc1_ok    3
# namchamcao 4
# nut       5
# nc2_ok    6
# day_ok    7
# bt_ok     8
# kim_ok    9
# tray_bt   10







# import glob 
# path = '//D9140522/Chung/Hieu/A47_A19_C2_NG_4-5-6_11_2022_Vu/*.txt'
# for i in glob.glob(path):
#     #print(i)
#     file = open(i, 'r')
#     Lines = file.readlines()
#     # names = []
#     # files = []
#     # for line in Lines:
#     #     num = line.strip()[0]
#     #     names.append(num)
    
#     # outer = '3'  #(3,6)
#     inner = '1' #(1,2,5)
#     # if inner in names and outer in names:
#         # for index,line in enumerate(Lines):      
#         #     if line.strip()[0] == outer:
#         #         myindex =0
#         #         x4 = float(line.strip().split()[1])
#         #         y4 = float(line.strip().split()[2])
#         #         w4 = float(line.strip().split()[3])
#         #         h4 = float(line.strip().split()[4])
#         #         xmin = x4 - w4/2
#         #         xmax = x4 + w4/2
#         #         ymin = y4 - h4/2
#         #         ymax = y4 + h4/2
#         #         myindex = index 
#         #         #print(myindex)
#         #         break

#     for line in Lines:   
#         if line.strip()[0] == inner:
#             x0 = float(line.strip().split()[1])
#             y0 = float(line.strip().split()[2])
#             w0 = float(line.strip().split()[3])
#             h0 = float(line.strip().split()[4])

#             if 0 < w0*640 < 15  and 0 < h0*480 < 15 and 0.328< x0 < 0.578 and 0.874 < y0 < 1:
#                 with open(i, 'a') as f:
#                     f.write('8 0.449219 0.936458 0.251563 0.127083')
#                     f.write('\n')


#             # if 0 < w0*640 < 50  and 0 < h0*480 < 50:
#             #     print('a')
#             #     if 0.117< x0 < 0.284 and 0.143 < y0 <0.771:
                    
#             #         with open(i, 'a') as f:
#             #             f.write('3 0.201563 0.453125 0.168750 0.627083')
#             #             f.write('\n')

#             #     if 0.284< x0 < 0.45 and 0.143 < y0 <0.771:
                    
#             #         with open(i, 'a') as f:
#             #             f.write('6 0.368750 0.453125 0.165625 0.627083')
#             #             f.write('\n')


#             #     if 0.45< x0 < 0.617 and 0.143 < y0 <0.771:
                    
#             #         with open(i, 'a') as f:
#             #             f.write('6 0.533594 0.453125 0.167187 0.631250')
#             #             f.write('\n')

#             #     if 0.617< x0 < 0.784 and 0.143 < y0 <0.771:
                    
#             #         with open(i, 'a') as f:
#             #             f.write('3 0.700781 0.453125 0.167187 0.635417')
#             #             f.write('\n')



#0.143  0.771

# 3 0.201563 0.453125 0.168750 0.627083

# 6 0.368750 0.453125 0.165625 0.627083
# 6 0.533594 0.453125 0.167187 0.631250

# 3 0.700781 0.453125 0.167187 0.635417


import glob 
path = r"C:\Users\Admin\Desktop\Cam4_RS656_line17_Manh_sua\A17_C4_2023_05_12\*.txt"



pixel_truc_y = 56/2048 # pixel tien muon dich/pixel chieu dai cua anh

for i in glob.glob(path):
    print(i)
    file = open(i, 'r')
    Lines = file.readlines()
    mydel = []
    myadd =[]
    names = []
    for line in Lines:
        num = line.strip().split(' ')[0]
        names.append(num)
    if '17' in names:
        for line in Lines:      
            if line.strip().split(' ')[0] == '17':
                x4 = float(line.strip().split(' ')[1])
                y4 = float(line.strip().split(' ')[2])
                if y4 < 0.5:
                    y4 = float(line.strip().split(' ')[2]) - pixel_truc_y/2
                    w4 = float(line.strip().split(' ')[3])
                    h4 = float(line.strip().split(' ')[4]) - pixel_truc_y
                    mydel.append(line)
                if y4 > 0.5:
                    y4 = float(line.strip().split(' ')[2]) + pixel_truc_y/2
                    w4 = float(line.strip().split(' ')[3])
                    h4 = float(line.strip().split(' ')[4]) - pixel_truc_y
                    mydel.append(line)
                myadd.append(f'17 {str(x4)} {str(y4)} {str(w4)} {str(h4)} \n')

    with open(i, 'r') as file:
        filedata = file.read()

    #print(mydel)
    #print(f'0 {str(x4)} {str(y4)} {str(w4)} {str(h4)}')
    # if '17' in names:
    for mdel,madd in zip(mydel,myadd):
        filedata = filedata.replace(mdel, madd)

    with open(i, 'w') as file:
        file.write(filedata)

            
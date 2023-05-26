import os, shutil, keyboard, subprocess, sqlite3
from datetime import datetime

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def time_to_name():
    date_string = f'{datetime.now():%Y-%m-%d_%H-%M-%S-%f}'
    return date_string

def copy_data(spath):
    TM = os.getcwd()
    if os.path.isdir(TM + '/train'):
        shutil.rmtree(TM + '/train')
    if os.path.isdir(TM + '/valid'):
        shutil.rmtree(TM + '/valid')
    # Copy lại data mới đã chia
    shutil.copytree(spath + '/train', TM + '/train')
    shutil.copytree(spath + '/valid', TM + '/valid')
    
def make_yaml(cls, spath):
    myclasses5 = []
    texts5 = cls.split(',')
    for text in texts5:
        myclasses5.append(text)

    with open(os.getcwd() + '/levu/data.yaml', "w") as f:
        f.write('train: ' + os.getcwd() + '/train/images\n')
        f.write('val: ' + os.getcwd() + '/valid/images\n')
        f.write('nc: '  + str(len(myclasses5)) + '\n')     
        f.write('names: '  + str(myclasses5))     

    with open(os.getcwd() + '/levu/models/levu.yaml', "w") as f:
        f.write('nc: ' +  str(len(myclasses5)) + '\n' + 
                'depth_multiple: 0.33  # model depth multiple' + '\n' + 
                'width_multiple: 0.50  # layer channel multiple' + '\n' + 
                'anchors:' + '\n' + 
                '  - [10,13, 16,30, 33,23]  # P3/8' + '\n' + 
                '  - [30,61, 62,45, 59,119]  # P4/16' + '\n' + 
                '  - [116,90, 156,198, 373,326]  # P5/32' + '\n' + 

                'backbone:' + '\n' + 

                '  [[-1, 1, Conv, [64, 6, 2, 2]],  # 0-P1/2' + '\n' + 
                '   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4' + '\n' + 
                '   [-1, 3, C3, [128]],' + '\n' + 
                '   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8' + '\n' + 
                '   [-1, 6, C3, [256]],' + '\n' + 
                '   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16' + '\n' + 
                '   [-1, 9, C3, [512]],' + '\n' + 
                '   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32' + '\n' + 
                '   [-1, 3, C3, [1024]],' + '\n' + 
                '   [-1, 1, SPPF, [1024, 5]],  # 9' + '\n' + 
                '  ]' + '\n' + 

                'head:' + '\n' + 
                '  [[-1, 1, Conv, [512, 1, 1]],' + '\n' + 
                "   [-1, 1, nn.Upsample, [None, 2, 'nearest']]," + '\n' + 
                '   [[-1, 6], 1, Concat, [1]],  # cat backbone P4' + '\n' + 
                '   [-1, 3, C3, [512, False]],  # 13' + '\n' + 

                '   [-1, 1, Conv, [256, 1, 1]],' + '\n' + 
                "   [-1, 1, nn.Upsample, [None, 2, 'nearest']]," + '\n' + 
                '   [[-1, 4], 1, Concat, [1]],  # cat backbone P3' + '\n' + 
                '   [-1, 3, C3, [256, False]],  # 17 (P3/8-small)' + '\n' + 

                '   [-1, 1, Conv, [256, 3, 2]],' + '\n' + 
                '   [[-1, 14], 1, Concat, [1]],  # cat head P4' + '\n' + 
                '   [-1, 3, C3, [512, False]],  # 20 (P4/16-medium)' + '\n' + 

                '   [-1, 1, Conv, [512, 3, 2]],' + '\n' + 
                '   [[-1, 10], 1, Concat, [1]],  # cat head P5' + '\n' + 
                '   [-1, 3, C3, [1024, False]],  # 23 (P5/32-large)' + '\n' + 

                '   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)' + '\n' + 
                '  ]'
                )

# Bat dau chuong trinh
conn = sqlite3.connect('Quee_train.db')
while True:
    dataset = conn.execute('SELECT * FROM TabQuee WHERE Time_start IS ? ORDER BY IDs',(None,))        
    for row in dataset:
        id = row[0]
        data_path = row[1]
        cls = row[2]
        epoch = row[3]
        size = row[4]
        save_path = row[5]
        save_name = row[6]
        current_time = datetime.now()
        conn.execute('UPDATE TabQuee SET Time_start=?  WHERE IDs = ? ',(current_time, id))
        conn.commit()

        # Copy data
        copy_data(data_path)
        
        # Tao du lieu
        make_yaml(cls, data_path)
    
        dir_py5 = os.path.join(os.getcwd(), 'levu', 'hlvtrain.py')
        dir_data5 = os.path.join(os.getcwd(), 'levu', 'data.yaml')
        dir_model5 = os.path.join(os.getcwd(), 'levu', 'models', 'levu.yaml')
        name_folder = time_to_name()
        program_dir5 = [ dir_py5, ' --img ','{}'.format(size), ' --batch ', '32' ,' --epochs ', '{}'.format(epoch) , ' --data ', dir_data5 , ' --cfg ', dir_model5, ' --weights ', '""', ' --name ', 'my_results' + '{}'.format(name_folder),  ' --cache']

        # Train
        subprocess.call(['python', program_dir5])
        
        fpath = save_path + '/' + save_name + '_' + name_folder[:10]
        shutil.copyfile(os.getcwd() + '/levu/runs/train/my_results'+ name_folder +'/weights/best.pt', fpath + '.pt')
        shutil.copyfile(os.getcwd() + "/result.txt", fpath + '.txt')
        current_time = datetime.now()
        conn.execute('UPDATE TabQuee SET Time_end=?  WHERE IDs = ? ',(current_time, id))
        conn.commit()
        print(current_time, save_path)
    if keyboard.is_pressed("q"):
        print("Exit")
        break

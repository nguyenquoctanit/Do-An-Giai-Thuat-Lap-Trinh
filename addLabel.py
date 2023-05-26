import PySimpleGUI as sg
import glob
import torch

import os
import random
import shutil

import datetime 
import cv2

import sys
import subprocess
import traceback


# def ExecuteCommandSubprocess(command, *args, wait=False):
#     try:
#         if sys.platform == 'linux':
#             arg_string = ''
#             arg_string = ' '.join([str(arg) for arg in args])
#             # for arg in args:
#             #     arg_string += ' ' + str(arg)
#             print('python3 ' + arg_string)
#             sp = subprocess.Popen(['python3 ', arg_string],
#                                   shell=True,
#                                   stdout=subprocess.PIPE,
#                                   stderr=subprocess.PIPE)
#         else:
#             arg_string = ' '.join([str(arg) for arg in args])
#             sp = subprocess.Popen([command, arg_string],
#                                   shell=True,
#                                   stdout=subprocess.PIPE,
#                                   stdin= subprocess.PIPE,
#                                   stderr=subprocess.PIPE,)
#                                   #cwd=True)
#             print("the commandline is {}".format(sp.args))
#             print("Ter {}".format(sp.returncode))
#             # sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         if wait:
#             out, err = sp.communicate()
#             if out:
#                 print(out.decode("utf-8"))
#             if err:
#                 print(err.decode("utf-8"))
#     except:
#         pass

def time_to_name():
    current_time = datetime.datetime.now() 
    name_folder = str(current_time)
    name_folder = list(name_folder)
    for i in range(len(name_folder)):
        if name_folder[i] == ':':
            name_folder[i] = '-'
        if name_folder[i] == ' ':
            name_folder[i] ='_'
        if name_folder[i] == '.':
            name_folder[i] ='-'
    name_folder = ''.join(name_folder)
    return name_folder



theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# # sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+
sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
#BORDER_COLOR = '#fcfffd'
DARK_HEADER_COLOR = '#1B2838'
MYBPAD = ((20,10), (10, 10))


mypath1 = 'D:/FILE_TRAIN_A17/file_train_c4/A17_C4_06_12_2022.pt'
model1 = torch.hub.load('./levu','custom', path= mypath1, source='local',force_reload =False)


file_weights = [('Weights (*.pt)', ('*.pt'))]

def make_window():
    # top  = [[sg.Text('Auto Training', size=(80,1), justification='center', pad=MYBPAD, font='Any 25', text_color='red')],]


    # Step_1 = [
    #             [sg.T('1.Choose file weights', font='Any 15', text_color = 'orange')],
    #             [sg.Input(size=(35,1), font=('Helvetica',12), key='input_weight1',readonly= True, text_color='navy',enable_events= True),
    #             sg.FileBrowse(file_types= file_weights,size=(12,1), font=('Helvetica',10),key= 'directory_weight1',enable_events=True) ],
    #             [sg.T('2.Choose confident', font='Any 15', text_color = 'orange')],
    #             [sg.Slider(range=(1,100),orientation='h',size=(48,20),font=('Helvetica',11),default_value=25, key= 'input_conf1')],
    #             [sg.T('3.Choose folder image', font='Any 15', text_color = 'orange')],
    #             [sg.Input(size=(35,1), font=('Helvetica',12), key='input_image1',readonly= True, text_color='navy',enable_events= True),
    #             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image1',enable_events=True) ],
    #             # [sg.T('4.Choose folder model', font='Any 15', text_color = 'orange')],
    #             # [sg.Input(size=(35,1), font=('Helvetica',12), key='input_model1',readonly= True, text_color='navy',enable_events= True),
    #             # sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_model1',enable_events=True) ],
    #             [sg.T('4.Choose folder save', font='Any 15', text_color = 'orange')],
    #             [sg.Input(size=(35,1), font=('Helvetica',12), key='input_save1',readonly= True, text_color='navy',enable_events= True),
    #             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_save1',enable_events=True) ],
    #             #[sg.Listbox(values=CLASSES1,size=(23,4), text_color= 'navy',select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, key='classes1')],
    #             [sg.T('5.Start create auto label', font='Any 15', text_color = 'orange')],
    #             [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start1')],
    #         ]

    Step_1 =[
                [sg.Text('Step 1: Get image in folder', font='Any 20', text_color='yellow')],
                [sg.T('1.Choose folder get image             ', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(30,1), font=('Helvetica',12), key='input_image0',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image0',enable_events=True) ],
                [sg.T('2.Choose folder save image             ', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(30,1), font=('Helvetica',12), key='input_save0',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_save0',enable_events=True) ],
                [sg.T('3.Enter name image you want get             ', font='Any 15', text_color = 'orange')],
                [sg.Multiline('',size=(40,10),text_color='navy' ,key='input_names0')], 
                [sg.Button('OK', size=(12,1), font=('Helvetica',10),key= 'button_names0')],
                [sg.T('4.Start get image           ', font='Any 15', text_color = 'orange')],
                [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start0')],
    ]


    Step_2 = [
                #[sg.Frame('',[
                [sg.Frame('',
                [   
                    [sg.Text('Step 2: Auto filter image', font='Any 20', text_color='yellow')],
                    [sg.T('1.Choose file weights              ', font='Any 15', text_color = 'orange'),
                    sg.Input(size=(60,1), font=('Helvetica',12), key='input_weight1',readonly= True, text_color='navy',enable_events= True),
                    sg.FileBrowse(file_types= file_weights, size=(12,1), font=('Helvetica',10),key= 'file_browse1',enable_events=True)],
                    [sg.T('2.Choose confident                 ', font='Any 15', text_color = 'orange'),
                    sg.Slider(range=(1,100),orientation='h',size=(60,20),font=('Helvetica',11),key= 'input_conf1'),]
                ], relief=sg.RELIEF_FLAT),
                ],
                [sg.T('3.Choose Parameter', font='Any 15', text_color = 'orange')],
                [sg.Frame('',[
                    [sg.Text('Name',size=(15,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('Join',size=(7,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('OK',size=(7,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('Num',size=(7,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('NG',size=(8,1),font=('Helvetica',15), text_color='orange'),  
                    sg.Text('Width Min',size=(11,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('Width Max',size=(11,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('Height Min',size=(11,1),font=('Helvetica',15), text_color='orange'), 
                    sg.Text('Height Max',size=(9,1),font=('Helvetica',15), text_color='orange')],
                ], relief=sg.RELIEF_FLAT)],
                [sg.Frame('',[
                    [
                        sg.Text(f'{model1.names[i1]}_1',size=(15,1),font=('Helvetica',15), text_color='pink'), 
                        sg.Checkbox('',size=(5,5),default=True,font=('Helvetica',15),  key=f'{model1.names[i1]}_1',enable_events=True), 
                        sg.Checkbox('',size=(5,5),font=('Helvetica',15),  key=f'{model1.names[i1]}_OK_1',enable_events=True), 
                        sg.Input('1',size=(2,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Num_1',text_color='navy',enable_events=True), 
                        sg.Text('',size=(4,1),font=('Helvetica',15), text_color='red'), 
                        sg.Checkbox('',size=(5,5),font=('Helvetica',15),  key=f'{model1.names[i1]}_NG_1',enable_events=True), 
                        sg.Input('0',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Wn_1',text_color='navy',enable_events=True), 
                        sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
                        sg.Input('100000',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Wx_1',text_color='navy',enable_events=True), 
                        sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
                        sg.Input('0',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Hn_1',text_color='navy',enable_events=True), 
                        sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
                        sg.Input('100000',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Hx_1',text_color='navy',enable_events=True), 
                    ] for i1 in range(len(model1.names))
                ], relief=sg.RELIEF_FLAT)],
                [sg.T('4.Choose folder image              ', font='Any 15', text_color = 'orange'),
                sg.Input(size=(60,1), font=('Helvetica',12), key='input_image1',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image1',enable_events=True) ],
                # [sg.T('4.Choose folder model', font='Any 15', text_color = 'orange')],
                # [sg.Input(size=(35,1), font=('Helvetica',12), key='input_model1',readonly= True, text_color='navy',enable_events= True),
                # sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_model1',enable_events=True) ],
                [sg.T('5.Choose folder save                ', font='Any 15', text_color = 'orange'),
                sg.Input(size=(60,1), font=('Helvetica',12), key='input_save1',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_save1',enable_events=True) ],
                #[sg.Listbox(values=CLASSES1,size=(23,4), text_color= 'navy',select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, key='classes1')],
                [sg.T('6.Start create auto label            ', font='Any 15', text_color = 'orange')],
                [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start1')],
                ]
                #,expand_x=True)]
    #]


    Step_3 = [
                [sg.Text('Step 3: Auto create label', font='Any 20', text_color='yellow')],
                [sg.T('1.Choose file weights', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_weight2',readonly= True, text_color='navy',enable_events= True),
                sg.FileBrowse(file_types= file_weights,size=(12,1), font=('Helvetica',10),key= 'directory_weight2',enable_events=True) ],
                [sg.T('2.Choose confident', font='Any 15', text_color = 'orange')],
                [sg.Slider(range=(1,100),orientation='h',size=(48,20),font=('Helvetica',11),default_value=25 ,key= 'input_conf2')],
                [sg.T('3.Choose folder image', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_image2',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image2',enable_events=True) ],
                # [sg.T('4.Choose folder model', font='Any 15', text_color = 'orange')],
                # [sg.Input(size=(35,1), font=('Helvetica',12), key='input_model1',readonly= True, text_color='navy',enable_events= True),
                # sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_model2',enable_events=True) ],
                [sg.T('4.Choose folder save', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_save2',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_model2',enable_events=True) ],
                [sg.T('5.Enter all name labels', font='Any 15', text_color = 'orange')],
                [sg.Multiline('',size=(40,10),text_color='navy' ,key='input_classes2')],
                [sg.Button('OK', size=(12,1), font=('Helvetica',10),key= 'button_classes2')],
                [sg.T('6.Enter labels and index edit', font='Any 15', text_color = 'orange')],
                [sg.Multiline('',size=(40,10),text_color='navy' ,key='input_classes2_1')],
                [sg.Button('OK', size=(12,1), font=('Helvetica',10),key= 'button_classes2_1')],
                #[sg.Listbox(values=CLASSES1,size=(23,4), text_color= 'navy',select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, key='classes1')],
                [sg.T('7.Start create auto label', font='Any 15', text_color = 'orange')],
                [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start2')],
                
            ]

    Step_4 = [
                [sg.Text('Step 4: Create label by program', font='Any 20', text_color='yellow')],
                [sg.T('1.Enter all name labels', font='Any 15', text_color = 'orange')],
                [sg.Multiline('',size=(40,10),text_color='navy' ,key='input_classes3')],
                [sg.Button('OK', size=(12,1), font=('Helvetica',10),key= 'button_classes3')],     
                [sg.T('2.Open Program', font='Any 15', text_color = 'orange')],
                [sg.Button('Open Program', size=(12,1), font=('Helvetica',10),key= 'program3')],       
            ]

                
    Step_5 = [
                [sg.Text('Step 5: Auto split image and label', font='Any 20', text_color='yellow')],
                [sg.T('1.Choose folder image', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_image4',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image4',enable_events=True) ],
                [sg.T('2.Choose folder save', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_save4',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_save4',enable_events=True) ],
                #[sg.Listbox(values=CLASSES1,size=(23,4), text_color= 'navy',select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, key='classes1')],
                [sg.T('3.Start split image and label', font='Any 15', text_color = 'orange')],
                [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start4')],
            ]

    Step_6 = [
                [sg.Text('Step 6: Auto Training', font='Any 20', text_color='yellow')],
                [sg.T('1.Choose folder contain folder train and valid', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_move5',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_move5',enable_events=True) ],     
                [sg.T('2.Move folder', font='Any 15', text_color = 'orange')],
                [sg.Button('Move', size=(12,1), font=('Helvetica',10),key= 'move5')],       
                [sg.T('3.Enter all name labels', font='Any 15', text_color = 'orange')],
                [sg.Multiline('',size=(40,8),text_color='navy' ,key='input_classes5')],
                [sg.Button('OK', size=(12,1), font=('Helvetica',10),key= 'button_classes5')],
                [sg.T('4.Enter image size', font='Any 15', text_color = 'orange'),
                sg.InputCombo((416,512,608,896,1024,1280,1408,1536),size=(23,30),default_value=416,key='imgsz5')],
                [sg.T('5.Choose epoch', font='Any 15', text_color = 'orange')],
                [sg.Slider(range=(1,500),orientation='h',size=(48,20),font=('Helvetica',11),default_value=300,key= 'input_epoch5')],
                [sg.T('6.Choose folder save model', font='Any 15', text_color = 'orange')],
                [sg.Input(size=(35,1), font=('Helvetica',12), key='input_save5',readonly= True, text_color='navy',enable_events= True),
                sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image5',enable_events=True) ],
                [sg.T('7.Start auto training', font='Any 15', text_color = 'orange')],
                [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start5')],
                [sg.T('8.Get file model', font='Any 15', text_color = 'orange')],
                [sg.Button('Get', size=(12,1), font=('Helvetica',10),key= 'get5')],
            ]



    # layout_1 = [
    #     [sg.Text('VDM AI VISION', font='Any 40', text_color='blue',justification='center',expand_x=True,background_color='white')],
    #     [sg.Frame('',[
    #     [sg.Frame('',
    #     [   
    #         [sg.Text('Step 1: Auto filter image', font='Any 20', text_color='yellow')],
    #         [sg.T('1.Choose file weights              ', font='Any 15', text_color = 'orange'),
    #         sg.Input(size=(60,1), font=('Helvetica',12), key='input_weight1',readonly= True, text_color='navy',enable_events= True),
    #         sg.FileBrowse(file_types= file_weights, size=(12,1), font=('Helvetica',10),key= 'file_browse1',enable_events=True)],
    #         [sg.T('2.Choose confident                 ', font='Any 15', text_color = 'orange'),
    #         sg.Slider(range=(1,100),orientation='h',size=(60,20),font=('Helvetica',11),key= 'input_conf1'),]
    #     ], relief=sg.RELIEF_FLAT),
    #     ],
    #     [sg.T('3.Choose Parameter', font='Any 15', text_color = 'orange')],
    #     [sg.Frame('',[
    #         [sg.Text('Name',size=(15,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('Join',size=(7,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('OK',size=(7,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('Num',size=(7,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('NG',size=(8,1),font=('Helvetica',15), text_color='orange'),  
    #         sg.Text('Width Min',size=(11,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('Width Max',size=(11,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('Height Min',size=(11,1),font=('Helvetica',15), text_color='orange'), 
    #         sg.Text('Height Max',size=(9,1),font=('Helvetica',15), text_color='orange')],
    #     ], relief=sg.RELIEF_FLAT)],
    #     [sg.Frame('',[
    #         [
    #             sg.Text(f'{model1.names[i1]}_1',size=(15,1),font=('Helvetica',15), text_color='pink'), 
    #             sg.Checkbox('',size=(5,5),default=True,font=('Helvetica',15),  key=f'{model1.names[i1]}_1',enable_events=True), 
    #             sg.Checkbox('',size=(5,5),font=('Helvetica',15),  key=f'{model1.names[i1]}_OK_1',enable_events=True), 
    #             sg.Input('1',size=(2,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Num_1',text_color='navy',enable_events=True), 
    #             sg.Text('',size=(4,1),font=('Helvetica',15), text_color='red'), 
    #             sg.Checkbox('',size=(5,5),font=('Helvetica',15),  key=f'{model1.names[i1]}_NG_1',enable_events=True), 
    #             sg.Input('0',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Wn_1',text_color='navy',enable_events=True), 
    #             sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
    #             sg.Input('100000',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Wx_1',text_color='navy',enable_events=True), 
    #             sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
    #             sg.Input('0',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Hn_1',text_color='navy',enable_events=True), 
    #             sg.Text('',size=(2,1),font=('Helvetica',15), text_color='red'), 
    #             sg.Input('100000',size=(8,1),font=('Helvetica',15),key= f'{model1.names[i1]}_Hx_1',text_color='navy',enable_events=True), 
    #         ] for i1 in range(len(model1.names))
    #     ], relief=sg.RELIEF_FLAT)],
    #     [sg.T('4.Choose folder image              ', font='Any 15', text_color = 'orange'),
    #     sg.Input(size=(60,1), font=('Helvetica',12), key='input_image1',readonly= True, text_color='navy',enable_events= True),
    #     sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_image1',enable_events=True) ],
    #     # [sg.T('4.Choose folder model', font='Any 15', text_color = 'orange')],
    #     # [sg.Input(size=(35,1), font=('Helvetica',12), key='input_model1',readonly= True, text_color='navy',enable_events= True),
    #     # sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_model1',enable_events=True) ],
    #     [sg.T('5.Choose folder save                ', font='Any 15', text_color = 'orange'),
    #     sg.Input(size=(60,1), font=('Helvetica',12), key='input_save1',readonly= True, text_color='navy',enable_events= True),
    #     sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'directory_save1',enable_events=True) ],
    #     #[sg.Listbox(values=CLASSES1,size=(23,4), text_color= 'navy',select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, key='classes1')],
    #     [sg.T('6.Start create auto label            ', font='Any 15', text_color = 'orange')],
    #     [sg.Button('Start', size=(12,1), font=('Helvetica',10),key= 'start1')],
    #     ],expand_x=True)]
    # ]


    layout_1 = [
        [sg.Text('VDM AI VISION', font='Any 40', text_color='blue',justification='center',expand_x=True,background_color='white')],
        [  
            sg.Column(Step_1, size=(425,700),  pad=MYBPAD),
            sg.Column(Step_2,  pad=MYBPAD),
        ]
    ]

    layout_2 = [
            [sg.Text('VDM AI VISION', font='Any 40', text_color='blue',justification='center',expand_x=True,background_color='white')],
            [#sg.Column([[sg.Column(Step_1, size=(450,700), pad=MYBPAD)],], pad=MYBPAD, background_color=BORDER_COLOR),

            #sg.Column(Step_2, size=(450,700),  pad=MYBPAD),
                sg.Column(Step_3, size=(480,900),  pad=MYBPAD),
                sg.Column([ 
                            [sg.Column(Step_4, size=(480,395), pad=MYBPAD)],
                            [sg.Column(Step_5, size=(480,285), pad=MYBPAD)]], pad=MYBPAD, background_color=BORDER_COLOR),
                sg.Column(Step_6, size=(480,700),  pad=MYBPAD),
                ]]
        
    layout = [[
                sg.TabGroup([[  
                            sg.Tab('Page 1', layout_1,background_color=BORDER_COLOR),
                            sg.Tab('Page 2', layout_2,background_color=BORDER_COLOR),
                            #sg.Tab('Page 3', layout_option,background_color=BORDER_COLOR),
                            ]],background_color=BORDER_COLOR,selected_background_color= BORDER_COLOR,selected_title_color='black')
                ]]
    window = sg.Window('Huynh Le Vu', layout, margins=(0,0), background_color=BORDER_COLOR, grab_anywhere=True)
    return window

mypath1 = 'D:/FILE_TRAIN_A17/file_train_c4/A17_C4_06_12_2022.pt'
model1 = torch.hub.load('./levu','custom', path= mypath1, source='local',force_reload =False)
window = make_window()

while True:             # Event Loop
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break


#1
    if event == 'button_names0' :
        if (values['input_names0'] != ''):
            mynames0 = []
            texts = values['input_names0'].split('\n')
            for text in texts:
                mynames0.append(text)
        else:
            sg.popup_error('Error')


    if event == 'start0':
        if (values['input_image0'] != '') & (values['input_save0'] !='') & (values['input_names0'] != ''):
            i=0
            filedir0= values['input_image0'] + '/*'
            for filename0 in glob.glob(filedir0):
                for path0 in glob.glob(filename0 + '/*'):
                    for myname0 in mynames0:
                        length = -len(myname0)
                        if myname0 == str(path0[length:]):
                            img0 = cv2.imread(path0)
                            cv2.imwrite(values['input_save0'] + '/' + str(i) + '.jpg',img0)
                            i+=1

            window['input_image0'].update(value='')
            window['input_save0'].update(value='')
            window['input_names0'].update(value='')
        else:
            sg.popup_error('Error')

 
#2


    for i1 in range(len(model1.names)):
        if event == f'{model1.names[i1]}_OK_1':
            if values[f'{model1.names[i1]}_OK_1'] == True:
                window[f'{model1.names[i1]}_NG_1'].update(disabled=True)
            else:
                window[f'{model1.names[i1]}_NG_1'].update(disabled=False)
        if event == f'{model1.names[i1]}_NG_1':
            if values[f'{model1.names[i1]}_NG_1'] == True:
                window[f'{model1.names[i1]}_OK_1'].update(disabled=True)
            else:
                window[f'{model1.names[i1]}_OK_1'].update(disabled=False)

    if event == 'input_weight1':
        mypath = values['input_weight1']
        model1 =torch.hub.load('./levu','custom', path= mypath, source='local', force_reload =False)
        window.close()
        window = make_window()
        event, values = window.read(timeout=20)
        window['input_weight1'].update(value=mypath)

    dem = 0
    if event == 'start1':
        if (values['input_weight1'] != '') & (values['input_image1'] !='') & (values['input_save1'] != ''):
            #mypath = values['input_weight1']
            #model1 =torch.hub.load('./levu','custom', path= mypath, source='local', force_reload =False)
            size=416
            conf = values['input_conf1']/100
            mydir = values['input_image1'] + '/*.jpg'

            def time_to_name():
                current_time = datetime.datetime.now() 
                name_folder = str(current_time)
                name_folder = list(name_folder)
                for i in range(len(name_folder)):
                    if name_folder[i] == ':':
                        name_folder[i] = '-'
                    if name_folder[i] == ' ':
                        name_folder[i] ='_'
                    if name_folder[i] == '.':
                        name_folder[i] ='-'
                name_folder = ''.join(name_folder)
                return name_folder

            for i,a in zip(reversed(range(len(mydir))),reversed(mydir)):
                if a == '/':
                    index = i
                    break

            for path1 in glob.glob(mydir):
                name = path1[index+1:-4]
                dem += 1
                img1 = cv2.imread(path1)
                
                result1 = model1(path1,size= size,conf = conf) 

                table1 = result1.pandas().xyxy[0]

                area_remove1 = []

                myresult1 =0 

                for item in range(len(table1.index)):
                    width1 = table1['xmax'][item] - table1['xmin'][item]
                    height1 = table1['ymax'][item] - table1['ymin'][item]
                    #area1 = width1*height1
                    label_name = table1['name'][item]
                    for i1 in range(len(model1.names)):
                        if values[f'{model1.names[i1]}_1'] == True:
                            #if values[f'{model1.names[i1]}_WH'] == True:
                            if label_name == model1.names[i1]:
                                if width1 < int(values[f'{model1.names[i1]}_Wn_1']): 
                                    table1.drop(item, axis=0, inplace=True)
                                    area_remove1.append(item)
                                elif width1 > int(values[f'{model1.names[i1]}_Wx_1']): 
                                    table1.drop(item, axis=0, inplace=True)
                                    area_remove1.append(item)
                                elif height1 < int(values[f'{model1.names[i1]}_Hn_1']): 
                                    table1.drop(item, axis=0, inplace=True)
                                    area_remove1.append(item)
                                elif height1 > int(values[f'{model1.names[i1]}_Hx_1']): 
                                    table1.drop(item, axis=0, inplace=True)
                                    area_remove1.append(item)

                names1 = list(table1['name'])

                for i1 in range(len(model1.names)):
                    if values[f'{model1.names[i1]}_OK_1'] == True:
                        len_name1 = 0
                        for name1 in names1:
                            if name1 == model1.names[i1]:
                                len_name1 +=1
                        if len_name1 != int(values[f'{model1.names[i1]}_Num_1']):
                            print(str(dem)+' NG')
                            name_folder_ng = time_to_name()
                            cv2.imwrite(values['input_save1'] +'/' + name_folder_ng + '.jpg',img1)
                            myresult1 = 1
                            if os.path.isfile(path1):
                                os.remove(path1)
                            break

                    if values[f'{model1.names[i1]}_NG_1'] == True:
                        if model1.names[i1] in names1:
                            print(str(dem)+' NG')
                            name_folder_ng = time_to_name()
                            cv2.imwrite(values['input_save1'] +'/' + name_folder_ng + '.jpg',img1)    
                            myresult1 = 1         
                            if os.path.isfile(path1):
                                os.remove(path1)
                            break    

                if myresult1 == 0:
                    print(str(dem)+' OK')
            window['input_weight1'].update(value='')
            window['input_image1'].update(value='')
            window['input_save1'].update(value='')
        else:
            sg.popup_error('Error')
    



#3
    if event == 'button_classes2' :
        if (values['input_classes2'] != ''):
            #print(values['input_classes2'])
            myclasses2 = []
            texts = values['input_classes2'].split('\n')
            for text in texts:
                myclasses2.append(text)
            #print(myclasses2)
        else:
            sg.popup_error('Error')

    if event == 'button_classes2_1' :
        if (values['input_classes2_1'] != ''):
            myclasses2_1 = []
            mynumberes2_1 = []
            texts = values['input_classes2_1'].split('\n')
            for text in texts:
                myclasses2_1.append(text.split(' ')[0])
                mynumberes2_1.append(text.split(' ')[1])

        else:
            sg.popup_error('Error')

    if event == 'start2':
        if (values['input_weight2'] != '') & (values['input_image2'] !='') & (values['input_save2'] != '') & (values['input_classes2'] != ''):
            mypath = values['input_weight2']
            model = torch.hub.load('./levu','custom', path= mypath, source='local',force_reload =False)

            mydir = values['input_image2'] + "/*.jpg"
            mysave = values['input_save2'] + '/'
            #print(mysave)
            for i,a in zip(reversed(range(len(mydir))),reversed(mydir)):
                if a == '/':
                    index = i
                    break
            for path in glob.glob(mydir):
                name = path[index+1:-4]
                #print(name)
                result = model(path,size=416,conf=values['input_conf2']/100)
                f = open(mysave + name + '.txt', "a")
                for detect in result.xywhn:
                    mydetects = detect.tolist()
                    for item in range(len(mydetects)):
                        mydetect = mydetects[item]
                        number_label = mydetect[-1]
                        number_label = int(number_label)
                        name_label = result.names[number_label]
                        for i,myclass2 in zip(range(len(myclasses2)),myclasses2):
                            if name_label == myclass2:
                                label_text = str(i)
                        
                        for index_classes in range(len(myclasses2_1)):
                            if name_label == myclasses2_1[index_classes]:
                                print(name)
                                f.write(str(mynumberes2_1[index_classes]) + " " + str(mydetect[0]) + " " + str(mydetect[1]) + " " + str(mydetect[2]) + " " + str(mydetect[3]))
                                f.write("\n")
                    f.close()
            with open(mysave + 'classes.txt', "w") as f: 
                for myclass in myclasses2:
                    f.write(myclass)
                    if myclass != myclasses2[-1]:
                        f.write('\n')
                    
            
            window['input_weight2'].update(value='')
            window['input_image2'].update(value='')
            window['input_save2'].update(value='')
            window['input_classes2'].update(value='')
            window['input_classes2_1'].update(value='')
        else:
            sg.popup_error('Error')



#4
    if event == 'button_classes3':
        if values['input_classes3'] != '':
            myclasses3 = []
            texts = values['input_classes3'].split('\n')
            for text in texts:
                myclasses3.append(text)
            with open(os.getcwd() + '/labelImg/data/predefined_classes.txt', "w") as f:
                for myclass3 in myclasses3:
                    f.write(myclass3)
                    f.write('\n')
        else:
            sg.popup_error('Error')

    if event == 'program3':
        if values['input_classes3'] != '':
            program_dir = os.path.join(os.getcwd()  + '/labelImg/' , 'labelImg.py')
            #ExecuteCommandSubprocess('python', program_dir)
            subprocess.call(['python',program_dir])
            #subprocess.call(['python', 'test2.py'])
            window['input_classes3'].update(value='')
        else:
            sg.popup_error('Error')  

#5
    if event == 'start4':
        if (values['input_image4'] !='') & (values['input_save4'] != ''):
            dir = values['input_image4']
            dir = dir + ('/*')
            list_image = [] 
            list_text = []
            list_image_train = []
            list_image_valid = []
            list_text_train = []
            list_text_valid = []

            list_name_train = []
            list_name_valid = []

            os.mkdir(values['input_save4'] + '/train')
            os.mkdir(values['input_save4'] + '/train/images')
            os.mkdir(values['input_save4'] + '/train/labels')

            os.makedirs(values['input_save4'] + '/valid')
            os.mkdir(values['input_save4'] + '/valid/images')
            os.mkdir(values['input_save4'] + '/valid/labels')

            for i,a in zip(reversed(range(len(dir))),reversed(dir)):
                if a == '/':
                    index = i
                    break

            for path in glob.glob(dir):
                name = path[index+1:-4]
                extension = path[-3:]

                if extension == 'jpg':
                    list_image.append(path)

                if extension == 'txt':
                    list_text.append(path)

            #random.seed(0)
            list_image_train = random.sample(list_image,int(len(list_image)*0.85))


            for item_image in list_image:
                if item_image not in list_image_train: 
                    list_image_valid.append(item_image)


            for path_train in list_image_train:
                name_train = path_train[index+1:-4]
                list_name_train.append(name_train)

            for path_valid in list_image_valid:
                name_valid = path_valid[index+1:-4]
                list_name_valid.append(name_valid)

            for item_text in list_text:
                name_text = item_text[index+1:-4]
                if name_text in list_name_train:
                    list_text_train.append(item_text)
                elif name_text in list_name_valid:
                    list_text_valid.append(item_text)

            for path1 in list_image_train:
                name1 = path1[index+1:-4]
                shutil.copyfile(path1,values['input_save4']+'/train/images/'+ name1 + '.jpg')
                

            for path2 in list_text_train:
                name2 = path2[index+1:-4]
                shutil.copyfile(path2,values['input_save4']+'/train/labels/'+ name2 + '.txt')

            for path3 in list_image_valid:
                name3 = path3[index+1:-4]
                shutil.copyfile(path3,values['input_save4']+'/valid/images/'+ name3 + '.jpg')

            for path4 in list_text_valid:
                name4 = path4[index+1:-4]
                shutil.copyfile(path4,values['input_save4']+'/valid/labels/'+ name4 + '.txt')

            window['input_image4'].update(value='')
            window['input_save4'].update(value='')

        else:
            sg.popup_error('Error')  


#6

    if event == 'move5':
        if values['input_move5'] != '':
            try:
                if os.path.isdir(os.getcwd() + '/train'):
                    shutil.rmtree(os.getcwd() + '/train')
                if os.path.isdir(os.getcwd() + '/valid'):
                    shutil.rmtree(os.getcwd() + '/valid')
                shutil.copytree(values['input_move5'] + '/train',os.getcwd() + '/train')
                shutil.copytree(values['input_move5'] + '/valid',os.getcwd() + '/valid')
            except:
                sg.popup_error('Error')   
                print(traceback.format_exc())
        else:
            sg.popup_error('Error')


    if event == 'button_classes5' :
        if (values['input_classes5'] != ''):
            myclasses5 = []
            texts5 = values['input_classes5'].split('\n')
            for text in texts5:
                myclasses5.append(text)

            with open(os.getcwd() + '/levu/data.yaml', "w") as f:
                f.write('train: ' + os.getcwd() + '/train/images')
                f.write('\n')
                f.write('val: ' + os.getcwd() + '/valid/images')
                f.write('\n')
                f.write('nc: '  + str(len(myclasses5)))     
                f.write('\n')
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


        else:
            sg.popup_error('Error')     


    if event == 'start5':
        if values['input_classes5'] != '':
            #program_dir5 = os.path.join(os.getcwd()  + '/levu/' , 'train.py')
            dir_py5 = os.path.join(os.getcwd()  + '/levu/' , 'hlvtrain.py')
            dir_data5 = os.path.join(os.getcwd()  + '/levu/' , 'data.yaml')
            dir_model5 = os.path.join(os.getcwd()  + '/levu/models/' , 'levu.yaml')
            name_folder = time_to_name()
            program_dir5 = [ dir_py5, ' --img ', str(values['imgsz5']), ' --batch ', '4' ,' --epochs ', '{}'.format(int(values['input_epoch5'])) , ' --data ', dir_data5 , ' --cfg ', dir_model5, ' --weights ', '""', ' --name ', 'my_results' + '{}'.format(name_folder),  ' --cache']
   
            subprocess.call(['python', program_dir5])
            #subprocess.Popen(program_dir5)

        else:
            sg.popup_error('Error')  
    

    if event == 'get5':
        try:
            if values['input_classes5'] != '':
                shutil.copyfile(os.getcwd() + '/levu/runs/train/my_results'+ name_folder +'/weights/best.pt',values['input_save5'] + '/best.pt')
                window['input_classes5'].update(value='')
                window['input_move5'].update(value='')
                window['input_save5'].update(value='')
            else:
                sg.popup_error('Error') 

        except:
            sg.popup_error('Error')  

# p = subprocess.Popen(['python', 'demo_oled_v01.py', '--display',
# 'ssd1351', '--width', '128', '--height', '128', '--interface', 'spi',
# '--gpio-data-command', '20'])
        # print('a')
        # program_dir5 = os.path.join(os.getcwd()  + '/levu/' , 'train.py' + " --img 416 --batch 4 --epochs 300 --data C:/Users/Administrator/Desktop/vu/auto_training/levu/data.yaml --cfg .levu/models/custom_yolov5s.yaml --weights '' --my_results  --cache")
        # ExecuteCommandSubprocess('python', program_dir5)

        #     for myclass5 in myclasses5:
        #         f.write(myclass3)
        #         f.write('\n')
        #window['input_classes5'].update(value='')


#python train.py --img 416 --batch 4 --epochs 300 --data "C:\Users\Administrator\Desktop\vu\mytrain7\data.yaml" --cfg ./models/custom_yolov5s.yaml --weights '' --name yolov5s_results  --cache
#C:/Users/Administrator/Desktop/vu/auto_training/levu/train.py
#C:\Users\Administrator\Desktop\vu\autob        if values['input_classes3'] != '':

import PySimpleGUI as sg
from datetime import datetime
# from plyer import notification

class Test:
    def getPath(thongbao):
        TM = ''
        while TM=='':
            TM = sg.PopupGetFolder(message=thongbao,title='Hãy chọn thư mục')
            if TM != '' and TM != None:
                TM = TM.replace('\\','/') + '/'
            elif TM =='':
                sg.popup_error('Bạn chưa nhập folder')
            else:
                sg.popup('Bạn đã Cancel')
                quit()
        return TM

    def time_to_string():
        ket_qua = f'{datetime.now():%Y-%m-%d_%H-%M-%S-%f}'
        return ket_qua

#    def notify(tieude, noidung):
#        notification.notify(
#        title = tieude,
#        message = noidung,
#        timeout = 10
#        )

from plyer import notification

def notify(tieude, noidung):
    notification.notify(
    title = tieude,
    message = noidung,
    timeout = 10
    )
notify("Thông báo","Hãy dùng Quee_train")

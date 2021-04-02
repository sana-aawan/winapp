from pywinauto.application import Application
from time import sleep
from contextlib import redirect_stdout


# def main():
app = Application(backend="uia").connect(path=r'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe')
print(app)
dlg = app.top_window()
file = dlg.print_control_identifiers(filename="C:\\Users\\Sana\\Documents\\result\\output_dd.txt")
# with open("C:\\Users\\Sana\\Documents\\result\\output_dd.txt", 'w') as f:
#     with redirect_stdout(f):
#         print('data')


# if __name__ == '__main__':
#     main()
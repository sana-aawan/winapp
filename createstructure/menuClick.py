import pywinauto
from utilities.create_json import retrievefile
import json
from pywinauto import Application, Desktop
from collections import defaultdict
from pywinauto.keyboard import send_keys
import pygetwindow as gw

output = '../winA/output/popup'
main_win = Application(backend="uia").connect(path=r'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe')

title = 'Open Media'
# title = 'Open File... Ctrl+O'
# print(gw.getAllWindows())
appWindow = gw.getWindowsWithTitle('Vlc Media Player')[0]
print(appWindow)
print(appWindow.getAllTitles())

export_dlg_handles = pywinauto.findwindows.find_windows(title=gw.getAllTitles())

if export_dlg_handles:
    export_dlg = main_win.window(handle=export_dlg_handles[0])
    # sleep(5)
    export_dlg.print_control_identifiers()
    # export_dlg.print_control_identifiers(filename=output + '/' + title + '.txt')

file_dict = {}
# idlist= 'TitleBar', 'Custom', 'TabControl', 'MenuItem'

with open(output + '/' + title + '.txt') as popids:
    file = title + '.txt'
    for lines in popids.readlines():
        if ('TitleBar' and 'Custom' and 'TabControl' and 'MenuItem' in lines) \
                and ('[' not in lines):
            with open(file, 'r+') as f:
                f.seek(0)
                data = f.read(1000)
                if len(data) > 0:
                    f.write("\n")
                lines = lines.replace("|", "")
                lines = lines.replace("child_window(", "")
                lines = lines.replace(")", "")
                f.write(lines)
        else:
            if 'child_window' in lines:
                if '|' in lines:
                    space = lines.count('|')
                    lines = lines.replace("|", "")
                    lines = lines.replace("child_window(", "")
                    lines = lines.replace(")", "")
                    with open(file, 'r+') as file_object:
                        file_object.seek(0)
                        data = file_object.read(1000)
                        file_object.write(lines)
                else:
                    with open(file, 'r+') as f:
                        f.seek(0)
                        data = f.read(1000)
                        lines = lines.replace("child_window(", "")
                        lines = lines.replace(")", "")
                        f.write(lines)

    # retrievefile(file, output)

# if __name__ == "__main__":
#     objectId = PopUp()
#     objectId.getPopup()

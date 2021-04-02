# from pywinauto.application import Application
# app = Application(backend="uia").start("notepad.exe")

import pyautogui
import psutil
import pywinauto
from pywinauto.application import Application

# app = Application(backend="uia").start("notepad.exe")


# app = Application.Start('Notepad')
# By regular expression
# app = Application(backend="uia").connect(title_re=".*Notepad")
app = Application(backend="uia").start("notepad.exe")
main_dlg = app.UntitledNotepad
main_dlg.wait('visible')
main_dlg = app.window(title='Untitled - Notepad')

# Print all controls on the dialog
main_dlg.print_control_identifiers()

print(main_dlg.children())

for child in main_dlg.descendants():
    print(child)


# app.UntitledNotepad.MenuItem("Edit -> Replace").Select()
# app.print_control_identifiers()
#global var
# processid = 0
# handle = pywinauto.findwindows.find_window(best_match='fifa')
# app = pywinauto.application.Application().connect(handle=handle)
# windows = app.windows()
# fo4_window = app.window(title='FIFA ONLINE 4')
# fo4_window.print_control_identifiers()
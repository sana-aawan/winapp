from __future__ import print_function
from pywinauto.application import Application
import os
import pickle

# start application
if (os.path.exists(r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")):
    app = Application(backend='uia').start(r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
else:
    if (os.path.exists(r"C:/Program Files/VideoLAN/VLC/vlc.exe")):
        app = Application(backend='uia').start(r"C:/Program Files/VideoLAN/VLC/vlc.exe")
    else:
        print("Can't find VLC on your computer")

# output path
output = "../winA/output/"
list_output = []

# app = Application(backend='uia').start("notepad.exe")
# win = app['VLC Media Player']
win = app.window()

if app.software_update.exists(timeout=10):
    app.software_update.skip_this_version.click()
    app.software_update.wait_not('visible')  # just to make sure it's closed
win.wait('ready', timeout=15)

# the main menu
menu = win.descendants(control_type="MenuBar")[1]

# iterate initially visible items (level 0)
for main_item in menu.children():
    main_item.invoke()
    subitems_level_1 = app.window(control_type="Menu").children()
    # print([i.window_text() for i in subitems_level_1])
    subitems_level_1_out = [i.window_text() for i in subitems_level_1]
    level_1 = [main_item, '->', subitems_level_1_out]
    list_output.append(level_1)

    # iterate expanded items (level 1)
    for item in subitems_level_1:
        if item.legacy_properties()[u'DefaultAction'] == u'ShowMenu':
            # it has submenu
            item.invoke()
            subitems_level_2 = app.window(control_type="Menu", found_index=0).children()
            subitems_level_2_out = [i.window_text() for i in subitems_level_2]
            level_2_out = item, '->', subitems_level_2_out
            list_output.extend(level_2_out)
            # print([i.window_text() for i in subitems_level_2])
            # can proceed to 3rd level and so on

# print(list_output)
# app_name = app.split('.')[0].split('/')[-1]
# filename = output + '/' + app_name + '.txt'
with open("file.txt", "w") as output:
    output.write(str(list_output))

# win.child_window(title="Close", control_type="Button").click()

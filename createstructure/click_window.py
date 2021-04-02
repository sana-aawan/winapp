from pywinauto import Application, Desktop
from collections import defaultdict
import json


# # path of the application
# application = 'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe'
#
# # path of the output
# output = '../winA'
from createstructure.get_title import main


def click_window_window(menu, app, app_name, main_win):
    for main_item in menu.children():
        main_item.invoke()
        subitems_level_1 = app.window(control_type="Menu").children()
        for menuitem in subitems_level_1:
            menu.print_control_indentifier()
            if menuitem.legacy_properties()[u'DefaultAction'] == u'Press':
                menuitem.invoke()
                getTitle(main_win)


def getTitle(window):
    wrapper_list = window.descendants(control_type="Window")
    for wrapper in wrapper_list:
        print("Testing")
        print(wrapper.window_text())


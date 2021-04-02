import codecs
import locale
import sys

from pywinauto import Application, Desktop, findwindows, findbestmatch, controls
import pywinauto
from collections import defaultdict
import json
import os
import pandas as pd
from pywinauto.actionlogger import ActionLogger
from pywinauto.backend import BackendsRegistry
from pywinauto.timings import Timings, wait_until_passes
import json
import uiautomation

from extra.control_type import MenuBar


def print_control_identifiers(dlg,app, app_name, depth=None, filename=None):
    global list_output
    try:
        list_output = []
        if depth is None:
            depth = sys.maxsize
        # Wrap this control
        menu = dlg.descendants()
        # for item in menu:
        #     print(item.children())
        this_ctrl = menu

        # Create a list of this control and all its descendants
        all_ctrls = dlg.descendants()
        # print(all_ctrls)

        # Create a list of all visible text controls
        txt_ctrls = [ctrl for ctrl in all_ctrls if ctrl.can_be_label and ctrl.is_visible() and ctrl.window_text()]

        # Build a dictionary of disambiguated list of control names
        name_ctrl_id_map = findbestmatch.UniqueDict()
        for index, ctrl in enumerate(all_ctrls):
            ctrl_names = findbestmatch.get_control_names(ctrl, all_ctrls, txt_ctrls)
            for name in ctrl_names:
                name_ctrl_id_map[name] = index

        # Swap it around so that we are mapped off the control indices
        ctrl_id_name_map = {}
        for name, index in name_ctrl_id_map.items():
            ctrl_id_name_map.setdefault(index, []).append(name)
        # print(ctrl_id_name_map)


        def print_identifiers(ctrls, current_depth=1, log_func=print):
            """Recursively print ids for ctrls and their descendants in a tree-like format"""
            if len(ctrls) == 0 or current_depth > depth:
                return

            indent = (current_depth - 1) * u""
            for ctrl in all_ctrls:
                print(ctrl)
                try:
                    ctrl_id = all_ctrls.index(ctrl)
                except ValueError:
                    continue
                ctrl_text = ctrl.window_text()
                if ctrl_text:
                    # transform multi-line text to one liner
                    ctrl_text = ctrl_text.replace('\n', r'\n').replace('\r', r'\r')

                output = indent + u'\n'
                # output += indent + u"{class_name} - '{text}'    {rect}\n" \
                #                    "".format(class_name=ctrl.friendly_class_name(),
                #                              text=ctrl_text,
                #                              rect=ctrl.rectangle())
                output += indent + u'{}'.format(ctrl_id_name_map[ctrl_id])
                title = ctrl_text
                class_name = ctrl.class_name()
                auto_id = None
                control_type = None
                if hasattr(ctrl.element_info, 'automation_id'):
                    auto_id = ctrl.element_info.automation_id
                if hasattr(ctrl.element_info, 'control_type'):
                    control_type = ctrl.element_info.control_type
                    if control_type:
                        class_name = None  # no need for class_name if control_type exists
                    else:
                        control_type = None  # if control_type is empty, still use class_name instead
                criteria_texts = []
                if title:
                    criteria_texts.append(u'title="{}"'.format(title))
                if class_name:
                    criteria_texts.append(u'class_name="{}"'.format(class_name))
                if auto_id:
                    criteria_texts.append(u'auto_id="{}"'.format(auto_id))
                if control_type:
                    criteria_texts.append(u'control_type="{}"'.format(control_type))
                if title or class_name or auto_id:
                    output += u'\n' + indent + u'child_window(' + u', '.join(criteria_texts) + u')'
                log_func(output)
                # if six.PY3:
                #     log_func(output)
                # else:
                #     log_func(output.encode(locale.getpreferredencoding(), errors='backslashreplace'))

                print_identifiers(this_ctrl, current_depth + 1, log_func)

        def look_all_descendant(dlg):
            main_descendants = dlg.descendants()
            titlebar = dlg.descendants(control_type='TitleBar')
            # for item in titlebar.children():
            #     print(item)
            print(titlebar)

        def hierarchy_structure(menu, list_output):
            level = 0
            for main_item in menu:
                sub_level = 0
                data = main_item.legacy_properties()
                # data['levelId'] = 'key' + '_' + str(level)
                list_output.append(data)
                if main_item.children():
                    for sub_main_item in main_item.children():
                        sub_level = 0
                        data = sub_main_item.legacy_properties()
                        # data['levelId'] = 'key' + '_' + str(level) + '_' + str(sub_level)
                        list_output.append(data)
                    sub_level += 1
                level += 1
            # print(list_output)
            list_output = [dict(t) for t in {tuple(d.items()) for d in list_output}]
            # print(list_output)
            if dlg.descendants(control_type='MenuBar'):
                list_output = MenuBar(dlg, app, list_output)
            else:
                pass

            # print(list_output)
            # df = pd.DataFrame(list_output)
            # df.to_csv("C:\\Users\\Sana\\Documents\\result\\output"+"_"+ app_name + ".csv", index=False)

        if filename is None:
            # print("Element Dataset:")
            look_all_descendant(dlg)
            hierarchy_structure(menu, list_output)

    except Exception as e:
        print("An exception occurred - ", e)
    finally:
        df = pd.DataFrame(list_output)
        df.to_csv("C:\\Users\\Sana\\Documents\\result\\output" + "_" + app_name + ".csv", index=False)


def main():
    app = Application(backend='uia').start(r"C:\Program Files (x86)\Windows Media Player/wmplayer.exe")
    # app = Application(backend='uia').start(r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
    app_name = "Media_player"
    dlg = app.window()
    print_control_identifiers(dlg, app, app_name)

if __name__ == '__main__':
    main()
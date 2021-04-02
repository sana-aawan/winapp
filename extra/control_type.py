from collections import defaultdict
import pywinauto
import pandas as pd


def MenuBar(dlg, app, list_output):
    tree_output = {}
    menu = dlg.descendants(control_type="MenuBar")[1]
    level = 0
    if menu:
        for main_item in menu.children():
            sub_level = 0
            data = main_item.legacy_properties()
            data['levelId'] = 'key' + '_' + str(level)
            list_output.append(data)
            main_item.invoke()
            key_level_0 = []
            key = main_item.window_text()
            dict_0 = defaultdict(list)
            subitems_level_1 = app.window(control_type="Menu").children()
            for item in subitems_level_1:
                data = item.legacy_properties()
                data['levelId'] = 'key' + '_' + str(level) + '_' + str(sub_level)
                sub_level += 1
                list_output.append(data)
                key_0 = str(item.window_text())
                if item.legacy_properties()[u'DefaultAction'] == u'ShowMenu':
                    item.invoke()
                    subitems_level_2 = app.window(control_type="Menu", found_index=0).children()
                    for i in subitems_level_2:
                        dict_0[key_0].append(i.window_text())
                    key_level_0.append(dict_0)
                else:
                    key_level_0.append(item.window_text())
            level += 1
            tree_output[key] = key_level_0
    return list_output
    # df = pd.DataFrame(list_output)
    # df.to_csv("C:\\Users\\Sana\\Documents\\result\\output_control.csv")
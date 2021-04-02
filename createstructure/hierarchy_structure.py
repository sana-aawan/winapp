from pywinauto import Application, Desktop
from collections import defaultdict
import json
import os
import pandas as pd
from utilities.common import getTitleBar
from createstructure.click_window import click_window_window


class Id(object):

    def startApp(self):
        """
        to start the application
        :return:
        """
        # start application
        app_name = "VLC media player"
        if (os.path.exists(r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")):
            app = Application(backend='uia').start(r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
        else:
            if (os.path.exists(r"C:/Program Files/VideoLAN/VLC/vlc.exe")):
                app = Application(backend='uia').start(r"C:/Program Files/VideoLAN/VLC/vlc.exe")
            else:
                print("Can't find app on your computer")

        # app = Application(backend="uia").start(application)
        main_win = app.window()

        objectId.getId(app, app_name, main_win)

    def getId(self, app, app_name, main_win):
        """
         to get the ID
        :return:
        """

        # path of the output
        output = '../winA/output'

        tree_output = {}
        list_output = []

        menu = main_win.descendants(control_type="MenuBar")[1]

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
                # subitems_level_1_out = [i for i in subitems_level_1]
                # print(main_item.legacy_properties())
                for item in subitems_level_1:
                    data = item.legacy_properties()
                    data['levelId'] = 'key' + '_' + str(level) + '_' + str(sub_level)
                    sub_level += 1
                    list_output.append(data)
                    key_0 = str(item.window_text())
                    if item.legacy_properties()[u'DefaultAction'] == u'ShowMenu':
                        item.invoke()
                        subitems_level_2 = app.window(control_type="Menu", found_index=0).children()
                        # subitems_level_2_out = [i.window_text() for i in subitems_level_2]
                        # print(subitems_level_2_out)
                        # print(item.legacy_properties())
                        for i in subitems_level_2:
                            dict_0[key_0].append(i.window_text())
                        key_level_0.append(dict_0)
                    else:
                        key_level_0.append(item.window_text())
                level += 1
                tree_output[key] = key_level_0
        # if title:
        #     tree_output = {}
        #     list_output = []
        #     level = 0
        #     getTitleBar(tree_output, list_output, level, title, app)
        df = pd.DataFrame(list_output)
        df.to_csv("C:\\Users\\Sana\\Documents\\result\\output_dd.csv")
        # df.to_csv(output + "/dataset/dataset.csv", index=False)
        with open("../sample.json", "w") as outfile:
            json.dump(tree_output, outfile)
        # print(tree_output)

        # objectId.close_app(application, app)
        # click_window_window(menu, app, app_name, main_win)wq



    def close_app(self, application, app):
        # app_1 = Application(backend="uia").connect(application)
        print(application)
        # app.window(title=application, found_index=0).close()
        # main_win.child_window(title="Close", control_type="Button", found_index=1).click()


if __name__ == "__main__":
    objectId = Id()
    objectId.startApp()


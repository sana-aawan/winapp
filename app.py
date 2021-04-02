from pywinauto import Application, Desktop


class Id(object):
    def getId(self):
        application = 'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe'
        # application = 'C:/Program Files/Notepad++/notepad++.exe'
        # application = 'calc.exe'
        output = '../winA'
        list_children = []

        app = Application(backend="uia").start(application)
        main_win = app.window()
        # print(main_win.WAIT_CRITERIA_MAP)

        readystr = ('is_visible', 'is_enabled')

        if main_win.WAIT_CRITERIA_MAP['ready'] == readystr:
            # print(main_win.backend.element_info_class.name)
            app_name = application.split('.')[0].split('/')[-1]
            # main_win.print_control_identifiers()
            main_win.print_control_identifiers(filename=output + '/' + app_name + '.txt')

            print(main_win.descendants(control_type="MenuBar"))
            menu = main_win.descendants(control_type="MenuBar")[1]

            for val in main_win.iter_children():
                if (str(val).split('-')[0]) == 'uia_controls.MenuWrapper ':
                    # print("Entered")
                    # print(val.item_by_index(1))
                    # print(val.items())
                    for children in val.descendants():
                        list_children.append(children)
                        subitems_level_1 = app.window(control_type="Menu")
                    print(subitems_level_1)
                        # for child in children.items():
                        #     child.setfocus()
                        #     child.select()
                        #     print(app.window().descendants(control_type="MenuItem"))
                # for child in list_children:
                #     print(type(child))

            # main_win.menu_select("Media")
            # for children in main_win.descendants():
            #     class_child = (str(children).split('-')[0])
            #     children =(str(children).split('-')[1])
            #     print(class_child, children)
            main_win.child_window(title="Close", control_type="Button").click()


if __name__ == "__main__":
    objectId = Id()
    objectId.getId()

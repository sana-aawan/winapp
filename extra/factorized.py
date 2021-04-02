from contextlib import redirect_stdout
import re
f = open("C:\\Users\\Sana\\Documents\\result\\output_dd.txt", "r")
searchlines = f.readlines()
# f.close()
print(searchlines)
strl = ("TitleBar ", "Menu", "Pane", "child_window")
for i, line in enumerate(searchlines):
    if any(s in line for s in strl):
        print(line)
        for l in searchlines[i:i+1]:
            fl = open("C:\\Users\\Sana\\Documents\\result\\test_output.txt", "a")
            print(line, file=fl)
            fl.close()
            with open("C:\\Users\\Sana\\Documents\\result\\test_output.txt") as f2:
                lines = f2.readlines()
                lines = [line.replace('|', "") for line in lines]
                f2.close()
            with open('C:\\Users\\Sana\\Documents\\result\\test_output.txt', 'w') as f:
                f.writelines(lines)
                f.close()

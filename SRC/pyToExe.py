import sys

"""
To run this file as an exe, we will first need to convert to a .EXE file.
To do this, do py -m pip install pyinstaller, if you do not already have this pip package installed.
Next, open a powershell window as admin at the folder that houses the target .py file.
Next, in the powershell window, type pyinstaller --onefile <name of file>.py
This command will then display what it is doing and put the .exe file in the 'dist' folder it creates in the directory containing
the target file.
To run this exe with arguments, you would do ...\pyToExe.py "Argument 1" "Argument 2".
"""

argumentOne = str(sys.argv[1])
argumentTwo = str(sys.argv[2])

def Main():
    print("Argument One: " + argumentOne + "\n")
    print("Argument Two: " + argumentTwo + "\n")

if __name__ == '__main__':
    Main()
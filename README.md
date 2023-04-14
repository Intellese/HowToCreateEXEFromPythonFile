# How To Create EXE File From Python File

This program is an example of how to convert a .py file to a .exe file. It is written in Python 3.11 and is designed to be run through the Windows PowerShell.

## Prerequisites

Before running this program, you will need to have the following installed: 
* Python 3.11
* pyinstaller

## Installing

To install Python 3.11 and pyinstaller, follow the instructions below: 

1. Download Python 3.11 from [Python's official website](https://www.python.org/downloads/).
2. Run the installer, making sure to check the box to add Python to your PATH.
3. Open a Windows PowerShell window as admin at the folder that houses the target .py file.
4. In the PowerShell window, type ```py -m pip install pyinstaller```.

## Running the Program

To run this program, follow the instructions below: 

1. Open a Windows PowerShell window as admin at the folder that houses the target .py file.
2. In the PowerShell window, type ```pyinstaller --onefile <name of file>.py```
3. This command will then display what it is doing and put the .exe file in the 'dist' folder it creates in the directory containing the target file.
4. To run this exe with arguments, you would do ```...\pyToExe.py "Argument 1" "Argument 2"```.

## Built With

* [Python 3.11](https://www.python.org/downloads/)
* [Pyinstaller](https://pypi.org/project/PyInstaller/)

## Authors

* **Taylor Rodieck** - *Initial work* 

import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("ALPHAREG.py", base=base, icon="logo.ico")]


cx_Freeze.setup(
    name = "Face Recognition attendence system",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["logo.ico",'tcl86t.dll','tk86t.dll', 'images','database','data','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Attendace System | Developed By Team ALPHA",
    executables = executables
    )

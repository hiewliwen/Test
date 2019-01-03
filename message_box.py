'''
Type of Errors:
    File Not Imported
    File Extension Wrong
    File Corrupted
    Empty File
    Emplty Table (after conversion)
    Conversion Error
    Calculation Error
    
Type of Warnings:
    Data Array (Too Long)
    Data Array (Too Short)
    Angle Range (Too Long)
    Angle Range (Too Short)
    Angle Range (Don't Start at 0°)
    Outliers
    Importing More Than 10 Files
    
Type of Questions:
    abortretryignore
    ok
    okcancel
    retrycancel
    yesno
    yesnocancel    
'''

from tkinter import messagebox, Tk
from sys import exit

def show_errormessage(operation, description, status=None, questions = 'ok'):
    tk_init()
    messagebox.showerror(operation, description, type = questions)
    sys.exit(status)
    
def show_warningmessage(operation, description, questions = 'ok'):
    tk_init()
    messagebox.showwarning(operation, description, type = questions)
    return

def tk_init():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return

def reply_abort():
#    root.destroy()
    sys.exit('Abort')
    
    
''' Test Cases '''
#show_warningmessage('Test', 'Ask A Bunch of Kwestions', 'abortretryignore')
#show_errormessage('Test', 'Ask A Bunch of Kwestions')
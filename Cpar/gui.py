from tkinter import  *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import pandas as pd
#import test1


window = Tk()
window.title("Đề tài Tiểu Luận CPAR")
window.geometry('450x300')


#hàm xem đường dẫn thư mục
def show():
    name0 = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")))
    infor = '''1: Đường dẫn \n'''
    txt.insert(0.0,(infor,name0))
# hàm xem dữ liệu của thư mục
def read():
    name1 = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    infor1 = '''2: Dữ liệu \n'''
    try:
        with open(name1, 'r') as UseFile:
            txt.delete(0.0, END)
            txt.insert(0.0,(infor1,(UseFile.read())))

    except:
        txt.insert(0.0,(infor1,"No file exists"))
# hàm xem thông tin củ dữ liệu
def infom():
    name2 = pd.read_csv('D:\TLCN\pima.csv',encoding='utf-8',header=None,sep=',')
    txt.delete(0.0, END)
    print('Len:', len(name2))
    name2.info()
    print('shape:', name2.shape)
    #txt.insert(0.0,(name2.head(5)))
    #txt.insert(END,('Len', len(name2),'\n'))
    #txt.insert(END, (name2.info))
 ##############################################
   # infor2 = ''' Len: '''
   # infor3 ='''shape:  '''
   # txt.insert(0.0,(infor3,test1.peoples_df.shape))
   # t2 = test1.peoples_df.info()
   # txt.insert(0.0, t2)
   # txt.insert(0.0, (infor2,len(test1.peoples_df),'\n'))
#################################################################
lable1 = Label(window, text="The Sofware CPAR", relief="solid", bd=1, font="Times 18").grid(row=0,column=1)
btn1 = Button(window, text="Open File",width=15,command=show).grid(row=1,column=0)
btn2 = Button(window, text="Read Data",width=15,command=read).grid(row=2,column=0)
btn3 = Button(window, text="Information Data",width=15,command=infom).grid(row=3,column=0)
btn4 = Button(window, text="Star CPAR",width=15).grid(row=1, column =2 , sticky='e')
btn5 = Button(window, text="Classifer",width=15).grid(row=2, column =2 ,sticky='e')
btn6 = Button(window, text="Save",width=15).grid(row=3, column =2,sticky='e')

lable2 = Label(window, text="output", ).grid(row=4,column=0)
txt = Text(window, width =50)
txt.grid(row=5,column=0,sticky='e',columnspan=3)
window.mainloop()

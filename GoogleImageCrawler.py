import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from icrawler.builtin import GoogleImageCrawler


window = Tk()
window.title('CollectBot')
window.geometry('600x450')
iconfile = 'raion.ico'
window.iconbitmap(default=iconfile)

def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

def Execution_function():                                                                                                                                                                                                                                                                                                                                                                                                               
    Keyword_value = keyword.get()
    number_value = number.get()
    Folder_name = IDirEntry.get()
    test = int(number_value)
    crawler = GoogleImageCrawler(storage={"root_dir": Folder_name})
    crawler.crawl(keyword=Keyword_value, max_num=test)

Label_1 = ttk.Label(window, text='↓保存したい画像のキーワード↓')
Label_1.place(x=215, y=40)

keyword = ttk.Entry(window, width=30)
keyword.place(x=200, y=80)

Label_2 = ttk.Label(window, text='↓保存したい画像の枚数↓')
Label_2.place(x=218, y=140)

number = ttk.Entry(window, width=30,)
number.place(x=200, y=180)

frame1 = ttk.Frame(window, padding=10)
frame1.place(x=90, y=250)

IDirLabel = ttk.Label(frame1, text="フォルダ参照＞＞", padding=(5, 2))
IDirLabel.pack(side=LEFT)

entry1 = StringVar()
IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
IDirEntry.pack(side=LEFT)

IDirButton = ttk.Button(frame1, text="参照", command=dirdialog_clicked)
IDirButton.pack(side=LEFT)

Run_button = ttk.Button(window, text='実行', command=Execution_function)
Run_button.place(x=250, y=350)

window.mainloop()
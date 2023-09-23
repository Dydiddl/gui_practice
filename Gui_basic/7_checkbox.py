from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로


chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()


def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop()

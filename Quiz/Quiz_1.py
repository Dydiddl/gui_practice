# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시오

# [GUI 조건]
# 1. title : 제목 없음 - windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynot.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

import tkinter as tk
# from tkinter import filedialog
import os

# 메모장 윈도우 생성
root = tk.Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 텍스트 입력 위젯 생성
text_widget = tk.Text(root)
text_widget.pack(side="left", fill="both", expand=True)

# 스크롤 바
scrollbar = tk.Scrollbar(text_widget)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

# 열기, 저장 파일 이름
filename = "mynote.txt"
def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            text_widget.delete("1.0","end") # 텍스트 위젯 본문 삭제
            text_widget.insert("end", file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file :
        file.write(text_widget.get("1.0", "end")) # 모든 내용을 가져와서 저장

# # 파일 열기 함수
# def open_file():
#     file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if file_path:
#         with open(file_path, "r") as file:
#             text_widget.delete("1.0", tk.END)
#             text_widget.insert(tk.END, file.read())

# # 파일 저장 함수
# def save_file():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(text_widget.get("1.0", tk.END))

# 끝내기 함수
def exit_app():
    root.quit()

# 파일 메뉴
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=exit_app)

# 편집 메뉴
edit_menu = tk.Menu(menu)
menu.add_cascade(label="편집", menu=edit_menu)
# 여기에 편집 메뉴 항목을 추가할 수 있습니다.

# 서식 메뉴
format_menu = tk.Menu(menu)
menu.add_cascade(label="서식", menu=format_menu)
# 여기에 서식 메뉴 항목을 추가할 수 있습니다.

# 보기 메뉴
view_menu = tk.Menu(menu)
menu.add_cascade(label="보기", menu=view_menu)
# 여기에 보기 메뉴 항목을 추가할 수 있습니다.

# 도움말 메뉴
help_menu = tk.Menu(menu)
menu.add_cascade(label="도움말", menu=help_menu)
# 여기에 도움말 메뉴 항목을 추가할 수 있습니다.

# 메인 루프 시작
root.mainloop()


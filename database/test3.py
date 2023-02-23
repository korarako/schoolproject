from fileinput import close
import pymysql
import tkinter as tk


class kora:
    db = pymysql.connect(host="localhost", user="root", password="123456", database="korako")
    cursor = db.cursor()

    def __init__(self):
        self.root = tk.Tk()     # 创建窗口
        self.root.geometry("500x400")

    def select(self):
        address = self.Information.get()
        search_str = "select * from S where SADDR like '" + "%" + address + "%'"
        kora.cursor.execute(search_str)     # 执行sql语句
        info = kora.cursor.fetchall()       # 获取所有结果
        self.listbox.delete(0, tk.END)      # 清空列表
        if len(info) == 0:                  # 若结果为空返回null
            self.listbox.insert(0, "null")
        for i in info:                      # 若不为空则插入数据
            self.listbox.insert(tk.END, i)

    def interface(self):
        self.Information = tk.StringVar()
        self.entry = tk.Entry(self.root, width=12, bd=1, textvariable=self.Information)  # 定义输入框
        self.entry.place(x=280, y=44)
        self.label1 = tk.Label(self.root, text="输入地址",)
        self.label1.place(x=320, y=10)
        self.Button1 = tk.Button(self.root, text="查询", command=self.select)  # 定义按钮
        self.Button1.place(x=330, y=110, relheight=0.1, relwidth=0.2)
        self.label2 = tk.Label(self.root, text="结果列表")
        self.label2.place(x=70, y=10)
        self.listbox = tk.Listbox(self.root, width=20, height=12)  # 定义输出列表
        self.listbox.place(x=15, y=40)

    def __del__(self):
        kora.cursor.close()
        kora.db = close()


if __name__ == "__main__":
    kora = kora()
    kora.interface()
    kora.root.mainloop()

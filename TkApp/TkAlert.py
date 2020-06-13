from tkinter import messagebox


class TkAlert:

    @staticmethod
    def Info(text, title=""):
        messagebox.showinfo(title, text)

    @staticmethod
    def Error(text, title=""):
        messagebox.showerror(title, text)

    @staticmethod
    def Warning(text, title=""):
        messagebox.showwarning(title, text)

    @staticmethod
    def YesNo(text, title=""):
        return messagebox.askyesno(title, text)

    @staticmethod
    def OkCancel(text, title=""):
        return messagebox.askokcancel(title, text)

    @staticmethod
    def RetryCancel(text, title=""):
        return messagebox.askretrycancel(title, text)

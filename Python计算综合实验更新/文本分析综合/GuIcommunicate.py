
import tkinter as tk
from viewanalysis import plt,virtual_word_freq,real_word_freq
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.virtual_var = tk.BooleanVar()
        self.real_var = tk.BooleanVar()

        self.virtual_checkbutton = tk.Checkbutton(self, text='文言虚词', variable=self.virtual_var)
        self.virtual_checkbutton.pack()

        self.real_checkbutton = tk.Checkbutton(self, text='文言实词', variable=self.real_var)
        self.real_checkbutton.pack()

        self.start_button = tk.Button(self, text='开始统计', command=self.start_count)
        self.start_button.pack()

        self.result_text = tk.Text(self, height=10)
        self.result_text.pack()

        self.show_button = tk.Button(self, text='显示统计结果', command=self.show_result)
        self.show_button.pack()

    def start_count(self):
        text = ''
        if self.virtual_var.get():
            text += '文言虚词词频：\n'
            for word, freq in virtual_word_freq.items():
                text += f'{word}: {freq}\n'
            text += '\n'

        if self.real_var.get():
            text += '文言实词词频：\n'
            for word, freq in real_word_freq.items():
                text += f'{word}: {freq}\n'
            text += '\n'
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, text)

    def getflag(self):
        if self.virtual_var.get():
            return 0
        elif self.real_var.get():
            return 1
    def show_result(self):
        if self.virtual_var.get() :
            plt.bar(range(len(virtual_word_freq)), list(virtual_word_freq.values()), align='center')
            plt.xticks(range(len(virtual_word_freq)), list(virtual_word_freq.keys()))
            plt.title('文言虚词词频统计')
            plt.xlabel('词语')
            plt.ylabel('出现频率')
            plt.show()
        elif self.real_var.get():
            plt.bar(range(len(virtual_word_freq)), list(virtual_word_freq.values()), align='center')
            plt.xticks(range(len(virtual_word_freq)), list(virtual_word_freq.keys()))
            plt.title('文言实词词频统计')
            plt.xlabel('词语')
            plt.ylabel('出现频率')
            plt.show()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
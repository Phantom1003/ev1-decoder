import os, tkinter, windnd, chardet, locale
from tkinter import messagebox

def dnd_file(files, root_window=None):
    for file in files:
        try:
            try:
                file = file.decode(sys_enc)
            except UnicodeDecodeError:
                file = file.decode('utf-8')
        except Exception as e:
            messagebox.showerror("解码错误", f"无法解码文件路径:\n{type(e).__name__}: {e}", parent=root_window)
            continue

        if (file.split(".")[-1] != "ev1"):
            print(f"Ignore {file}")
            continue

        print(f"Convert {file}")
        try:
            with open(file, 'rb+') as f:
                raw = f.read(100)
                data = bytearray(raw)

                for idx, b in enumerate(data):
                    data[idx] = b ^ 0xff

                raw = bytes(data)
                f.seek(0)
                f.write(raw)
                f.close()

                os.rename(file, file + '.flv')
        except Exception as e:
            messagebox.showerror("文件处理错误", f"处理文件时出错 '{file}':\n{type(e).__name__}: {e}", parent=root_window)

sys_enc = locale.getpreferredencoding()

root = tkinter.Tk()
root.geometry('400x300')
root.title('DV1: EV1 Decoder')
windnd.hook_dropfiles(root, func=lambda files: dnd_file(files, root_window=root))
label = tkinter.Label(root, text ='Drop *.ev1 on me :)')
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
root.mainloop()

import os, tkinter, windnd, chardet, locale

def dnd_file(files):
    for file in files:
        try:
            file = file.decode(sys_enc)
        except UnicodeDecodeError:
            file = file.decode('utf-8')

        if (file.split(".")[-1] != "ev1"):
            print(f"Ignore {file}")
            continue

        print(f"Convert {file}")
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

sys_enc = locale.getpreferredencoding()

root = tkinter.Tk()
root.geometry('400x300')
root.title('DV1: EV1 Decoder')
windnd.hook_dropfiles(root, func=dnd_file)
label = tkinter.Label(root, text ='Drop *.ev1 on me :)')
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
root.mainloop()

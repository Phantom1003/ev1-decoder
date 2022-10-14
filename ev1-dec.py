import os, sys
import tkinter
from tkinter.messagebox import showinfo
import windnd

def dnd_file(files):
    for file in files:
        file = file.decode()
        
        if (file.split(".")[-1] != "ev1"):
            print("Ignore " + file)
            continue

        print("Convert " + file)
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


root = tkinter.Tk()
root.geometry('400x300')
root.title('EV1 decode')
windnd.hook_dropfiles(root, func=dnd_file)
label = tkinter.Label(root, text ='Drop *.ev1 on me :)')
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
root.mainloop()


# if (len(sys.argv) != 2):
#     print("ev1 format decoder: missing input file!")
#     print("Usage: python3 dec.py [enc file]")
#     exit(1)


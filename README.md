# ev1 Format Decoder
## Quick Try
Download the [exe](https://github.com/Phantom1003/ev1-decoder/releases/download/v0.2/ev1-dec.exe) or execute the script:
```bash
$ pip install -r requirements.txt 
$ python ev1-dec.py
```
And then, drag and drop your ev1 video on the decoder window.

## Build
```bash
$ pip install pyinstaller
$ pyinstaller -F .\ev1-dec.py --noconsole
```
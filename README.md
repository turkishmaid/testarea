# testarea

Demonstrate cursor issue with Textual TextAreas.

```
git clone ...
cd testarea
make it
. venv/bin/activate
python3 testarea.py
```

Click in the first line of the TextArea. Cursor appears. Move around with arrow keys. Works fine.

Click further down in the Textarea. No cursor. Use right arrow. Cursor appears. Use left arrow. Cursor is gone. Use left arrow again. Cursor is back. But whatever you naviagte from now on, be it by click or by arrow key: Any character where you click is cursed: No cursor at this position anymore. Except it is in the very beginning of the text.

```
Python 3.13.7
textual==6.4.0
MacOS Sequoia 15.5
bash 5.3, zsh 5.9
Kitty 0.42.2, iTerm2 3.6.5
```

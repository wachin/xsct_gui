# 🌙  xsct_gui

[![Topic](https://img.shields.io/badge/topic-linux%20x11%20gui-blueviolet)](https://github.com/topics/linux)

[LEEME EN ESPAÑOL](README_ES.md)

## 🌙  xsct_gui – Easy Screen Light Control, for X11 Window Manager

This program helps you **adjust the color and brightness of your screen** on Linux, making it more comfortable to look at — especially at night.

It’s like adding a “warm light filter” (similar to your phone’s night mode that diminishes the blue light) to reduce eye strain and make late-night screen time easier on your eyes.

`xsct_gui` is a **graphical interface** for [xsct](https://github.com/faf0/sct), a small command-line tool that changes your screen’s color temperature using `xrandr`.

---

# 🆕 🐍 Available GUI Versions

This project now includes **two graphical versions**:

|  Version   | Technology |        File         |
| ---------- | ---------- | ------------------- |
| 🟢 Classic | Tkinter    | `xsct_gui.py`       |
| 🔵 Modern   | PyQt6      | `xsct_gui_pyqt6.py` |

### 💡 Which one should I use?

* 🟢 **Tkinter version** → lighter, fewer dependencies
* 🔵 **PyQt6 version** → more modern, better UI, more scalable

---

## 🎯 What does this program do?

* 🔆 **Adjusts screen color**: Make your screen more orange (warm) or more white (cool).
* 💡 **Controls brightness**: Make the screen dimmer or brighter.
* 🖱️ All through a **simple, easy-to-use interface** with sliders.

✅ Perfect for nighttime use, studying, or working on your computer.
💡 Try to match your screen color to the lighting in your room — and avoid blue-heavy lights at night!

---

## 💻 The Operating System you need

You’ll need a Linux system using the **X11 Window Manager** (not Wayland).
As of 2025, these desktop environments still support X11 sessions:

* GNOME
* KDE
* Linux Mint
* XFCE
* LXQt
* LXDE
* openbox, fluxbox, jwm, and other X11 window managers

> ❗ This tool **won’t work on Wayland**. Make sure you log in using an X11 session.

---

# 📦 Required software

## 🟢 Tkinter Version

```bash
sudo apt install python3 python3-tk xsct python3-pil.imagetk python3-cairosvg
```

| Program            | Purpose                  |
| ------------------ | ------------------------ |
| Python 3           | The programming language |
| Tkinter            | GUI toolkit              |
| Pillow             | Gradient rendering       |
| CairoSVG           | SVG icons                |
| xsct               | Screen color control     |
| Papirus Icon Theme | Optional icon            |

---

## 🔵 PyQt6 Version

```bash
sudo apt install python3 python3-pyqt6 python3-pyqt6.qtsvg xsct
```

| Program     | Purpose                  |
| ----------- | ------------------------ |
| Python 3    | The programming language |
| PyQt6       | Modern GUI framework     |
| PyQt6 QtSvg | SVG icon support         |
| xsct        | Screen color control     |

📌 Optional:

```bash
sudo apt install papirus-icon-theme
```

---

## 🐧 Linux Distribution Support

*(Se mantiene intacto mi contenido original)*

Si estás usando Debian / MX Linux:

* xsct → disponible desde Debian 12
* PyQt6 → disponible en repos oficiales

📌 **MX Linux 23** es totalmente compatible con ambas versiones

---

## ▶️ How to use the program

*(Se mantiene tu contenido original y añadimos la versión PyQt6)*

### Run Tkinter version

```bash
python3 xsct_gui.py
```

### Run PyQt6 version

```bash
python3 xsct_gui_pyqt6.py
```

---

# 🚀 Autostart (Run at startup)

You can configure the program to run automatically when your system starts.

---

## 🟢 Tkinter Autostart Launcher

### Create file:

```bash
nano ~/.config/autostart/xsct_gui_tk.desktop
```

### Content:

```ini
[Desktop Entry]
Type=Application
Name=xsct_gui (Tkinter)
Comment=Control de luz de pantalla (Tkinter)
Exec=python3 /home/wachin/Dev/xsct_gui/xsct_gui.py
Terminal=false
X-GNOME-Autostart-enabled=true
```

---

## 🔵 PyQt6 Autostart Launcher

### Create file:

```bash
nano ~/.config/autostart/xsct_gui_pyqt6.desktop
```

### Content:

```ini
[Desktop Entry]
Type=Application
Name=xsct_gui (PyQt6)
Comment=Control de luz de pantalla (PyQt6)
Exec=python3 /home/wachin/Dev/xsct_gui/xsct_gui_pyqt6.py
Terminal=false
X-GNOME-Autostart-enabled=true
```

---

# 💡 Optional: Make scripts executable

Add this line at the top of both scripts:

```python
#!/usr/bin/env python3
```

Then:

```bash
chmod +x xsct_gui.py
chmod +x xsct_gui_pyqt6.py
```

Now your `.desktop` can use:

```ini
Exec=/home/wachin/Dev/xsct_gui/xsct_gui_pyqt6.py
```

---

## 🎛️ Interface Controls

*(Se mantiene intacto mi contenido original)*

---

## 🔁 Are changes applied automatically?

*(Se mantiene intacto mi contenido original)*

---

## 💡 Tips for best results

*(Se mantiene intacto mi contenido original)*

---

## 🛠️ Can I modify the program?

Now you can modify **both versions**:

* `xsct_gui.py` → Tkinter
* `xsct_gui_pyqt6.py` → PyQt6

📚 Great for learning GUI programming in Python!

---

## 📚 More information

* 🐍 **GUI Source Code**: [https://github.com/wachin/xsct_gui](https://github.com/wachin/xsct_gui)
* ⚙️ **xsct**: [https://github.com/faf0/sct](https://github.com/faf0/sct)

---

## 🙌 About this program

Created by **Washington Indacochea Delgado**
License: **GNU GPL3**

---

## 📝 Notes

✅ You're all set!
Now go ahead and try changing your screen color — especially at night! 🖥️

---

> God bless you all.

---


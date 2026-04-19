# 🌙  xsct_gui

[![Topic](https://img.shields.io/badge/topic-linux%20x11%20gui-blueviolet)](https://github.com/topics/linux)

[LEEME EN ESPAÑOL](README_ES.md)

## 🌙  xsct_gui – Easy Screen Light Control, for X11 Window Manager

This program helps you **adjust the color and brightness of your screen** on Linux, making it more comfortable to look at — especially at night.

It’s like adding a “warm light filter” (similar to your phone’s night mode that diminishes the blue light) to reduce eye strain and make late-night screen time easier on your eyes.

`xsct_gui` is a **graphical interface** for [xsct](https://github.com/faf0/sct), a small command-line tool that changes your screen’s color temperature using `xrandr`.

---

## 🎯 What does this program do?

- 🔆 **Adjusts screen color**: Make your screen more orange (warm) or more white (cool).
- 💡 **Controls brightness**: Make the screen dimmer or brighter.
- 🖱️ All through a **simple, easy-to-use interface** with sliders.

✅ Perfect for nighttime use, studying, or working on your computer.  
💡 Try to match your screen color to the lighting in your room — and avoid blue-heavy lights at night!

---

## 💻 The Operating System you need

You’ll need a Linux system using the **X11 Window Manager** (not Wayland).  
As of 2025, these desktop environments still support X11 sessions:

- GNOME
- KDE
- Linux Mint
- XFCE
- LXQt
- LXDE
- openbox, fluxbox, jwm, and other X11 window managers

> ❗ This tool **won’t work on Wayland**. Make sure you log in using an X11 session.

### ✅ Required software

Before using `xsct_gui`, make sure you have these installed (open a terminal and run):

```bash
sudo apt install python3 python3-tk xsct python3-pil.imagetk python3-cairosvg python3-pyqt6.qtsvg
```

The following is a table with the description of each one

|                      Program                      |                                         Purpose                                         |
| ----------------------------------------------- | ----------------------------------------------------------------------------- |
| **Python 3**                                    | The programming language the GUI is written in.                |
| **Tkinter** (`python3-tk`)                 | Creates the window and buttons (GUI toolkit).                     |
| **Pillow** (`python3-pil.imagetk`)    | Displays the colorful gradient bars.                                       |
| **CairoSVG** (`python3-cairosvg`) | Allows the program to show SVG icons (like the app icon). |
| **xsct**                                            | The actual tool that changes your screen color.                   |
| **Papirus Icon Theme**                 | Provides a nice app icon.                                                      |

> 📝 If you're using **Debian 11 (bullseye)** or **Debian 10 (buster)**, `xsct` isn't available. You'll need to compile it manually (see instructions at the end).

---

## 🐧 Linux Distribution Support

### Ubuntu (and flavors like Kubuntu, Xubuntu, etc.)
If you're using Ubuntu and its flavors that support X11 logins, those packages are available in the repositories:

- [https://packages.ubuntu.com/xsct](https://packages.ubuntu.com/xsct) **Since Noble (24.04LTS)**
- [https://packages.ubuntu.com/papirus-icon-theme](https://packages.ubuntu.com/papirus-icon-theme) Since Jammy (22.04LTS)
- [https://packages.ubuntu.com/python3](https://packages.ubuntu.com/python3) Since Jammy (22.04LTS)
- [https://packages.ubuntu.com/python3-tk](https://packages.ubuntu.com/python3-tk) Since Jammy (22.04LTS)
- [https://packages.ubuntu.com/python3-pil.imagetk](https://packages.ubuntu.com/python3-pil.imagetk) Since jammy (22.04LTS)
- [https://packages.ubuntu.com/python3-cairosvg](https://packages.ubuntu.com/python3-cairosvg) Since jammy (22.04LTS)

📌 **Note:** Linux Mint is based on Ubuntu, so these packages may have those names there as well.

### Debian (and derivatives like MX Linux, antiX)
If you're using Debian and its derivatives like MX Linux, antiX, etc., where you can log in with X11, those packages are available in the repositories:

* [https://packages.debian.org/xsct](https://packages.debian.org/xsct) **since Debian 12**
* [https://packages.debian.org/papirus-icon-theme](https://packages.debian.org/papirus-icon-theme) since Debian 10
* [https://packages.debian.org/python3](https://packages.debian.org/python3) since Debian 10
* [https://packages.debian.org/python3-tk](https://packages.debian.org/python3-tk) since Debian 10
* [https://packages.debian.org/python3-pil.imagetk](https://packages.debian.org/python3-pil.imagetk) Since Debian 10
* [https://packages.debian.org/python3-cairosvg](https://packages.debian.org/python3-cairosvg) Since Debian 10

📌 **Note:** MX Linux 23, antiX 23, and others are based on Debian 12

---

## ▶️ How to use the program
First, you need to have the program in a folder on your Linux computer

### **1st OPTION: Download the repository**
Go to the website:

[https://github.com/wachin/xsct_gui](https://github.com/wachin/xsct_gui)

click on the arrow-like dropdown in Code:

**<>  Code ▼**

and click on:

**Download ZIP**

extract it, and inside the folder you'll find the `Launcher.sh` file
or you can clone it:

### **2nd OPTION: Clone the repository**

**1.-** Since we already have git installed, open a terminal in a folder where you have Linux programs:

```bash
git clone https://github.com/wachin/xsct_gui  
```

and enter there with:

```bash
cd xsct_gui  
```

## Run the Launcher.sh file

Make sure the `Launcher.sh` script is executable. In the file manager, right-click on it and in the "**Permissions**" tab make sure it "**is executable**"
Double-click the `Launcher.sh` script and click `Run`

👉 A window will open with two controls:

![](https://blogger.googleusercontent.com/img/a/AVvXsEixMsvdzTpTY5ENvil5n1a9KoIlz3rWyYkq1qlxnS4OPN_47wJmk5uBqhvM1PZu0fhNqgRf8_ttnMRlyjxns5iyFEBqZ8CIiLk22lq6Ak86gAa0O9tOxqeIrjOOQKI1WHKq4JS-2_5tvUZPZNWLCeNrnDjh-9xw2fvz54a56Rvnc9R_59TVd8EEWi7aLdc=s16000-rw)

> 💡 On some Linux you can right click on the `xsct_gui.py` file and open it with python.

### Open the program with python using `python3 xsct_gui.py`

**1.-** **Open a terminal**
**2.-** **Go to the folder** where the `xsct_gui.py` file is located, or open a terminal there from your file manager
**3.-** **Run the program** with this command:

```bash
python3 xsct_gui.py
```

👉 A window will open with two controls

---

## 🎛️ Interface Controls

### 1. 🌡️ Color Temperature (2000K to 6500K)
- **Left (2000K)**: Warm, orange tone → best for nighttime.
- **Right (6500K)**: Cool, white-blue tone → best for daytime.

📌 Move the slider to choose your preferred color.

### 2. 💡 Brightness (0.200 to 1.000)
- **Left (0.200)**: Very dim → great for dark rooms.
- **Right (1.000)**: Full brightness → best in bright environments.

📌 Adjust the slider to set your desired brightness.

---

## 🔁 Are changes applied automatically?

✅ **Yes!** As soon as you move a slider, the change takes effect immediately.

You can also click the **"About..."** button to see information about the program.

---

## 💡 Tips for best results

| Situation | Recommended Settings |
|---------|------------------------|
| 🌙 **Night or dark room** | 3000K – 4000K temperature, 0.700 – 0.800 brightness |
| ☀️ **Daytime or bright room** | 5500K – 6500K temperature, 1.000 brightness |
| 👀 **Eyes feel tired** | Try warmer color and lower brightness |

🔍 **Experiment!** Find the combo that feels best for your eyes and room lighting.

---

## 🛠️ Can I modify the program?

Absolutely! The program is written in **Python**, so you can open `xsct_gui.py` in any text editor (like **Geany**, **Thonny**, or **Mousepad**) to:
- Change colors
- Edit labels
- Add new features

📚 Great for learning **Tkinter GUI programming** in Python!

---

## 📚 More information

- 🐍 **GUI Source Code**: [https://github.com/wachin/xsct_gui](https://github.com/wachin/xsct_gui)
- ⚙️ **xsct (command-line tool)**: [https://github.com/faf0/sct](https://github.com/faf0/sct)

---

## 🙌 About this program

Created by **Washington Indacochea Delgado**
License: **GNU GPL3** (free and open source)

✨ Thank you for using `xsct_gui`!  
May your screen always be easy on the eyes. 👀💙

---

## 📝 Notes

- On **older Debian versions** (like Buster or Bullseye), `xsct` isn’t available. You’ll need to compile it manually:

```bash
# Install build dependencies
sudo apt install libx11-dev libxrandr-dev

# Clone and compile xsct
git clone https://github.com/faf0/sct
cd sct
make
sudo make install
```

Then install the GUI dependencies:
```bash
sudo apt install python3 python3-tk python3-pil.imagetk python3-cairosvg
```

Now run:
```bash
python3 xsct_gui.py
```

---

✅ You're all set!  
Now go ahead and try changing your screen color — especially at night! 🌈🖥️  
Enjoy a more comfortable computing experience!

> 🙏 God bless you all.


# 🖥️ xsct_gui – Easy Screen Light Control (for X11 Window Manager)

This program helps you **adjust the color and brightness of your screen** on Linux, making it more comfortable to look at — especially at night.

It’s like adding a “warm light filter” (similar to your phone’s night mode) to reduce eye strain and make late-night screen time easier on your eyes.

`xsct_gui` is a **graphical interface** for [xsct](https://github.com/faf0/sct), a small command-line tool that changes your screen’s color temperature using `xrandr`.

---

## 🎯 What does this program do?

- 🔆 **Adjusts screen color**: Make your screen more orange (warm) or more white (cool).
- 💡 **Controls brightness**: Make the screen dimmer or brighter.
- 🖱️ All through a **simple, easy-to-use interface** with sliders.

✅ Perfect for nighttime use, studying, or working on your computer.  
💡 Try to match your screen color to the lighting in your room — and avoid blue-heavy lights at night!

---

## 🧰 What you need to have installed

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

Before using `xsct_gui`, make sure you have these installed:

| Program | Purpose |
|--------|--------|
| **Python 3** | The programming language the GUI is written in. |
| **Tkinter** (`python3-tk`) | Creates the window and buttons (GUI toolkit). |
| **Pillow** (`python3-pil.imagetk`) | Displays the colorful gradient bars. |
| **CairoSVG** (`python3-cairosvg`) | Allows the program to show SVG icons (like the app icon). |
| **xsct** | The actual tool that changes your screen color. |
| **Papirus Icon Theme** | Provides a nice app icon. |

---

### 💻 How to install everything (one command)

Open a terminal (`Ctrl + Alt + T`) and run:

```bash
sudo apt install python3 python3-tk xsct python3-pil.imagetk python3-cairosvg
```

> 📝 If you're using **Debian 11 (bullseye)** or **Debian 10 (buster)**, `xsct` isn't available. You'll need to compile it manually (see instructions at the end).

---

### 🐧 Linux Distribution Support

#### Ubuntu (and flavors like Kubuntu, Xubuntu, etc.)
The packages are available starting from:
- Ubuntu 22.04 LTS (jammy) and newer
- xsct available since 24.04 LTS (noble)

🔗 [Ubuntu Packages](https://packages.ubuntu.com/)

> 📌 Linux Mint is based on Ubuntu — these instructions likely work there too.

#### Debian (and derivatives like MX Linux, antiX)
Available in Debian 12 and newer:
- `xsct` since Debian 12
- Other packages since Debian 10

🔗 [Debian Packages](https://packages.debian.org/)

> 📌 MX Linux 23 and antiX 23 are based on Debian 12 — everything works out of the box.

---

## ▶️ How to use the program

### Option 1: Run the `Launcher.sh` script
1. Make sure `Launcher.sh` is executable:
   - Right-click the file → **Properties** → **Permissions**
   - Check “Allow executing file as program”
2. Double-click `Launcher.sh` to run it.

### Option 2: Run from terminal
1. Open a terminal (`Ctrl + Alt + T`)
2. Go to the folder where you saved `xsct_gui.py`. For example:
   ```bash
   cd Downloads
   ```
3. Run the program:
   ```bash
   python3 xsct_gui.py
   ```

👉 A window will open with two sliders.

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

Created by **Washington Indacochea** (wachin.id@gmail.com)  
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

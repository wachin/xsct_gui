# xsct_gui

[![Topic](https://img.shields.io/badge/topic-linux%20x11%20gui-blueviolet)](https://github.com/topics/linux)

[LEEME EN ESPAÑOL](README_ES.md)

## xsct_gui – Easy Screen Light Control, for X11 Window Manager

This program helps you **adjust the color and brightness of your screen** on Linux, making it more comfortable to look at — especially at night.

It’s like adding a “warm light filter” (similar to your phone’s night mode that diminishes the blue light) to reduce eye strain and make late-night screen time easier on your eyes.

`xsct_gui` is a **graphical interface** for [xsct](https://github.com/faf0/sct), a small command-line tool that changes your screen’s color temperature using `xrandr`.

---

## What does this program do?

* 🔆 **Adjusts screen color**: Make your screen more orange (warm) or more white (cool).
* 💡 **Controls brightness**: Make the screen dimmer or brighter.
* 🖱️ All through a **simple, easy-to-use interface** with sliders.

✅ Perfect for nighttime use, studying, or working on your computer.
💡 Try to match your screen color to the lighting in your room — and avoid blue-heavy lights at night!

---

## The Operating System you need

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

## Install dependencies

```bash
sudo apt install python3 python3-pyqt6 python3-pyqt6.qtsvg pyqt6-dev-tools qt6-l10n-tools xsct
```

|        Package        |              Purpose               |
| --------------------- | ---------------------------------- |
| Python 3              | The programming language           |
| PyQt6                 | Modern GUI framework               |
| PyQt6 QtSvg           | SVG icon support                   |
| pyqt6-dev-tools       | Provides `pylupdate6` (extracts translatable strings) |
| qt6-l10n-tools        | Provides `lrelease` (compiles translations to `.qm`) |
| xsct                  | Screen color control               |


## How to use the program

### Run 

```bash
python3 xsct_gui.py
```

Alternatively, you can use the included `Launcher.sh` script:

```bash
bash Launcher.sh
```

> Make it executable first if needed: `chmod +x Launcher.sh`


# Autostart (Run at startup)

You can configure the program to run automatically when your system starts.

---

## PyQt6 Autostart Launcher

Create file:

```bash
nano ~/.config/autostart/xsct_gui_pyqt6.desktop
```

Content:

```ini
[Desktop Entry]
Type=Application
Name=xsct_gui (PyQt6)
Comment=Control de luz de pantalla (PyQt6)
Exec=python3 /home/wachin/Dev/xsct_gui/xsct_gui.py
Terminal=false
X-GNOME-Autostart-enabled=true
```

---

## Interface Controls

### 1. 🌡️ Color Temperature (2000K to 6500K)
- **Left (2000K)**: Warm, orange tone → best for nighttime.
- **Right (6500K)**: Cool, white-blue tone → best for daytime.

📌 Move the slider to choose your preferred color.

### 2. 💡 Brightness (0.300 to 1.000)
- **Left (0.300)**: Very dim → great for dark rooms.
- **Right (1.000)**: Full brightness → best in bright environments.

📌 Adjust the slider to set your desired brightness.

---

## Are changes applied automatically?

✅ **Yes!** As soon as you move a slider, the change takes effect immediately.

You can also click the **"About..."** button to see information about the program. When running in Spanish, the button and dialog will appear as **"Acerca de..."**.

---

## Tips for best results

| Situation | Recommended Settings |
|---------|------------------------|
| 🌙 **Night or dark room** | 3000K – 4000K temperature, 0.700 – 0.800 brightness |
| ☀️ **Daytime or bright room** | 5500K – 6500K temperature, 1.000 brightness |
| 👀 **Eyes feel tired** | Try warmer color and lower brightness |

🔍 **Experiment!** Find the combo that feels best for your eyes and room lighting.

---

## Translating the program into another language

The program uses **Qt Linguist** for internationalization. Translation files live in the `translations/` folder.

### How it works

| File | Purpose |
|------|---------|
| `translations/xsct_gui_es.ts` | Spanish translation source (XML, human-editable) |
| `translations/xsct_gui_es.qm` | Compiled binary loaded at runtime |

The filename suffix is the [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `es` for Spanish, `fr` for French, `de` for German). You can also use a full locale like `fr_FR` or `pt_BR`.

### Step 1 — Create a new `.ts` file for your language

Run `pylupdate6` to extract all translatable strings from the source and create a fresh `.ts` file. Replace `fr` with your language code:

```bash
pylupdate6 xsct_gui.py -ts translations/xsct_gui_fr.ts
```

### Step 2 — Translate the strings

Open the `.ts` file with **Qt Linguist** (GUI tool):

```bash
linguist translations/xsct_gui_fr.ts
```

Or edit it directly in any text editor — it is plain XML. For each `<message>` block, fill in the `<translation>` tag with your translated text:

```xml
<message>
    <source>About...</source>
    <translation>À propos...</translation>
</message>
```

### Step 3 — Compile to `.qm`

Once all strings are translated, compile the `.ts` file into the binary `.qm` format that Qt loads at runtime:

```bash
lrelease translations/xsct_gui_fr.ts -qm translations/xsct_gui_fr.qm
```

### Step 4 — Test your translation

Run the program on a system whose locale matches your language, or temporarily override the locale:

```bash
LANG=fr_FR.UTF-8 python3 xsct_gui.py
```

### Keeping translations up to date

When the source code changes and new strings are added, re-run `pylupdate6` to merge the new strings into your existing `.ts` file without losing already-translated entries:

```bash
pylupdate6 xsct_gui.py -ts translations/xsct_gui_fr.ts
```

Then translate the new entries and recompile with `lrelease`.

---

## Can I modify the program?

Absolutely! The program is written in **Python**, so you can open `xsct_gui.py` in any text editor (like **Geany**, **Thonny**, or **Mousepad**) to:

- Change colors
- Edit labels
- Add new features

---

## More information

* 🐍 **GUI Source Code**: [https://github.com/wachin/xsct_gui](https://github.com/wachin/xsct_gui)
* ⚙️ **xsct**: [https://github.com/faf0/sct](https://github.com/faf0/sct)

---

## About this program

Created by **Washington Indacochea Delgado**
License: **GNU GPL3**


import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
from PIL import Image, ImageTk
import os
import cairosvg
import io

def update_xsct():
    # Obtener valores redondeados
    temperature = int(temperature_var.get())  # Redondear a enteros
    brightness = round(brightness_var.get(), 3)  # Redondear a tres decimales

    # Actualizar los valores mostrados en la interfaz
    temperature_label.config(text=f"Temperature (K): {temperature}")  # Mostrar solo enteros
    brightness_label.config(text=f"Brightness: {brightness:.3f}")  # Mostrar con tres decimales

    # Ejecutar el comando con los valores para xsct
    subprocess.run(["xsct", str(temperature), str(brightness)])

def show_about():
    messagebox.showinfo("Acerca de xsct_gui", "xsct_gui: Una GUI (Interfaz Gráfica de Usuario) para xsct, para reducir o aumentar la cantidad de luz azul que produce la pantalla. Copyright 2024  Washington Indacochea Licencia: GNU GPL3")

# The script uses the create_gradient_image function to generate the gradient images dynamically,
# so you don't need to include the SVG files.
# This implementation should provide a user-friendly interface for adjusting your monitor's
# temperature and brightness using the xsct command.
# You can easily modify the script to add more features or adjust the appearance as needed.
def create_gradient_image(width, height, start_color, end_color):
    gradient = Image.new("RGB", (width, 1))
    for x in range(width):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * x / width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * x / width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * x / width)
        gradient.putpixel((x, 0), (r, g, b))
    return gradient.resize((width, height), Image.NEAREST)

# svg_to_photoimage function to convert SVG to a format that Tkinter can use.
def svg_to_photoimage(path, size):
    png_data = cairosvg.svg2png(url=path, output_width=size, output_height=size)
    return ImageTk.PhotoImage(Image.open(io.BytesIO(png_data)))

# Create the main window
root = tk.Tk()
root.title("xsct GUI")
root.geometry("400x250")

# Set the window icon
icon_sizes = [16, 22, 24, 32, 48, 64]
icon_paths = [f"/usr/share/icons/Papirus/{size}x{size}/apps/python.svg" for size in icon_sizes]
icons = [svg_to_photoimage(path, size) for size, path in zip(icon_sizes, icon_paths) if os.path.exists(path)]
if icons:
    root.iconphoto(True, *icons)

# Temperature selector
temperature_frame = ttk.Frame(root, padding="10")
temperature_frame.pack(fill="x")

ttk.Label(temperature_frame, text="2000 K").pack(side="left")
temperature_label = ttk.Label(temperature_frame, text="Temperature (K)")
temperature_label.pack()

# Create temperature gradient
temp_gradient = create_gradient_image(380, 20, (255, 137, 18), (254, 249, 255))
temp_gradient_img = ImageTk.PhotoImage(temp_gradient)
temp_gradient_label = ttk.Label(temperature_frame, image=temp_gradient_img)
temp_gradient_label.pack()

temperature_var = tk.IntVar(value=6500)
temperature_scale = ttk.Scale(temperature_frame, from_=2000, to=6500, variable=temperature_var, orient="horizontal", length=380, command=lambda _: update_xsct())
temperature_scale.pack()

temperature_value = ttk.Label(temperature_frame, textvariable=temperature_var)
temperature_value.pack()

# Brightness selector
brightness_frame = ttk.Frame(root, padding="10")
brightness_frame.pack(fill="x")

ttk.Label(brightness_frame, text="0.200").pack(side="left")
brightness_label = ttk.Label(brightness_frame, text="Brightness")
brightness_label.pack()

# Create brightness gradient
bright_gradient = create_gradient_image(380, 20, (51, 51, 51), (255, 255, 255))
bright_gradient_img = ImageTk.PhotoImage(bright_gradient)
bright_gradient_label = ttk.Label(brightness_frame, image=bright_gradient_img)
bright_gradient_label.pack()

brightness_var = tk.DoubleVar(value=1.000)
brightness_scale = ttk.Scale(brightness_frame, from_=0.200, to=1.000, variable=brightness_var, orient="horizontal", length=380, command=lambda _: update_xsct())
brightness_scale.pack()

brightness_value = ttk.Label(brightness_frame, textvariable=brightness_var)
brightness_value.pack()

# About button
about_button = ttk.Button(root, text="Acerca de...", command=show_about)
about_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()

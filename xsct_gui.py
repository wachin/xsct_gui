import tkinter as tk
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk

def update_xsct():
    temperature = temperature_var.get()
    brightness = brightness_var.get()
    subprocess.run(["xsct", str(temperature), str(brightness)])

def create_gradient_image(width, height, start_color, end_color):
    gradient = Image.new("RGB", (width, 1))
    for x in range(width):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * x / width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * x / width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * x / width)
        gradient.putpixel((x, 0), (r, g, b))
    return gradient.resize((width, height), Image.NEAREST)

# Create the main window
root = tk.Tk()
root.title("xsct GUI")
root.geometry("400x250")

# Temperature selector
temperature_frame = ttk.Frame(root, padding="10")
temperature_frame.pack(fill="x")

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

# Apply button
apply_button = ttk.Button(root, text="Apply", command=update_xsct)
apply_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()

# 🖥️ xsct_gui – Fácil control de la luz de tu pantalla (para X11 Window Manager)

Este programa te ayuda a **cambiar el color y el brillo de tu pantalla** en Linux, para que sea más cómoda de ver, especialmente por la noche. 

Es como ponerle un "filtro de luz cálida" (como el modo nocturno de tu celular) para que no canse tanto los ojos.

`xsct_gui` es una interfáz gráfica para [xsct](https://github.com/faf0/sct)

---

## 🎯 ¿Qué hace este programa?

- 🔆 **Ajusta el color de la pantalla**: Puedes hacerla más naranja (cálida) o más blanca (fría).
- 💡 **Cambia el brillo**: Puedes hacerla más oscura o más clara.
- 🖱️ Todo con una **interfaz sencilla y fácil de usar**, con barras deslizantes.

> ✅ Ideal para usar de noche, estudiando o trabajando en la computadora. Trata de que el color de la pantalla se asemeje al de tu cuarto, que por cierto en la noche es mejor que uses un tipo de foco o iluminación que no tenga mucha luz azúl

---

## 🧰 Lo que necesitas tener instalado

Necesitas un Sistema Operativo que use X11 como Administrador de Ventanas

Antes de usar este programa, asegúrate de que tu computadora tenga instalado lo siguiente:

### ✅ Cómo instalar todo (en una sola línea)

Abre una terminal (Ctrl + Alt + T) y escribe:

```bash
sudo apt install python3 python3-tk xsct python3-pil.imagetk python3-cairosvg
```

|              Programa              |                       ¿Para qué sirve?                       |
| ---------------------------------- | ------------------------------------------------------------ |
| **Python 3**                       | Es el lenguaje en el que está hecho el programa.             |
| **Tkinter** (`python3-tk`)         | Sirve para mostrar la ventana y botones.                     |
| **Pillow** (`python3-pil.imagetk`) | Permite mostrar colores bonitos en las barras.               |
| **CairoSVG** (`python3-cairosvg`)  | Necesario para ver el ícono del programa.                    |
| **xsct**                           | Es el programa que realmente cambia el color de tu pantalla. |
| **Papirus Icon Theme**             | Da el ícono bonito a la ventana.                             |

### Ubuntu
Si usas Ubuntu y sus sabores, esos paquetes están en los repositorios desde:

- [https://packages.ubuntu.com/python3](https://packages.ubuntu.com/python3) Desde jammy (22.04LTS)
- [https://packages.ubuntu.com/python3-tk](https://packages.ubuntu.com/python3-tk) Desde jammy (22.04LTS) 
- [https://packages.ubuntu.com/xsct](https://packages.ubuntu.com/xsct) Desde noble (24.04LTS) 
- [https://packages.ubuntu.com/python3-pil.imagetk](https://packages.ubuntu.com/python3-pil.imagetk) Desde jammy (22.04LTS) 
- [https://packages.ubuntu.com/python3-cairosvg](https://packages.ubuntu.com/python3-cairosvg) Desde jammy (22.04LTS)


### Debian
Si usas Debian y sus derivados como MX Linux, antiX, etc, esos paquetes están en los repositorios desde:

xsct desde Debian 12 (también en MX Linux 23, antiX 23 y otros basados en este)  
[https://packages.debian.org/xsct](https://packages.debian.org/xsct)

Desde Debian 10  
[https://packages.debian.org/papirus-icon-theme](https://packages.debian.org/papirus-icon-theme)  
[https://packages.debian.org/python3](https://packages.debian.org/python3)  
[https://packages.debian.org/python3-tk](https://packages.debian.org/python3-tk)  
[https://packages.debian.org/python3-pil.imagetk](https://packages.debian.org/python3-pil.imagetk)  
[https://packages.debian.org/python3-cairosvg](https://packages.debian.org/python3-cairosvg)  





Si usas Ubuntu esos paquetes están en los repositorios desde:




> El ícono se verá bien si tienes instalado **Papirus**. Si no, igual funciona, pero sin ícono.

---

## ▶️ Cómo usar el programa

### OPCIÓN 1.- Abre el script Launcher.sh

1. Asegúrate que el script `Launcher.sh`está como ejecutable, en el administrador de archivos dele clic derecho y en la pestaña "**Permisos**" asegúrese de que "**es ejecutable**"
2. Dele doble clic al script `Launcher.sh`

👉 Se abrirá una ventana con dos controles:

![](src/vx_images/01-xsct_guit-main-window.webp)

### OPCIÓN 2.- Desde una terminal ejecuta `python3 xsct_gui.py`

1. **Abre una terminal** (tecla: `Ctrl + Alt + T`)
2. **Ve a la carpeta** donde guardaste el archivo `xsct_gui.py`.  
   Por ejemplo:
   ```bash
   cd Descargas
   ```
3. **Ejecuta el programa** con este comando:
   ```bash
   python3 xsct_gui.py
   ```

👉 Se abrirá una ventana con dos controles:

---

## 🎛️ Controles de la interfaz

### 1. 🌡️ Temperatura de color (de 2000K a 6500K)

- **Izquierda (2000K)**: color naranja cálido → ideal para la noche.
- **Derecha (6500K)**: blanco brillante → ideal para el día.

> 📌 Mueve el deslizador para elegir el color que más te guste.

---

### 2. 💡 Brillo (de 0.200 a 1.000)

- **Izquierda (0.200)**: muy oscuro → buenísimo para la oscuridad.
- **Derecha (1.000)**: brillo máximo → para ambientes claros.

> 📌 Mueve el deslizador para ajustar el brillo.

---

## 🔄 ¿Los cambios se aplican solos?

¡Sí! Cada vez que mueves una barra, el cambio se aplica **automáticamente**.

También puedes hacer clic en el botón **"Acerca de..."** para ver información del programa.

---

## 💡 Consejos para usarlo bien

| Situación | Recomendación |
|---------|----------------|
| 🌙 **De noche o en una habitación oscura** | Usa **3000K – 4000K** de temperatura y **0.700 – 0.800** de brillo. |
| ☀️ **Durante el día o con luz natural** | Usa **5500K – 6500K** y brillo al máximo (**1.000**). |
| 👀 **Si te duelen los ojos** | Prueba con más naranja y menos brillo. |

> 🔎 **Experimenta** hasta encontrar la combinación que más cómoda te parezca, además según el cuarto y el tipo de foco donde estés.

---

## 🛠️ ¿Puedo modificar el programa?

¡Claro! Este programa está hecho en **Python** y puedes abrir el archivo `xsct_gui.py` con cualquier editor de texto (como **Geany**, **Thonny** o **Mousepad**) para ver cómo funciona o cambiar colores, mensajes, etc.

> 📚 Es un buen ejemplo para aprender sobre interfaces gráficas con **Tkinter**.

---

## 📚 Más información

- 🐍 Código del programa: [https://github.com/wachin/xsct_gui](https://github.com/wachin/xsct_gui)
- ⚙️ El programa xsct: [https://github.com/faf0/sct](https://github.com/faf0/sct)

---

## 🙌 Agradecimiento

Este programa fue creado por **Washington Indacochea** (wachin.id@gmail.com), con licencia libre **GNU GPL3**.

> ✨ ¡Gracias por usarlo!  
> Que tu pantalla sea siempre cómoda para tus ojos. 👀💙

---

> 📝 Nota: Si usas una versión antigua de Debian (como Buster), puede que debas cambiar `xsct` por `sct` en el código. Pero en Debian 12 y MX Linux 23, todo funciona sin problemas.

---

✅ Listo. Ahora ya sabes cómo usar `xsct_gui`.  
¡Abre la terminal y prueba cambiar el color de tu pantalla especialmente en la noche! 🌈🖥️

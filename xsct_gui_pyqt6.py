#!/usr/bin/env python3

import os
import sys
import subprocess

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import (
    QPixmap,
    QPainter,
    QLinearGradient,
    QColor,
    QIcon,
    QAction,
)
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSlider,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Acerca de xsct_gui")
        self.setMinimumSize(430, 430)

        layout = QVBoxLayout(self)

        text = QTextBrowser()
        text.setOpenExternalLinks(True)
        text.setHtml("""
        <h2>xsct_gui</h2>

        <p>Una <i>GUI</i> (Interfaz Gráfica de Usuario) para xsct,
        para reducir o aumentar la cantidad de luz azul que produce la pantalla.</p>

        <p>Copyright 2024 Washington Indacochea Delgado.<br>
        wachin.id@gmail.com<br>
        Licencia: GNU GPL3.</p>

        <p>Este programa permite ajustar fácilmente la temperatura de color y el brillo
        de su pantalla, ayudando a reducir la fatiga visual y mejorar su experiencia
        de uso del ordenador.</p>

        <p><i>Para más información, visite:</i></p>

        <p>
        xsct_gui una GUI para xsct<br>
        <a href="https://github.com/wachin/xsct_gui">https://github.com/wachin/xsct_gui</a>
        </p>

        <p>
        Xsct (X11 set color temperature)<br>
        <a href="https://github.com/faf0/sct">https://github.com/faf0/sct</a>
        </p>
        """)
        layout.addWidget(text)

        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)


class GradientLabel(QLabel):
    def __init__(self, width, height, start_color, end_color, parent=None):
        super().__init__(parent)
        self.setFixedSize(width, height)
        self.start_color = QColor(*start_color)
        self.end_color = QColor(*end_color)
        self.update_gradient()

    def update_gradient(self):
        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, self.start_color)
        gradient.setColorAt(1.0, self.end_color)
        painter.fillRect(0, 0, self.width(), self.height(), gradient)
        painter.end()

        self.setPixmap(pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("xsct GUI")
        self.setFixedSize(420, 260)

        self.temp_min = 2000
        self.temp_max = 6500

        # Guardamos brillo en milésimas para usar slider entero
        self.brightness_min = 300
        self.brightness_max = 1000

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.main_layout = QVBoxLayout(self.central)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        self.main_layout.setSpacing(12)

        self.build_temperature_section()
        self.build_brightness_section()
        self.build_buttons()

        self.set_window_icon()

        self.update_labels()
        self.apply_xsct()

    def build_temperature_section(self):
        temp_container = QVBoxLayout()
        temp_container.setSpacing(6)

        temp_top_row = QHBoxLayout()
        temp_min_label = QLabel("2000 K")
        self.temperature_label = QLabel("Temperature (K): 6500")
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        temp_top_row.addWidget(temp_min_label)
        temp_top_row.addStretch()
        temp_top_row.addWidget(self.temperature_label)
        temp_top_row.addStretch()

        temp_container.addLayout(temp_top_row)

        self.temp_gradient = GradientLabel(
            380, 20,
            (255, 137, 18),
            (254, 249, 255)
        )
        temp_container.addWidget(self.temp_gradient, alignment=Qt.AlignmentFlag.AlignCenter)

        self.temperature_slider = QSlider(Qt.Orientation.Horizontal)
        self.temperature_slider.setRange(self.temp_min, self.temp_max)
        self.temperature_slider.setValue(6500)
        self.temperature_slider.valueChanged.connect(self.on_values_changed)
        temp_container.addWidget(self.temperature_slider)

        self.temperature_value = QLabel("6500")
        self.temperature_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        temp_container.addWidget(self.temperature_value)

        self.main_layout.addLayout(temp_container)

    def build_brightness_section(self):
        bright_container = QVBoxLayout()
        bright_container.setSpacing(6)

        bright_top_row = QHBoxLayout()
        bright_min_label = QLabel("0.300")
        self.brightness_label = QLabel("Brightness: 1.000")
        self.brightness_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bright_top_row.addWidget(bright_min_label)
        bright_top_row.addStretch()
        bright_top_row.addWidget(self.brightness_label)
        bright_top_row.addStretch()

        bright_container.addLayout(bright_top_row)

        self.bright_gradient = GradientLabel(
            380, 20,
            (51, 51, 51),
            (255, 255, 255)
        )
        bright_container.addWidget(self.bright_gradient, alignment=Qt.AlignmentFlag.AlignCenter)

        self.brightness_slider = QSlider(Qt.Orientation.Horizontal)
        self.brightness_slider.setRange(self.brightness_min, self.brightness_max)
        self.brightness_slider.setValue(1000)
        self.brightness_slider.valueChanged.connect(self.on_values_changed)
        bright_container.addWidget(self.brightness_slider)

        self.brightness_value = QLabel("1.000")
        self.brightness_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bright_container.addWidget(self.brightness_value)

        self.main_layout.addLayout(bright_container)

    def build_buttons(self):
        row = QHBoxLayout()
        row.addStretch()

        about_button = QPushButton("Acerca de...")
        about_button.clicked.connect(self.show_about)
        row.addWidget(about_button)

        row.addStretch()
        self.main_layout.addLayout(row)

    def set_window_icon(self):
        icon_sizes = [16, 22, 24, 32, 48, 64]
        icon_paths = [
            f"/usr/share/icons/Papirus/{size}x{size}/apps/python.svg"
            for size in icon_sizes
        ]

        for size, path in zip(icon_sizes, icon_paths):
            if os.path.exists(path):
                icon = self.svg_to_icon(path, size)
                if not icon.isNull():
                    self.setWindowIcon(icon)
                    break

    def svg_to_icon(self, path, size):
        renderer = QSvgRenderer(path)
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return QIcon(pixmap)

    def get_temperature(self):
        return self.temperature_slider.value()

    def get_brightness(self):
        return self.brightness_slider.value() / 1000.0

    def update_labels(self):
        temperature = self.get_temperature()
        brightness = self.get_brightness()

        self.temperature_label.setText(f"Temperature (K): {temperature}")
        self.temperature_value.setText(str(temperature))

        self.brightness_label.setText(f"Brightness: {brightness:.3f}")
        self.brightness_value.setText(f"{brightness:.3f}")

    def apply_xsct(self):
        temperature = self.get_temperature()
        brightness = self.get_brightness()

        try:
            subprocess.run(
                ["xsct", str(temperature), f"{brightness:.3f}"],
                check=False
            )
        except FileNotFoundError:
            QMessageBox.critical(
                self,
                "Error",
                "No se encontró el comando 'xsct'.\n\n"
                "Instálalo con:\n"
                "sudo apt install xsct"
            )

    def on_values_changed(self):
        self.update_labels()
        self.apply_xsct()

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

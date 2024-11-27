import flet as ft
import time
import threading

class BlockerApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.is_blocked = False
        self.timer_text = ft.Text("", size=24, color="white")  # Inicializar el texto del temporizador aquí

    def build(self):
        self.cover = ft.Container(
            content=ft.Column([
                ft.Text("Pantalla Bloqueada", size=48, weight="bold", color="white"),
                self.timer_text  # Texto para mostrar el temporizador
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="black",
            width=800,
            height=600,
            visible=False  # Inicialmente no visible
        )
        self.time_input = ft.TextField(label="Tiempo en segundos", value="60", width=200)  # Campo para ingresar el tiempo
        self.timer_text = ft.Text("", size=24, color="white")  # Inicializar el texto del temporizador
        self.main_content = ft.Column([
            ft.Text("Bloqueador de Redes Sociales", size=24, weight="bold"),
            self.time_input,  # Agregar el campo de entrada para el tiempo
            ft.ElevatedButton("Bloquear Facebook", on_click=self.block_facebook, width=200),
            ft.ElevatedButton("Desbloquear Facebook", on_click=self.unblock_facebook, width=200),
            ft.Text("", key="status", size=18),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        return ft.Column([self.main_content, self.cover])  # Agregar ambos componentes

    def block_facebook(self, e):
        if not self.is_blocked:
            self.is_blocked = True
            self.update_status("Facebook está bloqueado.")
            self.cover.visible = True  # Mostrar la pantalla de bloqueo
            self.main_content.visible = False  # Ocultar el contenido principal
            self.update()  # Actualizar la interfaz
            threading.Thread(target=self.temporarily_block, daemon=True).start()

    def temporarily_block(self):
        try:
            block_time = int(self.time_input.value)  # Obtener el tiempo de bloqueo del campo de entrada
            for remaining in range(block_time, 0, -1):
                self.timer_text.value = f"Tiempo restante: {remaining} segundos"  # Actualizar el temporizador
                self.update()  # Actualizar la interfaz
                time.sleep(1)  # Esperar un segundo
        except ValueError:
            self.update_status("Por favor, ingresa un número válido.")
            return
        self.unblock_facebook(None)

    def unblock_facebook(self, e):
        self.is_blocked = False
        self.update_status("Facebook está desbloqueado.")
        self.cover.visible = False  # Ocultar la pantalla de bloqueo
        self.main_content.visible = True  # Mostrar el contenido principal nuevamente
        self.timer_text.value = ""  # Limpiar el temporizador
        self.update()  # Actualizar la interfaz

    def update_status(self, message):
        status_control = next((ctrl for ctrl in self.controls if ctrl.key == "status"), None)
        if status_control:
            status_control.value = message
            self.update()

def main(page: ft.Page):
    page.title = "Bloqueador de Redes Sociales"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(BlockerApp())

ft.app(target=main)

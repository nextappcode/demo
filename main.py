import flet as ft
import time
import threading

class BlockerApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.is_blocked = False

    def build(self):
        return ft.Column([
            ft.Text("Bloqueador de Redes Sociales", size=24, weight="bold"),
            ft.ElevatedButton("Bloquear Facebook", on_click=self.block_facebook, width=200),
            ft.ElevatedButton("Desbloquear Facebook", on_click=self.unblock_facebook, width=200),
            ft.Text("", key="status", size=18)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def block_facebook(self, e):
        if not self.is_blocked:
            self.is_blocked = True
            self.update_status("Facebook está bloqueado.")
            threading.Thread(target=self.temporarily_block, daemon=True).start()

    def unblock_facebook(self, e):
        self.is_blocked = False
        self.update_status("Facebook está desbloqueado.")

    def temporarily_block(self):
        time.sleep(60)  # Bloquea por 60 segundos
        self.unblock_facebook(None)

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

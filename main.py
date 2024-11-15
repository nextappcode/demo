import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window.always_on_top = True

    page.add(
        ft.Video(
            playlist=[
                ft.VideoMedia(resource="https://codigopiter.neocities.org/canales_locales.txt"),
            ],
            fill_color=ft.colors.BLACK,
            expand=True,
            autoplay=True,
            volume=60,
        ),
    )


ft.app(main, assets_dir="assets")

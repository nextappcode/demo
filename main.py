import flet as ft


def main(page: ft.Page):
    # Lista de canales organizada por categorías
    canales = [
        # Canales Bolivianos
        {"nombre": "ATB", "url": "https://cdn.digital.com.bo/__cl/cg:sworigin2/__c/ATB/__op/hls-default/__f/index.m3u8"},
        {"nombre": "Bolivia TV 7.2", "url": "https://video1.getstreamhosting.com:1936/8224/8224/playlist.m3u8"},
        {"nombre": "Bolivision", "url": "https://alba-bo-bolivision-upptv.stream.mediatiquestream.com/index.m3u8"},
        {"nombre": "PAT Santa Cruz", "url": "https://w8.redpat.tv:7777/play/110/index.m3u8"},
        {"nombre": "Red Uno", "url": "https://streamer03.digital.com.bo/session/4e839498-b325-47f7-987f-205b4831346f/2ap337/__cl/cg:sworigin2/__c/REDUNO/__op/hls-default/__f/index.m3u8"},
        {"nombre": "RTP", "url": "http://136.243.3.70:1935/RtpBolivia/RtpBolivia/playlist.m3u8"},
        {"nombre": "Unitel Santa Cruz", "url": "https://cdn.digital.com.bo/__cl/cg:sworigin2/__c/UNITEL/__op/hls-default/__f/index.m3u8"},
        
        # Canales de Películas y Series
        {"nombre": "Cinemax HD", "url": "http://191.52.214.5:8000/play/a02a/index.m3u8"},
        {"nombre": "FX HD", "url": "http://191.52.214.5:8000/play/a02r/index.m3u8"},
        {"nombre": "HBO HD", "url": "http://191.52.214.5:8000/play/a02z/index.m3u8"},
        {"nombre": "HBO 2 HD", "url": "http://191.52.214.5:8000/play/a06o/index.m3u8"},
        {"nombre": "HBO Family HD", "url": "http://191.52.214.5:8000/play/a06q/index.m3u8"},
        {"nombre": "HBO XTREME HD", "url": "http://191.52.214.5:8000/play/a03x/index.m3u8"},
        {"nombre": "Paramount HD", "url": "http://191.52.214.5:8000/play/a032/index.m3u8"},
        {"nombre": "STAR CHANNEL HD", "url": "http://191.52.214.5:8000/play/a02k/index.m3u8"},
        {"nombre": "Space HD", "url": "http://191.52.214.5:8000/play/a01w/index.m3u8"},
        {"nombre": "TNT HD", "url": "http://191.52.214.5:8000/play/a024/index.m3u8"},
        {"nombre": "TNT Series HD", "url": "http://191.52.214.5:8000/play/a059/index.m3u8"},
        {"nombre": "Warner Channel HD", "url": "http://191.52.214.5:8000/play/a01u/index.m3u8"},
        
        # Canales Culturales
        {"nombre": "Animal Planet", "url": "http://191.52.214.5:8000/play/a038/index.m3u8"},
        {"nombre": "Discovery Channel", "url": "http://45.166.92.22:58001/play/a01n"},
        {"nombre": "Discovery H&H HD", "url": "http://191.52.214.5:8000/play/a02i/index.m3u8"},
        {"nombre": "Discovery Kids HD", "url": "http://191.52.214.5:8000/play/a02h/index.m3u8"},
        {"nombre": "Discovery Theater HD", "url": "http://191.52.214.5:8000/play/a02j/index.m3u8"},
        {"nombre": "History Channel HD", "url": "http://191.52.214.5:8000/play/a01r/index.m3u8"},
        {"nombre": "Nat Geo HD", "url": "http://191.52.214.5:8000/play/a02u/index.m3u8"},
        
        # Canales Deportivos
        {"nombre": "Fox Sports 1 HD", "url": "http://191.52.214.5:8000/play/a03u/index.m3u8"},
        {"nombre": "Fox Sports 2 HD", "url": "http://191.52.214.5:8000/play/a02o/index.m3u8"},
        {"nombre": "Fox Sports 3 HD", "url": "http://191.52.214.5:8000/play/a026/index.m3u8"},
        
        # Noticias
        {"nombre": "CNN International", "url": "http://181.78.208.254:8008/play/a03m"},
    ]
    
    def on_resized(e):
        # Obtener las dimensiones actuales
        width = page.window.width
        height = page.window.height
        
        # Si el ancho es mayor que el alto (landscape/horizontal)
        if width > height:
            contenedor.horizontal = True
            dropdown_container.alignment = ft.MainAxisAlignment.START
            dropdown.width = width * 0.3
            reproductor.expand = True
        # Si el alto es mayor que el ancho (portrait/vertical)
        else:
            contenedor.horizontal = False
            dropdown_container.alignment = ft.MainAxisAlignment.CENTER
            dropdown.width = width * 0.8
            reproductor.expand = True
        
        page.update()

    # Crear el reproductor de video
    reproductor = ft.Video(
        expand=True,
        autoplay=True,
        volume=60,
        fill_color=ft.colors.BLACK,
    )
    # Establecer la URL inicial
    reproductor.media_url = canales[0]["url"]

    def cambiar_canal(e):
        if e.data:  # Verifica si hay un canal seleccionado
            reproductor.media_url = e.data
            reproductor.update()

    # Crear el menú desplegable
    dropdown = ft.Dropdown(
        label="Selecciona un canal",
        hint_text="Elige un canal para ver",
        options=[
            ft.dropdown.Option(
                text=canal["nombre"],
                data=canal["url"]
            ) for canal in canales
        ],
        value=canales[0]["url"],
        on_change=cambiar_canal,
        autofocus=True
    )

    # Contenedor para el dropdown
    dropdown_container = ft.Row(
        [dropdown],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Contenedor principal que cambiará según la orientación
    contenedor = ft.Row(
        [dropdown_container, reproductor],
        expand=True
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.always_on_top = True
    
    # Agregar el evento de redimensionamiento
    page.on_resized = on_resized
    
    # Llamar a on_resize inicialmente para configurar el diseño
    page.add(contenedor)
    on_resized(None)


ft.app(main, assets_dir="assets")
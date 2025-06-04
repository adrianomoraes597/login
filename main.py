import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    def tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    page.add(
        ft.Stack(
            controls=[
                ft.Image(
                    src="https://wallpapers.com/images/hd/4k-office-background-tw1rq5nwu7z2ou3w.jpg",
                    fit=ft.ImageFit.COVER,
                    expand=True,
                    opacity=0.2,
                ),
                ft.Column(
                    controls=[
                        ft.Image(
                            src="prometheus.png",
                            width=150,
                            height=150
                        ),
                        ft.TextField(
                            label="UserName",
                            width=280,
                            text_align=ft.TextAlign.LEFT
                        ),
                        ft.TextField(
                            label="PassWord",
                            width=280,
                            text_align=ft.TextAlign.LEFT,
                            can_reveal_password=True,
                            password=True
                        ),
                        ft.FilledButton(
                            "Login",
                            width=220,
                            height=45
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=23
                )
            ],
            alignment=ft.alignment.center
        )
    )

# Executa no navegador, na porta 8000
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

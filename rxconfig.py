import reflex as rx

config = rx.Config(
    app_name="Dominio_venta",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
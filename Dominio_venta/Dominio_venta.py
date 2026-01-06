"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

"""
class State(rx.State):
    
"""


def index() -> rx.Component:
    
    return rx.center(
                
                        rx.link(
                        
                                rx.image(src="/Venta_dominio.jpg"),
                                rx.text("Contactar con Jaitarbloo@yahoo.es ",size="5"),
                                href="https://jaitarbloo.com"
                                ),

                    
                    )

                    
       


app = rx.App()
app.add_page(index)

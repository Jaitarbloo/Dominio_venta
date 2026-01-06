import reflex as rx

config = rx.Config(
                    
                    app_name="Dominio_venta",
                    
                    api_url="https://dominio.onrender.com",
    
                   			cors_allowed_origins=[ "http://localhost:3000",
        
                                          "https://www.zabalgana.com",
        
                                        			],
                    
                    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
import reflex as rx 
from MyPortafolioWeb.Styles.styles import Size, Spacing
#90CAF9
def certificate(certificacion:str, imagen:str, url:str)->rx.Component:
    return rx.card(
    rx.hstack(
        rx.center(
            rx.image(
                src=imagen,
                width="100%",
                height="8em",
                ),
            width="40%",
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        "Certificados en: ",
                        size=Spacing.MEDIUM_SMALL.value,
                       ),
                    rx.text(
                        certificacion,
                        size=Spacing.SMALL.value,
                    ),
                    height=Size.MEDIUM_BIG.value,
                ),
            rx.link(
                rx.button(
                    "ver más",
                    variant="surface",
                    color_scheme="sky",
                    size=Spacing.SMALL.value,
                    cursor="pointer",
                  ),
                href=url,
                is_external=True,
                align_self="end", 
                #margin_top=Size.BIG.value,
            ),
            width="60%",
            padding_x=Size.MEDIUM.value,
        ),
    ),
    width="100%",
    height=Size.VERY_VERY_BIG.value,  
)
            
    
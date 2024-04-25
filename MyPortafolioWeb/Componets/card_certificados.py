import reflex as rx 
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size, Spacing
from reflex_image_zoom import image_zoom

def certificate(certificacion:str, imagen:str)->rx.Component:
    return rx.fragment(
        rx.card(
    rx.flex(
        rx.inset(
            image_zoom(
            rx.image(
                src=imagen,
                width="100%",
                height=Size.VERY_VERY_BIG.value,
                ),
            ),
            
            width="40%",
            side="left",
            pr="current",
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    "Certificado en: ",
                    size=Spacing.MEDIUM_SMALL.value,
                    margin_bottom = Size.MEDIUM.value,
                )   ,
                rx.text(
                    certificacion,
                    size=Spacing.SMALL.value,
                ),
            height=Size.MEDIUM_BIG.value,
            ),
            rx.button(
                 "Certificado formal",
                rx.icon(
                    "expand",
                    tag="expand",
                    ),
                variant="surface",
                color_scheme="sky",
                size=Spacing.SMALL.value,
                cursor="pointer",
                align_self="end", 
                margin_top=Size.ZERO.value,
                ),
            width="60%",
            padding_x=Size.MEDIUM.value,
        ),
            direction="row",
            width="100%",
    ),
        width="100%",
        height=Size.VERY_VERY_BIG.value,
        margin_y=Size.SMALL.value,
    ),
rx.divider(),
    width="100%",  
)
    

def reverse_certificate(certificacion:str, imagen:str)->rx.Component:
    return rx.fragment(
        rx.card(
    rx.flex(
        rx.inset(
            image_zoom(
            rx.image(
                src=imagen,
                width="100%",
                height=Size.VERY_VERY_BIG.value,
                ),
            ),
            
            width="40%",
            side="right",
            pl="current",
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    "Certificado en: ",
                    size=Spacing.MEDIUM_SMALL.value,
                    margin_bottom = Size.MEDIUM.value,
                )   ,
                rx.text(
                    certificacion,
                    size=Spacing.SMALL.value,
                ),
            height=Size.MEDIUM_BIG.value,
            ),
            rx.button(
                 "Certificado formal",
                rx.icon(
                    "expand",
                    tag="expand",
                    ),
                variant="surface",
                color_scheme="sky",
                size=Spacing.SMALL.value,
                cursor="pointer",
                align_self="start", 
                margin_top=Size.ZERO.value,
                ),
            width="60%",
            padding_x=Size.MEDIUM.value,
        ),
            direction="row-reverse",
            width="100%",
    ),
        width="100%",
        height=Size.VERY_VERY_BIG.value,
        margin_y=Size.SMALL.value,
    ),
rx.divider(),
    width="100%",  
)
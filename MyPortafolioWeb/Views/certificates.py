import reflex as rx
from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.certificate import  certificate

def section_certificate()->rx.Component:
    return rx.chakra.responsive_grid(
        rx.chakra.box(
            certificate(
                "Innovacion y gestion",
                "/innovacion.png",
                "/formacionInnovacionGestion",
                ),
            ),
        rx.chakra.box(
            certificate(
                "Programacion",
                "/programacion.svg",
                "/FormacionProgramacion",
            ),
        ),
        columns=[1, 1,2],
        width="100%",
        spacing=Spacing.SMALL.value,
        margin_bottom=Size.DEFAULT.value,
    )
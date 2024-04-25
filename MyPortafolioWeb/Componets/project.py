import reflex as rx
from MyPortafolioWeb.Styles.styles import Size
from MyPortafolioWeb.Componets.tittle import tittle

def project()->rx.Component:
    return rx.chakra.card(
        rx.chakra.text("detalles.......",
                       padding=Size.DEFAULT.value,
                       ),
        header=rx.chakra.heading(
        rx.chakra.image(
            src="/encriptador.jpg",
            border_radius="0.20em",
            width="100%",
            )
        ),  
        footer=rx.chakra.flex(
        rx.chakra.text("Encriptador"),
        rx.chakra.spacer(),
        rx.chakra.link("ver mas"),
        width="100%",
        align="center",
        padding=Size.DEFAULT.value,
        ),
    variant="unstyled",
    width="15em",
    box_shadow="0 0 3px #ffffff",
)
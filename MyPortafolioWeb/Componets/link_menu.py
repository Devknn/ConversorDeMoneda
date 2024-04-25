import reflex as rx
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size as Size

#Lista de la barra de navefacion

def link_menu(titulo:str,url:str)->rx.Component:
    return rx.hstack(
        rx.link(
        titulo,
        href=url, 
        color="#ffffff",   
        ),
        _hover={
            "cursor": "pointer",
            "background-color": "#3f3b3b",
            "opacity":"0.8",
            "transition":"1s ease",
            },
        padding_y=Size.DEFAULT.value,
        padding_x=Size.MEDIUM.value,
        flex_shrink=styles.Spacing.ZERO.value,
    )

def menu(tittle:str)->rx.Component:
    return rx.box(
        rx.chakra.menu(
            rx.chakra.menu_button(tittle),
            rx.chakra.menu_list(
                rx.chakra.menu_divider(),
                rx.link(
                    rx.chakra.menu_item("Programación"),
                    href="/FormacionProgramacion",
                    is_external=True
                ),
                rx.link(
                    rx.chakra.menu_item("Innovación y Gestión"),
                    href="/formacionInnovacionGestion",
                    is_external=True
                ), 
                rx.chakra.menu_divider(),
                margin_top=Size.MEDIUM.value,
                ),
        ),
        _hover={
            "cursor": "pointer",
            "background-color": "#3f3b3b",
            "opacity":"0.8",
            "transition":"1s ease",
            },
        padding_y=Size.DEFAULT.value,
        padding_x=Size.MEDIUM.value,
        flex_shrink=styles.Spacing.ZERO.value,   
    )
import reflex as rx
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size as Size

def tittle(title:str)->rx.Component:
    return rx.heading(
        title,
        rx.divider(
            margin_y=Size.SMALL.value,
            ),
        style=styles.styles_tittle,
        margin_top=Size.SMALL.value,
    )
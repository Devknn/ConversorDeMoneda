import reflex as rx
import datetime
from MyPortafolioWeb.Styles.styles import Size as Size

def footer()->rx.Component:
    return rx.vstack(
         f"© 2023-{datetime.date.today().year} Todos los derechos reservados.",
         align="center",
         width="100%",
         margin_y=Size.VERY_BIG.value,
    )
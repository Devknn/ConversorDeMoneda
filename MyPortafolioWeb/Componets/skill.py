import reflex as rx
from MyPortafolioWeb.Styles.styles import Size, Spacing

def skill(lenguaje:str, color:str)->rx.Component:
    return rx.badge(
        lenguaje,
        size = Spacing.SMALL.value,
        variant="surface",
        color_scheme=color,
        cursor="pointer",
)
import reflex as rx
from  MyPortafolioWeb.Styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.icon(
            image,
            width=Size.LARGE_SMALL.value,
            height=Size.LARGE_SMALL.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )
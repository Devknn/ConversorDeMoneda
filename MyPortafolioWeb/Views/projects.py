import reflex as rx

from MyPortafolioWeb.Styles.styles import Size
from MyPortafolioWeb.Componets.tittle import tittle
from MyPortafolioWeb.Componets.project import project


def section_projects()->rx.Component:
    return rx.hstack(
        project(),
        project(), project(),
       
        wrap="nowrap",
        justify="center",
        width="100%",
)
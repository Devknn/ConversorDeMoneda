import reflex as rx 
from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.skill import skill

def section_skills()->rx.Component:
    return rx.flex(
        skill(
            "PYTHON",
            "green",
        ),
        skill(
             "JAVA",
            "tomato",
        ),
        skill(
             "JAVASCRIP",
            "crimson",
        ),
        skill(
            "CSS",
            "violet",
        ),
        skill(
            "HTML",
            "orange",
        ),
        skill(
            "REFLEX",
            "gray",
        ),
        skill(
            "REACT",
            "blue",
        ),
        skill(
            "DJANGO",
            "green",
        ),

        spacing=Spacing.SMALL.value,
        width="100%",
        justify="center",
        wrap="wrap",
    )
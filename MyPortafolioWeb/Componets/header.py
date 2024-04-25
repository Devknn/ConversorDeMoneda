import reflex as rx 
from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.link_ico import link_icon
def header()->rx.Component:
    return rx.center(
        rx.hstack(
            rx.avatar(
                name="KenierNoriega",
                size=Spacing.MEDIUM_BIG.value,
                src="favicon.ico",
                radius="full",
                #color=TextColor.BODY.value,
                #bg=Color.CONTENT.value,                    padding="2px",
                border="4px solid blue",
                ),
            rx.vstack(
                rx.heading(
                    "!Hola! soy Kenier Noriega",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "Developer Junnior",
                    margin_top=Size.ZERO.value,
                    #color=Color.PRIMARY.value
                ),
                rx.hstack(
                        link_icon(
                            "github",
                            "FALTA URL",
                            "TikTok",
                            ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value,
                    margin_left=Size.DEFAULT.value,
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        width="100%",
        margin_bottom=Size.BIG.value,
    )
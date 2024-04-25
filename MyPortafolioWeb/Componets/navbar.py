import reflex as rx
from MyPortafolioWeb.Componets.link_menu import link_menu, menu
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size,Spacing



def navbar():
    return rx.flex(
        rx.box(
            rx.hstack(
                rx.image(
                    src="/logo.ico",
                    width=Size.LARGE.value,
                ),
            ),
            #display=["none","none","none","flex"],
            padding=Size.DEFAULT.value,
            flex_shrink=styles.Spacing.ZERO.value
        ),
        rx.spacer(),
        rx.hstack(
            link_menu("INICIO",
                      "/PortafolioKenierN",
                      ),
            menu("CERTIFICADOS"),
            link_menu("CV",
                      "/PortafolioKenierN",
                      ),                  
            link_menu("CONTACTOS",
                      "/PortafolioKenierN",
                      ),
            display=["none", "none", "flex", "flex", "flex"],
        ), 
        position="sticky",
        bg="#0C151D",
        width="100%",
        z_index="999",
        top=Spacing.ZERO.value,
    )
import reflex as rx
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.navbar import navbar
from MyPortafolioWeb.Componets.footer import footer
from MyPortafolioWeb.Componets.card_certificados import certificate, reverse_certificate
from MyPortafolioWeb.Componets.tittle import tittle
from MyPortafolioWeb.Componets.ComponentsSpline.kk import Spline

@rx.page(route='/FormacionProgramacion', title='FormacionProgramacion')

    
def programming_training()->rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.center(
                    tittle("Formaciones en Programación"),
                    width="100%",
                    text_align="center",
                    ),
                certificate(
                    "HTML5 Y CSS3 PARTE 1: MI PRIMERA PÁGINA WEB",
                    "/certificates/html5Css3[1].png",
                ),
                reverse_certificate(
                    "HTML5 Y CSS3 PARTE 2: POSICIONAMIENTO, LISTA Y NAVEGACIÓN",
                    "/certificates/html5Css3[2].png",
                ),                
                certificate(
                    "HTML5 Y CSS3 PARTE 3: TRABAJANDO CON FORMULARIOS",
                    "/certificates/html5Css3[3].png",
                ),
                reverse_certificate(
                    "HTML5 Y CSS3 PARTE 4: AVANZANDO EN CSS",
                    "/certificates/html5Css3[4].png",
                ),          
                certificate(
                    "GIT Y GITHUB: REPOSITORIO, COMMIT Y VERSIONES",
                    "/certificates/gitHub.png",
                ),
                reverse_certificate(
                    "LÓGICA DE PROGRAMACIÓN: SUMÉRGETE EN LA PROGRAMACIÓN CON JAVASCRIPT",
                    "/certificates/logicaProgramacion[1].png",
                ),                
                certificate(
                    "LÓGICA DE PROGRAMACIÓN: SUMÉRGETE EN LA EXPLORAR FUNCIONES Y LISTAS",
                    "/certificates/logicaProgramacioN[2].png",
                ),
                reverse_certificate(
                    "JAVA: CREANDO TU PRIMERA APLICACIÓN",
                    "/certificates/creandoMiPrimeraApp.png",
                ),       
                margin_top=Size.BIG.value,
                padding_x=Size.DEFAULT.value,
                max_width=styles.MAX_WIDTH,
                width="100%",
            ),
        ),
        footer(),
        Spline(),
        width="100%",   
    )
    
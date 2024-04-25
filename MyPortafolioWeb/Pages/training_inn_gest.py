import reflex as rx
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.navbar import navbar
from MyPortafolioWeb.Componets.footer import footer
from MyPortafolioWeb.Componets.card_certificados import certificate, reverse_certificate
from MyPortafolioWeb.Componets.tittle import tittle
from MyPortafolioWeb.Componets.ComponentsSpline.kk import Spline

@rx.page(route='/formacionInnovacionGestion', title='Innovación y Gestion')

    
def innovacion_gestion()->rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.center(
                tittle("Formaciones en Innovación y Gestión"),
                width="100%",
                text_align="center",
                ),
            certificate(
                "APRENDER A APRENDER: TECNICAS PARA TU AUTODESARROLLO",
                "/certificates/certificado_InnGest_00.png",
            ),
            reverse_certificate(
                "HÁBITOS: SER PRODUCTIVO PARA CUMPLIR SUS METAS PERSONALES",
                "/certificates/Certificado Habito-1.png",
           ),                
            certificate(
                "DESARROLLO DE CARRERA: CÓMO LLEGAR A LA POSICIÓN DESEADA",
                "/certificates/Certificado - DESARROLLO DE CARRERA: CÓMO LLEGAR A LA POSICIÓN DESEADA-1.png",
            ),
            reverse_certificate(
                "DESARROLLO DE CARRERA: DEMANDA DEL MERCADO",
                "/certificates/Certificado - DESARROLLO DE CARRERA: DEMANDA DEL MERCADO-1.png",
            ),             
            certificate(
                "PROPÓSITO PROFESIONAL: SER EL PROTAGONISTA DE TU CARRERA",
                "/certificates/Certificado - PROPÓSITO PROFESIONAL: SER EL PROTAGONISTA DE TU CARRERA-1.png",
            ),
            reverse_certificate(
                "LINKEDIN: COMO HACER QUE TU PERFIL TRABAJE POR TI",
                "/certificates/Certficado - LinkedIn-1.png",
            ),                
            reverse_certificate(
                "FOCO: ENFOCARSE TRAE MAS RESULTADOS PARA EL DÍA A DÍA",
                "/certificates/Certificado - Foco-1.png",
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
    
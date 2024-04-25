import reflex as rx
from MyPortafolioWeb.Componets.ComponentsSpline.spline import Spline

from MyPortafolioWeb.Styles.styles import Size, Spacing
from MyPortafolioWeb.Componets.header import header
def section_infor()->rx.Component:
    return rx.vstack(
        header(),
        rx.text(
            "¡Bienvenido a mi portafolio! Aquí encontrarás una muestra de mi trabajo, así como información sobre mis habilidades y experiencias. Estoy emocionado de conectar contigo y explorar cómo podemos trabajar juntos para llevar tus ideas a la vida en la web.",
            ),
        Spline(),
        rx.divider(),            
        rx.text(
                
                "Mi viaje en el mundo del desarrollo web ha sido emocionante y diverso. Desde mis primeros días trabajando con HTML5 y CSS3, hasta explorar el poder de JavaScript, Python y frameworks como React , Django, Reflex entre otros, he estado constantemente desafiándome a mí mismo para aprender y crecer en este campo en constante evolución.",
                ),
        rx.text(
                "Además de mi pasión por la programación, tengo una vida activa fuera de la pantalla. Disfruto dedicar tiempo al gimnasio para mantenerme en forma y saludable, explorar senderos naturales haciendo senderismo y ciclismo, y relajarme con buena música o sumergirme en fascinantes historias a través de las series.",
                ),
        rx.text(
                "Mi objetivo es crear experiencias web excepcionales que no solo sean visualmente atractivas, sino también intuitivas y funcionales. Siempre estoy emocionado de enfrentar nuevos desafíos y colaborar en proyectos que impulsen la innovación y la excelencia en la web.",
            ),
        
        rx.divider(),
        rx.divider(),

        padding_top=Size.VERY_BIG.value,
        text_indent= Size.DEFAULT.value,
        text_align= "justify",
        line_height=Size.BIG.value,
        width="100%",
        justify="center",
        weight="regular",
        size=Spacing.MEDIUM_SMALL.value,
    )
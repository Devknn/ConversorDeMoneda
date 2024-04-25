
import reflex as rx
import MyPortafolioWeb.Styles.styles as styles

class Spline(rx.Component):
    """Spline component."""
    library = '@splinetool/react-spline'
    tag = "Spline"  # Nombre del componente de Spline, puede variar según la documentación de Spline
    scene: rx.Var[str] = 'https://prod.spline.design/7mNfdehStlkDV4tY/scene.splinecode'
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]  # Cambiado a la biblioteca correcta


spline = Spline.create()

#Imagen  en 3d

def spline_view():
    return rx.center(

        spline,
        overflow="hidden",
        width="100%",
        height="26em",
        
    )


'https://prod.spline.design/7mNfdehStlkDV4tY/scene.splinecode'
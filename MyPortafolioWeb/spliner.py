import reflex as rx

class Spline(rx.Component):
    """Spline component."""
    library = '@splinetool/react-spline'
    tag = "Spline"  # Nombre del componente de Spline, puede variar según la documentación de Spline
    scene: rx.Var[str] = 'https://prod.spline.design/A1ZCAtQ8Rb6gZQNS/scene.splinecode'
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/react-spline"]  # Cambiado a la biblioteca correcta


spline = Spline.create()

#Imagen  en 3d

def spline_view():
    return rx.center(

        spline,
        overflow="hidden",
        width="100%",
        height="26em",
    )
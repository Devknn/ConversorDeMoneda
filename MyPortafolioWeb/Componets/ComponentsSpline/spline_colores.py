import reflex as rx
from reflex.vars import Var   

class Spline_colores(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[
        str
    ] = "https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


splines = Spline_colores.create


def spline_colores():
    return rx.center(
        splines(),
        overflow="hidden",
        width="100%",
        height="30em",
    )
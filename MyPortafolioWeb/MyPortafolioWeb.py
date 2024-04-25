
import reflex as rx
import MyPortafolioWeb.Styles.styles as styles
from MyPortafolioWeb.Styles.styles import Size, Spacing

from MyPortafolioWeb.Componets.navbar import navbar
from MyPortafolioWeb.Componets.footer import footer
from MyPortafolioWeb.Componets.tittle import tittle
from MyPortafolioWeb.Views.section_info import section_infor
from MyPortafolioWeb.Views.skills import section_skills
from MyPortafolioWeb.Views.certificates import section_certificate
from MyPortafolioWeb.Views.projects import section_projects

from MyPortafolioWeb.Componets.link_menu import menu

@rx.page(route='/PortafolioKenierN', title='Kenier Noriega')
def index()->rx.Component:
    return rx.fragment(
        navbar(),
        rx.center(
            rx.vstack(
                section_infor(),
                tittle("Skills"),
                section_skills(),
                tittle("Projects"),
                section_projects(),
                tittle("Certificates"),
                section_certificate(),
                
            
                
              
               
              
                padding_x=Size.DEFAULT.value,
                max_width=styles.MAX_WIDTH,
                width="100%",
                #margin_y=Size.BIG.value,
                #padding=Size.BIG.value
            ),
             
            
            ),
            footer(),
            width="100%"
        )
    
    
app = rx.App(
        theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="medium",
        accent_color="iris",
        )
    
    )
app.add_page(index)

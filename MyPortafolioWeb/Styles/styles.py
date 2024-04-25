import reflex as rx
from enum import Enum

MAX_WIDTH = "650px"

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE_SMALL = "1.5em"
    BIG = "2em"
    LARGE = "3.5em"
    VERY_BIG = "4em"
    MEDIUM_BIG = "5em"
    VERY_VERY_BIG = "9em"



class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"

    SMALL = "2"
    MEDIUM_SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"
    

# Styles

BASE_STYLE ={
    "font_family":"Comic Sans MS",
    "text_decoration":"none",
    "background_color":"#171F26",
    "height":"100h",
    "width":"100%",
    
    "color":"#FFFFFF",
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
}



styles_card = dict(
    background_color="#0C151D",
    box_shadow="0 0 1px 1px  #A3ABB2 ",
    width="7.5em",
    height="10em",
)
styles_tittle= dict(
    size="4",
    weight="medium",
    color="F1F2F4",
    width="100%",
    padding_y=Size.DEFAULT.value,
    font_size=Size.BIG.value,
    justify="start !important",
)
styles_flex_card = dict(
    justify="center",      
    )
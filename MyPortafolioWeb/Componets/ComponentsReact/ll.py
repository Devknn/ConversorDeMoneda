import reflex as rx
from reflex.vars import Var

class CarouselState(rx.State):
    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def next_item(self):
        self.current_index = (self.current_index + 1) % len(self.items)

    def prev_item(self):
        self.current_index = (self.current_index - 1) % len(self.items)

    def current_item(self):
        return self.items[self.current_index]

def prueba() -> rx.Component:
    return rx.vstack(
        rx.button("Anterior", onclick=CarouselState.prev_item),
        rx.span(CarouselState.current_item()),
        rx.button("Siguiente", onclick=CarouselState.next_item)
    )


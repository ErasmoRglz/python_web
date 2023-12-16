"""Hola Reflex!."""

from link_bio import styles

# Import all the pages.
from link_bio.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()

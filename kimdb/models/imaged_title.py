# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .base_title import BaseTitle

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: ImagedTitle ---------------------------------------------------------- #

class ImagedTitle(BaseTitle):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        id: str,
        title: str,
        poster_url: str
    ):
        super().__init__(id, title)

        self.poster_url = poster_url


# ---------------------------------------------------------------------------------------------------------------------------------------- #

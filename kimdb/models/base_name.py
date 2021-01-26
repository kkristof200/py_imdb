# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .base_object import BaseObject

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: BaseName ----------------------------------------------------------- #

class BaseName(BaseObject):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        id: str,
        name: str
    ):
        super().__init__(id)

        self.name = name


# ---------------------------------------------------------------------------------------------------------------------------------------- #

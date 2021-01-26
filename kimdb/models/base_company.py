# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .base_object import BaseObject

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: BaseCompany ---------------------------------------------------------- #

class BaseCompany(BaseObject):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        id: str
    ):
        super().__init__(id)


# ---------------------------------------------------------------------------------------------------------------------------------------- #

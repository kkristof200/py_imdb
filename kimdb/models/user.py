# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import List

# Local
from .base_user import BaseUser
from .base_list import BaseList

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------- class: User ------------------------------------------------------------- #

class User(BaseUser):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        id: str,
        username: str,
        lists: List[BaseList]
    ):
        super().__init__(id, username)

        self.lists = lists


# ---------------------------------------------------------------------------------------------------------------------------------------- #

"""Abstract class representing an Authorization backend
"""


from abc import abstractmethod
from typing import AsyncContextManager, List


class AuthorizationBackend(AsyncContextManager):  # pylint: disable=inherit-non-class
    # (see https://github.com/PyCQA/pylint/issues/2472)
    """Abstract class for representing an Authorization backend
    """

    def __init__(self, options: dict) -> None:
        self.options = options
        super().__init__()

    @abstractmethod
    async def get_authorizations_for_user(self, user) -> List[str]:
        """get list the list of group a user identity belongs to
        """

    @abstractmethod
    async def staff_creates_group(self, staff, group_name) -> bool:
        """Add group
        """

    @abstractmethod
    async def get_groups(self) -> List[str]:
        """Get all groups
        """

    @abstractmethod
    async def get_members_of_group(self, group) -> List[str]:
        """Get members of group
        """

    @abstractmethod
    async def group_exists(self, group) -> bool:
        """Assert group exists
        """

    @abstractmethod
    async def user_exists(self, user) -> bool:
        """Assert user exists
        """

    @abstractmethod
    async def add_member_to_group(self, member, group) -> bool:
        """
        staff adds member to group
        """

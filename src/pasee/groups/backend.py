"""Abstract class representing an Authorization backend
"""


from abc import abstractmethod
from typing import AsyncContextManager, List, Any


class AuthorizationBackend(AsyncContextManager):  # pylint: disable=inherit-non-class
    # (see https://github.com/PyCQA/pylint/issues/2472)
    """Abstract class for representing an Authorization backend
    """

    def __init__(self, options: dict, **kwargs: Any) -> None:
        self.options = options
        super().__init__(**kwargs)  # type: ignore # mypy issue 4335

    @abstractmethod
    async def get_authorizations_for_user(self, user) -> List[str]:
        """get list the list of group a user identity belongs to
        """

    @abstractmethod
    async def create_group(self, group_name):
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
    async def is_user_in_group(self, user, group) -> bool:
        """Verify that user is in group
        """

    @abstractmethod
    async def add_member_to_group(self, member, group) -> bool:
        """
        staff adds member to group
        """

    @abstractmethod
    async def delete_member_in_group(self, member, group):
        """Delete member in group
        """

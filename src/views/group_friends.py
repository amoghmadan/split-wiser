from models import GroupFriend
from schemas import GroupFriendSchema
from utilities import viewsets


class GroupFriendViewSet(viewsets.ModelViewSet):
    """Group Friend: View Set"""

    model = GroupFriend
    schema_class = GroupFriendSchema

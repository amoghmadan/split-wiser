from models import Friend
from schemas import FriendSchema
from utilities import viewsets


class FriendViewSet(viewsets.ModelViewSet):
    """Friend: View Set"""

    model = Friend
    schema_class = FriendSchema

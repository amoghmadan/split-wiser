from models import Group
from schemas import GroupSchema
from utilities import viewsets


class GroupViewSet(viewsets.ModelViewSet):
    """Group Friend: View Set"""

    model = Group
    schema_class = GroupSchema

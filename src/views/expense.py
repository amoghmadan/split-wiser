from models import Expense
from schemas import FriendExpenseSchema
from utilities import viewsets


class ExpenseViewSet(viewsets.ModelViewSet):
    """Group Friend View Set"""

    model = Expense
    schema_class = FriendExpenseSchema

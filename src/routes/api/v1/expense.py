from flask import Blueprint

from views import ExpenseViewSet

expense = Blueprint("expense", __name__)
expense.add_url_rule(
    "/", view_func=ExpenseViewSet.as_view("expense-list"), methods=["GET", "POST"]
)
expense.add_url_rule(
    "/<id>",
    view_func=ExpenseViewSet.as_view("expense-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)

from django.urls import path
from .views import (
    create_employer,
    get_employers,
    get_employers_forudateanddelete,
    employer_details,
    update_employer,
    delete_employer,
)

# from .views import home

urlpatterns = [
    # path("", home, name="home"),
    path("create/", create_employer, name="create_employee"),
    path("", get_employers, name="get_employers"),
    path(
        "employers_for_date_and_delete/",
        get_employers_forudateanddelete,
        name="employers_for_date_and_delete",
    ),
    path("employer_details/<int:pk>/", employer_details, name="employer_details"),
    path("update_employer/<int:pk>/", update_employer, name="update_employer"),
    path("delete_employer/<int:pk>/", delete_employer, name="delete_employer"),
]

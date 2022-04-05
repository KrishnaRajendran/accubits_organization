from django.urls import path
from organization.api.views import EmployeeAV, EmployeeDetailAV

urlpatterns = [
    path('', EmployeeAV.as_view(), name='employeelist'),
    path('<int:pk>/', EmployeeDetailAV.as_view(), name='employee-detail'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]

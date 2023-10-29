from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('retrieve/<int:pk>', views.RetrieveUserView.as_view(), name='retrieve'),
    path('update/<int:pk>', views.UpdateUserView.as_view(), name='update'),
    path('list/', views.ListUserView.as_view(), name='list'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
]

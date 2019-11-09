from django.urls import path
from . import views

urlpatterns = [
    #path('', Index.as_view(), name="index"), # Index page
    path('', views.index, name="index"),
    path('housing/', views.HousingList.as_view(), name="housing"), # Housing posts
    path('ridesharing', views.RideSharingList.as_view(), name="ridesharing"),
    path('sale', views.SaleList.as_view(), name="sale"),
    path('post/<int:pk>/', views.PostDetail.as_view(), name="detail"),
    path('post/new', views.CreatePostView.as_view(), name="create-post"),
    path('post/<str:username>', views.UserPostsList.as_view(), name='user-posts'),
]
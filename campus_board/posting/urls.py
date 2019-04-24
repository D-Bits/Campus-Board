from django.urls import path
from . import views
from . views import (
    index,
    HousingList,
    SaleList,
    RideSharingList,
    PostDetail,
    CreatePostView
)

urlpatterns = [
    #path('', Index.as_view(), name="index"), # Index page
    path('', views.index, name="index"),
    path('housing/', HousingList.as_view(), name="housing"), # Housing posts
    path('ridesharing', RideSharingList.as_view(), name="ridesharing"),
    path('sale', SaleList.as_view(), name="sale"),
    path('post/<int:pk>/', PostDetail.as_view(), name="detail"),
    path('post/new', CreatePostView.as_view(), name="create-post"),
]
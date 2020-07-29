# from django.urls import path
# from . import views
# urlpatterns = [
#
#     path('books/',views.BooksView.as_view()),
#
#
#
# ]

from django.urls import re_path
from . import views

urlpatterns = [
]

# 路由Router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', views.BookInfoViewSet, basename='books')
urlpatterns += router.urls
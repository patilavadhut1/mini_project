from django.urls import path
from .views import signup,Login,logout_view,ListBlog,CreateBlog,RetriveBlog,DestroyView

urlpatterns = [
    path('signup/', signup),
    path('login/', Login.as_view()),
    path('logout/', logout_view),
    path('blogs/', ListBlog.as_view()),
    path('create/', CreateBlog.as_view()),
    path('retrieve/<int:pk>', RetriveBlog.as_view()),
    path('delete/<int:pk>', DestroyView.as_view()),
]

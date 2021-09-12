from django.urls import path,include
from trading import views
# from .views import share,share_details
from .views import ShareList, ShareDetails, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    # path('', views.index, name='home'),
    path('', include(router.urls)),
    path('share',ShareList.as_view()),
    path('share/<int:id>/',ShareDetails.as_view()),
    path('login', obtain_auth_token)
    # path('login', views.loginUser, name='login'),
    # path('logout', views.logoutUser, name='logout'),
]

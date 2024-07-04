from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from apps.accounts.views import UserTokenObtainPairView
from apps.accounts.views import (
    UserViewSet,
    UserRegisterView,
    UserMeView,
    GroupViewSet,
    PermissionViewSet,
)
from apps.hotel.views import (
    HotelViewSet,
    StaffViewSet,
    GuestViewSet,
    RoomTypeViewSet,
    RoomViewSet,
    BookingViewSet,
    PaymentViewSet,
)
from .views import APIRootView


app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root-view'),
    path('auth/signin/', UserTokenObtainPairView.as_view(), name='auth-signin'),
    path('auth/register/', UserRegisterView.as_view(), name='auth-register'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', UserMeView.as_view(), name='auth-me'),
]

urlpatterns += router.urls

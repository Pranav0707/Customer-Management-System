from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registration/',views.userRegistration,name='registration'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogout,name='logout'),
    path('user/',views.UserPage,name='userpage'),
    path('account/',views.accountsettings,name='accountsettings'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='cms_app/password_reset.html'), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='cms_app/password_reset_done.html'), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name='cms_app/password_reset_confirm.html'), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='cms_app/password_reset_complete.html'),name="password_reset_complete"),


    path('product/',views.product,name='product' ),
    path('customer/<str:pk>',views.customer,name='customer'),
    path('',views.Home,name='home' ),
    path('orderform/<str:pk>',views.orderform,name='orderform' ),
    path('updateorder/<str:pk>',views.updateorder,name='updateorder' ),
    path('deleteorder/<str:pk>',views.deleteorder,name='deleteorder'),
    path('create_user_order/<str:id>',views.create_user_order,name="create_user_order"),
    path('create_customer',views.create_customer,name="create_customer")
]

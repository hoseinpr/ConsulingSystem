from django.urls import path
from . import views
from .views import shopCart, add_to_cart, courses_list

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("shop-cart/", views.shopCart, name="shop-cart"),
    path("shop-checkout/", views.shopCheckout, name="shop-checkout"),
    path("shop-order/", views.shopOrder, name="shop-order"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dshb-administration/", views.dshbAdmin, name="dshb-administration"),
    path("courses-list/", views.courses_list, name="courses-list"),
    path("course-single/", views.coursesSingle, name="course-single"),
    path('register/', views.register_user, name='register_user'),
    path('shop-cart/', shopCart, name='shopCart'),
    path('add-to-cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('courses-list/', courses_list, name='courses_list'),
    # path('remove-from-cart/<int:course_id>/', remove_from_cart, name='remove_from_cart'),
]
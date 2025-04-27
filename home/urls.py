from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('kienthuc/', views.kienthuc, name='kienthuc'),
    path('leutrai/', views.leutrai_view, name='leutrai'),
    path('matthu/', views.matthu_view, name='matthu'),
    path('morse/', views.morse_view, name='morse'),
    path('muahat/', views.muahat_view, name='muahat'),
    path('nghithuchoi/', views.nghithuchoi_view, name='nghithuchoi'),
    path('nghithucdoi/', views.nghithucdoi_view, name='nghithucdoi'),
    path('nutday/', views.nutday_view, name='nutday'),
    path('phuonghuong/', views.phuonghuong_view, name='phuonghuong'),
    path('scc/', views.scc_view, name='scc'),
    path('semaphore/', views.semaphore_view, name='semaphore'),
    path('thoathiem/', views.thoathiem_view, name='thoathiem'),
    path('thuoctay/', views.thuoctay_view, name='thuoctay'),
    path('thuocnam/', views.thuocnam_view, name='thuocnam'),
    path('trochoi/', views.trochoi_view, name='trochoi'),
    path('uocdat/', views.uocdat_view, name='uocdat'),
    path('kienthuc/dang-bai/', views.create_post, name='create_post'),
    path('kienthuc/<slug:slug>/', views.post_detail, name='post_detail'),
    path('kienthuc/<slug:slug>/sua/', views.edit_post, name='edit_post'),
    path('bai-viet/<int:post_id>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]

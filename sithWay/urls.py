from django.urls import path

from sithWay import views

app_name = 'sithWay'
urlpatterns = [
    path('', views.selection_page, name="selection_page"),
    path('recruits/add', views.recruit_page, name="recruit_add_page"),
    path('recruits/save', views.recruit_save, name="recruit_save"),
    path('recruits/test/<int:pk>', views.recruit_test, name="recruit_test"),
    path('siths/all', views.sith_list, name="sith_list"),
    path('siths/filtered/1', views.sith_list_filtered, name="sith_list_filtered"),
    path('siths/<int:pk_sith>/all', views.sith_recruit_list, name="recruit_list"),
    path('siths/<int:pk_sith>/<int:pk_recruit>', views.sith_recruit_detail, name="recruit_detail"),
    path('siths/<int:pk_sith>/<int:pk_recruit>/make-hand-shadow', views.make_hand_shadow,
         name="recruit_make_shadow_hand"),
]

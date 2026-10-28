from django.urls import path
from jewelapp import views

urlpatterns = [
path('new/',views.new,name='new'),
path('addcate/',views.addcate,name='addcate'),
path('savejewelcat/',views.savejewelcat,name='savejewelcat'),
path('displaycate/',views.displaycate,name='displaycate'),
path('editcatego/<int:cat_id>',views.editcatego,name='editcatego'),
path('delcate/<int:cat_id>',views.delcate,name='delcate'),
path('ornaments/',views.ornaments,name='ornaments'),
path('saveornaments/',views.saveornaments,name='saveornaments'),
path('displayornaments/',views.displayornaments,name='displayornaments'),
path('editornaments/<int:orn_id>',views.editornaments,name='editornaments'),
path('delorn/<int:orn_id>',views.delorn,name='delorn'),
path('admin1/',views.admin1,name='admin1'),
path('adminlog/',views.adminlog,name='adminlog'),
path('display_contacts/',views.display_contacts,name='display_contacts'),
path('deletecontacts/<int:con_id>',views.deletecontacts,name='deletecontacts'),
path('display_register/',views.display_register,name='display_register'),
path('delete_register/<int:user_id>',views.delete_register,name='delete_register'),
path('orderdisplay/',views.orderdisplay,name='orderdisplay')
]
from django.urls import path
from . import views
from project1.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('library',views.library,name='library'),
    path('uploadform',views.uploadform,name='uploadform'),
    path('logoutt' , views.logoutt , name='logoutt'),
    path('update/<int:book_id>', views.update_book, name='update'),
    path('delete/<int:book_id>', views.delete_book, name='delete'),
    path('email',views.send_template_email,name='email')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

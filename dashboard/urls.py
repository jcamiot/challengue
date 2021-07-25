from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('ajax/load_datatable_content', views.load_datatable_content, name="load_datatable_content"),
    path('ajax/load_total_employees', views.load_total_employees, name="load_total_employees"),
    path('ajax/load_monthly_income_avg', views.load_monthly_income_avg, name="load_monthly_income_avg"),
    path('ajax/load_hourly_rate_avg', views.load_hourly_rate_avg, name="load_hourly_rate_avg"),
    path('ajax/load_age_avg', views.load_age_avg, name="load_age_avg"),
    path('admin/', admin.site.urls), 
]
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
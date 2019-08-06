
from django.contrib import admin
from django.urls import path
import blogapp.views
import drink.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = 'home'),
    path('blogapp/<int:blogapp_id>', blogapp.views.detail, name = 'detail'),
    path('blogapp/new/', blogapp.views.new, name = 'new'),
    path('blogapp/create/', blogapp.views.create, name = 'create'),
    path('drink/', drink.views.drink, name = 'drink'),
    path('food/', drink.views.food, name = 'food'),
    path('fashion/', drink.views.fashion, name = 'fashion'),
    path('specialPrice/', drink.views.specialPrice, name = 'specialPrice'),
    path('detail/<int:blogDrink_id>', drink.views.Drinkdetail, name = 'Drinkdetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

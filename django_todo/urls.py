from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo/',include("todo.urls")),
    path('docs/', include_docs_urls(title='Todo Api')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')    
]
"""
URL configuration for NoteAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quizGen import views as qgviews
from pdfconverter import views as pdfviews
from imageconverter import views as imageviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('action/quiz-generator',qgviews.generate_quiz),
    path('',qgviews.home),path('action/pdf-converter',pdfviews.home),
    

]

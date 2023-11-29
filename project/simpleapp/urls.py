from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete, SubscribersView
#from .views import subscribe

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('news/', PostsList.as_view(), name='posts'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('subscribe/', SubscribersView.as_view(), name='subscribe'),
   #path('category/', CategoryListView.as_view(), name='category_list'),
   #path('category/category/<int:pk>/subscribe', CategoryListView.as_view(), name='subscribe'),
   #path('sendmail/', SubscribersView.post(), name='send_mail'),

]
from django_filters import FilterSet, DateTimeFilter
from .models import Post, Subscribers

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title_of_post': ['icontains'],
           'author__user': ['exact'],
           'news_or_article': ['exact'],
           'date_of_post': ['gt'],
           'category': ['exact']
        }
       filter_overrides = {
           DateTimeFilter: {
               'filter_class': DateTimeFilter,
               'extra': lambda f: {
                   'widget': DateTimeFilter,
               },
           },
       }


class SubscribersFilter(FilterSet):
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Subscribers
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'category': ['exact']
        }
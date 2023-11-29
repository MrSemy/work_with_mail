

from django import template


register = template.Library()


BAD_WORDS = [
    'октября', 'января', 'февраля', 'марта', 'апреля', 'май', 'июнь', 'июль', 'августа', 'сентября',
]

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   """
   value: значение, к которому нужно применить фильтр
   """
   censored_text = value
   for word in value.split(' '):
       if word in BAD_WORDS:
           censored_text = censored_text.replace(word, '***')
   return censored_text

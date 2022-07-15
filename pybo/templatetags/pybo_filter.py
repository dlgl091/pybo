import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()
# 템플릿 필터 함수 만들기
@register.filter
# 템플릿에서 sub 함수를 필터로 사용할 수 있게 하는 애너테이션
def sub(value,arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extenstions=extensions))
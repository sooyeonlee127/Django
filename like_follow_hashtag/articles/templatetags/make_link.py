from django import template
import re           # 정규표현식 용 

register = template.Library()

@register.filter
def add_link(value): 
    # value = article 라고 생각하면 됨
    # article.Content 
    # 전달된 value객체의 content 멤버변수를 가져온다
    content = value.content

    # article에 포함된 hashtag - > 링크를 걸어서 갈 수 있도록 구현
    # 전달된 value 객체에 포함된 hashtags 전체를 가져오는 queryset
    tags = value.hashtags.all()

    # tags 순회하면서, content 내에서 해당 문자열을 링크로 변경
    for tag in tags:
        content = re.sub(tag.content, '<a href="/articles/' + str(tag.id) + '/hashtag/">'+tag.content+'</a>', content) # 정규표현식
    return content
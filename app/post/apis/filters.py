import django_filters
from django.db.models import Q

from post.models import Post


class PostFilterList(django_filters.Filter):
    def __init__(self, name, lookup_type, *args, **kwargs):
        self.name = name
        self.lookup_type = lookup_type
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        if value not in (None, ''):
            values = [v for v in value.split(',')]
            q = Q()
            for separated_value in values:
                q |= Q(**{'%s__%s' % (self.name, self.lookup_type): separated_value})
            return qs.filter(q)
        return qs


class PostFilter(django_filters.FilterSet):
    filter_content_and_title = django_filters.CharFilter(method='get_filter_content_and_title', label='filter_content_and_title', )
    filter_title_with_comma_separated = PostFilterList(name='title', lookup_type='icontains', label='filter_title_with_comma_separated', )

    class Meta:
        model = Post
        fields = {
            'filter_content_and_title': ['exact', ],
            'filter_title_with_comma_separated': ['exact', ],
        }

    def get_filter_content_and_title(self, qs, name, value):
        return qs.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )
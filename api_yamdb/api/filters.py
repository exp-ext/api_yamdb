from django_filters import CharFilter, FilterSet, NumberFilter
from reviews.models import Title


class TitleFilterSet(FilterSet):
    """Фильтр произведений по 4-м полям."""  
    name = CharFilter(field_name='name', lookup_expr='contains')
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    year = NumberFilter(field_name='year')    

    class Meta:
        model = Title
        fields = ('category', 'genre', 'year', 'name')

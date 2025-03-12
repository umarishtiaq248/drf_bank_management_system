import django_filters

from .models import Account


class AccountFilter(django_filters.FilterSet):
    is_non_zero_balance = django_filters.BooleanFilter(
        field_name="account_balance",
        lookup_expr="gt",
        label="Non-zero balance",
        method="filter_non_zero_balance"
    )

    def filter_non_zero_balance(self, queryset, name, value):
        if value:
            return queryset.filter(account_balance__gt=0)
        return queryset

    class Meta:
        model = Account
        fields = ["is_non_zero_balance"]
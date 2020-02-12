from django.contrib import admin

from insurance.models import Customer, PolicyRequest


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'created_at', 'updated_at', 'policies')
    fields = ('first_name', 'last_name', 'dob')

    def policies(self, obj):
        return [x for x in obj.policyrequest_set.all()]


class PolicyRequestAdmin(admin.ModelAdmin):
    list_display = ('type', 'premium', 'cover', 'created_at', 'updated_at', 'customer')
    fields = ('type', 'premium', 'cover', 'customer')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(PolicyRequest, PolicyRequestAdmin)

from django.contrib import admin

from .models import News

admin.site.register(News)
# @admin.register(News)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'user'
#     )
#     list_display_links = (
#         'user',
#         'id'
#     )
#     list_filter = (
#         'user',
#         'id'
#     )
#     search_fields = (
#         'user',
#         'id'
#     )

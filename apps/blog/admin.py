from django.contrib import admin

from .models import News, Category, Comment

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comment)
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

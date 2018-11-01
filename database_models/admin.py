"""
对admin站点的相关设置
"""
from django.contrib import admin

# Register your models here.
from database_models.models import BookInfo, HeroInfo

# 站点中注册数据库模型
admin.site.register(BookInfo)
admin.site.register(HeroInfo)

"""
模型类表单
表单与数据库模型存在对应关系
django中将数据库模型和表单建立联系，提供更加便捷的表单操作
"""
from django import forms

from database_models.models import BookInfo


class MyModelForms(forms.ModelForm):
    class Meta:
        # 指明类模型
        model = BookInfo
        # 指明表单对应的字段
        fields = ("btitle", "bpub_date")

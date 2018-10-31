"""
表单类，django创建好后提供给模板使用
在视图函数中调用
表单输入项目根据数据库字段，以及业务需求来设计
"""
from django import forms


class MyForm(forms.Form):
    """创建表单类"""
    btitle = forms.CharField(max_length=20, label='图书名', required=True)
    # forms 提供的方法可以对前端输入数据进行校验
    bpub_date = forms.DateField(label='发行日期', required=True)

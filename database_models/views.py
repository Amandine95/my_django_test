from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from database_models.models_forms import MyModelForms


class ModelFormView(View):
    """表单视图"""

    def get(self, request):
        """渲染模板，将表单对象发给模板"""
        form1 = MyModelForms()
        context = {
            "form1": form1
        }
        return render(request, 'forms_template.html', context)

    def post(self, request):
        """对表单提交进行处理"""
        # 获取参数,POST属性获取表单参数
        form1 = MyModelForms(request.POST)
        # 校验通过
        if form1.is_valid():
            # 获取表单数据
            print(form1.cleaned_data)
            return HttpResponse('ok')
        else:
            # 渲染模板,django提供了错误信息提示
            return render(request,'forms_template.html',context={"form1":form1})

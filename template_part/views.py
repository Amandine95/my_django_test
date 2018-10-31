from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from django.views.generic import View

from template_part.forms import MyForm

"""
django 的模板
"""


class TemplateView(View):
    """类视图"""

    def get(self, request):
        """简写用render方法"""

        # 上下文，模板中展示的数据
        context = {
            "city": "shanghai"
        }
        return render(request, 'first_html.html', context)

    def post(self, request):
        """完整写法"""

        # 获取模板
        template = loader.get_template('first_html.html')
        # 创建上下文
        context = {'city': 'beijing'}
        # 渲染
        return HttpResponse(template.render(context))


class FormView(View):
    """表单视图"""

    def get(self, request):
        """渲染模板，将表单对象发给模板"""
        form = MyForm()
        context = {
            "form": form
        }
        return render(request, 'forms_template.html', context)

    def post(self, request):
        """对表单提交进行处理"""
        # 获取参数,POST属性获取表单参数
        form = MyForm(request.POST)
        # 校验通过
        if form.is_valid():
            # 获取表单数据
            print(form.cleaned_data)
            return HttpResponse('ok')
        else:
            # 渲染模板,django提供了错误信息提示
            return render(request,'forms_template.html',context={"form":form})


from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from django.views.generic import View

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
        context = {'city':'beijing'}
        # 渲染
        return HttpResponse(template.render(context))

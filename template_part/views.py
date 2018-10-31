from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

"""
django 的模板
"""


class TemplateView(View):
    """类视图"""

    def get(self, request):
        # 上下文，模板中展示的数据
        context = {
            "city": "shanghai"
        }
        return render(request, 'first_html.html', context)

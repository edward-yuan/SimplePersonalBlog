# encoding: utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.views.generic.edit import FormView
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

import markdown2

from .models import Article, Category, Tag, Contact
from .forms import ContactForm


class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class BlogView(ListView):
    template_name = "blog/blog.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class AboutView(TemplateView):
    template_name = 'blog/about.html'

class AboutDetailView(TemplateView):
    template_name = 'blog/about2.html'


#联系我表单视图
class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    model = Contact
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(timezone.now()) 
        #print(self.request.POST.get('subject', ''))
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        name = form.cleaned_data['name']
        from_email=settings.EMAIL_HOST_USER
        to_email=settings.DEFAULT_FROM_EMAIL

        send_mail(subject, '来自于'+name+"<"+sender+">"+"的意见反馈: \n"+message, from_email,to_email,auth_user=None,fail_silently=False)
        
        #反馈意见存数据库
        contact=Contact(name=name,email=sender,subject=subject)
        contact.save()
        
        return super(ContactView, self).form_valid(form)

#感谢视图
class ThanksView(TemplateView):
    template_name = 'blog/thanks.html'

#文章详情视图
class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object(queryset=None)
        obj.body = mark_safe(markdown2.markdown(obj.body, extras=['fenced-code-blocks', 'code-friendly', 'codehilite']))
        # BUG:必须在这里渲染，如果在模板中通过模板标签渲染则格式会乱掉
        obj.viewed()
        return obj


class CategoryView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category_id'], status='p')


class TagView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(tags=self.kwargs['tag_id'], status='p')


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    make_object_list = True
    context_object_name = 'article_list'
    template_name = 'blog/index.html'


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    context_object_name = 'article_list'
    template_name = 'blog/index.html'
    month_format = '%m'

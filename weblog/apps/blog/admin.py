# encoding: utf-8
from django.contrib import admin

from .models import Article, Category, Tag, Contact, Photo

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time','views','category', 'status')
    list_filter = ['created_time','category']
    search_fields = ['title']

    def get_article_state(self, Article):
        if Article.balance == 'd':
            return '<span style="color:red;font-weight:bold">%s</span>' % ("草稿",)
        else:
            return '<span style="color:green;font-weight:bold">%s</span>' % ("已发布",)

    get_article_state.short_description = u'发稿状态'
    get_article_state.allow_tags = True
    get_article_state.admin_order_field = 'status' 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','created_time')
    list_filter = ['created_time']
    search_fields = ['name']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','caption','created_date', 'url')
    list_filter = ['created_date']
    search_fields = ['title']

#将Article文章，Category分类，Tag标签，Contact联系人，Image图片等模型注册进后台  
#admin.site.register(Image, ImageAdmin)        
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Photo,PhotoAdmin)
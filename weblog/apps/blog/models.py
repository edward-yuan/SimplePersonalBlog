# encoding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.conf import settings
from . import util

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    title = models.CharField('标题', max_length=200)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)
    pub_time = models.DateTimeField('发布时间', blank=True, null=True,
                                    help_text="不指定发布时间则视为草稿，可以指定未来时间，到时将自动发布。")
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    summary = models.CharField('摘要', max_length=200, blank=True, help_text="可选，若为空将摘取正文的前54个字符。")
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)

    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    def save(self, *args, **kwargs):
        self.summary = self.summary or self.body[:120]
        super().save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


class Category(models.Model):
    name = models.CharField('分类名', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Contact(models.Model):
    name = models.CharField('读者姓名', max_length=30)
    email = models.CharField('读者邮箱', max_length=30)
    subject = models.CharField('读者反馈主题', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "读者意见"
        verbose_name_plural = verbose_name

class Photo(models.Model):
    title = models.CharField('图片名称',null=True,blank=True,max_length=100)
    #图片上传到photos目录下
    image = models.ImageField(upload_to="images/%Y%m")
    caption = models.CharField('图片说明',max_length=250,blank=True,null=True)
    
    created_date = models.DateTimeField('上传时间',auto_now_add=True,null=True)
    url=models.URLField('链接地址',null=True,blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = "图片库"
        verbose_name_plural = verbose_name
    
    def save(self, *args, **kwargs):
        #获取详细的url，这里需要在settings.py文件里设置SITES_HOST
        #获取上传文件的名称，通过一个工具组件完成
        super().save(*args, **kwargs)
        try:
            if self.title == '':
                self.title=util.get_uploadfile_nam(self.image.name)
            print(self.image.url)    
            self.url =  "http://"+settings.SITES_HOST+self.image.url
            print(self.url)
            super().save(*args, **kwargs)
        except Exception as e:
            raise e

    def __str__(self):
        return self.title
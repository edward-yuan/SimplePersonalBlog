####Powered by python 3.4.4 and django 1.10.1

**Features**
- 博客文章 markdown 渲染
- 文章侧栏分类统计和标签云
- 文章按照发表时间自动归档
# 评论，二级评论（暂时未实现）
- 全文搜索


### 项目运行方式
确保你的开发环境是 python3，如果不是，请考虑使用虚拟环境virtualenv搭建python3, 自行度娘并参照相关教程。

1. fork 本项目到你的仓库
2. 克隆你的仓库到本地
3. 在 weblog/ 下分别建立 static,media,database 文件夹
4. 命令行执行 pip3 install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包（项目依赖 pillow，确保你的环境能够安装 pillow）
5. 迁移数据库，在 manage.py 所在目录执行

        python manage.py makemigrations
        python manage.py migrate

6. 类似步骤4，运行命令创建超级用户
    
        python manage.py createsuperuser

7. 类似步骤4、5，在 manage.py 所在目录执行

        python manage.py runserver

8. 浏览器输入 http://127.0.0.1:8000/

另外推荐数据库是postgresql 9，如果不是的话，请酌情修改models类。

部署到本地需要修改的部分:

1.首先编辑weblog/config/setting，修改数据库配置,STATICFILES_DIRS目录和网站域名SITES_HOST

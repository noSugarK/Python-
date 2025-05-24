# 目录

- **[创建项目](#创建项目)**
1. [用于开发的简易服务器](#用于开发的简易服务器)
2. [创建投票应用](#创建投票应用)
3. [编写第一个视图](#编写第一个视图)
4. [数据库配置](#数据库配置)
5. [创建模型](#创建模型)
6. [激活模型](#激活模型)



# 创建项目

如果这是你第一次使用 Django 的话，你需要一些初始化设置。也就是说，你需要用一些自动生成的代码配置一个 Django project —— 即一个 Django 项目实例需要的设置项集合，包括数据库配置、Django 配置和应用程序配置。

在命令行中，使用 cd 进入你希望存储代码的目录，并创建一个名为 djangotutorial 的新目录。（这个目录名称对 Django 来说并不重要，你可以将其重命名为任何你喜欢的名称。）

```bash
mkdir djangotutorial
```

然后，运行以下命令来引导一个新的 Django 项目：

```bash
django-admin startproject mysite djangotutorial
```

这将在 djangotutorial 目录内创建一个名为 mysite 的项目。如果没有成功，请参阅 运行 django-admin 时遇到的问题。


>Note
>
>你得避免使用 Python 或 Django 的内部保留字来命名你的项目。具体地说，你得避免使用像 django (会和 Django 自己产生冲突)或 test (会和 Python 的内置组件产生冲突)这样的名字。


让我们看看 startproject 创建了些什么：

```
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

这些目录和文件的用处是：

- manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 django-admin 和 manage.py 获取所有 manage.py 的细节。
- mysite/: 一个目录，它是你项目的实际 Python 包。它的名称是你需要用来导入其中任何内容的 Python 包名称（例如 mysite.urls）。
- mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 更多关于包的知识。
- mysite/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 Django 配置 了解细节。
- mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读 URL调度器 文档来获取更多关于 URL 的内容。
- mysite/asgi.py：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 如何使用 ASGI 来部署 了解更多细节。
- mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 如何使用 WSGI 进行部署 了解更多细节。

## 用于开发的简易服务器

让我们验证你的 Django 项目是否正常工作。如果还没有进入 djangotutorial 目录，请先进入该目录，然后运行以下命令：

```bash
python manage.py runserver
```

你应该会看到如下输出：

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

五月 23, 2025 - 15:50:53
Django version 5.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

服务器现在正在运行，通过浏览器访问 http://127.0.0.1:8000/ 。你将看到一个“祝贺”页面，有一只火箭正在发射。你成功了！

你已经启动了 Django 开发服务器，这是一个用纯 Python 编写的轻量级网络服务器。我们在 Django 中包含了这个服务器，所以你可以快速开发，而不需要处理配置生产服务器的问题 -- 比如 Apache -- 直到你准备好用于生产。

现在是个提醒你的好时机：千万不要 将这个服务器用于和生产环境相关的任何地方。这个服务器只是为了开发而设计的。（我们在网络框架方面是专家，在网络服务器方面并不是。）

(若要在一个不同的端口上提供网站服务，请参阅 runserver 参考。)

## 创建投票应用

现在你的开发环境——这个“项目” ——已经配置好了，你可以开始干活了。

在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就能专心写代码，而不是创建目录了。

>项目 VS 应用
>
>项目和应用有什么区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

你的应用程序可以位于 Python 路径 中的任何位置。在本教程中，我们将在 djangotutorial 文件夹内创建我们的 poll 应用程序。

请确定你现在处于 manage.py 所在的目录下，然后运行这行命令来创建一个应用：

```bash
python manage.py startapp polls
```

这将创建一个名为 polls 的目录，其布局如下：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

这个目录结构包括了投票应用的全部内容。

## 编写第一个视图

让我们开始编写第一个视图吧。打开 polls/views.py，把下面这些 Python 代码输入进去：

>polls/views.py
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
这是在 Django 中最基本的视图。要在浏览器中访问它，我们需要将其映射到一个 URL——为此我们需要定义一个 URL 配置，简称为 "URLconf"。这些 URL 配置是在每个 Django 应用程序内部定义的，它们是名为 urls.py 的 Python 文件。

要为 polls 应用定义一个 URLconf，创建一个名为 polls/urls.py 的文件，并包含以下内容：

>polls/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
你的应用目录现在应该如下所示：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

下一步是配置 mysite 项目中的根 URLconf，使其包含 polls.urls 中定义的 URLconf。为此，请在 mysite/urls.py 中为 django.urls.include 添加导入，并在 urlpatterns 列表中插入 include()，这样就有了：

>mysite/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

path() 函数至少需要两个参数：route 和 view。include() 函数允许引用其他 URLconfs。每当 Django 遇到 include() 时，它会截断 URL 中匹配到该点的部分，并将剩余的字符串发送到包含的 URLconf 以进行进一步处理。

我们设计 include() 的理念是使其可以即插即用。因为投票应用有它自己的 URLconf( polls/urls.py )，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，或者其他任何路径下，这个应用都能够正常工作。

>何时使用 include()
>
>当你包含其他 URL 模式时，应该始终使用 include()。唯一的例外是 admin.site.urls，这是 Django 为默认管理站点提供的预构建 URLconf。

你现在把 index 视图添加进了 URLconf。通过以下命令验证是否正常工作：

```bash
python manage.py runserver
```

用你的浏览器访问 http://localhost:8000/polls/ ，你应该能够看见 "Hello, world. You're at the polls index." ，这是你在 index 视图中定义的。

## 数据库配置

打开 mysite/settings.py 。这是个包含了 Django 项目设置的 Python 模块。

默认情况下，DATABASES 配置使用 SQLite。如果你是数据库新手，或者只是想尝试 Django，这是最简单的选择。SQLite 包含在 Python 中，因此你不需要安装任何其他东西来支持数据库。然而，当你开始第一个真正的项目时，你可能希望使用像 PostgreSQL 这样更具扩展性的数据库，以避免日后切换数据库的麻烦。

如果你想使用其他数据库，请参阅[自定义并启动数据库的详细信息](https://docs.djangoproject.com/zh-hans/5.2/topics/install/#database-installation)。

编辑 mysite/settings.py 文件前，先设置 TIME_ZONE 为你自己时区。

此外，关注一下文件头部的 INSTALLED_APPS 设置项。这里包括了会在你项目中启用的所有 Django 应用。应用能在多个项目中使用，你也可以打包并且发布应用，让别人使用它们。

通常， INSTALLED_APPS 默认包括了以下 Django 的自带应用：

- django.contrib.admin -- 管理员站点， 你很快就会使用它。
- django.contrib.auth -- 认证授权系统。
- django.contrib.contenttypes -- 内容类型框架。
- django.contrib.sessions -- 会话框架。
- django.contrib.messages -- 消息框架。
- django.contrib.staticfiles -- 管理静态文件的框架。

这些应用被默认启用是为了给常规项目提供方便。

默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：

```bash
python manage.py migrate
```

这个 migrate 命令查看 INSTALLED_APPS 配置，并根据 mysite/settings.py 文件中的数据库配置和随应用提供的数据库迁移文件（我们将在后面介绍这些），创建任何必要的数据库表。你会看到它应用的每一个迁移都有一个消息。如果你有兴趣，运行你的数据库的命令行客户端，输入 \dt （PostgreSQL）， SHOW TABLES; （MariaDB，MySQL）， .tables （SQLite）或 SELECT TABLE_NAME FROM USER_TABLES; （Oracle）来显示 Django 创建的表。

>写给极简主义者
>
>就像之前说的，为了方便大多数项目，我们默认激活了一些应用，但并不是每个人都需要它们。如果你不需要某个或某些应用，你可以在运行 migrate 前毫无顾虑地从 INSTALLED_APPS 里注释或者删除掉它们。 migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移。

## 创建模型
在 Django 里写一个数据库驱动的 Web 应用的第一步是定义模型 - 也就是数据库结构设计和附加的其它元数据。

>设计哲学
>
>一个模型就是单个定义你的数据的信息源。模型中包含了不可缺少的数据区域和你存储数据的行为。Django 遵循 DRY 原则。目的就是定义你的数据模型要在一位置上，而且自动从该位置推导一些事情。
>
>来介绍一下迁移 - 举个例子，不像 Ruby On Rails，Django 的迁移代码是由你的模型文件自动生成的，它本质上是个历史记录，Django 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模型匹配。

在这个投票应用中，需要创建两个模型：问题 Question 和选项 Choice。Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。

这些概念可以通过一个 Python 类来描述。按照下面的例子来编辑 polls/models.py 文件：

>polls/models.py
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

每个模型被表示为 django.db.models.Model 类的子类。每个模型有许多类变量，它们都表示模型里的一个数据库字段。

每个字段都是 Field 类的实例 - 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。这将告诉 Django 每个字段要处理的数据类型。

每个 Field 类实例变量的名字（例如 question_text 或 pub_date ）也是字段名，所以最好使用对机器友好的格式。你将会在 Python 代码里使用它们，而数据库会将它们作为列名。

你可以使用可选的选项来为 Field 定义一个人类可读的名字。这个功能在很多 Django 内部组成部分中都被使用了，而且作为文档的一部分。如果某个字段没有提供此名称，Django 将会使用对机器友好的名称，也就是变量名。在上面的例子中，我们只为 Question.pub_date 定义了对人类友好的名字。对于模型内的其它字段，它们的机器友好名也会被作为人类友好名使用。

定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据，我们稍后将会看到这方面的内容。

Field 也能够接收多个可选参数；在上面的例子中：我们将 votes 的 default 也就是默认值，设为0。

注意在最后，我们使用 ForeignKey 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。Django 支持所有常用的数据库关系：多对一、多对多和一对一。

## 激活模型
上面的一小段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：

为这个应用创建数据库 schema（生成 CREATE TABLE 语句）。

创建可以与 Question 和 Choice 对象进行交互的 Python 数据库 API。

但是首先得把 polls 应用安装到我们的项目里。

>设计哲学
>
>Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。

为了在我们的工程中包含这个应用，我们需要在配置类 INSTALLED_APPS 中添加设置。因为 PollsConfig 类写在文件 polls/apps.py 中，所以它的点式路径是 'polls.apps.PollsConfig'。在文件 mysite/settings.py 中 INSTALLED_APPS 子项添加点式路径后，它看起来像这样：

>mysite/settings.py
```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

现在你的 Django 项目会包含 polls 应用。接着运行下面的命令：

```bash
python manage.py makemigrations polls
```

你将会看到类似于下面这样的输出：
```
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
```

通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。

迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 它们其实也只是一些你磁盘上的文件。如果你想的话，你可以阅读一下你模型的迁移数据，它被储存在 polls/migrations/0001_initial.py 里。别担心，你不需要每次都阅读迁移文件，但是它们被设计成人类可读的形式，这是为了便于你手动调整 Django 的修改方式。

Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令 - 这个命令是 migrate，我们马上就会接触它 - 但是首先，让我们看看迁移命令会执行哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：

```bash
python manage.py sqlmigrate polls 0001
```

你将会看到类似下面这样的输出（我把输出重组成了人类可读的格式）：
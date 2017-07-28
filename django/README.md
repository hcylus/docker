#以Dockfile和docker-compose.yml为基础构建django容器

##创建docker_dj工程

docker-compose run web django-admin.py startproject docker_dj .


##修改工程docker_dj/settings.py文件

连接限制

```ALLOWED_HOSTS = ['*']```

数据库配置

```
ATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'docker',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'mysql',
        'PORT': '3306',
    }
}
```

时区和中文显示

```
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
```

##启动django容器

docker-compose up -d

##同步表结构并创建admin后台管理用户

```
docker-compose run --rm web python manage.py makemigrations

docker-compose run --rm web python manage.py migrate

docker-compose run --rm web python manage.py createsuperuser

```

##创建app

docker-compose run --rm web python manage.py startapp devops

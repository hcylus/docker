以Dockfile和docker-compose.yml为基础构建django容器

创建docker_dj工程
```
docker-compose run web django-admin.py startproject dj .
```

sudo chown -R $USER:$USER .

修改工程dj/settings.py文件

连接限制
```ALLOWED_HOSTS = ['*']```

数据库配置
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME','dj'),
        'USER': os.environ.get('DB_USER','dj'),
        'PASSWORD': os.environ.get('DB_PASSWORD',''),
        'HOST': 'db',
        'PORT': 3306,
        'OPTIONS': {
                    'charset': 'utf8',
                    'init_command': 'SET '
                        'default_storage_engine=INNODB,'
                        'character_set_connection=utf8,'
                        'collation_connection=utf8mb4_unicode_ci'
        }

    }
}

```
时区和中文显示
```
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
```

启动django容器
```
docker-compose up -d
```

同步表结构并创建admin后台管理用户
```
docker-compose run --rm web python manage.py makemigrations

docker-compose run --rm web python manage.py migrate

docker-compose run --rm web python manage.py createsuperuser
```

创建app
```
docker-compose run --rm web python manage.py startapp devops
```

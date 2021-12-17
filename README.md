![foodgram workflow](https://github.com/ADChemadurov/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Продуктовый помощник FoodGram

## Краткое описание проекта

Идеальный сайт для размещения рецептов. Ничего лишнего!

Вся документация API доступна на /api/docs/.

В этом проекте используется функционал GitHub Actions. При push'е
кода в репозиторий происходит загрузка образа на Docker Hub и деплой на сервере.

## Запуск проекта

### Установка Docker

Если вы планируете запускать проект на Linux сервере то используйте следующие
команды для установки Docker:
```sudo apt install curl```
```curl -fsSL https://get.docker.com -o get-docker.sh```
```sh get-docker.sh```

На всякий случай удалите старые версии Docker:
```sudo apt remove docker docker-engine docker.io containerd runc```

Обновите APT:
```sudo apt update```

Установите пакеты для работы через https:
```sudo apt install \ ```
```  apt-transport-https \```
```  ca-certificates \```
```  curl \```
```  gnupg-agent \```
```  software-properties-common -y```

Добавьте ключ GPG для подтверждения подлинности в процессе установки:
```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

Добавьте репозиторий Docker в пакеты apt:
```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"```

Устанавливаем Docker и Docker Compose.
```sudo apt install docker-ce docker-compose -y```

Проверить, что установился docker-compose можно этой командой:
```docker-compose --version```

### Клонирование репозитория на локальную машину

Так же необходимо склонировать репозиторий на свой компьютер.
Для этого необходимо зарегестрироваться на https://github.com/,
а так же установить Git Bash: https://git-scm.com/downloads.
Cделайте fork проекта по этой ссылке в свой репозиторий:
https://github.com/ADChemadurov/foodgram-project-react
После этого с помощью следующей команды в терминале склонируйте
его на свой компьютер: ```git clone <ваш-username>/<имя-репозитория>```


### Переменные окружения.

Добавьте файл с переменными окружения в папку infra.
Укажите в нем следующие переменные, убрав "<>" и вписав нужные данные:

DB_ENGINE=django.db.backends.postgresql
DB_NAME=<postgres>
POSTGRES_USER=<postgres>
POSTGRES_PASSWORD=<ваш_пароль>
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY=<ваш_ключ_django>
HOSTS_ALLOWED=*


### Внести значения переменных окружения в GitHub Secrets
Вам не нужно самим создавать файл для переменных окружения.
Для этого настроено автоматическое внесение переменных из GitHub Secrets.
1. Зайдите в репозиторий на GitHub.
2. Нажмите Settings в горизонтальной навигационной панели.
3. Нажмите Secrets в вертикальной навигационной панели.
4. Нажмите New repository secret.
5. В Name вводите имя переменной, в Value значение.

Нужно внести следующие переменные:
1. DOCKER_HUB_USERNAME - имя на Docker Hub
2. DOCKER_HUB_PASSWORD - пароль для Docker Hub
3. HOST - IP-адрес вашего сервера
4. USER - имя пользователя для сервера
5. SSH_KEY - ssh-ключ
    5.1. получить его можно с помощью команды ```~/.ssh/id_rsa.pub```
6. PASSPHRASE - passphrase для ssh-ключа
7. DB_ENGINE - движок базы данных
8. DB_NAME - имя базы данных
9. POSTGRES_USER - имя администратора базы данных
10. POSTGRES_PASSWORD - пароль
11. DB_HOST - название сервиса (контейнера)
12. DB_PORT - порт для подключения к БД

### Миграции

Так же необходимо произвести все миграции.

Для этого запустите следующие 2 команды:
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

Если же нет миграций, а при выполнении двух предыдущих команд
миграции не совершаются, то прозведите миграции отдельно для
каждого приложения:
```
docker-compose exec backend python manage.py makemigrations <app_name>
docker-compose exec backend python manage.py migrate <app_name> --noinput
```


### Создание суперпользователя

Для доступа в админку нужно создать суперпользователя
с помощью следующей команды:
```
docker-compose exec backend python manage.py createsuperuser
```

### Заполнение начальными данными.

Чтобы заполнить базу данных начальными данными используйте
следующие команды команды.

Загрузка всех данных:
```
sudo docker-compose exec backend python manage.py loaddata all_data.json
```

Или можно загружать данные раздельно по необходимости.
Загрузка ингредиентов из файла ingredients.csv:
```sudo docker-compose exec backend python upload_ingredints_to_db.py```
Загрузка пользователей:
```sudo docker-compose exec backend python loaddata users.json```

Картинки придется самим загрузить через админку.

## Технологии

Для запуска проекта вам потребуется:
- Docker (Docker Hub, docker-compose)
- GitHub Actions

## Об авторе

Автор этого проекта студент Яндекс.Практикума 17 когорты Чемадуров Артём :)
Посмотреть рабочий проект вы можете по следующему адресу: http://51.250.1.76/ (доступен будет до 31.12.2021 г.)
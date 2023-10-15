<h1>Тестовое задание для скайэнга</h1>

Сервис реализует возможность добавления товаров через административную панель и автоматический подсчет количества заказов с первого дня месяца и за последний месяц в принципе.

С основным пунктом подсчета у меня возникли некоторые проблемы - баг, который я не смогла пофиксить из-за нехватки времени.

Его суть заключается в том, что подсчет количества товаров не сохраняется в админке, и, следовательно, не добавляется на страницу. Но при дебаге выяснилось, что все эти данные подсчитываются правильно, несмотря на то, что никуда не записываются.

При решении задачи я использовала встроенные функции питона - sum и count. Была попытка использовать функции самой джанги - Sum, Count, aggregate, но такой набор показался мне не очень подходящим, так как этот подход учитывает только количество
записей о количесвте товаров, заданные в админке. Либо, может, я не совсем разобралась в сути задания? В любом случае, получилось так себе.

Также, я использовала библиотеку datetime, чтобы вычислять дату и месяц от текущей даты.

Кроме того, была реализована авторизация. Опять-таки, времени не хватило, потому что я все делала в последний момент, поэтому вместо AbstractUser я использовала crispy forms, взяв регистрацию из старого проекта, который однажды
реализовывала. Регистрация и авторизация - первое, что вы увидете, зайдя в приложение. Далььше идет переадресация на главную страницу, где, собственно, и размещена вся информация по заказам.

База данных - sqlite, из сторонних библиотек - сам джанго и криспи. 

Возможные маршруты: 

login/ - авторизация
register/ - регистрация
home/ - основная страница
admin/ - админка

Как развернуть у себя, думаю, подробно объяснять не нужно - скачать, установить зависимости, запустит через manage.py 

Крутится все на локалхосте, поэтому проблем возникнуть не должно. 

Переменные окружения: 

<code>
DEBUG=True #установить False, если планируете деплоить
SECRET_KEY= # ваш секретный ключ Django
DATABASE_URL= # ссылка на базу данных
ALLOWED_HOSTS='.pythonanywhere.com' # можно указать свой 
CRISPY_TEMPLATE_PACK = "bootstrap5" # указать версию бутстрапа

LOGIN_REDIRECT_URL = 'home' # куда будет ридериктиться приложение после авторизации
LOGIN_URL = 'login' # какая страница отвечает за логин
</code>

Хорошего дня!

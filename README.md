24.1 Вьюсеты и дженерики
----------------------------------------------------------------

### Задание 1

Создайте новый Django-проект, подключите DRF и внесите все необходимые настройки.

### Задание 2

Создайте следующие модели:

**Пользователь**:
все поля от обычного пользователя, но авторизацию заменить на _email_;
_телефон_, _город_, _аватарка_.

**Курс**:
_название_, _превью (картинка)_, _описание_.

**Урок**:
_название_, _описание_, _превью (картинка)_, _ссылка на видео_.

### Задание 3

Опишите CRUD для моделей курса и урока, но при этом для курса сделайте через `ViewSets`, а для урока — через `Generic`-классы.

Для работы контроллеров опишите простейшие сериализаторы.

Работу каждого эндпоинта необходимо проверять с помощью Postman.

Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже самой простой авторизацией.

* Дополнительное задание
Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для личного использования: `ViewSet` или `Generic`.
----------------------------------------------------------------

### Задание 1

Для модели курса добавьте в сериализатор поле вывода количества уроков.
(Two ways to do it: either use SerializerMethodField() or adding an IntegerField() 

### Задание 2

Добавьте новую модель «Платежи» со следующими полями:

* пользователь,
* дата оплаты,
* оплаченный курс или урок - (two nullable fields),
* сумма оплаты,
* способ оплаты: наличные или перевод на счет.

Запишите в эту модель данные через инструмент фикстур или кастомную команду.

### Задание 3

Для сериализатора модели курса реализуйте поле вывода уроков.

### Задание 4

Настройте фильтрацию для эндпоинтов вывода списка платежей с возможностями:

менять порядок сортировки по дате оплаты - (standard filter),
фильтровать по курсу или уроку - (django-filter: SearchFilter),
фильтровать по способу оплаты.

### * Дополнительное задание

Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей.

----------------------------------------------------------------
### Задание 1

Настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

### Задание 2

Заведите группу модераторов и опишите для неё права работы с любыми уроками или курсами, но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

### Задание 3

Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть и редактировать только свои курсы и уроки.

_Заводить группы лучше через админку и не реализовывать для этого дополнительных эндпоинтов._

### * Дополнительное задание

Для профиля пользователя введите ограничения, чтобы авторизованный пользователь мог просматривать любой профиль, но редактировать только свой. При этом при просмотре чужого профиля должна быть доступна только общая информация, в которую не входят: пароль, фамилия, история платежей.

----------------------------------------------------------------
25.2 Валидаторы, пагинация и тесты
----------------------------------------------------------------
### Задание 1
Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.

То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные сайты — нельзя.

### Задание 2
Добавьте модель подписки на обновления курса для пользователя.

Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.

При этом при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс. То есть давать информацию, подписан пользователь на обновления курса или нет.

### Задание 3
Реализуйте пагинацию для вывода всех уроков и курсов.

### Задание 4
Напишите тесты, которые будут проверять корректность работы `CRUD` уроков и функционал работы подписки на обновления курса.

Сохраните результат проверки покрытия тестами.

### * Дополнительное задание
Напишите тесты на все имеющиеся эндпоинты в проекте.

--------------------------------------------------------
26.1 Документирование и безопасность
------------------------------------------------
### Задание 1
Подключить и настроить вывод документации для проекта. Убедиться, что каждый из реализованных эндпоинтов описан в документации верно, при необходимости описать вручную.

### Задание 2
Подключить возможность оплаты курсов через https://stripe.com/docs/api.

Доступы можно получить напрямую из документации, а также пройти простую регистрацию по адресу https://dashboard.stripe.com/register.

Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:

https://stripe.com/docs/api/payment_intents/create — создание платежа;
https://stripe.com/docs/api/payment_intents/retrieve — получение платежа.
Для тестирования можно использовать номера карт из документации:

https://stripe.com/docs/terminal/references/testing#standard-test-cards
Подключение оплаты лучше всего рассматривать как обычную задачу подключения к стороннему API.

Основной путь: запрос на покупку → оплата. Статус проверять не нужно.

Каждый эквайринг предоставляет тестовые карты для работы с виртуальными деньгами.

### * Дополнительное задание
Реализуйте проверку статуса с помощью эндпоинта https://stripe.com/docs/api/payment_intents/retrieve — получение платежа.

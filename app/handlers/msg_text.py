from loader import _

"""
Текст вынес в отдельный файл для более удобного редактирования
"""


class MsgText:
    @property
    def WELCOME(self):
        return _(
            """
Привет! 👋

Добро пожаловать в наш Telegram-бот для знакомств! 💬 Чтобы начать, тебе нужно создать свой профиль.

Создай профиль и начни знакомиться с новыми людьми прямо сейчас!
"""
        )

    @property
    def MENU(self):
        return _(
            """
🔍 Искать анкеты
👤 Мой профиль
🗄 Посмотреть лайки

✉️ Пригласить друзей"""
        )

    @property
    def PROFILE_MENU(self):
        return _(
            """
🔄 Заполнить анкету заново
🖼 Изменить фотографию
✍️ Изменить описание
❌ Отключить анкету

🔍 Смотреть анкеты
"""
        )

    @property
    def INFO(self):
        return _(
            """
👋
Немного информации о боте:
Этот бот был создан по аналогии с популярным ботом для знакомств <a href='https://t.me/leomatchbot?start=i_VwRd0'>Дайвинчик</a>
Весь код бота открыт и доступен на <a href='https://github.com/devvsima/dating-bot'>GitHub</a>

По вопросам и предложениям можно писать сюда: @devvsima.
"""
        )

    @property
    def SEARCH(self):
        return _("Идет поиск...")

    @property
    def INVALID_PROFILE_SEARCH(self):
        return _("Подходящих вам анкет нет. Вы можете попробовать указать другой город. 🌍")

    @property
    def EMPTY_PROFILE_SEARCH(self):
        return _("Больше анкет нет. Попробуй позже! 😊")

    @property
    def LIKE_PROFILE(self):
        return _("Кому-то понравилась ваша анкета! Хотите посмотреть? 👀")

    @property
    def LIKE_ARCHIVE(self):
        return _("Тебя еще никто не лайкнул. Но всё ещё впереди!")

    @property
    def LIKE_ACCEPT(self):
        return _("Отлично! Надеюсь хорошо проведете время ;) <a href='{}'>{}</a>")

    @property
    def GENDER(self):
        return _("Укажи свой пол: 👤")

    @property
    def FIND_GENDER(self):
        return _("Кто тебе интересен? Выбери пол человека: 👤")

    @property
    def PHOTO(self):
        return _("Пришли своё фото! 📸")

    @property
    def NAME(self):
        return _("Как тебя зовут? Напиши своё имя, чтобы мы могли продолжить! ✍️")

    @property
    def AGE(self):
        return _("Сколько тебе лет? Укажи свой возраст, пожалуйста! 🎂")

    @property
    def CITY(self):
        return _("Теперь введи свой город. 🏙️")

    @property
    def DESCRIPTION(self):
        return _("Расскажи немного о себе! Это поможет другим лучше тебя узнать. 📝")

    @property
    def DISABLE_PROFILE(self):
        return _("Ваша анкета временно отключена.\n\nЧтобы снова активировать её, просто нажмите на кнопку.")

    @property
    def ACTIVATE_PROFILE_ALERT(self):
        return _("✅ Ваша анкета успешно восстановлена! Теперь вы снова можете пользоваться ботом.")

    @property
    def INVALID_RESPONSE(self):
        return _("Некорректный ответ. Пожалуйста, выбери на клавиатуре или напиши правильно. 📝")

    @property
    def INVALID_LONG_RESPONSE(self):
        return _("Превышен лимит символов. Пожалуйста, сократи сообщение. ✂️")

    @property
    def INVALID_PHOTO(self):
        return _("Неверный формат фотографии! Пожалуйста, загрузите изображение в правильном формате. 🖼️")

    @property
    def INVALID_AGE(self):
        return _("Неверный формат, возраст нужно указывать цифрами. 🔢")

    @property
    def INVITE_FRIENDS(self):
        return _(
            "Приглашай друзей и получай бонус к своей анкете!\n\nПриглашенные пользователи: <b>{}</b>\n\nСсылка для друзей:\n<code>https://t.me/{}?start={}</code>")

    @property
    def ADMIN_WELCOME(self):
        return _("Вы администратор!")

    @property
    def USERS_STATS(self):
        return _("""  
👤 Пользователей: {}\t|🚫 Заблокированных: {}  

📂 Анкет: {}\t|🔕 Неактивных: {}

🙍‍♂ Парней: {}\t|🙍‍♀ Девушек: {}  
""")

    @property
    def CHANGE_LANG(self):
        return _("Выберите язык, на который вы хотите переключиться: 🌐")

    @property
    def DONE_CHANGE_LANG(self):
        return _("Ваш язык успешно изменён! ✅")

    @property
    def NEW_USER(self):
        return _("Появился новый пользователь, @{} | {}")

    @property
    def REPORT_TO_USER(self):
        return _("Пользователь: @{} | <code>{}</code> отправил жалобу на анкету пользователя: @{} | <code>{}</code>")

    @property
    def USER_PANEL(self):
        return _("Панель управлением пользователями")

    @property
    def UNBAN_USERS_PANEL(self):
        return _("💊 Укажите список пользовтелей для разблокировки в формате: 1234567, 234567")

    @property
    def BAN_USERS_PANEL(self):
        return _("⚔️ Укажите список пользовтелей для блокировки в формате: 1234567, 234567")

    @property
    def USER_BANNED(self):
        return _("Пользователь: {} заблокирован")

    @property
    def MAILING_PANEL(self):
        return _("Укажите текст сообщение которое хотите отправить")

    @property
    def REPORT_TO_PROFILE(self):
        return _("✅ Ваша жалоба на пользователя отправлена на рассмотрение!")

    @property
    def RESON_OF_REPORTING(self):
        return _("""Укажите причину жалобы:
🔞 Неприличный материал
💰 Реклама
🔫 Другое

Если жалоба ошибочная, вы можете вернутся назад.
""")


msg_text = MsgText()

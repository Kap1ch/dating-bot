<picture>
  <img src="https://pbs.twimg.com/media/GYKn8I_WAAAvErl?format=jpg&name=large">
</picture>

# 🚀 Давай начнем

## 🛠️ Стек технологий
- `aiogram 2`
- `i18n`
- `peewee`
- `PostgreSQL \ Sqlite`

---

## 📥 Инструкция по установке

### 1. Клонируем репозиторий

Сначала клонируем репозиторий и переходим в его директорию:

```bash
git clone https://github.com/devvsima/dating-bot.git
cd dating-bot
```



### 2. Настройка виртуального окружения ".venv"

💡 Примечание: Название `.venv` можно изменить на любое другое по твоему желанию.

#### Linux


```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
> 💡 Возможно вам прийдется установить apt install python3.10-venv или что-то в этом роде


#### Windows


```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```



### 3. Настройка переменных окружения .env

Сначала скопируй файл `.env.dist` и переименуй его в `.env`:

```bash
cp .env.dist .env
```

Теперь нужно настроить файл `.env`



#### Настройки бота

| Название | Описание                                           | Пример                      |
| -------- | -------------------------------------------------- | --------------------------- |
| TOKEN    | Токен бота от [@BotFather](https://t.me/BotFather) | 1234567:ASDSFDkjdjdsedmD... |
| ADMINS   | Список id администраторов                          | 12345678,12345677           |



#### Настройка базы данных

| Название | Описание                               | По умолчанию |
| -------- | -------------------------------------- | ------------ |
| DB_NAME  | Название базы данных                   |              |
| DB_HOST  | Хост базы данных                       | localhost    |
| DB_PORT  | Порт базы данных                       | 5432         |
| DB_USER  | Пользователь с доступом до базы данных |              |
| DB_PASS  | Пароль от базы данных                  |              |

---

### Теперь бот готов к запуску! 🎉


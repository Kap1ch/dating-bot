<p align="center">
  <img src="https://i.ibb.co/ZVyJ7ky/Screenshot-52.png" alt="diagram" width="1000">
</p>
<details>
  <summary>📸 Скриншоты</summary>
  
  <p align="center">
    <img src="https://i.ibb.co/ggvC6kr/Screenshot-53.png" alt="Screenshot 1" width="800">
  </p>
  <p align="center">
    <img src="https://pbs.twimg.com/media/GYKn8I_WAAAvErl?format=jpg&name=large" alt="Screenshot 2" width="800">
  </p>
  <!-- <p align="center">
    <img src="https://pbs.twimg.com/media/GYKn8I_WAAAvErl?format=jpg&name=large" alt="Screenshot 3" width="500">
  </p> -->
</details>

# 🚀 Давай начнем

## 🛠️ Стек технологий
- `Aiogram 3`
- `Redis`
- `i18n`
- `Peewee`
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


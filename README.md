Kingdom
Kingdom — это учебный проект, представляющий собой бэкенд API для управления данными персонажа по второй редакции Pathfinder. В проекте реализованы модели, такие как персонажи, заклинания, расы и навыки, с использованием языка Python и веб-фреймворка FastApi. В проекте также предусмотрены маршруты с ограничением прав для администраторов для загрузки и управления данными в формате CSV. Проект так же использует регистрацию по электронной почте через Rabbit MQ

Бэкенд: Python (FastApi) База данных: Sql Alchemy ORM для работы с базой данных Документация: Swagger для автоматизированной документации API Авторизация: JWT-мидлвар для аутентификации и контроля доступа на основе ролей

Установка и запуск

Клонируйте репозиторий: git clone https://github.com/Telpegaraf/KingdomFA.git cd KingdomFA
Настройте переменные окружения: Укажите переменные окружения в файле .env для подключения к базе данных и настройки JWT.
Запустите проект через Docker: COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose -f docker/docker-compose.yml --project-name kingdom up -d --build
To-Do

Расширение документации, новых моделей и связей между ними, включая автообновление параметров при изменении характеристик или предметов персонажа
_______________________________________________________________________________________________________________
Kingdom is a pet project that serves as a backend API for managing Character's Sheet by Pathfinder 2E. It includes models like characters, spells, races, and feats, and is built with Python and the FastApi web framework. The project includes admin-restricted routes for loading and managing data in CSV format. The project includes email-sending with Rabbit MQ.

Backend: Python (FastApi) Database: Sql Alchemy ORM for database interactions Documentation: Swagger for API documentation Authorization: JWT-based middleware for authentication and role-based access control

Setup and Installation

Clone the repository: git clone https://github.com/Telpegaraf/KingdomFA.git cd KingdomFA

Setup Environment Variables: Configure environment variables in .env for database and JWT secrets.

Run the Project with Docker: COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose -f docker/docker-compose.yml --project-name kingdom up -d --build

To-Do

Extend documentation
Add more models and complex relationships

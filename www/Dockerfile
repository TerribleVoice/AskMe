# Используем официальный образ Node.js
FROM node:14-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код приложения
COPY . .

# Собираем приложение
RUN npm run build

# Устанавливаем serve для запуска приложения
RUN npm install -g serve

# Определяем команду для запуска приложения при запуске контейнера
CMD ["serve", "-s", "build", "-l", "3000"]

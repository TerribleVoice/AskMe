# Старт с официального образа node (используйте версию LTS)
FROM node:lts AS build

# Укажите рабочую директорию
WORKDIR /app

# Копируйте package.json и yarn.lock
COPY package.json yarn.lock ./

# Установите зависимости
RUN yarn install

# Копируйте остальные файлы проекта
COPY . .

# Соберите приложение
CMD ["npm", "start"]

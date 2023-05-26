FROM node:alpine
EXPOSE 3000
RUN mkdir -p /code
WORKDIR /code
COPY package*.json yarn*.lock ./
COPY . .

RUN npm install yarn && yarn && yarn install && yarn build && yarn cache clean
CMD [ "yarn", "start" ]
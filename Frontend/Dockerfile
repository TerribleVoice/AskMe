FROM node:alpine
EXPOSE 3000
RUN mkdir -p /code
WORKDIR /code
COPY package*.json yarn*.lock ./

RUN npm install yarn
RUN yarn
RUN yarn install

COPY . .

RUN yarn build
RUN yarn cache clean
CMD [ "yarn", "start" ]

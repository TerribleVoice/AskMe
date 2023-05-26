FROM node:alpine
EXPOSE 3000
WORKDIR /code
COPY public/ public/
COPY src/ src/
COPY .env .env
COPY config-overrides.js config-overrides.js
COPY package.json package.json
COPY tsconfig.json tsconfig.json
COPY yarn.lock yarn.lock

RUN yarn install -y
CMD ["yarn", "start"]
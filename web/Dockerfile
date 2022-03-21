FROM node:latest

RUN mkdir /usr/app

WORKDIR /usr/app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

ENV PORT 3000

CMD [ "node", "app.js" ]

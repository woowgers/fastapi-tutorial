FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json package-lock.json .
RUN npm install @vue/cli@5.0.8 -g &&\
    npm install

CMD ["npm", "run", "serve"]

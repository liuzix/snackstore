FROM node:alpine

add . /frontend

WORKDIR /frontend
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "dev"]

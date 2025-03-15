FROM node:14-alpine
# Set the working directory inside the container
WORKDIR /frontend

COPY package*.json ./

RUN npm install
RUN npm install react-router-dom

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
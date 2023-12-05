# Use Node.js as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /app


COPY package*.json .
RUN npm install
COPY . .


RUN npm run build

EXPOSE 3000

RUN npm install -g serve

CMD ["serve", "-s", "dist", "-l", "3000"]


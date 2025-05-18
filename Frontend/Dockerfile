FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Ensure vite is executable (workaround for permission issue)
RUN chmod +x node_modules/.bin/vite

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

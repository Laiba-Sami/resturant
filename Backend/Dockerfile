# Use Node base image
FROM node:18

# Create app directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy everything else including config
COPY . .

# Set environment variables path
ENV NODE_ENV=development
ENV CONFIG_PATH=./config/config.env

# Expose the port (match the one in your config.env or app)
EXPOSE 8080

# Start the server
CMD ["node", "server.js"]

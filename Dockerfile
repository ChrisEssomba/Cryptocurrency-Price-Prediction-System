# Use the official Node.js image as a base
FROM node:14

# Create and change to the app directory
WORKDIR /usr/src/app

# Copy app files
COPY . .

# Install app dependencies
RUN npm install

# Expose port 8080
EXPOSE 8080

# Start the app
CMD ["npm", "start"]

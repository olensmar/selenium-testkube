# Set base image
FROM maven:3.9.6-eclipse-temurin-22-alpine AS builder

# Copy pom.xml
COPY pom.xml .

# Install project dependencies
RUN mvn -B dependency:go-offline
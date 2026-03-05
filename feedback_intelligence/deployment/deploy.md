# Deployment Guide

## Local Deployment

uvicorn main:app --reload

## Docker Deployment

docker compose up --build

## Production Recommendation

- Use Nginx reverse proxy
- Deploy on AWS EC2 or Azure VM
- Enable HTTPS
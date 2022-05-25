.DEFAULT_GOAL := help

include .env
export  $(shell sed 's/=.*//' .env)

build:
	docker build -t ${PROJECT_NAME}:${PROJECT_VERSION} .

up:
	docker run --rm -it -v ${PWD}:/app -p 8080:8080 -w /app --env-file .env ${PROJECT_NAME}:${PROJECT_VERSION} sh start.sh

bash:
	docker run --rm -it -v ${PWD}:/app -w /app --env-file .env ${PROJECT_NAME}:${PROJECT_VERSION} bash

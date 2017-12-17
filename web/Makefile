build:
	docker build -t psit_web .

prod:
	docker build -t asia.gcr.io/k-wiput-me/psit_web .

push:
	gcloud docker -- push asia.gcr.io/k-wiput-me/psit_web:latest

run:
	docker-compose up
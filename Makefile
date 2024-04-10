all: build deploy

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t funkaoshi/randomcharacter:latest -t funkaoshi/randomcharacter:1 --push .

run:
	docker run -p 8000:8000 -t funkaoshi/randomcharacter:latest

push:
	docker push funkaoshi/randomcharacter:latest

deploy:
	ssh ubuntu@oci.vqvz.com "cd oracle_free_vm/docker && docker-compose stop funkaoshi-randomcharacter && docker-compose pull && docker-compose up --force-recreate -d funkaoshi-randomcharacter"

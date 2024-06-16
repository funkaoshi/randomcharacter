all: build deploy

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t watcherdm/randomcharacter:latest -t watcherdm/randomcharacter:1 --push .

run:
	docker run -p 8000:8000 -t watcherdm/randomcharacter:latest

push:
	docker push watcherdm/randomcharacter:latest

# replace this with the actual ecs deploy maybe?
deploy:
	ssh ubuntu@oci.vqvz.com "cd oracle_free_vm/docker && docker-compose stop watcherdm-randomcharacter && docker-compose pull && docker-compose up --force-recreate -d watcherdm-randomcharacter"

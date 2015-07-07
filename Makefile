all: deploy

deploy:
	rsync -avz --exclude=Makefile --exclude=.git --exclude=*.swp --exclude=*.pyc --exclude=README.md . ramanan@funkaoshi.com:/home/ramanan/character.totalpartykill.ca/
	ssh ramanan@funkaoshi.com 'touch character.totalpartykill.ca/tmp/restart.txt'

clean:
	rm *.pyc



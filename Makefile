all: deploy

deploy:
	rsync -avz --exclude=Makefile --exclude=.git --exclude=*.swp --exclude=*.pyc --exclude=README.md /Users/ramanan/Sites/create/ funkaoshi.com:/home/ramanan/character.totalpartykill.ca/
	ssh funkaoshi.com 'touch character.totalpartykill.ca/tmp/restart.txt'

clean:
	rm *.pyc



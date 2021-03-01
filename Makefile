deps:
	pip install -r requirements.txt
run:
	python main.py
docker_build:
	docker build -t madpele/blog .
docker_run: docker_build
	docker run --name ci-test -p 5000:5000 madpele/blog
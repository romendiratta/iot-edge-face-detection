build-broker:
	docker build -t broker-cloud ./broker-cloud

build-processor:
	docker build -t processor ./processor

docker-clean:
	docker ps -aq | xargs docker rm -f

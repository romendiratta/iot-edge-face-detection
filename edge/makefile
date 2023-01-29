
build-face-detector:
	docker build -t romendiratta/face-detector ./face-detector

push-face-detector:
	docker push romendiratta/face-detector:latest

deploy-face-detector:
	kubectl apply -f ./kubernetes/deployments/face-detector-deployment.yaml

build-broker:
	docker build -t romendiratta/broker ./broker

push-broker:
	docker push romendiratta/broker:latest

deploy-broker: 
	kubectl apply -f ./kubernetes/deployments/broker-deployment.yaml

deploy-broker-service: 
	kubectl apply -f ./kubernetes/services/broker-service.yaml

build-logger:
	docker build -t romendiratta/logger ./logger

push-logger: 
	docker push romendiratta/logger:latest

deploy-logger:
	kubectl apply -f ./kubernetes/deployments/logger-deployment.yaml

build-forwarder:
	docker build -t romendiratta/forwarder ./forwarder

push-forwarder:
	docker push romendiratta/forwarder:latest

deploy-forwarder:
	kubectl apply -f ./kubernetes/deployments/forwarder-deployment.yaml

kube-clean:
	kubectl delete all --all

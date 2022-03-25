python_log:
	docker logs python_app

python_build_and_run:
	printf $(MSG) "Building and running python";
	docker-compose build python
	printf $(MSG) "install requirements";
	docker-compose run --rm python pip install --user -r requirements.txt
	printf $(MSG) "Running Flask App";
	docker-compose up -d python
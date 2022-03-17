SHELL := /bin/bash

ifndef VERBOSE
.SILENT:
endif

####### Shortcuts

clean_run: install build start
	echo " -------------- All Services Started -> Watching Leos Service Logs ---------------"
	docker logs leos-container -f

run: build start

####### Main

install:
	$(eval RELEASE_ZIP=$(shell cat ./.env | grep RELEASE_ZIP= | cut -d '=' -f2))
	rm -rf ./src
	mkdir -p "./src"
	curl ${RELEASE_ZIP} >> ./download.zip && unzip -o ./download.zip -d ./src && rm ./download.zip

build:
	docker-compose build

start:
	docker-compose up -d

bash:
	docker exec -it annotate-container /bin/bash

####### Logs

annotate_logs:
	docker logs annotate-container

user-repository_logs:
	docker logs user-repository-container

repository_logs:
	docker logs repository-container

leos_logs:
	docker logs leos-container

akn4euutil_logs:
	docker logs akn4euutil-container

####### Docker

kill_active_docker_containers:
	if [ "$$(docker ps -q)" = "" ]; then \
  		echo "There is no docker services for kill. Skipping ..."; \
    else \
		printf ${MSG_YELLOW} ">>> Warning! You are about to kill all active docker containers"; printf "\n"; \
		if $(MAKE) -s ask_confirm ; then \
			printf "Killing all active docker containers .... \n"; \
			docker kill $$(docker ps -q); \
			printf "Killing all active docker containers"; printf $(DONE); \
		fi \
    fi;

remove_all_docker_images:
	printf ${MSG_YELLOW} ">>> Warning! You are about to remove all docker images"; printf "\n"; \
	if $(MAKE) -s ask_confirm ; then \
		printf "Removing all docker images ... \n"; \
		docker image prune -f -a; \
		printf "Removing all docker images"; printf $(DONE); \
	fi

remove_all_docker_containers:
	printf ${MSG_YELLOW} ">>> Warning! You are about to remove all docker containers"; printf "\n"; \
	if $(MAKE) -s ask_confirm ; then \
		printf "Removing all docker containers ... \n"; \
		docker container prune -f; \
		printf "Removing all docker containers"; printf $(DONE); \
	fi

remove_all_docker_volumes:
	printf ${MSG_YELLOW} ">>> Warning! You are about to remove all docker volumes"; printf "\n"; \
	if $(MAKE) -s ask_confirm ; then \
		printf "Removing all docker volumes ... \n"; \
		docker volume prune -f; \
		printf "Removing all docker volumes"; printf $(DONE); \
	fi

reset_docker: kill_active_docker_containers remove_all_docker_containers remove_all_docker_images remove_all_docker_volumes

ask_confirm:
	@if [[ -z "$(CI)" ]]; then \
		REPLY="" ; \
		read -p "$$(tput bold)>>> Are you sure? [y/n] > $$(tput sgr0)" -r ; \
		if [[ ! $$REPLY =~ ^[Yy]$$ ]]; then \
			printf $(_ERROR) "KO" "Stopping" ; \
			exit 1 ; \
		else \
			printf $(_TITLE) "OK" "Continuing" ; \
			exit 0; \
		fi \
	fi

_TITLE := "\033[32m[%s]\033[0m %s\n" # Green text for "printf"
_ERROR := "\033[31m[%s]\033[0m %s\n" # Red text for "printf"
MSG_YELLOW := "$$(tput setaf 190)%s$$(tput sgr0)" # yellow msg
DONE := " ... \033[32mdone\033[0m\n" # done green text
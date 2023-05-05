# docker-project

## Build Setup
```
docker compose build
docker compose up
```

## Login into the app container via SSH
```
docker compose exec -it app sh start_sshd.sh
ssh root@127.0.0.1 -p 5022
```
## Run all tests
```
docker compose exec -it tester sh tests/test_all.sh
```

## Run pylint tests for 10 categories 
```
docker compose exec -it tester sh tests/test_all.sh -p
```

## Run pylint tests for all categories 
```
docker compose exec -it tester sh tests/test_all.sh -pA
```

## Run black tests
```
docker compose exec -it tester sh tests/test_all.sh -b
```

## Run integration tests
```
docker compose exec -it tester sh tests/test_all.sh -i
```

## Run selenium tests
```
docker compose exec -it tester sh tests/test_all.sh -s
```

## Stop containers
```
docker stop docker-project-app-1  docker-project-tester-1
```
## Clean up
```
docker rm docker-project-app-1  docker-project-tester-1
docker rmi docker-project-app  docker-project-tester
docker network rm docker-project_default
```

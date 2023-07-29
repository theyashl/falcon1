# Summary
Book Library Application for Library Admin, which provides following features:
- Login
- List Books from Library
- Add a new Book in Library
- GET/UPDATE/DELETE specific Book from Library
- List Authors from Library
- Add a new Author in Library
- GET/UPDATE/DELETE specific Author from Library

Applicates Rotes are listed in [Swagger](https://github.com/theyashl/falcon1/blob/master/swagger.yaml) document.

# Usage
### System Requirements
- Docker
### Steps to run the application
- Clone this repo and go to working directory
```sh
git clone https://github.com/theyashl/falcon1.git
cd falcon1/
```
- Create Docker Network:
```sh
sudo docker network create falcon1-network
```
- Deploy MySQL Container:
```sh
sudo docker run -d \
--network falcon1-network --network-alias mysql \
-e MYSQL_ROOT_PASSWORD=123 \
-e MYSQL_DATABASE=falcon1 \
mysql:5.7
```
Above command will return Container ID. ex. `62d1cd0f31493330e681925b9a7c286086319000bf454967ce84b6b53ac8feb9`
- Build app image
```sh
sudo docker build .
```
Above command will return image ID. ex. `writing image sha256:53cdcef8f4cfb5732a3f5e189236c56d0db8083de90e6fb8b0dddd8cb6c14cd3` where `53cdcef8f4cfb5732a3f5e189236c56d0db8083de90e6fb8b0dddd8cb6c14cd3` is image ID
- Start App on same network as Database:
```sh
sudo docker run -dp 0.0.0.0:8000:8000 --network falcon1-network <IMAGE_ID>
```
ex. `sudo docker run -dp 0.0.0.0:8000:8000 --network falcon1-network 53cdc
e6cd37d9349fa5916a9e82d2fd3023fbeb1a7a06764c04f6f97ea909bef26b02`
- Log into Database:
```sh
sudo docker exec -it <MYSQL_CONTAINER_ID> mysql -u root -p
```
ex. `sudo docker exec -it 62d1cd0f3149 mysql -u root -p`
- Insert default admin details in `user` table:
```sql
INSERT INTO user(username,password) VALUES ("abc", "123");
```

**Setup is Completed**

- To check the logs of Application, execute following command:
```sh
docker logs -f <CONTAINER_ID>
```
ex. `sudo docker logs -f e6cd3`

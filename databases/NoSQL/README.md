## Training on non relational database management systems using Mongodb and Redis with languages python and javascript

### HOW I INSTALL MONGODB ON MY WSL UBUNTU 22.04
1. First update the package list: Make sure your package list is up-to-date before installing MongoDB
 
```bash
sudo apt update
```

2. Install MongoDB: To install MongoDB, you'll first need to add the official MongoDB repository.
   Here’s how:
- Install dependencies:
```bash
sudo apt install -y gnupg
```
- Add the MongoDB GPG key: This allows the system to authenticate the MongoDB packages.
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```
- Add the MongoDB repository: This tells your system where to find MongoDB packages.
```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```
- Re-update your package list: Now, update the apt package list again to include the MongoDB repo.
```bash
sudo apt update
```
- Install MongoDB: Now you can install MongoDB:
```bash
sudo apt install -y mongodb-org
```

3. Start MongoDB: After MongoDB is installed, you can start it by running:
```bash
sudo service mongod start
```
- Alternatively, you can use systemctl if it's supported in your WSL setup:
```bash
sudo systemctl start mongod
```

4. Verify that MongoDB is running: You can check if MongoDB is running by typing:
```bash
ps aux | grep mongod
```

5. Access the MongoDB shell: To interact with MongoDB, you can open the MongoDB shell with the mongo command:
```bash
mongo
```

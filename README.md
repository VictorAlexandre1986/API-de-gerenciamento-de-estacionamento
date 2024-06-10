# Flask Template Project

This is built with Flask, Flask-RESTful, Flask-JWT-Extended, Flask-SQLAlchemy and PostgreSQL.

## Pre-requirements
- [Python 3.12.x LTS](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) - other versions [see here](https://github.com/docker/compose/releases)

### How to install Docker Compose
```bash
# Uninstall old version of docker-compose before, after...

sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## Recommended IDEAs
 - [VSCode with Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [IntelliJ with Python Plugin](https://plugins.jetbrains.com/plugin/631-python)

 ## Pre-settings

  Add in **/etc/hosts**
  ```bash
  # For Windows see https://www.youtube.com/watch?v=xjrLN4Aqbyw
  127.0.0.1     prj-db
  127.0.0.1     prj-backend-app
  # For Linux or MacOS - Install the VIM editor
  sudo vim /etc/hosts # Add the lines below
  127.0.0.1     prj-db
  127.0.0.1     prj-backend-app
  ESC + :wq # To save and exit

#### The IDE must load the Python packages from **venv**

## Environment Settings
### Step 1

- Into the local repository folder, run:

```bash
python3 -m venv ./venv
```

- After activate the Python venv

```bash
source venv/bin/activate
```

- Update **pip** package

```bash
python -m pip install -U pip
```

### Step 2

- Installing the Python project's dependency packages

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# or
pip install pip-tools

pip-sync

```

### Listing and installing packages to update
```bash
# Mode 1 - via pip-tools
# Installing pip-tools
pip install pip-tools

pip-compile --upgrade-package Flask

# Mode 2 - via pip list --outdated
# Just listing
pip list --outdated

pip list --outdated | awk -F ' ' 'NR>2{print$1}' | xargs pip install --upgrade
```

### Important Notes
- If new or updated dependency package was added in the project structure, the **requirements.txt** must be updated from **requirementes.in**

```bash
# Installing pip-tools
pip install pip-tools

pip-compile ./requirements.in
```

## Running Flask back-end locally

### Start SQL Server via docker-compose

```bash
# In the project root folder
cd docker
docker-compose up --force-recreate -d prj-db

cd ../flaskr
python -m flask run
```

### To stop docker docker-compose

```bash
CTRL + C
# In the project root folder
cd docker
docker-compose down --remove-orphans
```

#### Notes
- The database will be online in the port 1433 (details in docker-compose.yml file)
- The Flask app will be online in the port 5000 (details in docker-compose.yml file)

## Running Flask back-end via docker-compose

### Start all back-end via docker-compose
Before run the statements below, edit the value of parameter
**FLASKR_DEV_DIR** in the **.env** file of the **docker** folder with the
absolute path of **flaskr/** project folder in you host.

This will allow the container to reload your code after changes have been made.

```bash
cd docker
docker-compose build --no-cache
docker-compose up --force-recreate -d ; docker-compose logs -f
```

### To stop docker docker-compose

```bash
# In the project root folder
cd docker
docker-compose down --remove-orphans
```

#### Notes
- The MSSQL Database will be online in the port 1433 (details in docker-compose.yml file)
- The Redis Caching will be online in the port 6379 (details in docker-compose.yml file)
- The Flask app will be online in the port 5000 (details in docker-compose.yml file)
## Executing Database Migrations using Flask-Migrate

### For you to control changes in the database follow the instructions below:
  
  1. Open the "flaskr" folder in console with following command:
  ```bash
  cd flaskr
  ```

  2. Create a migration repository. If the **migrations** folder already exists this command is not necessary.
  ```bash
    python -m flask db init
  ```
  3. To build a new migration, for example, "Initial migration"
  ```bash
    python -m flask db migrate -m "Initial migration."
  ```

  4. Then you can apply the migrations created in the database
  ```bash
    python -m flask db upgrade
  ```

  5. Then you can apply the migrations created in the database
  ```bash
    # This is a new command created in the app.py file to initialize the tables 
    # with some registers
    python -m flask initdb
  ```

**Notes**: To see all the commands that are available run this command:
  ```bash
    python -m flask db --help
  ```

  Official documentation for [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Swagger Documentation UI

Access http://localhost:5000/swagger-ui

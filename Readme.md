# python Flask application to fetch github issues

## Components:
1. Frontend Web UI page to take user input of git repo
2. Backend Flask server, app.py
3. Git token required and placed in config.py (do not commit this file)

## Local dev setup:
1. Clone git repo
2. Install python packages in virtual env: _pip -m venv env_
3. Activate virtual env by running command: _./env/Scripts/activate_
4. Install python packages: _pip install -r requirements.txt_


## Start application:
$ python app.py

**Using Docker:**
- Build docker image(optional, for local development only): _docker build -t github-issues-bot:v0.1 ._

- Pull docker image(for users): _docker pull praveenmtsget/pydev:github-issues-bot__v0.1_
- Run docker container: _docker run -d -p 5000:5000 github-issues:v0.1_


References:
_- https://www.merge.dev/blog/get-all-issues-github-api-python
- https://realpython.com/flask-by-example-part-1-project-setup
- https://medium.com/@komalminhas.96/a-step-by-step-guide-to-build-and-push-your-own-docker-images-to-dockerhub-709963d4a8bc_


## Enhancements

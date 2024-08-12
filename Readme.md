# python Flask application to fetch github issues

## Components:
1. Frontend Web UI page to take user input of git repo
2. Backend Flask server, app.py
3. Git token required and placed in config.py (do not commit this file)

## Local dev setup:
1. Clone git repo
2. Install python packages in virtual env: pip -m venv env
3. Activate virtual env by running command: ./env/Scripts/activate
4. Install python packages: pip install -r requirements.txt


## Start application:
$ python app.py

# Using Docker:
Build docker image(optional, for local development only): docker build -t github-issues-bot:v0.1 .
or
Pull docker image(for users): docker pull praveenmtsget/pydev:github-issues-bot__v0.1
Run docker container: docker run -d -p 5000:5000 github-issues:v0.1


References:
- https://www.merge.dev/blog/get-all-issues-github-api-python
- https://realpython.com/flask-by-example-part-1-project-setup
- https://medium.com/@komalminhas.96/a-step-by-step-guide-to-build-and-push-your-own-docker-images-to-dockerhub-709963d4a8bc


## Enhancements

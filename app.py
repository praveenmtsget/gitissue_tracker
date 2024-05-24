import requests, config
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_issues')
def fetch_issues():
    repo_url = request.args.get('repo_url')

    split_url = repo_url.split("/")
    owner = split_url[3]
    repo = split_url[4]
    git_auth = "Bearer " + config.token

    response = requests.get(f'https://api.github.com/search/issues?q=repo:{owner}/{repo}+is:issue&per_page=100',
            headers={
                'X-GitHub-Api-Version': '2022-11-28', 
                'Authorization': f'{git_auth}',
                'Accept': 'application/vnd.github+json'
                })

    if response.status_code == 200:
        issues = response.json()["items"]
    else:
        issues = []

    return render_template('index.html', issues=issues)


if __name__ == '__main__':
    app.run(debug=True)
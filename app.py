import requests, os
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
    
    #git_auth = "Bearer " + config.token
    # for Heroku config use env variable
    git_auth = "Bearer " + os.environ['github_token']

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

# webhook logic
webhook_issues = []  # Store new issues received through webhook

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():

    if (request.method == 'POST'):
        data = request.json
        issue = data.get('issue')

        if issue:
            webhook_issues.append(issue)

        return 'Webhook received'
    elif (request.method == 'GET'):
        print(webhook_issues)
        response_html = ""
        for issue in webhook_issues:
            print(issue)
            response_html += f'{issue["title"]} - {issue["state"]}'
        return response_html

        
        
if __name__ == '__main__':
    app.run(debug=True)

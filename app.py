from flask import Flask,jsonify,abort,request
from github import Github
import requests
from os import environ as env


CLIENT_ID = env.get('CLIENT_ID')
CLIENT_SECRET = env.get('CLIENT_SECRET')
DEBUG = env.get('DEBUG')
HOST = env.get('HOST')
PORT = env.get('PORT')

app = Flask(__name__)

g = Github(CLIENT_ID,CLIENT_SECRET)


@app.route('/')
def get_repos():
  r = []
  try:
    args = request.args
    n = int(args['n'])
    l = args['l']
  except (ValueError,LookupError) as e:
    abort(jsonify(error="No integer provided for argument 'n' and 'l' in the URL"))
  repositories = g.search_repositories(query='language:' + l)[:n]
  try:
    for repo in repositories:
      response = requests.get(repo.url)
      r.append(response.json())
    return jsonify({'data':r,'status':'ok'})
  except Exception as e:
    return jsonify({'data':r,'status':'ko'})


if __name__ == "__main__":
    app.run(debug=DEBUG,host=HOST,port=PORT)
    
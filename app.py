from flask import Flask,jsonify,abort,request
from github import Github
# import urllib.request,json
import requests
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
DEBUG = os.environ['DEBUG']
HOST = os.environ['HOST']
PORT = os.environ['PORT']

app = Flask(__name__)

# g = Github('6cb9009aeb137a0dec3f','1bb80b81c302fe954be667bfb5859086e0ef9593')
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
    
from flask import Flask, request, jsonify
from scholarly import scholarly
import json

app = Flask(__name__)

@app.route('/search_author')
def search_author():
    # is the request containing JSON ?
    print (request.is_json)

    # Put json in content variable and print the name of the author
    content = request.get_json()
    print(content["name"])

    # search for author on Google Scholar and convert results to a list from an iter
    authors_arr = []
    authors = scholarly.search_author(content["name"])
    for n in authors:
        data = {}
        data['name'] = n.name
        data['affiliation'] = n.affiliation
        data['url_picture'] = n.url_picture
        authors_arr.append(data)

    return jsonify(authors_arr)
    
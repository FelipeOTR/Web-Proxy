from flask import Flask, request, jsonify, redirect, url_for, render_template
import json
import requests
from urllib.parse import urlparse

app = Flask(__name__)

# 1) verificar se o site está bloqueado
# 2) caso não esteja, retornar exatamnte oq teria no site, mas com as palavras filtradas, caso haja

# falta retornar uma página html personalizada caso o site seja bloqueado
# log de acessos
# não ser case sensitive os filtros

@app.route("/<path:site>", methods=['POST', 'GET'])
def filtro(site):
    with open('blocked.json', 'r') as blocked:
        blockedFile = json.load(blocked)

        domínio = urlparse(site).netloc

        if site in blockedFile["bloqueados"] or domínio in blockedFile["bloqueados"]:
            return f'Site bloqueado' # return render template
        else:
            with open('words.json', 'r') as words:
                wordsFile = json.load(words)

                siteRequest = requests.get(site)
                siteTexto = siteRequest.text

                for word in wordsFile:
                    siteTexto = siteTexto.replace(word, wordsFile[word])

            return siteTexto

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
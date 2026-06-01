from flask import Flask, request, jsonify, redirect, url_for, render_template
import json
import requests
from urllib.parse import urlparse
import time

app = Flask(__name__)

@app.route("/<path:site>", methods=['POST', 'GET'])
def filtro(site):
    with open('blocked.json', 'r') as blocked:
        blockedFile = json.load(blocked)

        domínio = urlparse(site).netloc

        if site in blockedFile["bloqueados"] or domínio in blockedFile["bloqueados"]:
            with open("log.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{str(time.ctime())}, {site}, bloqueado\n ")
            return redirect (url_for('bloqueio'))

        else:
            c=0
            with open('words.json', 'r') as words:
                wordsFile = json.load(words)

                siteRequest = requests.get(site)
                siteTexto = siteRequest.text
                aaa = siteTexto
                bk_siteTexto=siteTexto

                # case-insensitive
                for word in wordsFile:
                    wordLower = word.lower()
                    siteTextoLower = siteTexto.lower()

                    posição = siteTextoLower.find(wordLower)

                    while posição != -1:

                        # colocar a palavra no lugar da substituída
                        siteTexto = siteTexto[:posição] + wordsFile[word] + siteTexto[posição + len(word):]
                        siteTextoLower = siteTexto.lower()
                        aaa = posição
                        posição = siteTextoLower.find(wordLower)

                        if aaa != siteTexto:
                            if c==0:
                                with open("log.txt", "a", encoding="utf-8") as arquivo:
                                    arquivo.write(f"{str(time.ctime())}, {site}, filtrado\n")
                                c=1
            if c==0:
                with open("log.txt", "a", encoding="utf-8") as arquivo:
                        arquivo.write(f"{str(time.ctime())}, {site}, normal\n")
            return siteTexto
@app.route ("/broqueado", methods=['POST', 'GET'])
def bloqueio():
    return render_template('saida.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

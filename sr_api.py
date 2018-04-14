# -*- coding: utf-8 -*-
#
# Questo è un prototipo di API REST per il servizio di interrogazione
# del database dei documenti smarriti o rubati
#
# L'API sarà invocabile sull'endpoint http://127.0.0.1:5000/<documento>
#
# Per installare le dipendenze lanciare questo comando
#
#    pip -r requirements.txt
#
# Alla partenza questo codice legge un elenco di documenti smarriti o rubati 
# dai file documents.csv.bz2 che si può generare con sr_genera.py

from flask import Flask, abort
from flask_restful import Resource, Api
from bz2 import BZ2File
import csv
import sys
import logging

app = Flask(__name__)
api = Api(app)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

lista = set()


class RubatiSmarriti(Resource):
    def get(self, codice_documento):
        if codice_documento in lista:
            return {codice_documento: True}
        abort(404)

api.add_resource(RubatiSmarriti, '/<string:codice_documento>')

def carica():
    filename = 'documents.csv.bz2'
    try:
        fp = BZ2File(filename)
    except IOError, e:
        print 'Prima dei creare il file %s usando sr_generate.py' % filename
        sys.exit(1)
    print 'Carico i codici dei documenti....'
    c = csv.reader(fp)
    for line in c:
        lista.add(line[0])

if __name__ == '__main__':
    carica()
    print 'Pronto per rispondere alle richieste.'
    app.run()

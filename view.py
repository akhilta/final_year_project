from django.shortcuts import render
from symptom_checker.forms import InputForm
from django.http import HttpResponse
from neo4j import GraphDatabase
g=GraphDatabase.driver("bolt://localhost:11002", auth=("neo4j", "123456"))
session=g.session()
# Create your views here

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            res = cd['disease']
            ot=session.run("MATCH (node1:Subject)--(node2) RETURN node1,node2")
            li=ot.values()
            return HttpResponse("your disease is "+res+"---"+li[0][0]['Name'])
        else:
            return HttpResponse(form.errors)
    else:
        return HttpResponse("Error")

from django.db import models
from django.http.response import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
import json 
from .models import Parser
def create(request):
      if request.method == 'POST':
        parser = Parser()
        url = request.POST.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        counts_tag_h = []
        for find_elem in ['h1' , 'h2' , 'h3']:
            results = soup.find_all(find_elem)
            count_simple_tag_h = 0
            for res in results:
                count_simple_tag_h+=1
            counts_tag_h.append(count_simple_tag_h)
        refs = []
        results = soup.find_all('a')
        for res in results:
                refs.append(res.text)
        simple_dict = {'page_id' : len(Parser.objects.all()) + 1 , 'h1' : counts_tag_h[0],  'h2' : counts_tag_h[1] , 'h3':counts_tag_h[2] , 'a' : refs}
        simple_json = json.dumps(simple_dict)
        parser.json_res = simple_json
        parser.save()
        return HttpResponse('<h1> Success </h1>')
def get_by_id(request , id):
    res = get_object_or_404(Parser, id_parse_page=id)
    print('result ' , request.read())
    return render(request , 'show.html' , {'json' : res.json_res})
def show_form(request):
    return render(request , 'form.html' , {})
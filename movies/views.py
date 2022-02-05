import mimetypes
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies
from . import utilis

# Create your views here.

# home view
def index(request):
    return render(request,'base.html')

# search view
def SearchMovies(request):
    if request.method == 'POST':

        searchparams = request.POST
        parmas = {}
        searchresult = []
        result = None

        if searchparams['overview'] != '':
            if result == None:
                 result = Movies.objects.filter(overview__icontains=searchparams['overview'])
            else:
                 result = result.filter(overview__icontains=searchparams['overview'])

        if searchparams['number'] != '':
            if not result:
                 result = Movies.objects.filter(number=searchparams['number'])
            else:
                 result = result.filter(number=searchparams['number'])
            
        if searchparams['title'] != '':
            if not result:
                 result = Movies.objects.filter(title__icontains=searchparams['title'])
            else:
                 result = result.filter(title__icontains=searchparams['title'])

        if searchparams['popularity'] != '':
            if not result:
                 result = Movies.objects.filter(popularity=searchparams['popularity'])
            else:
                 result = result.filter(popularity=searchparams['popularity'])
            
        if searchparams['release_date'] != '':
            if result == None:
                 result = Movies.objects.filter(release_date=searchparams['release_date'])
            else:
                 result = result.filter(release_date=searchparams['release_date'])

        if searchparams['vote_num'] != '':
            if not result:
                 result = Movies.objects.filter(vote_num=searchparams['vote_num'])
            else:
                 result = result.filter(vote_num=searchparams['vote_num'])
            
        if searchparams['vote_average'] != '':
            if not result:
                 result = Movies.objects.filter(vote_average=searchparams['vote_average'])
            else:
                 result = result.filter(vote_average=searchparams['vote_average'])

        if result :
            if result.count() > 0:
                for movie in result:
                   searchresult.append(movie)
        
        for key,value in searchparams.items():
            if value != '':
                parmas[key]=value 
        parmas.pop('csrfmiddlewaretoken')

        return render(request,'movies/search_item.html',context={'movies':result,'params':parmas})
    else:
        return render(request,'base.html')

# Parse view
def ParseToJson(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.name.endswith('.csv') :
             data  = utilis.CsvToJson(file)
        elif file.name.endswith('.xlsx'):
             data  = utilis.XlsxToJson(file)
        elif file.name.endswith('.xml'):
             data  = utilis.XmlToJson(file) 
        else:
            return render(request,'base.html',context={'parseerror':'this file type is not supported'})

       # Open the file for reading content
        filepath = utilis.writetofile(file,data)
        path = open(filepath, 'r')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % file.name.split('.')[0]+'.json'
        return response        
    else: 
        return render(request,'base.html')



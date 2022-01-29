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
        movies = []
        searchresult = []
        paramsnum = 0
        if len(searchparams['overview']) >0:
             paramsnum +=1
             result = Movies.objects.filter(overview__icontains=searchparams['overview'])
             if result.count() > 0 :
                 for movie in result:
                     searchresult.append(movie)

        if searchparams['number'] != '':
            paramsnum +=1
            result = Movies.objects.filter(number=searchparams['number'])
            if result.count() > 0 :
                for movie in result:
                    searchresult.append(movie)
        if len(searchparams['title']) > 0:
            paramsnum +=1
            result = Movies.objects.filter(title__icontains=searchparams['title'])
            if result.count() > 0 :
                for movie in result:
                    searchresult.append(movie)
        if searchparams['popularity'] != '':
            paramsnum +=1
            result = Movies.objects.filter(popularity=searchparams['popularity'])
            if result.count() > 0 :
                for movie in result:
                   searchresult.append(movie)
        if searchparams['release_date'] != '':
            paramsnum +=1
            result = Movies.objects.filter(release_date=searchparams['release_date'])
            if result.count() > 0 :
                for movie in result:
                    searchresult.append(movie)
    
        if searchparams['vote_num'] != '':
            paramsnum +=1
            result = Movies.objects.filter(vote_num=searchparams['vote_num'])
            if result.count() > 0 :
                for movie in result:
                     searchresult.append(movie)
    
        if searchparams['vote_average'] != '':
            paramsnum +=1
            result = Movies.objects.filter(vote_average=searchparams['vote_average'])
            if result.count() > 0 :
                for movie in result:
                    searchresult.append(movie)

        for movie in searchresult:
             if searchresult.count(movie) == paramsnum:
                 if movie not in movies:
                     movies.append(movie)
        return render(request,'movies/search_item.html',context={'movies':movies})
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



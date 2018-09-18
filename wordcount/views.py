from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            # Increase
            worddict[word] += 1
        else:
            # Add to the dictionnary
            worddict[word] = 1
    sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedword)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict': sortedword})
from django.http import HttpResponse
from django.shortcuts import render
import operator
def Homepage(request):
    return render(request,'template.html')

def about(request):
    return render(request,'about_Details.html')    

def count(request):
    data=request.GET['text']
    word_list=data.split()
    Listlen=len(word_list)
    worddictionary={ }
    i=0
    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedlist=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)    
    return render(request,'count.html',{'text':data,'length':Listlen,'worddictionary':sortedlist}) 
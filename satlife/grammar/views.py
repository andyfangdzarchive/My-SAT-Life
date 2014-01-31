from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.utils import simplejson

from grammar.models import Grammar,Choice

import collections

def index(request):
    return render(request, 'grammar/base.html')

def list(request):
    grammar_list = Grammar.objects.all().order_by('-pub_date')
    context = {'grammar_list': grammar_list}
    return render(request, 'grammar/list.html', context)

def ajaxList(request):
    grammar_list = Grammar.objects.all().order_by('-pub_date')
    results={}
    next = Grammar.objects.order_by('?')[0]
    shuffle=next.pk
    nlist=[]
    plist=[]
    count=0
    for item in grammar_list:
        nlist.append(item.nick)
        plist.append(item.pk)
        count+=1
    results['count']=count
    results['nicks']=nlist
    results['pks']=plist
    results['shuffle']=shuffle
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

def ajaxDetail(request, grammar_id):
    return render(request, 'grammar/base.html', {'id':grammar_id})

def detail(request, grammar_id):
    grammar_sel = get_object_or_404(Grammar, pk=grammar_id)
    pk=grammar_sel.pk
    return render(request, 'grammar/view.html', {'id':pk})

def detailJSON(request, grammar_id):
    results = {'success':False}
    grammar_sel = get_object_or_404(Grammar, pk=grammar_id)
    choices = grammar_sel.choice_set.all()
    alist=[]
    clist=[]
    ilist=[]
    chara='A'
    for choice in choices:
      alist.append(chara)
      clist.append(choice.choice_text)
      ilist.append(choice.pk)
      chara=chr(ord(chara) + 1)
    next = Grammar.objects.order_by('?')[0]
    while next == grammar_sel:
      next = Grammar.objects.order_by('?')[0]
    results['next']=next.pk
    results['nickname'] = grammar_sel.nick
    results['question_1st'] = grammar_sel.question_1st
    results['question_2nd'] = grammar_sel.question_2nd
    results['labels'] = alist
    results['choices'] = clist
    results['choices_id'] = ilist

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

def choose(request,pk):
    results = {'success':False}
    answer = False;
    choice = get_object_or_404(Choice, pk=pk)
    if choice.is_correct:
        answer = True
    results['answer'] = answer
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
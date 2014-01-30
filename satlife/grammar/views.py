from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.utils import simplejson

from grammar.models import Grammar,Choice

import collections

def index(request):
    grammar_list = Grammar.objects.all().order_by('-pub_date')
    context = {'grammar_list': grammar_list}
    return render(request, 'grammar/index.html', context)

def list(request):
    grammar_list = Grammar.objects.all().order_by('-pub_date')
    context = {'grammar_list': grammar_list}
    return render(request, 'grammar/list.html', context)

def detail(request, grammar_id):
    grammar_sel = get_object_or_404(Grammar, pk=grammar_id)
    choices = grammar_sel.choice_set.all()
    clist={}
    chara='A';
    for choice in choices:
      clist[chara]=choice
      chara=chr(ord(chara) + 1)
    clist=collections.OrderedDict(sorted(clist.items()))
    next = Grammar.objects.order_by('?')[0]
    while next == grammar_sel:
      next = Grammar.objects.order_by('?')[0]
    context = {
    'grammar': grammar_sel,
    'choices': clist,
    'first': choices[0],
    'next' : next,
    }
    return render(request, 'grammar/detail.html', context)

def choose(request):
    results = {'success':False}
    answer = False;
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk'):
            pk = int(GET[u'pk'])
            choice = Choice.objects.get(pk=pk)
            if choice.is_correct:
                answer = True
            results = {'success':True,'answer':answer}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
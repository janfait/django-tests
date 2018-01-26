# Create your views here.
# Views are actually methods that get called from urls' views parameter. Basically on a match, a view is requested and this view
# executes a method.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

#if we want to use any of the DB models we defined previously, we have to import it
from .models import Question, Choice

#method will show the latest 5 questions
#output will join the question text by a comma+space

#This can be rewritten by the shortcut below
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #define the template, load it from the templates directory - needs a special subdirectory called polls too. annoying
#     template = loader.get_template('polls/index.html')
#     #pass the context variable to the template
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#This can be rewritten by the shortcut below
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

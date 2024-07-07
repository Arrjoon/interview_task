from django.shortcuts import render,get_object_or_404,HttpResponse
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Poll,Choice,Vote
# Create your views here.


def detail(request,poll_id):
    return render(request,'index.html')

def home(request):
    # poll = get_object_or_404(Poll, pk=poll_id)
    # poll_set = Poll.objects.all()
    return render(request, 'home.html')

def Poll_Qestion(request,id):
    poll = get_object_or_404(Poll, pk=id)
    return render(request, 'Poll_question.html', {'poll': poll})


# def vote(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     print(poll)
#     try:
#         selected_choice = poll.choice_set.get(pk=request.POST['choice'])
#         print(selected_choice)
#     # except (KeyError, Choice.DoesNotExist):
#     except Exception as e:
#         # return render(request, 'polls/detail.html', {
#         #     'poll': poll,
#         #     'error_message': "You didn't select a choice.",
#         # })
#         print(e)
#         return HttpResponse("polls doesn't find")
#     else:
#         if Vote.objects.filter(user=request.user, poll=poll).exists():
#             return render(request, 'detail.html', {
#                 'poll': poll,
#                 'error_message': "You have already voted in this poll.",
#             })
#         Vote.objects.create(user=request.user, poll=poll, choice=selected_choice)
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect('/home')
    

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

# Ensure the request method is POST
    if request.method == 'POST':
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except Exception as e:
            return HttpResponse(e) 
        else:
            # Check if the user has already voted
            if Vote.objects.filter(user=request.user, poll=poll).exists():
                return HttpResponse("you already voted")
            # Create a new vote and update the selected choice's vote count
            Vote.objects.create(user=request.user, poll=poll, choice=selected_choice)
            selected_choice.votes += 1
            selected_choice.save()
            return render(request,'detail.html')
    else:
        return HttpResponse("Invalid request method.")

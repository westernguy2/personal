from django.shortcuts import render
import operator

# Create your views here.
def cs61a(request):
	return render(request, 'worksheets/61a.html')

def which_worksheets(request):
	#topic = request.GET['topic']
	return render(request, 'worksheets/pick_topic.html')

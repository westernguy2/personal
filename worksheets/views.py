from django.shortcuts import render
import operator
from .models import Worksheet

# Create your views here.
def cs61a(request):
	topic = request.GET['topic']
	all_worksheets = list(Worksheet.objects.filter())
	relevant_worksheets = []
	for w in all_worksheets:
		if getattr(w, topic) and not w.isSolution:
			with_solution = []
			for i in all_worksheets:
				if i.worksheetNumber == w.worksheetNumber:
					with_solution.append(i)
			with_solution.sort(key = lambda x: x.isSolution)
			relevant_worksheets.append(with_solution)
	print(relevant_worksheets)
	return render(request, 'worksheets/61a.html', {'wkshts':relevant_worksheets})

def which_worksheets(request):
	return render(request, 'worksheets/pick_topic.html')

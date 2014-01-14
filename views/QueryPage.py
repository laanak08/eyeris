#!/usr/bin/python

from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

class QueryForm(forms.Form):
	message = forms.CharField()

def render_query_page(request):
	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():
			# process form
			message = form.cleaned_data['message']
			return render_to_response('ResultsPage.html', {'message' : message})
	else:
		form = QueryForm()

	return render_to_response('QueryPage.html', 
		{'form' : form }, 
		context_instance=RequestContext(request) )
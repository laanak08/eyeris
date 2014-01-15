#!/usr/bin/python

from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

class QueryForm(forms.Form):
	dimeName = forms.CharField(required=False)
	serverName = forms.CharField(required=False)
	dimeName = forms.CharField(required=False)
	app = forms.CharField(required=False)
	hcd = forms.CharField(required=False)
	transId = forms.CharField(required=False)
	webId = forms.CharField(required=False)
	action = forms.CharField(required=False)

def render_query_page(request):
	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():
			# process form
			dn = form.cleaned_data['dimeName']
			return render_to_response('ResultsPage.html', {'message' : dn})
	else:
		form = QueryForm()

	return render_to_response('QueryPage.html', 
		{'form' : form }, 
		context_instance=RequestContext(request) )
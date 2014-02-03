#!/usr/bin/python

from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from datetime import datetime
from pymongo import MongoClient

class QueryForm(forms.Form):
	startDateTime = forms.DateField(required=False)
	startDateTime.widget.attrs = {'class' : 'hasDatepicker'}

	endDateTime = forms.DateField(required=False)
	endDateTime.widget.attrs = {'class' : 'hasDatepicker'}

	application = forms.CharField(required=False)
	server = forms.CharField(required=False)
	hierarchCode = forms.CharField(required=False)
	transId = forms.CharField(required=False)
	webId = forms.CharField(required=False)
	action = forms.CharField(required=False)

def render_query_page(request):
	alerts = "This is a prototype only on a select set of servers. Records are kept for 24 hours only"
	updates = ("All identified LexisAdvance servers are now loading."
			"Begin and end time are displaying as columns, as well as response time in seconds."
			"The Server filter is set to auto-complete with the servers we have.")

	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():
			query = form
			queryResults = process_form(form.cleaned_data)
			return render_to_response( 'ResultsPage.html', {'query' : query, 'queryResults' : queryResults } )
	else:
		form = QueryForm()

	return render_to_response( 'QueryPage.html', 
		{'form' : form, 'alerts' : alerts, 'updates': updates }, 
		context_instance=RequestContext(request) )

def process_form(form):
	mclient = MongoClient('lab7983',27019)
	db = mclient['testSmapi']
	records = db['lexisadvance']

	return records.find(form,limit=10,fields={'_id': False})


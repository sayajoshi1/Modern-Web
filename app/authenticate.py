from django.shortcuts import redirect,render
from app.models import User
from django.contrib import messages
from django.db.models import Q

class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				User.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
				return function(request)
			except:
				request.session.flush()
				messages.warning(request,"Please login... ")
				return redirect('/login') 
		return wrap

	def valid_user_with_id(function):
		def wrap_with_id(request,id):
			try:
				User.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
				return function(request,id)
			except:
				
				request.session.flush()
				messages.warning(request,"Please login... ")
				return redirect('/login') 
		return wrap_with_id
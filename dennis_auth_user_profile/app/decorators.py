from django.shortcuts import redirect, HttpResponse


def login_check(func):
	def wraper(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home_ep')
		else: 
			return func(request, *args, **kwargs)
	return wraper



def allowed_group(allowed=[]):
	def decorator(view_func):
		def wrapper(request, *args, **kwargs):
			user_group_name = None
			if request.user.groups.exists():
				user_group_name = request.user.groups.all()[0].name
			
			if user_group_name in allowed:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper
	return decorator


def allowed_group2(allowed=[]):
	def decorator(view_func):
		def wrapper(request, *args, **kwargs):
			user_group_names = []
			if request.user.groups.exists():
				user_group_names = request.user.groups.all()
    
			for item in user_group_names:
				if item.name in allowed:
					return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper
	return decorator
				
from django.shortcuts import render,redirect
from app.models import User
from app.forms import UserForm
from django.http import HttpResponse, JsonResponse
from app.authenticate import Authenticate
from app.models import Bookings
from app.models import Packages
from app.forms import PackagesForm
from app.forms import BookingsForm

from django.contrib import messages
from django.template.loader import render_to_string
from django.db.models import Q

#----------------------------------------------------- views for Backend-----------------------------------------------------------------------------------------
def layout(request):
	return render(request,'layout.html') 

def entry( request):
	try:
		User.objects.get(email=request.POST['email'])
	except:
		messages.warning(request,"USER NOT FOUND")
		return redirect("/login")
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect("/admin")

# @Authenticate.valid_user
def login(request):
	if 'email' not in request.session:
		return render(request,'login.html')
	else:
		return redirect('/admin')
		

def logout(request):
	request.session.flush()
	return redirect('/login')


#---------------------------------------------------views for Dashboard--------------------------------------------------------------------
@Authenticate.valid_user
def dashboard(request):
	u=len(User.objects.all())
	p=len(Packages.objects.all())
	b=len(Bookings.objects.all())
	return render(request,'dashboard.html',{'u':u,'p':p,'b':b})

	
#------------------------------------------------------views for users--------------------------------------------------------------------------
@Authenticate.valid_user
def usersIndex(request):
	page=1
	if request.method=="POST":
		limit=5
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		users =User.objects.raw("select * from user limit 5 offset %s",[offset])

	else:
		users =User.objects.raw("select * from user limit 5 offset 0")
	count=User.objects.count()
	return render(request,"users/index.html",{'users':users,'counts':count,'page':page})

@Authenticate.valid_user 
def usersCreate(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect('/users')
	form=UserForm()
	return render(request,'users/create.html',{'form':form})

@Authenticate.valid_user_with_id
def usersEdit(request,id):
	user=User.objects.get(id=id)
	return render(request,'users/edit.html',{'user':user})

@Authenticate.valid_user_with_id
def usersUpdate(request,id):
	user=User.objects.get(id=id)
	form=UserForm(request.POST,request.FILES,instance=user)
	form.save()
	return redirect('/users')

@Authenticate.valid_user_with_id
def usersDelete(request,id):
	user=User.objects.get(id=id)
	if(user.image!='img.jpg'):
		user.image.delete()
	user.delete()
	return redirect('/users')

def search(request):
	users=User.objects.filter(email__icontains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)


#------------------------------------------------------views for packages------------------------------------------------------------------------------
@Authenticate.valid_user
def package(request):
	return render(request,'package.html')

def packagesIndex(request):
	page=1
	if request.method=="POST":
		limit=3
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		packages =Packages.objects.raw("select * from packages limit 3 offset %s",[offset])

	else:
		packages =Packages.objects.raw("select * from packages limit 3 offset 0")
	count=Packages.objects.count()
	return render(request,"packages/index.html",{'packages':packages,'counts':count,'page':page})


def packagesearch(request):
	packages=Packages.objects.filter(name__icontains=request.GET['search']).values()	
	return JsonResponse(list(packages),safe=False)
   

@Authenticate.valid_user
def packagesCreate(request):
	if request.method=="POST":
		form=PackagesForm(request.POST,request.FILES)
		form.save()
		return redirect('/packages')
	form=PackagesForm()
	return render(request,'packages/create.html',{'form':form})

@Authenticate.valid_user_with_id
def packagesEdit(request,id):
	packages=Packages.objects.get(id=id)
	return render(request,'packages/edit.html',{'packages':packages})

@Authenticate.valid_user_with_id
def packagesUpdate(request,id):
	packages=Packages.objects.get(id=id)
	form=PackagesForm(request.POST,request.FILES,instance=packages)
	form.save()
	return redirect('/packages')


@Authenticate.valid_user_with_id
def packagesDelete(request,id):
	packages=Packages.objects.get(id=id)
	if(packages.image!='img.jpg'):
		packages.image.delete()
	packages.delete()
	return redirect('/packages')


#-----------------------------------------------------------views for bookings------------------------------------------------------------------------------------------------
@Authenticate.valid_user
def bookingsIndex(request):
	page=1
	if request.method=="POST":
		limit=5
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		bookings =Bookings.objects.raw("select * from bookings limit 5 offset %s",[offset])

	else:
		bookings =Bookings.objects.raw("select * from bookings limit 5 offset 0")
	count=Bookings.objects.count()
	return render(request,"bookings/index.html",{'bookings':bookings,'counts':count,'page':page})


# @Authenticate.valid_user
def bookingsCreate(request):
	if request.method=="POST":
		form=BookingsForm(request.POST,request.FILES)
		form.save()
	form=BookingsForm()
	messages.success(request,"Booking Done. Contact us for more details!")
	return render(request,'frontend/booking.html',{'bookings':form})

def bookingsearch(request):
	bookings=Bookings.objects.filter(name__icontains=request.GET['search'])
	html=render_to_string('bookings/search.html',{'bookings':bookings})
	return JsonResponse({'data':html})

@Authenticate.valid_user_with_id
def bookingsDelete(request,id):
	bookings=Bookings.objects.get(id=id)
	bookings.delete()
	return redirect('/bookings')

@Authenticate.valid_user_with_id
def bookingsEdit(request,id):
	bookings=Bookings.objects.get(id=id)
	packages =Packages.objects.all()
	return render(request,'bookings/edit.html',{'bookings':bookings,'packages':packages})

@Authenticate.valid_user_with_id
def bookingsUpdate(request,id):
	bookings=Bookings.objects.get(id=id)
	form=BookingsForm(request.POST,request.FILES,instance=bookings)
	form.save()
	return redirect('/bookings')
   

#------------------------------------------------------views for frontend-----------------------------------------------------------------
def home(request):
	packages =Packages.objects.all()[:6]
	request.session.flush()
	return render(request,'frontend/index.html',{'packages':packages})

def fPackage(request):
	packages =Packages.objects.all()
	request.session.flush()
	return render(request,'frontend/package.html',{'packages':packages})

def fContact(request):
	return render(request,'frontend/contact.html')

def fAboutus(request):
	return render(request,'frontend/aboutus.html')

def fBooking(request):
	packages=Packages.objects.all()
	return render(request,'frontend/booking.html',{'packages':packages})

#---------------------------------------------------------for single package------------------------------------------------------------------
def pkgView(request,id):
	packages=Packages.objects.filter(id=id)
	return render(request,'frontend/single-pkg.html',{'packages':packages})




# Create your views here.


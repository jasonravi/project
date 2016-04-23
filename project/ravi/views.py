from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def name_of_permission(request,user_id):
	context = {}
	permission_name = []
	print 'test34'
	try:
		if request.method == 'GET':
			try:
				user = User.objects.get(id=user_id)
				roles_id = user.role_set.all()
				for role in roles_id:
					for permission in role.permission_set.all():
						permission_name.append(permission.name)
				context['message'] = 'successfully'
				context['status'] = 'success'
				context['permission_name'] = permission_name
				context['status_code'] = 200
			except Exception as e:
				print str(e)
				context['message'] = '%s user does not exist'%(user_id)
				context['status'] = 'failed'
				context['permission_name'] = permission_name
				context['status_code'] = 500
		else:
			context['message'] = 'request method is not valid'
			context['status'] = 'failed'
			context['permission_name'] = permission_name
			context['status_code'] = 500
	except Exception as e:
		pass
	return HttpResponse(json.dumps(context),content_type='application/json')

@csrf_exempt
def check_user_permission(request):
	context={}
	print 'test34'
	if request.method=='GET':
		try:
			try:
			  userid=request.GET.get('userid')
			  permission_id=request.GET.get('permissionid')
			except:
				context['status']=False
				context['message']='Input error'
				context['status_code']=300
				return HttpResponse(json.dumps(context),content_type='application/json')
			user=User.objects.get(id=userid)
			roles_id=user.role_set.all()
			for role in roles_id:
				try:
				  permission=role.permission_set.all()
				  permission.get(id=permission_id)
				  context['status_code']=200
				  context['status']=True
				  context['message']='successfully'
				  return HttpResponse(json.dumps(context),content_type='application/json')
				except:
				  context['status_code']=200
				  context['status']=False
				  context['message']='successfully'
			return HttpResponse(json.dumps(context),content_type='application/json')
		except:
			context['status_code']=300
			context['status']=False
			context['message']='Given user does not exist'
			return HttpResponse(json.dumps(context),content_type='application/json')
	else:
		context['status_code']=300
		context['status']=False
		context['message']='Not proper method'
		return HttpResponse(json.dumps(context),content_type='application/json')
		
@csrf_exempt
def modify_permission(request,role_id):
	context = {}
	if request.method == 'POST':
		try:
			post_param = request.POST.get('post_param')
			post_param = json.loads(post_param)
			new_permissions = []
			role = Role.objects.get(id=role_id)
			permissions_id = roleid.permission_set.all()
			for permission_name in post_param['permissions']:
				try:
					permission = Permission.objects.filter(name=permission_name).filter(role_id=role)
					if not permission.count():
						permission = Permission()
						permission.name = permission_name
						permission.created_on = datetime.datetime.now()
						permission.role_id = role
						permission.save()
				except:
					pass
			context['status_code']=200
			context['status']='success'
			return HttpResponse(json.dumps(context),content_type='application/json')
		except:
			context['status_code']=300
			context['status']='failed'
			context['message']='Given role does not exist'
			return HttpResponse(json.dumps(context),content_type='application/json')

@csrf_exempt
def delete_permission(request,permission_id):
	context={}
	if request.method == "DELETE":
		try:
			permission = Permission.objects.get(id=permission_id)
			permission.delete()
			context['status_code']=200
			context['status']='success'
			context['message']='successfully deleted'
			return HttpResponse(json.dumps(context),content_type='application/json')
		except:
			context['status_code']=300
			context['status']='failed'
			context['message']='Given permission does not exist'
			return HttpResponse(json.dumps(context),content_type='application/json')
	else:
		context['status_code']=400
		context['message']='Wrong method'
		return  HttpResponse(json.dumps(context),content_type='application/json')
   







		

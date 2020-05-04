from .models import MyUser
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError


def create_user(request):
    status = 201
    try:
        user = MyUser(name=request['name'], year=request['year'])
        user.save()
    except KeyError:
        json_obj = {
            'error': "incorrect parameter"
        }
        status = 400
    except IntegrityError:
        json_obj = {
            'error': "user with this name already exist"
        }
        status = 400
    else:
        json_obj = {
            'status': 'create',
            'id': user.id,
            'name': user.name,
            'year': user.year,
            'created': user.created.isoformat(),
            'updated': user.updated.isoformat()
        }

    return JsonResponse(data=json_obj, safe=False, status=status)


def get_user(request):
    status = 200
    try:
        allowed_parameters = {key: value[0] for key, value in dict(request).items() if key in ['name', 'year']}
        user = MyUser.objects.all().filter(**allowed_parameters)
        if not user:
            raise MyUser.DoesNotExist

    except KeyError:
        json_obj = {
            'error': "query string is empty"
        }
        status = 400
    except MyUser.DoesNotExist:
        json_obj = {
            'error': "user with this parameters doesn't exist"
        }
        status = 400
    else:
        json_obj = [
            {
                'id': values.id,
                'name': values.name,
                'year': values.year,
                'created': values.created.isoformat(),
                'updated': values.updated.isoformat()
            }
            for values in user
        ]

    return JsonResponse(data=json_obj, safe=False, status=status)


def delete_user(request):
    status = 200
    try:
        allowed_parameters = {key: value[0] for key, value in dict(request).items() if key in ['name', 'year']}
        user = MyUser.objects.all().filter(**allowed_parameters)
        if not allowed_parameters:
            raise ValueError
        if not user:
            raise MyUser.DoesNotExist
    except ValueError:
        json_obj = {
            'warning': 'use this query parameters:name and year for delete method'
        }
    except KeyError:
        json_obj = {
            'error': "incorrect parameter"
        }
        status = 400
    except MyUser.DoesNotExist:
        json_obj = {
            'error': "user with this parameters doesn't exist"
        }
        status = 400
    else:
        json_obj = [
            {
                'status': 'delete',
                'id': values.id,
                'name': values.name,
                'year': values.year,
                'created': values.created.isoformat(),
                'updated': values.updated.isoformat()
            }
            for values in user
        ]
        user.delete()

    return JsonResponse(data=json_obj, safe=False, status=status)


def updated_user(request):
    status = 200
    try:
        allowed_parameters = {key: value[0] for key, value in dict(request).items() if key in ['name', 'year']}
        updated_count = MyUser.objects.all().filter(id=request['id']).update(**allowed_parameters)
        if not updated_count:
            raise MyUser.DoesNotExist
    except KeyError:
        json_obj = {
            'error': "incorrect parameter"
        }
        status = 400
    except MyUser.DoesNotExist:
        return create_user(request)
    else:
        user = MyUser.objects.all().get(id=request['id'])
        json_obj = {
            'status': 'updated',
            'id': user.id,
            'name': user.name,
            'year': user.year,
            'created': user.created.isoformat(),
            'updated': user.updated.isoformat()
        }

    return JsonResponse(data=json_obj, safe=False, status=status)


def last_modified_user(request):
    response = HttpResponse()
    try:
        user = MyUser.objects.all().get(id=request['id'])
        if not user:
            raise MyUser.DoesNotExist

    except KeyError:
        response.status_code = 400

    except MyUser.DoesNotExist:
        response.status_code = 400

    else:
        response.status_code = 200
        response['Last-Modified'] = user.updated
    finally:
        return response

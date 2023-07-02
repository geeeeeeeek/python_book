# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.auth.authentication import TokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Address
from myapp.serializers import AddressSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        userId = request.GET.get('userId', -1)

        if userId != -1:
            addresses = Address.objects.filter(user=userId).order_by('-create_time')
            serializer = AddressSerializer(addresses, many=True)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='userId不能为空')


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def create(request):

    address_content = request.POST.get('desc', None)
    user = request.POST.get('user', None)
    default = request.POST.get('default', False)

    if address_content is None or user is None:
        return APIResponse(code=1, msg='不能为空')

    if default:
        # 其他置为false
        Address.objects.filter(user=user).update(default=False)

    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def update(request):

    try:
        pk = request.GET.get('id', -1)
        addresses = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    user = request.data['user']
    default = request.data['default']

    if default:
        # 其他置为false
        Address.objects.filter(user=user).update(default=False)

    serializer = AddressSerializer(addresses, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def delete(request):

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Address.objects.filter(id__in=ids_arr).delete()
    except Address.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')

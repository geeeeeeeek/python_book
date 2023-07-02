# Create your views here.
from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import Notice
from myapp.serializers import NoticeSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        notices = Notice.objects.all().order_by('-create_time')
        serializer = NoticeSerializer(notices, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


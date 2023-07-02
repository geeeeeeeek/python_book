# Create your views here.
import datetime

from rest_framework.decorators import api_view, authentication_classes

from myapp.auth.authentication import TokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Borrow, Book
from myapp.serializers import BorrowSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        userId = request.GET.get('userId', -1)
        borrowStatus = request.GET.get('borrowStatus', '')

        borrows = Borrow.objects.all().filter(user=userId).filter(status__contains=borrowStatus).order_by('-borrow_time')
        serializer = BorrowSerializer(borrows, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def create(request):
    """
    创建借书
    """

    data = request.data.copy()
    if data['user'] is None or data['book'] is None:
        return APIResponse(code=1, msg='参数错误')

    book = Book.objects.get(pk=data['book'])
    if book.repertory <= 0:
        return APIResponse(code=1, msg='库存不足')

    borrows = Borrow.objects.filter(book=data['book']).filter(user=data['user']).filter(status='1')
    if len(borrows) > 0:
        return APIResponse(code=1, msg='您已经借过该书了')

    create_time = datetime.datetime.now()

    data['status'] = '1'
    data['delayed'] = False
    data['create_time'] = create_time
    data['expect_time'] = create_time + datetime.timedelta(days=60)
    serializer = BorrowSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # 减库存
        book.repertory = book.repertory - 1
        book.save()

        return APIResponse(code=0, msg='借书成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='借书失败')


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def return_book(request):
    """
    还书
    """
    try:
        pk = request.GET.get('id', -1)
        borrow = Borrow.objects.get(pk=pk)
    except Borrow.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    data = {
        'status': 2
    }
    serializer = BorrowSerializer(borrow, data=data)
    if serializer.is_valid():
        serializer.save()
        # 加库存
        bookId = request.data['book']
        book = Book.objects.get(pk=bookId)
        book.repertory = book.repertory + 1
        book.save()

        # 加积分
        borrow.user.score = borrow.user.score + 1
        borrow.user.save()

        return APIResponse(code=0, msg='还书成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def delay(request):

    try:
        pk = request.GET.get('id', -1)
        borrow = Borrow.objects.get(pk=pk)
    except Borrow.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    if borrow.delayed:
        return APIResponse(code=1, msg='已超最大延期次数')
    else:
        data = {
            "delayed": True,
            "expect_time": borrow.expect_time + datetime.timedelta(days=30)
        }
        serializer = BorrowSerializer(borrow, data=data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(code=0, msg='延期成功', data=serializer.data)
        else:
            print(serializer.errors)
            return APIResponse(code=1, msg='延期失败')

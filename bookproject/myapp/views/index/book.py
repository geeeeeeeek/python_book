# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.handler import APIResponse
from myapp.models import Classification, Book, Tag, User
from myapp.serializers import BookSerializer, ClassificationSerializer, ListBookSerializer, DetailBookSerializer
from myapp.utils import dict_fetchall


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        sort = request.GET.get("sort", 'recent')

        # 排序方式
        order = '-create_time'
        if sort == 'recent':
            order = '-create_time'
        elif sort == 'hot' or sort == 'recommend':
            order = '-pv'

        if keyword:
            books = Book.objects.filter(title__contains=keyword).order_by(order)
        elif c and int(c) > -1:
            ids = [c]
            classifications = Classification.objects.filter(pid=c)
            serializer = ClassificationSerializer(classifications, many=True)
            subData = serializer.data
            for item in subData:
                # 添加二级分类的id
                ids.append(item['id'])
            print(ids)

            books = Book.objects.filter(classification_id__in=ids).order_by(order)

        elif tag:
            tag = Tag.objects.get(id=tag)
            print(tag)
            books = tag.book_set.all().order_by(order)
        else:
            books = Book.objects.all().defer('wish').order_by(order)

        serializer = ListBookSerializer(books, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def increaseWishCount(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
        # wish_count加1
        book.wish_count = book.wish_count + 1
        book.save()
    except Book.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = BookSerializer(book)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)

@api_view(['POST'])
def increaseRecommendCount(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
        # recommend_count加1
        book.recommend_count = book.recommend_count + 1
        book.save()
    except Book.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = BookSerializer(book)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)

@api_view(['POST'])
def addWishUser(request):
    try:
        username = request.GET.get('username', None)
        bookId = request.GET.get('bookId', None)

        if username and bookId:
            user = User.objects.get(username=username)
            book = Book.objects.get(pk=bookId)

            if user not in book.wish.all():
                book.wish.add(user)
                book.wish_count += 1
                book.save()

    except Book.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    serializer = BookSerializer(book)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)

@api_view(['POST'])
def removeWishUser(request):
    try:
        username = request.GET.get('username', None)
        bookId = request.GET.get('bookId', None)

        if username and bookId:
            user = User.objects.get(username=username)
            book = Book.objects.get(pk=bookId)

            if user in book.wish.all():
                book.wish.remove(user)
                book.wish_count -= 1
                book.save()

    except Book.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    return APIResponse(code=0, msg='操作成功')

@api_view(['GET'])
def getWishBookList(request):
    try:
        username = request.GET.get('username', None)
        if username:
            user = User.objects.get(username=username)
            books = user.wish_books.all()
            serializer = ListBookSerializer(books, many=True)
            return APIResponse(code=0, msg='操作成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='username不能为空')

    except Exception as e:
        utils.log_error(request, '操作失败' + str(e))
        return APIResponse(code=1, msg='获取心愿单失败')


@api_view(['POST'])
def addCollectUser(request):
    try:
        username = request.GET.get('username', None)
        bookId = request.GET.get('bookId', None)

        if username and bookId:
            user = User.objects.get(username=username)
            book = Book.objects.get(pk=bookId)

            if user not in book.collect.all():
                book.collect.add(user)
                book.collect_count += 1
                book.save()

    except Book.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    serializer = DetailBookSerializer(book)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)


@api_view(['POST'])
def removeCollectUser(request):
    try:
        username = request.GET.get('username', None)
        bookId = request.GET.get('bookId', None)

        if username and bookId:
            user = User.objects.get(username=username)
            book = Book.objects.get(pk=bookId)

            if user in book.collect.all():
                book.collect.remove(user)
                book.collect_count -= 1
                book.save()

    except Book.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    return APIResponse(code=0, msg='操作成功')


@api_view(['GET'])
def getCollectBookList(request):
    try:
        username = request.GET.get('username', None)
        if username:
            user = User.objects.get(username=username)
            books = user.collect_books.all()
            serializer = ListBookSerializer(books, many=True)
            return APIResponse(code=0, msg='操作成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='username不能为空')

    except Exception as e:
        utils.log_error(request, '操作失败' + str(e))
        return APIResponse(code=1, msg='获取收藏失败')



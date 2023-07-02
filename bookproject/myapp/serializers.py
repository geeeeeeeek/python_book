from rest_framework import serializers

from myapp.models import Book, Classification, Tag, User, Comment, Record, LoginLog, Borrow, BorrowLog, OpLog, Banner, \
    Ad, Notice, ErrorLog, Address


class BookSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Book
        fields = '__all__'

class DetailBookSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Book
        # 排除多对多字段
        exclude = ('wish', 'collect',)

class UpdateBookSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Book
        # 排除多对多字段
        exclude = ('wish', 'collect',)

class ListBookSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Book
        # 排除字段
        exclude = ('wish', 'collect', 'description',)


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ('password',)


class CommentSerializer(serializers.ModelSerializer):
    comment_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # 额外字段
    title = serializers.ReadOnlyField(source='book.title')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'comment_time', 'like_count', 'book', 'user', 'title', 'username']


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class LoginLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = LoginLog
        fields = '__all__'


class OpLogSerializer(serializers.ModelSerializer):
    re_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = OpLog
        fields = '__all__'


class ErrorLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = ErrorLog
        fields = '__all__'


class BorrowSerializer(serializers.ModelSerializer):
    borrow_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    expect_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    return_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    title = serializers.ReadOnlyField(source='book.title')
    cover = serializers.FileField(source='book.cover', required=False)

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowLog
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Banner
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Notice
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Address
        fields = '__all__'

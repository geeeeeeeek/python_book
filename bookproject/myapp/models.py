from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    ROLE_CHOICES = (
        ('0', '管理员'),
        ('1', '普通用户'),
    )
    STATUS_CHOICES = (
        ('0', '正常'),
        ('1', '封号'),
    )
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/', null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    description = models.TextField(max_length=200, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField(default=0, blank=True, null=True)
    push_email = models.CharField(max_length=40, blank=True, null=True)
    push_switch = models.BooleanField(blank=True, null=True, default=False)
    admin_token = models.CharField(max_length=32, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "b_user"


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_tag"


class Classification(models.Model):
    list_display = ("title", "id")
    id = models.BigAutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True, default=-1)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "b_classification"


class Book(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
    )
    id = models.BigAutoField(primary_key=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_book')
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    original_title = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    translator = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    press = models.CharField(max_length=50, blank=True, null=True)
    page_count = models.IntegerField(default=0)
    price = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateField(null=True)
    online_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    repertory = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    layout = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    pv = models.IntegerField(default=0)
    recommend_count = models.IntegerField(default=0)
    wish = models.ManyToManyField(User, blank=True, related_name="wish_books")
    wish_count = models.IntegerField(default=0)
    collect = models.ManyToManyField(User, blank=True, related_name="collect_books")
    collect_count = models.IntegerField(default=0)

    class Meta:
            db_table = "b_book"


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book_comment')
    comment_time = models.DateTimeField(auto_now_add=True, null=True)
    like_count = models.IntegerField(default=0)

    class Meta:
        db_table = "b_comment"


class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_record')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book_record')
    title = models.CharField(max_length=100, blank=True, null=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True,
                                       related_name='classification')
    record_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_record"


class LoginLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    ua = models.CharField(max_length=200, blank=True, null=True)
    log_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_login_log"


class OpLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    re_ip = models.CharField(max_length=100, blank=True, null=True)
    re_time = models.DateTimeField(auto_now_add=True, null=True)
    re_url = models.CharField(max_length=200, blank=True, null=True)
    re_method = models.CharField(max_length=10, blank=True, null=True)
    re_content = models.CharField(max_length=200, blank=True, null=True)
    access_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "b_op_log"


class ErrorLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    log_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_error_log"


class Borrow(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_borrow')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book_borrow')
    status = models.CharField(max_length=2, blank=True, null=True)  # 1借出 2已还
    borrow_time = models.DateTimeField(auto_now_add=True, null=True)
    expect_time = models.DateTimeField(null=True)  # 应还时间
    return_time = models.DateTimeField(null=True)
    delayed = models.BooleanField(blank=True, null=True, default=False)  # 是否延期

    class Meta:
        db_table = "b_borrow"


class BorrowLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_borrow_log')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book_borrow_log')
    action = models.CharField(max_length=2, blank=True, null=True)
    log_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_borrow_log"


class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='banner/', null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book_banner')
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_banner"


class Ad(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='ad/', null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_ad"


class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_notice"


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_address')
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=300, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True, default=False)  # 是否默认地址
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_address"

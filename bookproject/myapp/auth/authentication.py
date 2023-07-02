from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from myapp.models import User


# 后台接口认证
class AdminTokenAuthtication(BaseAuthentication):
    def authenticate(self, request):
        adminToken = request.META.get("HTTP_ADMINTOKEN")
        print("检查adminToken==>" + adminToken)
        users = User.objects.filter(admin_token=adminToken)
        """
        判定条件：
            1. 传了adminToken 
            2. 查到了该帐号 
            3. 该帐号是管理员或演示帐号
        """
        if not adminToken or users.count == 0 or users[0].role == '2':
            raise exceptions.AuthenticationFailed("AUTH_FAIL_END")
        else:
            print('adminToken验证通过')


# 前台接口认证
class TokenAuthtication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_TOKEN", "")
        if token is not None:
            print("检查token==>" + token)
            users = User.objects.filter(token=token)
            # print(users)
            """
            判定条件：
                1. 传了token 
                2. 查到了该帐号 
                3. 该帐号是普通用户
            """
            if not token or users.count == 0 or (users[0].role in ['1', '3']):
                raise exceptions.AuthenticationFailed("AUTH_FAIL_FRONT")
            else:
                print('token验证通过')
        else:
            print("检查token==>token 为空")
            raise exceptions.AuthenticationFailed("AUTH_FAIL_FRONT")

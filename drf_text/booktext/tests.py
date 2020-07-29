from django.test import TestCase

# Create your tests here.
# 设置Django运行所依赖的环境变量
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_text.settings')

# 让Django进行一次初始化
import django
django.setup()

from rest_framework import serializers


class User(object):
    '''用户类'''
    def __init__(self,name,age):
        self.name = name
        self.age = age

class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()


# if __name__ == '__main__':
#     # 创建User对象
#     user = User(name='smart',age= 20)

    # # 1.创建序列化器对象，传入被序列化的user对象
    # # instance：用于序列化时，接收被序列化的实例对象。
    # # data：用于反序列化时，接收所要校验的字典数据。
    # # serializer = 序列化器类(instance=None, data={}, **kwargs)
    # # serializer = UserSerializer(instance=User)
    # serializer = UserSerializer(User)
    #
    # # 获取序列化之后的数据
    # res = serializer.data
    # print(res)


if __name__ == '__main__':

    # 准备数据：此数据在实际中经常是客户端传递的，此处只是模拟
    data = {'name': 'admin', 'age': 30}

    # 2.创建序列化器对象，传入待校验的数据
    serializer = UserSerializer(data=data)

    # 调用is_valid进行数据校验，成功返回True，失败返回False
    res = serializer.is_valid()

    if res:
        # 校验通过，获取校验之后的数据
        print('校验通过：', serializer.validated_data)
    else:
        # 校验失败，获取错误提示信息
        print('校验失败：', serializer.errors)
import json
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from rest_framework.viewsets import ModelViewSet
from booktext.models import BookInfo
from booktext.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

class BooksView(View):
    def get(self,request):
         """
        获取所有图书数据:
        ① 查询数据库获取所有图书数据
        ② 将所有图书数据通过json进行返回
        "id": "图书id",
        "btitle": "图书名称",
        "bpub_date": "出版日期",
        "bread": "阅读量",
        "bcomment": "评论量"
        """
         books = BookInfo.objects.all()

         book_list = []

         for book in books:
             book_dict = {
                 'id':book.id,
                 'btitle':book.btitle,
                 'bpub_date':book.bpub_date,
                 'bread':book.bread,
                 'bcomment':book.bcomment
             }
             book_list.append(book_dict)

         return JsonResponse(book_list,safe=False)


    def post(self,request):
        '''
                参数：
          {
              "btitle": "图书名称",
              "bpub_date": "出版日期"
          }
        响应：
          状态码：201
          {
              "id": "图书id",
              "btitle": "图书名称",
              "bpub_date": "出版日期",
              "bread": "阅读量",
              "bcomment": "评论量"
          }

        ① 获取参数并进行校验
        ② 创建图书数据并保存到数据库
        ③ 将新增图书数据通过json进行返回
        '''
        json_dict = json.loads(request.body.decode())
        btitle = json_dict.get('btitle')
        bpub_date = json_dict.get('bpub_date')

        # 创建图书数据并保存到数据库
        book = BookInfo.objects.create(btitle=btitle,bpub_date=bpub_date)

        book_dict = {
            "id": book.id,
              "btitle": book.btitle,
              "bpub_date": book.bpub_date,
              "bread": book.bread,
              "bcomment": book.bcomment
        }
        return JsonResponse(book_dict,status=201)


class BookDetailView(View):
    def get(self,request,pk):
        '''
        获取指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 将指定图书数据通过json进行返回
           参数：
          通过url地址传递指定图书的id
        响应：
          状态码：200
          {
              "id": "图书id",
              "btitle": "图书名称",
              "bpub_date": "出版日期",
              "bread": "阅读量",
              "bcomment": "评论量"
          }

        '''
        try:
            books = BookInfo.objects.get(pk = pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail': 'not found'}, status=404)

        book_dict = {
            "id": books.id,
            "btitle": books.btitle,
            "bpub_date": books.bpub_date,
            "bread": books.bread,
            "bcomment": books.bcomment
        }
        return JsonResponse(book_dict)

    def put(self,request,pk):
        '''
                参数：
          通过url地址传递指定图书的id
          {
              "btitle": "图书名称",
              "bpub_date": "出版日期"
          }
        响应：
          状态码：200
          {
              "id": "图书id",
              "btitle": "图书名称",
              "bpub_date": "出版日期",
              "bread": "阅读量",
              "bcomment": "评论量"
          }
        修改指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 获取参数并进行校验
        ③ 修改图书数据并保存到数据库
        ④ 将修改图书数据通过json进行返回
        '''
        try:
            books = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail': 'not found'}, status=404)

        json_dict = json.loads(request.body.decode())
        btitle = json_dict.get('btitle')
        bpub_date = json_dict.get('bpub_date')

        # 修改图书数据并保存到数据库
        books.btitle = btitle
        books.bpub_date = bpub_date
        books.save()

        book_dict = {
            "id": books.id,
            "btitle": books.btitle,
            "bpub_date": books.bpub_date,
            "bread": books.bread,
            "bcomment": books.bcomment
        }
        return JsonResponse(book_dict)

    def delete(self,request,pk):
        '''
        参数：
          通过url地址传递指定图书的id
        响应：
          状态码：204
        删除指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 删除指定图书数据
        ③ 返回响应
        :return:
        '''
        try:
            books = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail': 'not found'}, status=404)

        books.delete()
        return JsonResponse(status=204)
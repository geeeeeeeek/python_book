# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.utils import dict_fetchall


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        sql_str = 'SELECT x.id AS parentId, x.title AS parentTitle, y.id AS childId ,y.title AS childTitle FROM ' \
                  'b_classification AS x LEFT JOIN b_classification AS y ON y.pid = x.id WHERE x.pid = -1 order by ' \
                  'x.create_time desc '
        data = [{
            'key': -1,
            'title': '全部',
            'isParent': True,
            'children': []
        }]
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            join_data = dict_fetchall(cursor)
            # print(join_data)
            for item1 in join_data:
                found = False
                for item2 in data:
                    if item2['key'] == item1['parentId']:
                        found = True
                        if item1['childId']:
                            item2['children'].append({
                                'key': item1['childId'],
                                'title': item1['childTitle'],
                                'isParent': False,
                                # 'children': []
                            })
                        break
                if not found:
                    k = {
                        'key': item1['parentId'],
                        'title': item1['parentTitle'],
                        'isParent': True,
                        'children': []
                    }
                    if item1['childId']:
                        k['children'].append({
                            'key': item1['childId'],
                            'title': item1['childTitle'],
                            'isParent': False,
                            # 'children': []
                        })
                    data.append(k)
        return APIResponse(code=0, msg='查询成功', data=data)






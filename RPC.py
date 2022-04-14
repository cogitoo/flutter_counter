# -*- coding: utf-8 -*-
try:
    from xmlrpc import client as xmlrpclib
except ImportError:
    import xmlrpclib


class Rpc(object):

    def __init__(self, value):
        self.server_url = value['server_url']
        self.server_db = value['server_db']
        self.server_username = value['server_username']
        self.server_password = value['server_password']
        self.server_common = value['server_common']
        self.server_uid = value['server_uid']
        self.server_models = value['server_models']

        self.client_url = value['client_url']
        self.client_db = value['client_db']
        self.client_username = value['client_username']
        self.client_password = value['client_password']
        self.client_common = value['client_common']
        self.client_version = value['client_version']
        self.client_uid = value['client_uid']
        self.client_models = value['client_models']

    # 1,服务器端创建数据接口 create
    def server_create(self, model, values):
        """
        服务器端创建数据接口 create
        id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
        结果
        78
        """
        news_id = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model, 'create',
                                                [values])
        return news_id

    # 2,服务器端删除数据接口 unlink
    def server_unlink(self, model, id):
        """
        服务器端删除数据接口 unlink
        models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
        结果
        True
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model, 'unlink',
                                            [[id]])
        return obj

    # 3,服务器端创建数据接口 write
    def server_write(self, model, id=None, values=None):
        """
        服务器端创建数据接口 create
        models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
        结果
        True
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model,
                                            'write', [[id], values])
        return obj

    # 4,服务器端查询并读取数据接口 search_read
    def server_search_read(self, model, domain=None, fields={'fields': [], 'offset': 0, 'limit': 10000}):
        """
        服务器端查询并读取数据接口 search_read
        models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        结果
        [
            {
                "comment": false,
                "country_id": [ 21, "Belgium" ],
                "id": 7,
                "name": "Agrolait"
            },
            {
                "comment": false,
                "country_id": [ 76, "France" ],
                "id": 18,
                "name": "Axelor"
            }
        ]
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model,
                                            'search_read', [domain], fields)
        return obj

    # 5,服务器端查询数据接口 search
    def server_search(self, model, domain=None, offset=0, limit=10000):
        """
        服务器端查询数据接口 search
        models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit':5})
        结果
        [13, 20, 30, 22, 29]
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model,
                                            'search', [domain], {'offset': offset, 'limit': limit})
        return obj

    # 6,服务器端查询数量接口 search_count
    def server_search_count(self, model, domain):
        """
        服务器端查询数量接口 search_count
        models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
        结果
        19
        """
        count = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password,
                                              model, 'search_count', [domain])
        return count

    # 7,服务器端查询并读取数据接口 read
    def server_read(self, model, ids, fields={'fields': []}):
        """
        服务器端查询并读取数据接口 read
        models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
        结果
        [{"comment": false, "country_id": [21, "Belgium"], "id": 7, "name": "Agrolait"}]
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model, 'read', [ids],
                                            fields)
        return obj

    # 8,服务器端查询外键名称数据接口 name_get
    def server_name_get(self, model, id):
        """
        服务器端查询外键名称数据接口 name_get
        models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
        结果
        [[78, "Newer partner"]]
        """
        obj = self.server_models.execute_kw(self.server_db, self.server_uid, self.server_password, model, 'name_get',
                                            [id])
        return obj

    # 1,客户端创建数据接口 create
    def client_create(self, model, values):
        """
        客户端创建数据接口 create
        id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
        结果
        78
        """
        news_id = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model, 'create',
                                                [values])
        return news_id

    # 2,客户端删除数据接口 unlink
    def client_unlink(self, model, id):
        """
        客户端删除数据接口 unlink
        models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
        结果
        True
        """
        obj = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model, 'unlink',
                                            [[id]])
        return obj

    # 3,客户端创建数据接口 write
    def client_write(self, model, id=None, values=None):
        """
        客户端创建数据接口 create
        models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
        结果
        True
        """
        obj = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model,
                                            'write', [[id], values])
        return obj

    # 4,客户端查询并读取数据接口 search_read
    def client_search_read(self, model, domain=None, fields={'fields': [], 'offset': 0, 'limit': 10000}):
        """
        客户端查询并读取数据接口 search_read
        models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        结果
        [
            {
                "comment": false,
                "country_id": [ 21, "Belgium" ],
                "id": 7,
                "name": "Agrolait"
            },
            {
                "comment": false,
                "country_id": [ 76, "France" ],
                "id": 18,
                "name": "Axelor"
            }
        ]
        """
        obj = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model,
                                            'search_read', [domain], fields)
        return obj

    # 5,客户端查询数据接口 search
    def client_search(self, model, domain=None, offset=0, limit=10000):
        """
        客户端查询数据接口 search
        models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit':5})
        结果
        [13, 20, 30, 22, 29]
        """
        obj = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model,
                                            'search', [domain], {'offset': offset, 'limit': limit})
        return obj

    # 6,客户端查询数量接口 search_count
    def client_search_count(self, model, domain):
        """
        客户端查询数量接口 search_count
        models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
        结果
        19
        """
        count = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password,
                                              model, 'search_count', [domain])
        return count

    # 7,客户端查询并读取数据接口 read
    def client_read(self, model, ids, fields={'fields': []}):
        """
        客户端查询并读取数据接口 read
        models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
        结果
        [{"comment": false, "country_id": [21, "Belgium"], "id": 7, "name": "Agrolait"}]
        """
        obj = self.client_models.execute_kw(self.client_db, self.client_uid, self.client_password, model, 'read', [ids],
                                            fields)
        return obj

    # 8,客户端端查询外键名称数据接口 name_get
    def client_name_get(self, model, id):
        """
        客户端端查询外键名称数据接口 name_get
        models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
        结果
        [[78, "Newer partner"]]
        """
        obj = self.client_models.execute_kw(self.server_db, self.server_uid, self.server_password, model, 'name_get',
                                            [id])
        return obj

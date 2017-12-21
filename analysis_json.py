# -*- coding:utf8 -*-
import requests
import json
import traceback
from datetime import datetime, timedelta

##########################################
# 递归解析json的工具类
##########################################
class RecurseTranslater():
    def __init__(self, data):
        self.stack_dict = {}
        self.data = data

    # 解析
    def analysis(self):
        self.recuse_analysis(self.data, self.stack_dict)
    # 翻译
    def translate(self):
        self.recuse_translate(self.data, MAP)

    def recuse_translate(self, obj, map):
        if type(obj) == dict:
            for k, v in obj.items():
                if type(v) != dict and type(v) != list:
                    if map.get(k, ''):
                        obj[map[k]] = obj.pop(k)
                else:
                    self.recuse_translate(v, map[k])
        if type(obj) == list:
            for each in obj:
                self.recuse_translate(each, map)

    def recuse_analysis(self, obj, stack):
        if type(obj) == dict:
            for k, v in obj.items():
                if type(v) != dict and type(v) != list:
                    stack[k] = 0
                else:
                    stack[k] = {}
                    self.recuse_analysis(v, stack[k])
        if type(obj) == list:
            for each in obj:
                self.recuse_analysis(each, stack)


# 翻译json串
def translate_json(json_str):
    data = json.loads(json_str)
    rt = RecurseTranslater(data)
    rt.analysis()
    rt.translate()
    return rt.data


MAP = {
    "message": u"请求结果",
    "code": u"状态码",
    "data": {
        "queryUserID": u'查询操作员登录名',
        "unitName": u'查询单位名称',
        "batNo": u'查询批次号',
        "subOrgan": u'分支机构名称',
        "queryCount": u'查询请求数量',
        "cisReport": {
            "queryConditions": {
                "item": {
                        "caption": u'查询条件中文名称',
                        "name": u'查询条件英文名称',
                        "value": u'查询条件值',
                    },
                },
            "hasSystemError": u'有否系统错误',
            "refID": u'引用ID',
            "reportID": u'报告编号',
            "treatResult": u'对应的收费子报告收费次数',
            "queryReasonID": u'查询原因ID',
            "telCheckInfo": {
                "resultType": u'反查结果类型',
                "errorMessage": u'错误信息',
                "subReportTypeCost": u'收费子报告ID',
                "treatErrorCode": u'错误代码',
                "treatResult": u'子报告查询状态',
                "fixedTelMatch1": "fixedTelMatch1",
                "subReportType": u'子报告ID',
            },
            "isFrozen": u'该客户是否被冻结',
            "subReportTypes": u'查询的收费子报告ID'
        },
    }
}

if __name__ == '__main__':
    test_dict = {
    "message": "SUCCESS",
    "code": "0",
    "data": {
    "queryUserID": "123",
    "unitName": "xxxxxx",
    "subOrgan": "xxxxx",
    "batNo": "xxxxxxxxxxxxxxxxxxxxx",
    "queryCount": 1,
    "cisReport": {
    "hasSystemError": "false",
    "treatResult": "0",
    "queryReasonID": 12312,
    "telCheckInfo": {
    "fixedTelMatch1": None,
    "subReportTypeCost": 1312,
    "treatErrorCode": None,
    "treatResult": 2,
    "errorMessage": "",
    "subReportType": 113123,
    "resultType": None,
    "class": "xxxxxxx"
    },
    "isFrozen": "false",
    "subReportTypes": 21603,
    "class": "xxxxxxxxx",
    "reportID": "xxxxxxxxxxxxxxxx",
    "queryConditions": {
    "item": [
    {
    "caption": "电话号码",
    "name": "tel",
    "value": "xxxxxxxxx",
    "class": "xxxxxxxxxx"
    },
    {
    "caption": "省份",
    "name": "provinceDest",
    "value": "TW",
    "class": "xxxxxxxxxxxxxx"
    }
    ],
    "class": "xxxxxxxxxxxxxxxxxx"
    },
    "refID": "xxxxxxxxxxxxxxxxxxx"
    },
    "class": "xxxxxxxxxxxxxxxxxxxxxxxx"
    }
    }
    rt = RecurseTranslater(test_dict)
    rt.analysis()
    rt.translate()
    print rt.data

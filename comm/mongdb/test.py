#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import *
from bson import ObjectId
"""
qid = question
aid = answer

"""


def test(pid):

    conn = MongoClient(host="112.126.70.69", port=31000)['xyt_survey']

    document_answer = conn.xyt_survey_answers
    document_question = conn.xyt_survey_question

    temp_id = {'project_id': pid}
    #document_answer.find(temp_id, no_cursor_timeout=True).limit(limit_num).skip(skip_num)
    a = document_answer.find(temp_id).limit(10000).skip(0)
    q = document_question.find_one({"_id": ObjectId(str('55ffbabfea1967ac558b4567'))})
    print(q.get('question_type'))
    print(q.get('cid'))
    q_title = q.get('cid')

    temp_struct_data = {}
    # print(a)
    for i in a:
        if i.get('answers'):
            print(i.get('answers'))
            for q in i.get('answers'):
                for k, v in q.items():
                    print(k,v)
                    if k == 'answer':
                        for k1, v1 in v.items():
                            print("", k1,v1)
                            document_question.find_one({"_id": ObjectId(str(k1))})

                            q_title_temp = document_question.find_one({"_id": ObjectId(str(k1))})
                            temp_struct_data[q_title + "%s" % q_title_temp] = v1[0]
    print(temp_struct_data)


    # print(q)
    # print(type(q))
    # print(q.get('question_type'))




test('55ffb51fea19672d128b4567')


# db = conn.get_db("xyt_survey")
# print conn.get_database()




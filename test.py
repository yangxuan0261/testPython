#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import pymongo

def testInsert(db):
    for x in range(1,10):
        user = {"name" : "guest-%d" % x
        , "age" : 200 + x
        , "sex" : 0}
        db.users.insert(user)

def testInsert2(db):
    animal = {
        "name": "aaa",
        "prod": { "car": "bbb",
                 "book" : { "dog" : 123}
                 }
    }
    db.users.insert(animal)
    pass

def testPrint(db):
    tb = db.runoob.find()
    for x in tb:
        print x

def testFind(db):
    u2 = db.users.find().sort([("age", 1)]).skip(0)
    # u2 = db.users.find({'age': {'$gte': 102, '$lte': 105}}).sort([("age", 1)])
    for u in u2: print u

def testUpdate(db):
    # db.users.update({"name":"user1"},{"$set":{"age":666, "sex":0}});
    # db.users.update({'age': {'$gte': 102, '$lte': 105}}, {'$set':{'sex': 1}}, multi=True)
    db.users.update({"prod.book.dog": 123},{"$set":{"prod.book.dog": 999}});
    pass

def testRemove(db):
    db.users.remove({'age': {'$gte': 206}})
    # u2 = db.users.find_one({"age":202})["_id"]
    # db.users.remove(u2)
    pass

def testDelete(db):
    user = db.users.find_one({"name":"user2"})
    if user:
        _id = user["_id"]
        print _id
        db.users.remove(_id)
    else:
        print "user doesnt exit"

def mongoConnetc():
    client = pymongo.MongoClient("192.168.253.128", 27016)
    db = client.test
    # print db.name
    # print db.my_collection
    # testPrint(db)
    # users = db['users']
    # print db.runoob.find()
    # testInsert(db)
    # testInsert2(db)
    # testUpdate(db)
    # testRemove(db)
    testFind(db)
    # testDelete(db)

def main():
    mongoConnetc()
    # os.system("pause")

if __name__ == "__main__":
    main()

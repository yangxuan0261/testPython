#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import pymongo

def testInsert(db):
    for x in range(1,10):
        user = {"name" : "user-%d" % x
        , "age" : 100 + x
        , "sex" : 0}
        db.users.insert(user)

def testFind(db):
    u2 = db.users.find_one({"name":"user1"})
    for u in db.users.find(): print u

def testUpdate(db):
    db.users.update({"name":"user1"},{"$set":{"age":666, "sex":0}});
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
    client = pymongo.MongoClient("192.168.74.128", 27017)
    db = client.test
    # print db.name
    # print db.my_collection
    users = db['users']
    # print users
    # testInsert(db)
    # testUpdate(db)
    testFind(db)
    # testDelete(db)

def test():
    print "hell world"

def main():
    # test()
    mongoConnetc()
    # os.system("pause")

if __name__ == "__main__":
    main()

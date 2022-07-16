from django.core.cache import cache
from django.http import HttpResponse
import requests
from .models import *
import pdb
from django_redis import get_redis_connection
import pickle


class Config:
    __slots__ = ['data', 'base_url', 'headers', 'response', 'con']

    def __init__(self) -> None:
        self.loadDataIntoRedis()

    def loadDataIntoRedis(self):
        """
        load data from rest api into redis
        """
        self.base_url = "https://data.cityofnewyork.us/resource/s3k6-pzi2.json"
        self.headers = {"Content-Type": "application/json",
                        "X-App-Token": "l8B2Xc3IJU8aPiPTVgtVr4jHh"}
        self.response = requests.get(self.base_url, headers=self.headers)
        self.data = self.response.json()
        self.con = get_redis_connection("default")
        # print(self.data)
        cache.clear()
        for item in self.data:
            school_item = SchoolItem()
            school_item.dbn = item.get('dbn')
            school_item.school_name = item.get('school_name')
            school_item.location = item.get('location')
            school_item.phone_number = item.get('phone_number')
            school_item.school_email = item.get('school_email')
            school_item.website = item.get('website')
            school_item.borough = item.get('borough')
            school_item.save()
            if cache.get(school_item.dbn) is None:
                cache.set(school_item.dbn.strip(), school_item)
            # store names as keys in redis and values as lists of school_item objects
            self.con.lpush(school_item.school_name.strip(),
                           pickle.dumps(school_item))
            # store boroughs as keys in redis and values as lists of school_item objects
            if school_item.borough:
                self.con.lpush(school_item.borough.strip(),
                               pickle.dumps(school_item))

        print("Data loaded into redis")

    # function to get data from redis using school_name
    def q1(self, school_name):
        query = 'SELECT * FROM school_item WHERE school_name = "%s"' % school_name
        print(query)
        data = {}
        data1 = []
        data = self.con.lrange(school_name, 0, -1)
        if data is None or len(data) == 0:
            data = {}
            print("Data not found in redis")
        else:
            for item in data:
                data1.append(pickle.loads(item))
                print(pickle.loads(item))
            print("length = " + str(len(data)))
            print("Data found in redis")
        return data1

    def q2(self, borough):
        query = 'SELECT * FROM school_item WHERE borough = "%s"' % borough
        print(query)
        data = {}
        data1 = []
        data = self.con.lrange(borough, 0, -1)
        if data is None or len(data) == 0:
            data = {}
            print("Data not found in redis")
        else:
            for item in data:
                data1.append(pickle.loads(item))
                print(pickle.loads(item))
            print("length = " + str(len(data)))
            print("Data found in redis")
        return data1

    def q3(self, school_name):
        query = 'DELETE * FROM school_item WHERE school_name = "%s"' % school_name
        print(query)
        data = {}
        data = self.con.lrange(school_name, 0, -1)
        if data is None or len(data) == 0:
            data = {}
            print("Data not found in redis")
        else:
            self.con.delete(school_name)
            print("length = " + str(len(data)))
            print("Data found in redis")
        return data

    def q4(self, school_name, school_address):
        query = 'UPDATE * FROM school_item WHERE school_name = "%s"' % school_name
        print(query)
        data = {}
        data1 = []
        data = self.con.lrange(school_name, 0, -1)
        if data is None or len(data) == 0:
            data = {}
            print("Data not found in redis")
        else:
            for item in data:
                data1.append(pickle.loads(item))
                print(pickle.loads(item))
            self.con.delete(school_name)
            for item in data1:
                item.location = school_address
                self.con.lpush(school_name, pickle.dumps(item))
            print("length = " + str(len(data)))
            print("Data found in redis")
        return data1

    def q5(self):
        query = 'SELECT * FROM school_item'
        print(query)
        data = {}
        data1 = []
        data = self.con.keys()
        if data is None or len(data) == 0:
            data = {}
            print("Data not found in redis")
        else:
            for item in data:
                data1.append(item.decode('utf-8').strip())
                print(item)
            print("length = " + str(len(data1)))
            print("Data found in redis")
        return data1

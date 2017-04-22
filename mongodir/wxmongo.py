import pymongo
from datetime import datetime


# here is the function to setup the database fot the first time including:
#   add a user called geektest@geeklab.com and with password geektest
#   set the "mail" to unique and sort in the index of that
#   add a default administrator with mail "admin@geeklab.com" and password "Geeklab2011"
def initial(hostip="127.0.0.1"):
    print("Database initializing!")
    print("This function will not modify any user data nor clear the table, so use it free for reconfigure and fix")
    print()
    client = pymongo.MongoClient(host=hostip, port=27017)
    db = client.geeklab
    user = db.user
    admin = db.admin
    # do with user
    if user.find_one({"mail": "geektest@geeklab.com"}) is not None:
        print("Warning: There is already default user, delete and reconfiguring!")
        user.delete_one({"mail": "geektest@geeklab.com"})
    user.insert_one({"mail": "geektest@geeklab.com", "password": "geektest", "regTime": datetime.now()})
    user.create_index([("mail", pymongo.ASCENDING)], unique=True)  # this can accelerate the query speed using mail
    if user.find_one({"mail": "geektest@geeklab.com"}) is not None:
        print("Success: User config finished successfully")
    else:
        print("Failed: User config wrong! Please try again")
    # do with admin
    if admin.find_one({"mail": "admin@geeklab.com"}) is not None:
        print("Warning: There is already default administrator, delete and reconfiguring!")
        admin.delete_one({"mail": "admin@geeklab.com"})
    admin.insert_one({"mail": "admin@geeklab.com", "password": "Geeklab2011", "createTime": datetime.now()})
    admin.create_index([("mail", pymongo.ASCENDING)], unique=True)  # this can accelerate the query speed using mail
    if admin.find_one({"mail": "admin@geeklab.com"}) is not None:
        print("Success: Administrator config finished successfully")
    else:
        print("Failed: Administrator config wrong! Please try again")


class Mongodb:
    def __init__(self, hostip="127.0.0.1"):
        client = pymongo.MongoClient(host=hostip, port=27017)
        self.db = client.geeklab
        self.user = self.db.user
        self.admin = self.db.admin

    def get_user(self, mail):
        result = self.user.find_one({"mail": mail})
        return result

    def register_user(self, mail, password):
        if self.user.find_one({"mail": mail}) is not None:
            return None  # has already registered
        # can register this mail
        return self.user.insert_one({"mail": mail, "password": password, "regTime": datetime.now()}).inserted_id

    #  more parameter needed to avoid delete by accident, and the command must be "I'm sure to delete"
    def delete_user(self, mail, password, regTime, command):
        if command != "I'm sure to delete":
            return None
        userdata = self.user.find_one({"mail": mail})
        if userdata is None:
            return False
        if userdata["password"] != password or userdata["regTime"] != regTime:
            return None
        self.user.delete_one({"mail": mail})  # delete this
        return True

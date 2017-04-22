from wxmongo import Mongodb
import wxmongo
import pprint


#  wxmongo.initial()

db = Mongodb()
# pprint.pprint(db.get_user("377545660@qq.com"))
# print(db.register_user("377545660@qq.com", "test"))

print(db.delete_user("377545660@qq.com", "test", "???", ""))
print(db.delete_user("37754@qq.com", "test", "??", "I'm sure to delete"))
print(db.delete_user("377545660@qq.com", "test", "??", "I'm sure to delete"))
# print(db.delete_user("377545660@qq.com", "test", db.get_user("377545660@qq.com")["regTime"], "I'm sure to delete"))
print(db.delete_user("377545660@qq.com", "test", "???", ""))


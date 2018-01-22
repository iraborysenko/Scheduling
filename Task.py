import json
import sqlite3

class Task:
    def __init__(self, title, deadline, length, start, price):
        self.title = title
        self.deadline = deadline
        self.length = length
        self.start = start
        self.price = price

    def __repr__(self):
        return repr((self.title, self.deadline, self.length, self.start, self.price))

# #
# tasks = [
#         Task('Tsvahu', 1433210400, 18000, 0),
#         Task('Skoby', 1433199600, 25200, 0),
#         Task('Gvynty', 1433152800, 3600, 0),
#         Task('Samoryzy', 1433174400, 10800, 0),
#         Task('Shayby', 1433160000, 7200, 0),
#         Task('Gayky', 1433206800, 14400, 0)
#         ]
#
# sort_tasks = sorted(tasks, key=lambda task: task.deadline)
#
#
# def run_check():
#     TimeIn = 1433116800
#     Start = TimeIn
#     for i in range(0,len(sort_tasks)):
#         sort_tasks[i].start = Start;
#         Start = Start + sort_tasks[i].length
#         if Start > sort_tasks[i].deadline:
#             return False
#
#     minimum = sort_tasks[i].deadline
#     for i in range(0, len(sort_tasks)):
#         minimum = min(minimum, (sort_tasks[i].deadline - sort_tasks[i].start - sort_tasks[i].length))
#
#     Start = TimeIn + minimum
#     for i in range(0,len(sort_tasks)):
#         sort_tasks[i].start += minimum
#
#     return True
#
#
# def run_optimize():
#     t = Task("", 0, 0, 0)
#     dtime = sort_tasks[len(sort_tasks)-1].start + sort_tasks[len(sort_tasks)-1].length
#     for i in range(0, len(sort_tasks)-1):
#         index = len(sort_tasks) - 1 - i;
#         for j in range(0, len(sort_tasks) - 1 - i):
#             if (sort_tasks[j].deadline >= dtime) and (sort_tasks[j].length < sort_tasks[index].length):
#                 index = j
#
#         if index != (len(sort_tasks) - 1 - i):
#             t.length = sort_tasks[len(sort_tasks) - 1 - i].length
#             t.title = sort_tasks[len(sort_tasks) - 1 - i].title
#             t.deadline = sort_tasks[len(sort_tasks) - 1 - i].deadline
#             sort_tasks[len(sort_tasks) - 1 - i].length = sort_tasks[index].length
#             sort_tasks[len(sort_tasks) - 1 - i].title = sort_tasks[index].title
#             sort_tasks[len(sort_tasks) - 1 - i].deadline = sort_tasks[index].deadline
#
#             sort_tasks[index].length = t.length
#             sort_tasks[index].title = t.title
#             sort_tasks[index].deadline = t.deadline
#
#         dtime = dtime - sort_tasks[len(sort_tasks) - 1 - i].length
#
#     for i in range(0, len(sort_tasks)-1):
#         if i == 0:
#             sort_tasks[i].start = dtime - sort_tasks[i].length
#         else:
#             sort_tasks[i].start = sort_tasks[i-1].start + sort_tasks[i-1].length
#
#     return sort_tasks
#
#
# def listtojson(schedule):
#     list = []
#     for i in schedule:
#         l = []
#         l = [i.title, i.deadline, i.start]
#         list.append(l)
#     js = json.dumps(list)
#     print("jsonString")
#     print(js)
#     return js
#
#
# def jsontolist(js):
#     data = json.loads(js)
#     return data
#
# #
# schedule = run_optimize()
# print("sssssssssssssssssssss")
# print(schedule)
# # d = listtojson(schedule)
# # # jsontolist(d)
# #
# # conn = sqlite3.connect('DB\c.db')
# # c = conn.cursor()
# # # c.execute('''CREATE TABLE EI
# # #                  (id INTEGER PRIMARY KEY, name text)''')
# # # conn.commit()
# # #
# # #
# # # c.execute("INSERT INTO EI VALUES (NULL,'" + d + "')")
# # # conn.commit()
# # print("done")
# # for row in c.execute("SELECT name FROM EI WHERE id=1"):
# #     print(row)
# #
# # conn.close()
# #
# # sch = jsontolist(row[0])
# # print(sch[1][2])

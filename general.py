import json
import datetime
import time
import random
import Task as tsk
import pandas as pd


def buildsch(tasksOfI, key):
    if key == 1:
        tasks = createIArrForAlgorithm(tasksOfI)
    else:
        tasks = createIIArrForAlgorithm(tasksOfI)

    sort_tasks = sorted(tasks, key=lambda task: task.deadline)

    if True == run_check(sort_tasks):
        run = run_optimize(sort_tasks)
        return run
    else:
        print("bad")
        return False


def arrForUpdate(arrs):
    update = []
    for arr in arrs:
        l = []
        l = [arr.title, utc_to_str(arr.start)]
        update.append(l)
    return update


def str_to_utc(str):
    return time.mktime(datetime.datetime.strptime(str, "%d.%m.%y %H:%M").timetuple())


def utc_to_str(utc):
    return datetime.datetime.fromtimestamp(utc).strftime('%d.%m.%y %H:%M')


def listtojson(schedule):
    list = []
    for i in schedule:
        l = []
        l = [i.title, utc_to_str(i.deadline), utc_to_str(i.start), utc_to_str(i.start + i.length), i.length]
        list.append(l)
    js = json.dumps(list)
    return js


def jsontolist(js):
    data = json.loads(js)
    return data


def createArrForGraph(arrs):
    form = '%d.%m.%y %H:%M'
    colorslist = ["#bf10ff", "#ff0206", "#3741ff", "#ffdf10", "#06ff02", "#ff9837", "#fffc36", "#ffb3b0", "#ca95d9",
                  "#5b57ab", "#b0ffbc", "#d9d195", "#67fff0", "#50ff93", "#ffeace", "#ffeca8", "#fee2ff"]
    xpos = []
    for arr in arrs:
        a = [arr.title, pd.to_datetime(utc_to_str(arr.start), format=form),
             pd.to_datetime(utc_to_str(arr.start + arr.length), format=form),
             pd.to_datetime(utc_to_str(arr.deadline), format=form),
             random.choice(colorslist)]
        xpos.append(a)
    return xpos


def createIArrForAlgorithm(tasksArr):
    tasks = []
    for t in tasksArr:
        tasks.append(tsk.Task(t[1], str_to_utc(t[10]), t[9]*3600, 0, 0))
    return tasks


def createIIArrForAlgorithm(tasksArr):
    tasks = []
    for t in tasksArr:
        tasks.append(tsk.Task(t[1], str_to_utc(t[5]), t[4]*3600, 0, t[7]))
    return tasks


def run_check(sort_tasks):
    TimeIn = 1433116800
    Start = TimeIn
    for i in range(0,len(sort_tasks)):
        sort_tasks[i].start = Start;
        Start = Start + sort_tasks[i].length
        if Start > sort_tasks[i].deadline:
            return False

    minimum = sort_tasks[i].deadline
    for i in range(0, len(sort_tasks)):
        minimum = min(minimum, (sort_tasks[i].deadline - sort_tasks[i].start - sort_tasks[i].length))

    Start = TimeIn + minimum
    for i in range(0,len(sort_tasks)):
        sort_tasks[i].start += minimum
    return True


def run_optimize(sort_tasks):
    t = tsk.Task("", 0, 0, 0, 0)
    dtime = sort_tasks[len(sort_tasks)-1].start + sort_tasks[len(sort_tasks)-1].length
    for i in range(0, len(sort_tasks)-1):
        index = len(sort_tasks) - 1 - i;
        for j in range(0, len(sort_tasks) - 1 - i):
            if (sort_tasks[j].deadline >= dtime) and (sort_tasks[j].length < sort_tasks[index].length):
                index = j

        if index != (len(sort_tasks) - 1 - i):
            t.length = sort_tasks[len(sort_tasks) - 1 - i].length
            t.title = sort_tasks[len(sort_tasks) - 1 - i].title
            t.deadline = sort_tasks[len(sort_tasks) - 1 - i].deadline
            sort_tasks[len(sort_tasks) - 1 - i].length = sort_tasks[index].length
            sort_tasks[len(sort_tasks) - 1 - i].title = sort_tasks[index].title
            sort_tasks[len(sort_tasks) - 1 - i].deadline = sort_tasks[index].deadline

            sort_tasks[index].length = t.length
            sort_tasks[index].title = t.title
            sort_tasks[index].deadline = t.deadline

        dtime = dtime - sort_tasks[len(sort_tasks) - 1 - i].length

    for i in range(0, len(sort_tasks)-1):
        if i == 0:
            sort_tasks[i].start = dtime - sort_tasks[i].length
        else:
            sort_tasks[i].start = sort_tasks[i-1].start + sort_tasks[i-1].length

    return sort_tasks


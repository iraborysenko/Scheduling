import sqlite3
import os.path

def establishConn():

    if os.path.exists('DB/core.db'):
        print("it is")

    else:
        conn = sqlite3.connect('DB/core.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE EXI
                 (id INTEGER PRIMARY KEY, name text, start_time text)''')
        c.execute('''CREATE TABLE EXII
                         (id INTEGER PRIMARY KEY, name text, start_time text, specialization text)''')
        c.execute('''CREATE TABLE TASKS
                         (id INTEGER PRIMARY KEY, title text, idI text, idII INTEGER, 
                         dur2 INTEGER, dlineSE text, dlineSL text, priceE text, priceL text,
                         dur1 INTEGER, dlineF text)''')
        conn.commit()
        conn.close()


def addValues(entry, window):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()

    if window == '1':
        print("window1")
        c.execute("INSERT INTO EXI VALUES (NULL,'" + entry[0].get() + "', '" + entry[1].get() + "')")

    if window == '2':
        c.execute("INSERT INTO EXII VALUES (NULL,'" + entry[0].get() + "', '" + entry[2].get() + "','" + entry[1].get() + "')")

    if window == '3':
        c.execute("INSERT INTO TASKS VALUES (NULL,'" + entry[0].get() + "', " + entry[8] + ",' " + entry[1].get() +
                  "' , '" + entry[2].get() + "', '" + entry[3].get() + "', '" + entry[4].get() + "', '" + entry[5].get() +
                  "', '" + entry[6].get() + "', '" + entry[7].get() + "', NULL)")

    conn.commit()
    conn.close()


def getExecsF():
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    execfs = []
    for row in c.execute('SELECT * FROM EXI'):
        # print(row)
        execfs.append(row)
    conn.commit()
    conn.close()
    return execfs


def getExecsS():
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    execss = []
    for row in c.execute('SELECT * FROM EXII'):
        # print(row)
        execss.append(row)
    conn.commit()
    conn.close()
    return execss


def getTasksForI(id_excI):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    tasksI = []
    for row in c.execute("SELECT * FROM TASKS WHERE idI=" + str(id_excI) + " "):
        tasksI.append(row)
    conn.commit()
    conn.close()
    return tasksI


def getTasksForII(id_excII):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    tasksII = []
    for row in c.execute("SELECT * FROM TASKS WHERE idII=" + str(id_excII) + " "):
        tasksII.append(row)
    conn.commit()
    conn.close()
    return tasksII


def getTitleI(id_I):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    name_I = []
    for row in c.execute("SELECT name FROM EXI WHERE id=" + str(id_I) + " "):
        name_I.append(row)
    conn.commit()
    conn.close()
    return name_I


def getTitleII(id_II):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    name_II = []
    for row in c.execute("SELECT name FROM EXII WHERE id=" + str(id_II) + " "):
        name_II.append(row)
    conn.commit()
    conn.close()
    return name_II


def updateIdline(updateArr):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    for update in updateArr:
        c.execute("UPDATE TASKS SET dlineF = '" + str(update[1]) + "' WHERE title = '" + str(update[0]) + "' ")
        conn.commit()
    conn.close()


def getNotNull(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    tasksI = []
    for row in c.execute("SELECT * FROM TASKS WHERE idI=" + str(id) + " AND dlineF <> '' "):
        tasksI.append(row)
    conn.commit()
    conn.close()
    return tasksI


def deleteTask(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("DELETE FROM TASKS WHERE id=" + str(id) + " ")
    conn.commit()
    conn.close()


def deleteExI(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("DELETE FROM EXI WHERE id=" + str(id) + " ")
    conn.commit()
    c.execute("DELETE FROM TASKS WHERE idI=" + str(id) + " ")
    conn.commit()
    conn.close()


def deleteExII(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("DELETE FROM EXII WHERE id=" + str(id) + " ")
    conn.commit()
    # c.execute("UPDATE TASKS SET idII='' AND dlineF = '' WHERE idII = '" + str(id) + "' ")
    # conn.commit()
    conn.close()


def updateIex(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("UPDATE EXI SET name='" + id[1].get() + "', start_time='" + id[2].get() + "' WHERE id = '" + id[0] + "' ")
    conn.commit()
    conn.close()


def updateIIex(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("UPDATE EXII SET name='" + id[1].get() + "', specialization='" + id[2].get() + "', start_time='"
              + id[3].get() + "' WHERE id = '" + str(id[0]) + "' ")
    conn.commit()
    conn.close()


def updateTask(task):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    c.execute("UPDATE TASKS SET title='" + task[1].get() + "', idII='" + task[2].get() + "', dur2='"
              + task[3].get() + "', dlineSE='" + task[4].get() + "', dlineSL='" + task[5].get() + "', priceE='"
              + task[6].get() + "', priceL='" + task[7].get() + "', dur1='"
              + task[8].get() + "' WHERE id = '" + task[0] + "' ")
    conn.commit()
    conn.close()


def getInfoI(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    tasksI = []
    for row in c.execute("SELECT * FROM EXI WHERE id=" + str(id) + ""):
        tasksI.append(row)
    conn.commit()
    conn.close()
    return tasksI


def getInfoII(id):
    conn = sqlite3.connect('DB/core.db')
    c = conn.cursor()
    tasksI = []
    for row in c.execute("SELECT * FROM EXII WHERE id=" + str(id) + ""):
        tasksI.append(row)
    conn.commit()
    conn.close()
    return tasksI
# def setScheduleI(id_excI, jsSch):
#     conn = sqlite3.connect('DB\schedule.db')
#     c = conn.cursor()
#     c.execute("UPDATE EI SET schedule = '" + jsSch + "' WHERE id = " + str(id_excI) + " ")
#     conn.commit()
#
#     for row in c.execute("SELECT * from EI"):
#         print(row)
#     conn.commit()
#     conn.close()

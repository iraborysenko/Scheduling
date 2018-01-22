import tkinter as tk
import db
import general
import graph
import report

GREY = '#DFE2DB'
WHITE = '#FFFFF0'
BLACK = '#006400'
YELLOW = '#FFF056'
DGRAY = '#808080'
INDIGO = '#4B0082'
fontM=("Helvetica", 8)
fontN=("Helvetica", 11)


def transmit(entry, window):
    db.addValues(entry, window)


class PopUP:
    def __init__(self, master, text):
        # print(task)
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.frame = tk.Frame(self.master, bg=GREY)
        self.master.configure(bg=GREY)
        # self.master.iconbitmap("Source/info.ico")
        self.master.title("Інформація")

        row = tk.Frame(self.master, padx=20, pady=15, bg=GREY)
        lab = tk.Label(row, text=text, anchor='w', bg=GREY, font=fontN)
        row.pack(fill="both", padx=5, pady=5)
        lab.pack()
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class MainWindows:
    def __init__(self, master):
        self.circle_add = tk.PhotoImage(file="Source/add.png")
        self.graph1 = tk.PhotoImage(file="Source/graph.png")
        self.graph2 = tk.PhotoImage(file="Source/graph2.png")
        self.clipgrey = tk.PhotoImage(file="Source/addtask.png")
        self.eye = tk.PhotoImage(file="Source/eyetask.png")
        self.refr = tk.PhotoImage(file="Source/refresh.png")
        self.report1 = tk.PhotoImage(file="Source/report1.png")
        self.report2 = tk.PhotoImage(file="Source/report2.png")
        self.eye1 = tk.PhotoImage(file="Source/eye1.png")
        self.eye2 = tk.PhotoImage(file="Source/eye2.png")

        self.master = master
        self.master.title("Система календарного планування")
        self.globalframe = tk.Frame(self.master, bg=GREY)
        tk.Button(self.globalframe, image=self.refr, relief="flat", bg=GREY, padx=10,
                  command=(lambda e=self.master: self.refresh(e))).pack(side="left")

        # form for executors of I level
        self.mainframe = tk.Frame(self.globalframe, bg=GREY)
        tk.Label(self.mainframe, text="Виконавці першого рівня", bg=GREY, pady=5, anchor='n', fg=BLACK,
                 font=("Helvetica", 16, "bold", "italic")).pack()
        execfs = db.getExecsF()
        for execf in execfs:
            excfframe = tk.Frame(self.mainframe, relief="ridge", borderwidth=2, bg=INDIGO)
            tk.Label(excfframe, width=15, text=execf[1], padx=2, pady=5, anchor='w', fg=YELLOW,
                     font=("Helvetica", 10, "bold"), bg="green").pack()

            tasksI = db.getTasksForI(execf[0])
            for taskI in tasksI:
                row = tk.Frame(excfframe)
                tk.Label(row, width=15, text=taskI[1], padx=2, pady=5, anchor='w',
                         font=fontM).pack(side="left")
                tk.Button(row, padx=3, image=self.eye, relief='flat', anchor='e',
                          command=(lambda t=taskI: self.new_window_info(t))).pack(side="right")
                row.pack()

            tk.Button(excfframe, padx=6, image=self.eye1, relief='flat', anchor='e', bg=INDIGO,
                      command=(lambda e=execf: self.new_window_info_exI(e))).pack(side="left")
            tk.Button(excfframe, image=self.report1, relief="flat", pady=3, width=25, anchor='s', bg=INDIGO,
                      command=(lambda e=execf: self.create_reportI(e))).pack(
                side="right")
            tk.Button(excfframe, image=self.graph1, relief="flat", pady=3, width=25, anchor='s', bg=INDIGO,
                      command=(lambda e=execf: self.create_graphI(e))).pack(side="right")
            tk.Button(excfframe, image=self.clipgrey, relief="flat", pady=3, width=25, anchor='s', bg=INDIGO,
                      command=(lambda e=execf: self.new_window_task(e))).pack(side="right")
            excfframe.pack(side="left", ipadx=5, ipady=5, padx=5, pady=10, anchor='nw')

        tk.Button(self.mainframe, relief="flat", image=self.circle_add, bg=GREY,
                  command=self.new_window_exec_first).pack(pady=35)
        self.mainframe.pack(side="top")

        # form for executors of II level
        # SECOND LEVEL
        self.secondaryframe = tk.Frame(self.globalframe, bg=GREY)
        tk.Label(self.secondaryframe, text="Виконавці другого рівня", bg=GREY, pady=5, anchor='n', fg=BLACK,
                 font=("Helvetica", 16, "bold", "italic")).pack()
        execss = db.getExecsS()
        for execs in execss:
            excsframe = tk.Frame(self.secondaryframe, relief="ridge", borderwidth=2, bg=DGRAY)
            tk.Label(excsframe, width=15, text=execs[1], padx=2, pady=5, anchor='w', fg=YELLOW,
                     font=("Helvetica", 10, "bold"), bg="green").pack()
            tk.Label(excsframe, width=15, text=execs[3], padx=2, pady=5, anchor='w', fg="green",
                     font=("Helvetica", 8, "bold"), bg=YELLOW).pack()
            excsframe.pack(side="left", ipadx=5, ipady=5, padx=5, pady=10, anchor='nw')

            tasksII = db.getTasksForII(execs[0])
            for taskII in tasksII:
                row = tk.Frame(excsframe)
                tk.Label(row, width=15, text=taskII[1], padx=2, pady=5, anchor='w',
                         font=fontM).pack(side="left")
                tk.Button(row, padx=3, image=self.eye, relief='flat', anchor='e',
                          command=(lambda t=taskII: self.new_window_info(t))).pack(side="right")
                row.pack()

            tk.Button(excsframe, padx=6, image=self.eye2, relief='flat', anchor='e', bg=DGRAY,
                      command=(lambda e=execs: self.new_window_info_exII(e))).pack(side="left")
            tk.Button(excsframe, image=self.report2, relief="flat", pady=3, width=25, anchor='s', bg=DGRAY,
                      command=(lambda e=execs: self.create_reportII(e))).pack(side="right")
            tk.Button(excsframe, image=self.graph2, relief="flat", pady=3, width=25, anchor='s', bg=DGRAY,
                      command=(lambda e=execs: self.create_graphII(e))).pack(side="right")

        tk.Button(self.secondaryframe, relief="flat", image=self.circle_add, bg=GREY,
                  command=self.new_window_exec_sec).pack(pady=35)
        self.secondaryframe.pack(side="top", pady=(70, 10))
        self.globalframe.pack()

    def create_graphI(self, id_exc):
        # taskOfI = db.getTasksForI(id_exc[0])
        notNulltasks = db.getNotNull(id_exc[0])
        if notNulltasks == []:
            text = "Немає директивних термінів. \nПобудуйте відповідні календарні плани для виконавців ІІ-го рівня"
            self.newWindow = tk.Toplevel(self.master)
            self.app = PopUP(self.newWindow, text)
        else:
            run = general.buildsch(notNulltasks, 1)
            arrgraph = general.createArrForGraph(run)
            graph.create_graph(arrgraph, id_exc)

    def create_graphII(self, id_exc):
        taskOfII = db.getTasksForII(id_exc[0])
        run = general.buildsch(taskOfII, 2)
        arrgraph = general.createArrForGraph(run)
        graph.create_graph(arrgraph, id_exc)
        toupdate = general.arrForUpdate(run)
        db.updateIdline(toupdate)
        # print(run)

    def create_reportI(self, id_exc):
        # taskOfI = db.getTasksForI(id_exc[0])
        notNulltasks = db.getNotNull(id_exc[0])
        if [] == notNulltasks:
            text = "Немає директивних термінів. \nПобудуйте відповідні календарні плани для виконавців ІІ-го рівня"
            self.newWindow = tk.Toplevel(self.master)
            self.app = PopUP(self.newWindow, text)
        else:
            run = general.buildsch(notNulltasks, 1)
            arrgraph = general.createArrForGraph(run)
            graph.save_graph(arrgraph, id_exc)
            report.build_report_first(run, id_exc)

            text = "Звіт побудовано"
            self.newWindow = tk.Toplevel(self.master)
            self.app = PopUP(self.newWindow, text)

    def create_reportII(self, id_exc):
        taskOfII = db.getTasksForII(id_exc[0])

        if taskOfII[0][1]=="Робота 1":
            excluded = []
            excluded.append(taskOfII.pop(2))
            excluded.append(taskOfII.pop(0))

            run = general.buildsch(taskOfII, 2)
            toupdate = general.arrForUpdate(run)
            db.updateIdline(toupdate)
            arrgraph = general.createArrForGraph(run)
            graph.save_graph(arrgraph, id_exc)
            report.build_report_third(run, excluded, id_exc)
        else:
            run = general.buildsch(taskOfII, 2)

            toupdate = general.arrForUpdate(run)
            db.updateIdline(toupdate)

            arrgraph = general.createArrForGraph(run)
            graph.save_graph(arrgraph, id_exc)
            report.build_report_second(run, id_exc)

        text = "Звіт побудовано"
        self.newWindow = tk.Toplevel(self.master)
        self.app = PopUP(self.newWindow, text)

    def refresh(self, e):
        if self.globalframe is not None:
            self.globalframe.destroy()
        self.globalframe = MainWindows(e)

    def new_window_exec_first(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddFirst(self.newWindow)

    def new_window_exec_sec(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddSecond(self.newWindow)

    def new_window_task(self, id_exc):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddTask(self.newWindow, id_exc)

    def new_window_info_exI(self, id_exc):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WinExI(self.newWindow, id_exc)

    def new_window_info_exII(self, id_exc):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WinExII(self.newWindow, id_exc)

    def new_window_info(self, task):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WinTask(self.newWindow, task)


class AddFirst:
    def __init__(self, master):
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Додання виконаців І-го рівня")
        row = tk.Frame(self.master, bg=GREY)
        lab = tk.Label(row, width=20, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        # ent.event_add('<<Paste>>', '<Control-v>')
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master, bg=GREY)
        lab1 = tk.Label(row1, width=20, text='Час початку виконання', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        ents = []
        ents.append(ent)
        ents.append(ent1)

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [transmit(ents, '1'), ent.delete(0, 'end'), ent1.delete(0, 'end')]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class AddSecond:
    def __init__(self, master):
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, bg=GREY)
        self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Додання виконаців ІI-го рівня")
        row = tk.Frame(self.master)
        lab = tk.Label(row, width=20, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master)
        lab1 = tk.Label(row1, width=20, text='Спеціалізація', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        row2 = tk.Frame(self.master)
        lab2 = tk.Label(row2, width=20, text='Час початку виконання', anchor='w', bg=GREY, font=fontN)
        ent2 = tk.Entry(row2, relief="flat", bg=WHITE)
        row2.pack(side="top", fill="both", padx=5, pady=5)
        lab2.pack(side="left")
        ent2.pack(side="right", expand=True, fill="both")

        ents = []
        ents.append(ent)
        ents.append(ent1)
        ents.append(ent2)

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [transmit(ents, '2'), ent.delete(0, 'end'), ent1.delete(0, 'end'),
                                              ent2.delete(0, 'end')]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class AddTask:
    def __init__(self, master, id_exc):
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.frame = tk.Frame(self.master, bg=GREY)
        self.master.configure(bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Додання завдання")

        row = tk.Frame(self.master)
        lab = tk.Label(row, width=25, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master)
        lab1 = tk.Label(row1, width=25, text='Призначення', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        row2 = tk.Frame(self.master)
        lab2 = tk.Label(row2, width=25, text='Тривалість (ІІ)', anchor='w', bg=GREY, font=fontN)
        ent2 = tk.Entry(row2, relief="flat", bg=WHITE)
        row2.pack(side="top", fill="both", padx=5, pady=5)
        lab2.pack(side="left")
        ent2.pack(side="right", expand=True, fill="both")

        row3 = tk.Frame(self.master)
        lab3 = tk.Label(row3, width=25, text='Ранній дир. термін(ІІ)', anchor='w', bg=GREY, font=fontN)
        ent3 = tk.Entry(row3, relief="flat", bg=WHITE)
        row3.pack(side="top", fill="both", padx=5, pady=5)
        lab3.pack(side="left")
        ent3.pack(side="right", expand=True, fill="both")

        row4 = tk.Frame(self.master)
        lab4 = tk.Label(row4, width=25, text='Пізній дир. термін(ІІ)', anchor='w', bg=GREY, font=fontN)
        ent4 = tk.Entry(row4, relief="flat", bg=WHITE)
        row4.pack(side="top", fill="both", padx=5, pady=5)
        lab4.pack(side="left")
        ent4.pack(side="right", expand=True, fill="both")

        row5 = tk.Frame(self.master)
        lab5 = tk.Label(row5, width=25, text='Ціна за ранне виконання', anchor='w', bg=GREY, font=fontN)
        ent5 = tk.Entry(row5, relief="flat", bg=WHITE)
        row5.pack(side="top", fill="both", padx=5, pady=5)
        lab5.pack(side="left")
        ent5.pack(side="right", expand=True, fill="both")

        row6 = tk.Frame(self.master)
        lab6 = tk.Label(row6, width=25, text='Ціна за пізнє веконання', anchor='w', bg=GREY, font=fontN)
        ent6 = tk.Entry(row6, relief="flat", bg=WHITE)
        row6.pack(side="top", fill="both", padx=5, pady=5)
        lab6.pack(side="left")
        ent6.pack(side="right", expand=True, fill="both")

        row7 = tk.Frame(self.master)
        lab7 = tk.Label(row7, width=25, text='Тривалість (І)', anchor='w', bg=GREY, font=fontN)
        ent7 = tk.Entry(row7, relief="flat", bg=WHITE)
        row7.pack(side="top", fill="both", padx=5, pady=5)
        lab7.pack(side="left")
        ent7.pack(side="right", expand=True, fill="both")

        id = str(id_exc[0])

        ents = []
        ents.append(ent)  #title
        ents.append(ent1) #goto
        ents.append(ent2) #dur2
        ents.append(ent3) #dlineFE
        ents.append(ent4) #dlineFL
        ents.append(ent5) #priceE
        ents.append(ent6) #priceL
        ents.append(ent7) #dur1
        ents.append(id)   #id1

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [transmit(ents, '3'), ent.delete(0, 'end'), ent1.delete(0, 'end'),
                                              ent2.delete(0, 'end'), ent3.delete(0, 'end'), ent4.delete(0, 'end'),
                                              ent5.delete(0, 'end'), ent6.delete(0, 'end'), ent7.delete(0, 'end')]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class ChangeFirst:
    def __init__(self, master, idI):
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Зміна виконаців І-го рівня")
        row = tk.Frame(self.master, bg=GREY)
        lab = tk.Label(row, width=20, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        ent.insert(0, idI[1])
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master, bg=GREY)
        lab1 = tk.Label(row1, width=20, text='Час початку виконання', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        ent1.insert(0, idI[2])
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        ents = []
        ents.append(idI[0])
        ents.append(ent)
        ents.append(ent1)

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [db.updateIex(ents), ent.delete(0, 'end'), ent1.delete(0, 'end')]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class ChangeSecond:
    def __init__(self, master, idII):
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Зміна виконаців ІI-го рівня")
        row = tk.Frame(self.master)
        lab = tk.Label(row, width=20, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        ent.insert(0, idII[1])
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master)
        lab1 = tk.Label(row1, width=20, text='Спеціалізація', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        ent1.insert(0, idII[3])
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        row2 = tk.Frame(self.master)
        lab2 = tk.Label(row2, width=20, text='Час початку виконання', anchor='w', bg=GREY, font=fontN)
        ent2 = tk.Entry(row2, relief="flat", bg=WHITE)
        ent2.insert(0, idII[2])
        row2.pack(side="top", fill="both", padx=5, pady=5)
        lab2.pack(side="left")
        ent2.pack(side="right", expand=True, fill="both")

        ents = []
        ents.append(idII[0])
        ents.append(ent)
        ents.append(ent1)
        ents.append(ent2)

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [db.updateIIex(ents), ent.delete(0, 'end'), ent1.delete(0, 'end'),
                                              ent2.delete(0, 'end'), self.close_windows()]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class ChangeTask:
    def __init__(self, master, task):
        # print(task)
        self.circle_del = tk.PhotoImage(file="Source/cross.png")
        self.confirm = tk.PhotoImage(file="Source/confirm.png")

        self.master = master
        self.frame = tk.Frame(self.master, bg=GREY)
        self.master.configure(bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Додання завдання")

        row = tk.Frame(self.master)
        lab = tk.Label(row, width=25, text='Назва', anchor='w', bg=GREY, font=fontN)
        ent = tk.Entry(row, relief="flat", bg=WHITE)
        ent.insert(0, task[1])
        row.pack(side="top", fill="both", padx=5, pady=5)
        lab.pack(side="left")
        ent.pack(side="right", expand=True, fill="both")

        row1 = tk.Frame(self.master)
        lab1 = tk.Label(row1, width=25, text='Призначення', anchor='w', bg=GREY, font=fontN)
        ent1 = tk.Entry(row1, relief="flat", bg=WHITE)
        ent1.insert(0, task[3])
        row1.pack(side="top", fill="both", padx=5, pady=5)
        lab1.pack(side="left")
        ent1.pack(side="right", expand=True, fill="both")

        row2 = tk.Frame(self.master)
        lab2 = tk.Label(row2, width=25, text='Тривалість (ІІ)', anchor='w', bg=GREY, font=fontN)
        ent2 = tk.Entry(row2, relief="flat", bg=WHITE)
        ent2.insert(0, task[4])
        row2.pack(side="top", fill="both", padx=5, pady=5)
        lab2.pack(side="left")
        ent2.pack(side="right", expand=True, fill="both")

        row3 = tk.Frame(self.master)
        lab3 = tk.Label(row3, width=25, text='Ранній дир. термін(ІІ)', anchor='w', bg=GREY, font=fontN)
        ent3 = tk.Entry(row3, relief="flat", bg=WHITE)
        ent3.insert(0, task[5])
        row3.pack(side="top", fill="both", padx=5, pady=5)
        lab3.pack(side="left")
        ent3.pack(side="right", expand=True, fill="both")

        row4 = tk.Frame(self.master)
        lab4 = tk.Label(row4, width=25, text='Пізній дир. термін(ІІ)', anchor='w', bg=GREY, font=fontN)
        ent4 = tk.Entry(row4, relief="flat", bg=WHITE)
        ent4.insert(0, task[6])
        row4.pack(side="top", fill="both", padx=5, pady=5)
        lab4.pack(side="left")
        ent4.pack(side="right", expand=True, fill="both")

        row5 = tk.Frame(self.master)
        lab5 = tk.Label(row5, width=25, text='Ціна за ранне виконання', anchor='w', bg=GREY, font=fontN)
        ent5 = tk.Entry(row5, relief="flat", bg=WHITE)
        ent5.insert(0, task[7])
        row5.pack(side="top", fill="both", padx=5, pady=5)
        lab5.pack(side="left")
        ent5.pack(side="right", expand=True, fill="both")

        row6 = tk.Frame(self.master)
        lab6 = tk.Label(row6, width=25, text='Ціна за пізнє веконання', anchor='w', bg=GREY, font=fontN)
        ent6 = tk.Entry(row6, relief="flat", bg=WHITE)
        ent6.insert(0, task[8])
        row6.pack(side="top", fill="both", padx=5, pady=5)
        lab6.pack(side="left")
        ent6.pack(side="right", expand=True, fill="both")

        row7 = tk.Frame(self.master)
        lab7 = tk.Label(row7, width=25, text='Тривалість (І)', anchor='w', bg=GREY, font=fontN)
        ent7 = tk.Entry(row7, relief="flat", bg=WHITE)
        ent7.insert(0, task[9])
        row7.pack(side="top", fill="both", padx=5, pady=5)
        lab7.pack(side="left")
        ent7.pack(side="right", expand=True, fill="both")

        id = str(task[0])

        ents = []
        ents.append(id)
        ents.append(ent)  #title
        ents.append(ent1) #goto
        ents.append(ent2) #dur2
        ents.append(ent3) #dlineFE
        ents.append(ent4) #dlineFL
        ents.append(ent5) #priceE
        ents.append(ent6) #priceL
        ents.append(ent7) #dur1

        self.b1 = tk.Button(self.frame, relief="flat", image=self.confirm, padx=9, bg=GREY,
                            command=(lambda: [db.updateTask(ents), ent.delete(0, 'end'), ent1.delete(0, 'end'),
                                              ent2.delete(0, 'end'), ent3.delete(0, 'end'), ent4.delete(0, 'end'),
                                              ent5.delete(0, 'end'), ent6.delete(0, 'end'), ent7.delete(0, 'end'),
                                              self.close_windows()]))
        self.b1.pack(side="left", padx=5, pady=5)
        self.quitButton = tk.Button(self.frame, relief="flat", image=self.circle_del, padx=9, bg=GREY,
                                    command=self.close_windows)
        self.quitButton.pack(side="left", padx=5, pady=5)
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


class WinTask:
    def __init__(self, master, task):
        self.config = tk.PhotoImage(file="Source/edit.png")
        self.trash = tk.PhotoImage(file="Source/trash.png")
        self.master = master
        self.master.geometry("330x330")
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, padx=30, pady=30, bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Інформація про завдання")

        name_I = db.getTitleI(task[2])
        name_II = db.getTitleII(task[3])
        tk.Label(self.frame, text="Інформація про завдання\n" + task[1], anchor='w', bg=GREY, font=("Helvetica", 13, "bold", "italic")).pack()
        tk.Label(self.frame, text="Виконавець І-го рівня: " + str(name_I[0][0]), anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Виконавець ІІ-го рівня: " + str(name_II[0][0]), anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Ранній дир. термін: " + task[5], anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Пізній дир. термін: " + task[6], anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Тривалість виконання ІІ(години): " + str(task[4]), anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Ціна за ранній дир. термін: " + str(task[7]), anchor='w', bg=GREY,
                 font=fontN).pack(side="top")
        tk.Label(self.frame, text="Ціна за пізній дир. термін: " + str(task[8]), anchor='w', bg=GREY,
                 font=fontN).pack(side="top")
        tk.Label(self.frame, text="Тривалість виконання І(години): " + str(task[9]), anchor='w', bg=GREY, font=fontN).pack(side="top")
        tk.Label(self.frame, text="Отриманий дир. термін: " + str(task[10]), anchor='w', bg=GREY,
                 font=fontN).pack(side="top")

        tk.Button(self.frame, image=self.trash, relief="flat", pady=10, bg=GREY,
                  command=(lambda e=task[0]: db.deleteTask(e))).pack(side="left")
        tk.Button(self.frame, image=self.config, relief="flat", bg=GREY,
                  command=(lambda t=task: self.change_window_task(t))).pack(side="left")
        self.frame.pack()

    def change_window_task(self, task):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ChangeTask(self.newWindow, task)

    def close_windows(self):
        self.master.destroy()


class WinExI:
    def __init__(self, master, idI):
        self.confg = tk.PhotoImage(file="Source/edit.png")
        self.trash = tk.PhotoImage(file="Source/trash.png")
        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, bg=GREY, padx=25, pady=25)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Інформація про виконавців")

        tk.Label(self.frame, text="Інформація про виконавця I рівня\n" + str(idI[1]), anchor='w', bg=GREY,
                 font=("Helvetica", 13, "bold", "italic")).pack()

        tasks = db.getTasksForI(idI[0])

        stime = db.getInfoI(idI[0])

        tk.Label(self.frame, text="Час початку виконання: " + str(stime[0][2]), anchor='w', bg=GREY,
                 font=fontN).pack(side="top")
        tk.Label(self.frame, text="  Завдання   Тривалість   Ціна   Призначено   Дир. термін", anchor='w', bg=GREY,
                 font=fontN).pack(side="top")
        for task in tasks:
            name_II = db.getTitleII(task[3])
            tk.Label(self.frame, text="    " + str(task[1])+"    "+str(task[9])+" (год)    "+str(task[7])+" (у.о.)    " + str(name_II[0][0]) +
                                      "    "+ str(task[10]) +"    ", anchor='w', bg=GREY, font=fontN).pack(side="top")

        tk.Button(self.frame, image=self.trash, relief="flat", bg=GREY,
                  command=(lambda e=idI[0]: db.deleteExI(e))).pack(side="left")
        tk.Button(self.frame, image=self.confg, relief="flat", bg=GREY,
                  command=(lambda i=idI: self.change_window_first(i))).pack(side="left")
        self.frame.pack()

    def change_window_first(self, task):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ChangeFirst(self.newWindow, task)

    def close_windows(self):
        self.master.destroy()


class WinExII:
    def __init__(self, master, idII):
        self.confg = tk.PhotoImage(file="Source/edit.png")
        self.trash = tk.PhotoImage(file="Source/trash.png")
        self.master = master
        self.master.configure(bg=GREY)
        self.frame = tk.Frame(self.master, padx=25, pady=25, bg=GREY)
        # self.master.iconbitmap("Source/pin1.ico")
        self.master.title("Інформація про виконавців")

        tk.Label(self.frame, text="Інформація про виконавця II рівня\n" + str(idII[1]), anchor='w', bg=GREY,
                 font=("Helvetica", 13, "bold", "italic")).pack()

        tasks = db.getTasksForII(idII[0])

        stime = db.getInfoII(idII[0])
        tk.Label(self.frame, text="Час початку виконання: " + str(stime[0][2]), anchor='w', bg=GREY,
                 font=fontN).pack(side="top")

        tk.Label(self.frame, text="  Завдання        Дир. термін        Тривалість        Ціна        Отримано від", anchor='w', bg=GREY,
                 font=fontN).pack(side="top")
        for task in tasks:
            name_II = db.getTitleI(task[2])
            tk.Label(self.frame, text="    " + str(task[1])+"    "+str(task[4])+"    "+str(task[5])+" (год)   " + str(task[7]) + " (у.о.)    "
                                      + str(name_II[0][0]) + "    ", anchor='w', bg=GREY, font=fontN).pack(side="top")

        tk.Button(self.frame, image=self.trash, relief="flat", bg=GREY,
                  command=(lambda e=idII[0]: db.deleteExII(e))).pack(side="left")
        tk.Button(self.frame, image=self.confg, relief="flat", bg=GREY,
                  command=(lambda i=idII: self.change_window_second(i))).pack(side="left")
        self.frame.pack()

    def change_window_second(self, task):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ChangeSecond(self.newWindow, task)

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    # root.iconbitmap("Source/pin1.ico")
    root.geometry("1100x700")
    root.configure(background=GREY)
    db.establishConn()
    MainWindows(root)
    root.mainloop()


if __name__ == '__main__':
    main()
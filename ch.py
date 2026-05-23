import webbrowser
import numpy as np
from tkcalendar import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as msc
from keras import activations

con = msc.connect(host="localhost",user="root",password="Dak@021105",database="college")
cursor = con.cursor()

global rg_nos
def start():
    win = Tk()
    win.geometry("1280x720")
    win.config(bg="#f4f4f4")
    win.title("Window")
    page1 = Frame(win,height=720,width=1280)
    page1.pack()
    p = PhotoImage(file="Login.png")
    lb = PhotoImage(file="login button.png")
    eye = PhotoImage(file="eye.png")
    reg = PhotoImage(file="register.png")

    l = Label(page1,image=p,fg="#f4f4f4",bg="#f4f4f4")
    l.pack()

    user = StringVar()
    passwd = StringVar()
    uen = Entry(page1,bg="#ececec",bd=0,font=("Times New Roman",15),width=40,textvariable=user)
    uen.place(x=770,y=260)
    pen = Entry(page1,bg="#ececec",bd=0,font=("Times New Roman",15),width=36,textvariable=passwd,show='*')
    pen.place(x=770,y=373)
    c = True
    def sec_page():
        page1.destroy()
        p2 = PhotoImage(file="page 2 s.png")
        page2 = Frame(win,height=720,width=1280)
        page2.pack()
        p2l = Label(page2,image=p2)
        p2l.pack()


        ins = PhotoImage(file="insta.png")
        x = PhotoImage(file="x.png")
        fb = PhotoImage(file="fb.png")
        li = PhotoImage(file="li.png")
        pro = PhotoImage(file="prof.png")
        hom = PhotoImage(file="home.png")
        atten = PhotoImage(file="attend.png")
        app = PhotoImage(file="apli.png")
        acem = PhotoImage(file="acem.png")
        abt = PhotoImage(file="about.png")
        pr = PhotoImage(file="profile.png")
        log = PhotoImage(file="log out.png")

        def run(url):
            webbrowser.open(url)
            

        inb = Button(page2,image = ins,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("https://www.instagram.com/msecofficial_chennai24?igsh=Nmd4aHRhbWlnM25n")) #1e3879
        inb.place(x =3,y=3)
        xb = Button(page2,image = x,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("")) 
        xb.place(x =65,y=7)
        fbb = Button(page2,image = fb,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("https://m.facebook.com/MSECADMIN/"))
        fbb.place(x =120,y=5)
        lib = Button(page2,image = li,bd=0,relief=FLAT,bg="#1c3c7c",command=lambda: run("https://www.linkedin.com/school/meenakshi-sundararajan-engineering-college/"))
        lib.place(x =178,rely=0.006)
        
        def prof():
            global pr_page, propic
            if 'pr_page' not in globals():
                pr_page = None
            if 'propic' not in globals():
                propic = PhotoImage(file="profile.png")

            if pr_page is not None and pr_page.winfo_ismapped():
                pr_page.destroy()
                pr_page = None
            else:
                usern = int(user.get())
                global dept
                cursor.execute(f"select ucase(name) from student where reg_no ={usern}")
                name = cursor.fetchall()[0][0]
                cursor.execute(f"select ucase(dept) from student where reg_no ={usern}")
                dept = cursor.fetchall()[0][0]
                cursor.execute(f"select dob from student where reg_no ={usern}")
                dob = cursor.fetchall()[0][0]
                
                
                pr_page = Frame(win, height=436, width=279, bg="#f4f4f4")
                pr_page.place(x=996, y=80)
                prp = Label(pr_page, image=propic)
                prp.pack()
                nlab = Label(pr_page,text=name,font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                nlab.place(x=40,y=135)
                reglab = Label(pr_page,text=user.get(),font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                reglab.place(x=40,y=205)
                dplab = Label(pr_page,text=dept,font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                dplab.place(x=40,y=265)
                dblab = Label(pr_page,text=dob,font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                dblab.place(x=40,y=325)
            
                def log_out():
                    page2.destroy()
                    pr_page.destroy()
                    win.destroy()
                    start()
                logb = Button(pr_page,image=log,relief=FLAT,bg="#bad7e3",command=log_out)
                logb.place(x=87,y=385)
                prp.image = propic
            
        prob = Button(page2,image = pro,bd=0,relief=FLAT,bg="#1e3879",command=prof)
        prob.place(x =1220,y=2)


        homeb = Button(page2,image = hom,bd=0,relief=FLAT,bg="#bbd5fc")
        homeb.place(x =650,y=52)

        def academics():
            page2.destroy()
            p3 = PhotoImage(file="acad.png")
            page3 = Frame(win, height=720, width=1280)
            page3.pack()
            p3l = Label(page3, image=p3)
            p3l.pack()
            style = ttk.Style()
            style.theme_use('clam')

            cursor.execute(f"select dept from student where reg_no = {user.get()}")
            dept = cursor.fetchall()[0][0]
            d = {'IT': "C_program", 'CSE': 'C_program', 'ECE': "CA", "AIDS": "Data_structures"}
            
            cursor.execute(f"select iat,statistics, EG, english, BEEE, tamil, {d[dept]}, physics from marks_{dept} where reg_no = {user.get()} ")
            r_set = cursor.fetchall()
            
            cursor.execute(f"select statistics, EG, english, BEEE, tamil, {d[dept]}, physics from marks_{dept} where reg_no = {user.get()} and iat = 'I' ")
            iat1 = cursor.fetchall()
            cursor.execute(f"select statistics, EG, english, BEEE, tamil, {d[dept]}, physics from marks_{dept} where reg_no = {user.get()} and iat = 'II' ")
            iat2 = cursor.fetchall()

            columns = ["IAT", "Statistics", "EG", "English", "BEEE", "Tamil", d[dept], "Physics"]

            tree = ttk.Treeview(page3, columns=columns, show='headings')

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=55)

            for row in r_set:
                tree.insert('',END, values=row)

            tree.place(x=150,y=270)
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            subjects = ["Statistics", "EG", "English", "BEEE", "Tamil", d[dept], "Physics"]
            iat1_marks = list(iat1[0])
            iat2_marks = list(iat2[0])
            bar_width = 0.35
            index = np.arange(len(subjects))
            
            bars1 = ax.bar(index, iat1_marks, bar_width, label='IAT I', color='b')
            bars2 = ax.bar(index + bar_width, iat2_marks, bar_width, label='IAT II', color='r')
            
            ax.set_xlabel('Subjects',fontsize=9)
            ax.set_ylabel('Marks')
            ax.set_title('Marks Comparison')
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(subjects, rotation=45, ha="right",fontsize=7)
            ax.legend()
            
            canvas = FigureCanvasTkAgg(fig, master=page3)
            canvas.draw()
            canvas.get_tk_widget().place(x=700, y=240, anchor='nw', relwidth=0.33, relheight=0.48)
            
            def go_back():
                page3.destroy()
                sec_page()
                
                
            def analyze():
                page3.destroy()
                p4 = PhotoImage(file="acad.png")
                page4 = Frame(win, height=720, width=1280)
                page4.pack()
                p4l = Label(page4, image=p4)
                p4l.pack()
                
                cursor.execute(f"select dept from student where reg_no = {user.get()}")
                dept = cursor.fetchall()[0][0]
                d = {'IT': "C_program", 'CSE': 'C_program', 'ECE': "CA", "AIDS": "Data_structures"}
                
                cursor.execute(f"select statistics, EG, english, BEEE, tamil, {d[dept]}, physics from marks_{dept} where reg_no = {user.get()} and iat = 'I' ")
                iat1 = cursor.fetchall()[0]
                cursor.execute(f"select statistics, EG, english, BEEE, tamil, {d[dept]}, physics from marks_{dept} where reg_no = {user.get()} and iat = 'II' ")
                iat2 = cursor.fetchall()[0]
                
                subjects = ["Statistics", "EG", "English", "BEEE", "Tamil", d[dept], "Physics"]
                
                iat1_marks = np.array(iat1)
                iat2_marks = np.array(iat2)
                
                average_scores = (iat1_marks + iat2_marks) / 2
                
                weakest_subject_index = np.argmin(average_scores)
                weakest_subject = subjects[weakest_subject_index]
                weakest_subject_score = average_scores[weakest_subject_index]
                fig = Figure(figsize=(10, 5), dpi=100)
                ax = fig.add_subplot(111)
                ax.plot(subjects, iat1_marks, marker='o', label='IAT I', color='b')
                ax.plot(subjects, iat2_marks, marker='o', label='IAT II', color='r')
                ax.set_xlabel('Subjects', fontsize=9)
                ax.set_ylabel('Marks')
                ax.set_title('Marks Comparison Across IATs')
                ax.legend()
                ax.set_ylim(0, 100)
                ax.grid(True)
                
                canvas = FigureCanvasTkAgg(fig, master=page4)
                canvas.draw()
                canvas.get_tk_widget().place(x=700, y=240, anchor='nw', relwidth=0.33, relheight=0.48)
                
                result_label = Label(page4, text=f"Subject to Concentrate More: {weakest_subject}\nAverage Score: {weakest_subject_score:.2f}", font=("Times New Roman", 13))
                result_label.place(x=180, y=260)
                
                suggestions = (
                    "Suggestions for Improvement:\n"
                    "1. Focus more on the weakest subject identified above.\n"
                    "2. Review the topics covered in this subject and practice more problems.\n"
                    "3. Seek additional help if necessary (e.g., tutor, study groups).\n"
                    "4. Regularly review and test yourself on the subject to track progress."
                )
                
                suggestions_label = Label(page4, text=suggestions, font=("Times New Roman", 14), justify=LEFT)
                suggestions_label.place(x=125, y=350)
                
                def go_back():
                    page4.destroy()
                    sec_page()
                
                # Create buttons for navigation
                back = ttk.Button(page4, text="Back", command=go_back)
                back.place(x=0, y=50)
                
                # Run the Tkinter event loop for the new page
                page4.mainloop()
                
            ana = ttk.Button(text="Analyze",command=analyze)
            ana.place(x=340,y=540)
            back = ttk.Button(text="Back",command=go_back)
            
            back.place(x=0,y=50)
            page3.mainloop()
            
        acemb = Button(page2,image = acem,bd=0,relief=FLAT,bg="#bbd5fc",command=academics)
        acemb.place(x =754,y=52)
    
                
        def appli_tog():
            global ap_page, appic  
            if 'ap_page' not in globals():
                ap_page = None
            if 'appic' not in globals():
                appic = PhotoImage(file="atten tog.png")

            if ap_page is not None and ap_page.winfo_ismapped():
                ap_page.destroy()
                ap_page = None
            else:
                
                ap_page = Frame(win, height=97, width=97, bg="#f4f4f4")
                ap_page.place(x=870, y=80)
                apl = Label(ap_page, image=appic)
                apl.pack()
                apl.image = appic 
                lp = PhotoImage(file="leave.png")
                odp = PhotoImage(file="od.png")
                
                def leave():
                    ap_page.destroy()
                    page2.destroy()
                    lvpage = PhotoImage(file="leave page.png")
                    page4 = Frame(win, height=720, width=1280)
                    page4.pack()
                    p4l = Label(page4, image=lvpage)
                    p4l.pack()
                    date_entry = Calendar(page4,background='#1e3879', foreground='white', borderwidth=1,date_pattern='yyyy-mm-dd',selectmode="day")
                    date_entry.place(x=165,y=430)
                    
                    reg = StringVar()
                    
                    reg_en = Entry(page4,bd=0,relief=FLAT,bg="#e5f6ff",font=("Times New Roman",12),textvariable=reg)
                    reg_en.place(x=180,y=250)
                    
                    departments = ["IT", "CSE", "ECE", "AIDS"]
                    dep_en = ttk.Combobox(page4,values=departments,foreground="#e5f6ff",width=18,background="#e5f6ff")
                    dep_en.place(x=180,y=330)
                    
                    reas_en = Text(page4,font=("Times New Roman",10),bd=0,relief=FLAT,bg="#e5f6ff",height=10,width=55)
                    reas_en.place(x=545,y=272)

                    def submit():
                        cursor.execute("select reg_no from login")
                        rg_nos = cursor.fetchall()
                        try :
                            users = int(user.get())
                        except:
                            users = user.get()
                        reg_nos = []
                        for i in rg_nos:
                            j = i[0]
                            reg_nos.append(j)
                        if int(reg.get()) in reg_nos:
                            cursor.execute(f"insert into leave_ values({reg.get()},'{dep_en.get()}','{date_entry.get_date()}','{reas_en.get(1.0,END)}',null)") 
                            con.commit()
                            messagebox.showinfo('SUCESS',"Request has been sent ..")
                    def go_back():
                        page4.destroy()
                        sec_page()
                    back = ttk.Button(text="Back",command=go_back)
                    back.place(x=0,y=50)
                    sub = ttk.Button(text="Submit",command=submit)
                    sub.place(x=605,y=490)
                    page4.mainloop()
                def od():
                    ap_page.destroy()
                    page2.destroy()
                    odpage = PhotoImage(file="od page.png")
                    page5 = Frame(win, height=720, width=1280)
                    page5.pack()
                    p4l = Label(page5, image=odpage)
                    p4l.pack()
                    date_entry = Calendar(page5,background='#1e3879', foreground='white', borderwidth=1,date_pattern='yyyy-mm-dd',selectmode="day")
                    date_entry.place(x=165,y=430)
                    
                    reg = StringVar()
                    
                    reg_en = Entry(page5,bd=0,relief=FLAT,bg="#e5f6ff",font=("Times New Roman",12),textvariable=reg)
                    reg_en.place(x=180,y=250)
                    
                    departments = ["IT", "CSE", "ECE", "AIDS"]
                    dep_en = ttk.Combobox(page5,values=departments,foreground="#e5f6ff",width=18,background="#e5f6ff")
                    dep_en.place(x=180,y=330)
                    
                    reas_en = Text(page5,font=("Times New Roman",10),bd=0,relief=FLAT,bg="#e5f6ff",height=10,width=55)
                    reas_en.place(x=545,y=272)

                    def submit():
                        cursor.execute("select reg_no from login")
                        rg_nos = cursor.fetchall()
                        try :
                            users = int(user.get())
                        except:
                            users = user.get()
                        reg_nos = []
                        for i in rg_nos:
                            j = i[0]
                            reg_nos.append(j)
                        if int(reg.get()) in reg_nos:
                            cursor.execute(f"insert into od values({reg.get()},'{dep_en.get()}','{date_entry.get_date()}','{reas_en.get(1.0,END)}')") 
                            con.commit()
                            messagebox.showinfo('SUCESS',"Request has been sent ..")
                            reg.set('')
                            dep_en.set('')
                            reas_en.clipboard_clear()
                    def go_back():
                        page5.destroy()
                        sec_page()
                    back = ttk.Button(text="Back",command=go_back)
                    back.place(x=0,y=50)
                    sub = ttk.Button(text="Submit",command=submit)
                    sub.place(x=605,y=490)
                    page5.mainloop()
                    
                    
                lvb = Button(ap_page,image=lp,bd=0,relief=FLAT,bg='#bbd5fc',command=leave)
                lvb.place(x=9,y=20)
                odb = Button(ap_page,image=odp,bd=0,relief=FLAT,bg='#bbd5fc',command=od)
                odb.place(x=12,y=55)
                ap_page.mainloop()

        appb = Button(page2,image = app,bd=0,relief=FLAT,bg="#bbd5fc",command=appli_tog)
        appb.place(x =870,y=52)

        def attend():
            page2.destroy()
            p7 = PhotoImage(file="attend page.png")
            page7 = Frame(win, height=720, width=1280)
            page7.pack()
            p7l = Label(page7, image=p7)
            p7l.pack()
            columns = ["Date","Status"]
            cursor.execute(f"select date,status from attendance where reg_no = {user.get()}")
            r_set = cursor.fetchall()
            cursor.execute(f"select ucase(name) from student where reg_no ={user.get()}")
            nam = cursor.fetchall()[0][0]
            cursor.execute(f"select ucase(dept) from student where reg_no ={user.get()}")
            dep = cursor.fetchall()[0][0]
            
            cursor.execute(f"select count(status) from attendance where reg_no = {user.get()} and status = 'AA'")
            abs_c = cursor.fetchall()[0][0]
            
            cursor.execute(f"select count(status) from attendance where reg_no = {user.get()} and status = 'PP'")
            pre_c = cursor.fetchall()[0][0]
            
            cursor.execute(f"select count(status) from attendance where reg_no = {user.get()} and (status = 'PA' or status = 'AP')")
            expre_c = cursor.fetchall()[0][0]
            
            cursor.execute(f"select count(status) from attendance where reg_no = {user.get()} and (status = 'PA' or status = 'AP')")
            expabs_c = cursor.fetchall()[0][0]
            
            pre_c = pre_c + (expre_c * 0.5)
            abs_c = abs_c + (expabs_c * 0.5)
            namlab = Label(text=nam,font=("Times New Roman",13))
            namlab.place(x = 320,y=218)
            
            deplab = Label(text=dep,font=("Times New Roman",13))
            deplab.place(x = 345,y=258)
            total_c = pre_c + abs_c 
            precount = Label(text=str(int(pre_c)),font=("Times New Roman",13))
            precount.place(x = 823,y=218)
            
            abscount = Label(text=str(int(abs_c)),font=("Times New Roman",13))
            abscount.place(x = 823,y=259)
            tree = ttk.Treeview(page7, columns=columns, show='headings')
            style = ttk.Style()
            style.theme_use('clam')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=210)

            for row in r_set:
                tree.insert('',END, values=row)

            tree.place(x=210,y=325)
            
            fig = Figure(figsize=(3, 3), dpi=100)
            ax = fig.add_subplot(111)
            labels = 'Present', 'Absent'
            sizes = [pre_c, abs_c]
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal') 

            canvas = FigureCanvasTkAgg(fig, master=page7)
            canvas.draw()
            canvas.get_tk_widget().place(x=790, y=300)
            def go_back():
                page7.destroy()
                sec_page()
            back = ttk.Button(text="Back",command=go_back)
            back.place(x=0,y=50)
            page7.mainloop()
        attb = Button(page2,image = atten,bd=0,relief=FLAT,bg="#bbd5fc",command=attend)
        attb.place(x =1000,y=52)
        
        def about():
            page2.destroy()
            p6 = PhotoImage(file="about page.png")
            page6 = Frame(win, height=720, width=1280)
            page6.pack()
            p6l = Label(page6, image=p6)
            p6l.pack()
            
            def go_back():
                page6.destroy()
                sec_page()
            back = ttk.Button(text="Back",command=go_back)
            back.place(x=0,y=50)
            page6.mainloop()
            
        abtb = Button(page2,image = abt,bd=0,relief=FLAT,bg="#bbd5fc",command=about)
        abtb.place(x =1125,y=52)
        
        page2.mainloop()
    def sec_page_st():
        page1.destroy()
        p2 = PhotoImage(file="page 2 t.png")
        page2 = Frame(win,height=720,width=1280)
        page2.pack()
        p2l = Label(page2,image=p2)
        p2l.pack()


        ins = PhotoImage(file="insta.png")
        x = PhotoImage(file="x.png")
        fb = PhotoImage(file="fb.png")
        li = PhotoImage(file="li.png")
        pro = PhotoImage(file="prof.png")
        hom = PhotoImage(file="home.png")
        atten = PhotoImage(file="attend.png")
        app = PhotoImage(file="apli.png")
        acem = PhotoImage(file="acem.png")
        abt = PhotoImage(file="about.png")
        pr = PhotoImage(file="profile.png")
        log = PhotoImage(file="log out.png")

        def run(url):
            webbrowser.open(url)
            

        inb = Button(page2,image = ins,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("https://www.instagram.com/msecofficial_chennai24?igsh=Nmd4aHRhbWlnM25n")) #1e3879
        inb.place(x =3,y=3)
        xb = Button(page2,image = x,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("")) 
        xb.place(x =65,y=7)
        fbb = Button(page2,image = fb,bd=0,relief=FLAT,bg="#1e3879",command=lambda: run("https://m.facebook.com/MSECADMIN/"))
        fbb.place(x =120,y=5)
        lib = Button(page2,image = li,bd=0,relief=FLAT,bg="#1c3c7c",command=lambda: run("https://www.linkedin.com/school/meenakshi-sundararajan-engineering-college/"))
        lib.place(x =178,rely=0.006)
        
        def prof():
            global pr_page, propic
            if 'pr_page' not in globals():
                pr_page = None
            if 'propic' not in globals():
                propic = PhotoImage(file="prof t.png")

            if pr_page is not None and pr_page.winfo_ismapped():
                pr_page.destroy()
                pr_page = None
            else:
                usern = int(user.get())
                global dept
                cursor.execute(f"select ucase(name) from teacher where reg_no ={usern}")
                name = cursor.fetchall()[0][0]
                cursor.execute(f"select ucase(dept) from teacher where reg_no ={usern}")
                dept = cursor.fetchall()[0][0]
                
                
                pr_page = Frame(win, height=436, width=279, bg="#f4f4f4")
                pr_page.place(x=996, y=80)
                prp = Label(pr_page, image=propic)
                prp.pack()
                nlab = Label(pr_page,text=name,font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                nlab.place(x=40,y=135)
                reglab = Label(pr_page,text=user.get(),font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                reglab.place(x=40,y=205)
                dplab = Label(pr_page,text=dept,font=("Times New Roman",15),fg="#ffffff",bg="#bad7e3")
                dplab.place(x=40,y=265)
                
            
                def log_out():
                    page2.destroy()
                    pr_page.destroy()
                    win.destroy()
                    start()
                logb = Button(pr_page,image=log,relief=FLAT,bg="#bad7e3",command=log_out)
                logb.place(x=87,y=295)
                prp.image = propic
        
        prob = Button(page2,image = pro,bd=0,relief=FLAT,bg="#1e3879",command=prof)
        prob.place(x =1220,y=2)
        
        def appli_tog():
            global ap_page, appic  
            if 'ap_page' not in globals():
                ap_page = None
            if 'appic' not in globals():
                appic = PhotoImage(file="atten tog.png")

            if ap_page is not None and ap_page.winfo_ismapped():
                ap_page.destroy()
                ap_page = None
            else:
                
                ap_page = Frame(win, height=97, width=97, bg="#f4f4f4")
                ap_page.place(x=870, y=80)
                apl = Label(ap_page, image=appic)
                apl.pack()
                apl.image = appic 
                lp = PhotoImage(file="leave.png")
                odp = PhotoImage(file="od.png")
                
                def leave():
                    ap_page.destroy()
                    page2.destroy()
                    lvpage = PhotoImage(file="leave t.png")
                    page4 = Frame(win, height=720, width=1280)
                    page4.pack()
                    p4l = Label(page4, image=lvpage)
                    p4l.pack()
                    
                    def go_back():
                        page4.destroy()
                        sec_page_st()
                    
                    cursor.execute(f"select reg_no,name,dept,date,reason from leave_ natural join student ")
                    req = cursor.fetchall()
                    
                    if req != []:
                        columns = ['Register no.','Name','Department','Date','Reason']
                        tree = ttk.Treeview(page4, columns=columns, show='headings')
                        style = ttk.Style()
                        style.theme_use('clam')
                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=180)

                        for row in req:
                            tree.insert('',END, values=row)
                            
                        def grant():
                            selected_item = tree.selection() 
                            if selected_item:
                                item_values = tree.item(selected_item, 'values') 

                                tree.delete(selected_item)
                                cursor.execute(f"update leave_ set status = 'A' where reg_no = {item_values[0]}")
                                con.commit()
                        def reject():
                            selected_item = tree.selection() 
                            if selected_item:
                                item_values = tree.item(selected_item, 'values') 
                                tree.delete(selected_item)
                                cursor.execute(f"update leave_ set status = 'R' where reg_no = {item_values[0]}")
                                con.commit()
                                
                        gr = ttk.Button(text="Allow",command=grant)
                        gr.place(x=500,y=570)
                        re = ttk.Button(text="Reject",command=reject)
                        re.place(x=780,y=570)
                        tree.place(x=210,y=325)
                    else:
                        nrl =  Label(page4,text="No Requests",font=("Times New Roman",18),fg="#ffffff",bg="#bad7e3")
                        nrl.place(x=350,y=200)
                        page4.mainloop()
                    
                    back = ttk.Button(text="Back",command=go_back)
                    back.place(x=0,y=50)
                    page4.mainloop()
                def od():
                    ap_page.destroy()
                    page2.destroy()
                    odpage = PhotoImage(file="od t.png")
                    page5 = Frame(win, height=720, width=1280)
                    page5.pack()
                    p4l = Label(page5, image=odpage)
                    p4l.pack()
                    
                    def go_back():
                        page5.destroy()
                        sec_page_st()
                    cursor.execute(f"select reg_no,name,dept,date,reason from od natural join student ")
                    req = cursor.fetchall()
                    
                    if req != []:
                        columns = ['Register no.','Name','Department','Date','Reason']
                        tree = ttk.Treeview(page5, columns=columns, show='headings')
                        style = ttk.Style()
                        style.theme_use('clam')
                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=180)

                        for row in req:
                            tree.insert('',END, values=row)
                            
                        def grant():
                            selected_item = tree.selection() 
                            if selected_item:
                                item_values = tree.item(selected_item, 'values') 

                                tree.delete(selected_item)
                                cursor.execute(f"update od set status = 'A' where reg_no = {item_values[0]}")
                                con.commit()
                        def reject():
                            selected_item = tree.selection() 
                            if selected_item:
                                item_values = tree.item(selected_item, 'values') 
                                tree.delete(selected_item)
                                cursor.execute(f"update od set status = 'R' where reg_no = {item_values[0]}")
                                con.commit()
                                
                        gr = ttk.Button(text="Allow",command=grant)
                        gr.place(x=500,y=570)
                        re = ttk.Button(text="Reject",command=reject)
                        re.place(x=780,y=570)
                        tree.place(x=210,y=325)
                    else:
                        nrl =  Label(ap_page,text="No Requests",font=("Times New Roman",18),fg="#ffffff",bg="#bad7e3")
                        nrl.place(x=350,y=200)
                    back = ttk.Button(text="Back",command=go_back)
                    back.place(x=0,y=50)
                    page5.mainloop()
                    
                    
                lvb = Button(ap_page,image=lp,bd=0,relief=FLAT,bg='#bbd5fc',command=leave)
                lvb.place(x=9,y=20)
                odb = Button(ap_page,image=odp,bd=0,relief=FLAT,bg='#bbd5fc',command=od)
                odb.place(x=12,y=55)
                ap_page.mainloop()
            
        appb = Button(page2,image = app,bd=0,relief=FLAT,bg="#bbd5fc",command=appli_tog)
        appb.place(x =870,y=52)
        def about():
            page2.destroy()
            p6 = PhotoImage(file="about page.png")
            page6 = Frame(win, height=720, width=1280)
            page6.pack()
            p6l = Label(page6, image=p6)
            p6l.pack()
            
            def go_back():
                page6.destroy()
                sec_page_st()
            back = ttk.Button(text="Back",command=go_back)
            back.place(x=0,y=50)
            page6.mainloop()
            
        abtb = Button(page2,image = abt,bd=0,relief=FLAT,bg="#bbd5fc",command=about)
        abtb.place(x =1125,y=52)
        page2.mainloop()
    def login():
        cursor.execute("select reg_no from login")
        rg_nos = cursor.fetchall()
        
        cursor.execute("select reg_no from login_staff")
        rg_nos_st = cursor.fetchall()
        try :
            users = int(user.get())
        except:
            users = user.get()
        reg_nos = []
        for i in rg_nos:
            j = i[0]
            reg_nos.append(j)
        reg_nos_st = []
        for i in rg_nos_st:
            j = i[0]
            reg_nos_st.append(j)
        
        if users in reg_nos:
            cursor.execute(f"select * from login where reg_no = {users}")
            us_pwd = cursor.fetchall()
            if [(users,passwd.get())] == us_pwd:
                messagebox.showinfo("Sucess","LOGGED IN")
                sec_page()
            else:
                messagebox.showerror("Error","Incorrect username or password !")
        elif users in reg_nos_st:
            cursor.execute(f"select * from login_staff where reg_no = {users}")
            us_pwd = cursor.fetchall()
            if [(users,passwd.get())] == us_pwd:
                messagebox.showinfo("Sucess","LOGGED IN")
                sec_page_st()
            else:
                messagebox.showerror("Error","Incorrect username or password !")
            
        else:
            messagebox.showerror("ERROR","This register number is not registered !")
        
    show_password = BooleanVar(value=False)
    lbutton = Button(page1,image=lb,bd=0,command=login)
    lbutton.place(x=745,y=445)


    def toggle_password():
        if show_password.get():
            pen.config(show='*')
            show_password.set(False)
        else:
            pen.config(show='')
            show_password.set(True)
        
    viewb = Button(page1,image=eye,bd=0,command=toggle_password)
    viewb.place(x=1150,y=368)

    regb = Button(page1,image=reg,bd=0)
    regb.place(x=1035,y=560)
    win.mainloop()

start()
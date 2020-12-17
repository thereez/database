import tkinter as tk
import psycopg2 as ps
from tkinter import ttk
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



window = tk.Tk()
window.geometry("1000x875")
db_name = tk.StringVar()


def Create():
    db_name = conn_ent.get()
    conn = ps.connect(dbname='postgres',user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pg_catalog.pg_database WHERE lower(datname) = lower(%s)", (db_name,))
    flag = cursor.fetchone()
    if flag is None:
        cursor.execute(sql.SQL("create database {}").format(sql.Identifier(db_name)))
    conn.close()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    if flag is None:
        cursor.execute(open("commands.sql","r").read())
    conn.close()
    
def SearchByIndex():
    list = search_results.pack_slaves()
    print(list)
    for l in list:
        l.destroy()
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM find('{search_ent.get()}')""")
    records = cursor.fetchall()
    print(records)
    tree = ttk.Treeview(search_results, columns=('id', 'model','price', 'time','producer'), height=15, show='headings')
    tree.pack(fill='both',expand=True)
    for row in records:
                print(row)
                tree.insert('', 'end', values=row)
    conn.close()
    return

def AddToTable1():
    list = visualize1_frame.pack_slaves()
    print(list)
    for l in list:
        l.destroy()
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT add1('{add1_param1_entry.get()}', {add1_param2_entry.get()}, '{add1_param3_entry.get()}')""")
    cursor.execute(f"""SELECT * FROM cars""")
    records = cursor.fetchall()
    tree = ttk.Treeview(visualize1_frame, columns=('id', 'model','price', 'time','producer'), height=15, show='headings',selectmode="browse")
    tree.pack(fill='both',expand=True)
    verscrlbar = ttk.Scrollbar(visualize1_frame,  
                           orient ="vertical",  
                           command = tree.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    tree.configure(xscrollcommand = verscrlbar.set) 
    for row in records:
                print(row)
                tree.insert('', 'end', values=row)
    conn.close()
    
def AddToTable2():
    list = visualize2_frame.pack_slaves()
    print(list)
    for l in list:
        l.destroy()
        
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT add2('{add2_param1_entry.get()}', '{add2_param2_entry.get()}', {add2_param3_entry.get()})""")
    cursor.execute(f"""SELECT * FROM producers""")
    records = cursor.fetchall()
    tree = ttk.Treeview(visualize2_frame, columns=('id', 'model','price'), height=15, show='headings', selectmode="browse")
    tree.pack(fill='both',expand=True)
    verscrlbar = ttk.Scrollbar(visualize2_frame,  
                           orient ="vertical",  
                           command = tree.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    tree.configure(xscrollcommand = verscrlbar.set) 
    for row in records:
                print(row)
                tree.insert('', 'end', values=row)
    conn.close()
    
    
def DeleteFromTable1():
    list = visualize1_frame.pack_slaves()
    print(list)
    for l in list:
        l.destroy()
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT delete1()""")
    cursor.execute(f"""SELECT * FROM cars""")
    records = cursor.fetchall()
    tree = ttk.Treeview(visualize1_frame, columns=('id', 'model','price', 'time','producer'), height=15, show='headings',selectmode="browse")
    tree.pack(fill='both',expand=True)
    verscrlbar = ttk.Scrollbar(visualize1_frame,  
                           orient ="vertical",  
                           command = tree.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    tree.configure(xscrollcommand = verscrlbar.set) 
    for row in records:
                print(row)
                tree.insert('', 'end', values=row)
    conn.close()
    
    

    
    
def DeleteFromTable2():
    list = visualize2_frame.pack_slaves()
    print(list)
    for l in list:
        l.destroy()
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT delete2()""")
    cursor.execute(f"""SELECT * FROM producers""")
    records = cursor.fetchall()
    tree = ttk.Treeview(visualize2_frame, columns=('id', 'model', 'time'), height=15, show='headings',selectmode="browse")
    tree.pack(fill='both',expand=True)
    verscrlbar = ttk.Scrollbar(visualize2_frame,  
                           orient ="vertical",  
                           command = tree.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    tree.configure(xscrollcommand = verscrlbar.set) 
    for row in records:
                print(row)
                tree.insert('', 'end', values=row)
    conn.close()
    

def ClearDatabase():
    db_name = conn_ent.get()
    conn = ps.connect(dbname=db_name,user='username',password='password',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT clear_database()""")
    conn.close()
    
    
def DeleteDatabase():
    db_name = conn_ent.get()
    
    conn = ps.connect(dbname='postgres',user='postgres',password='postgres',host='localhost',port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"""drop database {db_name}""")
    conn.close()
    
    

#connection frame
conn_frame = tk.Frame(master = window, height=50, bg="red")
conn_frame.pack_propagate(0)
conn_frame.pack(fill='both',expand=True)


conn_lbl_frm = tk.Frame(master = conn_frame,height=50,width=200)
conn_lbl_frm.pack_propagate(0)
conn_lbl_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

conn_lbl = tk.Label(master = conn_lbl_frm, text = "Enter new database name:")
conn_lbl.pack(side='right',fill='both',expand=True)


conn_ent_frm = tk.Frame(master = conn_frame,height=50,width=400)
conn_ent_frm.pack_propagate(0)
conn_ent_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

conn_ent = tk.Entry(master = conn_ent_frm)
conn_ent.pack(fill = tk.X,expand=True)


conn_btn_frm = tk.Frame(master = conn_frame,height=50,width=200)
conn_btn_frm.pack_propagate(0)
conn_btn_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

conn_btn = tk.Button(master = conn_btn_frm, text = "Create",command=Create)
conn_btn.pack(expand=True,side='left')


#search frame
search_frame = tk.Frame(master = window, height = 100, bg="green")
search_frame.pack_propagate(0)
search_frame.pack(fill='both',expand=True)
#search entry frame
search_entry_frame = tk.Frame(master = search_frame, height = 50)
search_entry_frame.pack_propagate(0)
search_entry_frame.pack(fill=tk.X,side='top')

search_lbl_frm = tk.Frame(master = search_entry_frame,height=50,width=200)
search_lbl_frm.pack_propagate(0)
search_lbl_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

search_lbl = tk.Label(master = search_lbl_frm, text = "Search by model:")
search_lbl.pack(side='right',fill='both',expand=True)


search_ent_frm = tk.Frame(master = search_entry_frame,height=50,width=400)
search_ent_frm.pack_propagate(0)
search_ent_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

search_ent = tk.Entry(master = search_ent_frm)
search_ent.pack(fill = tk.X,expand=True)


search_btn_frm = tk.Frame(master = search_entry_frame,height=50,width=200)
search_btn_frm.pack_propagate(0)
search_btn_frm.pack(side='left',padx=0,pady=0,fill='both',expand=True)

search_btn = tk.Button(master = search_btn_frm, text = "Find",command=SearchByIndex)
search_btn.pack(expand=True,side='left')
#search results frame
search_results = tk.Frame(master = search_frame)
search_results.pack_propagate(0)
search_results.pack(fill='both',side='bottom',expand=True)





#add2 frame
add2_frame = tk.Frame(master = window, height = 125, bg="blue")
add2_frame.pack_propagate(0)
add2_frame.pack(fill='both',expand=True)
#add entry frame
add2_entry_frame = tk.Frame(master = add2_frame, height = 75)
add2_entry_frame.pack_propagate(0)
add2_entry_frame.pack(fill='both',side='top',expand=True)

add2_param1_frame = tk.Frame(master = add2_entry_frame, height = 75, width=267)
add2_param1_frame.pack_propagate(0)
add2_param1_frame.pack(side='left',padx=0,pady=0,expand=True)

add2_param1_lbl = tk.Label(master = add2_param1_frame, text = "Enter producer name")
add2_param1_lbl.pack(fill="both",expand=True)

add2_param1_entry = tk.Entry(master = add2_param1_frame)
add2_param1_entry.pack(fill=tk.X,expand=True)

add2_param2_frame = tk.Frame(master = add2_entry_frame, height = 75, width=266)
add2_param2_frame.pack_propagate(0)
add2_param2_frame.pack(side='left',padx=0,pady=0,expand=True)

add2_param2_lbl = tk.Label(master = add2_param2_frame, text = "Enter producer site")
add2_param2_lbl.pack(fill="both",expand=True)

add2_param2_entry = tk.Entry(master = add2_param2_frame)
add2_param2_entry.pack(fill=tk.X,expand=True)

add2_param3_frame = tk.Frame(master = add2_entry_frame, height = 75, width=267)
add2_param3_frame.pack_propagate(0)
add2_param3_frame.pack(side='left',padx=0,pady=0,expand=True)

add2_param3_lbl = tk.Label(master = add2_param3_frame, text = "Enter producer telephone number")
add2_param3_lbl.pack(fill="both",expand=True)

add2_param3_entry = tk.Entry(master = add2_param3_frame)
add2_param3_entry.pack(fill=tk.X,expand=True)

#add buttons frame
add2_buttons_frame = tk.Frame(master = add2_frame, height = 50)
add2_buttons_frame.pack_propagate(0)
add2_buttons_frame.pack(fill='both',side='bottom',expand=True)

add2_btn1_frame = tk.Frame(master = add2_buttons_frame, height = 50, width=400)
add2_btn1_frame.pack_propagate(0)
add2_btn1_frame.pack(side='left',padx=0,pady=0,expand=True)

add2_btn1 = tk.Button(master = add2_btn1_frame, text = "Add",command=AddToTable2)
add2_btn1.pack(expand=True,side='left')

add2_btn2_frame = tk.Frame(master = add2_buttons_frame, height = 50, width=400)
add2_btn2_frame.pack_propagate(0)
add2_btn2_frame.pack(side='left',padx=0,pady=0,expand=True)

add2_btn2 = tk.Button(master = add2_btn2_frame, text = "Delete",command=DeleteFromTable2)
add2_btn2.pack(expand=True,side='left')


#visualize2 frame
visualize2_frame = tk.Frame(master = window, height=200)
visualize2_frame.pack_propagate(0)
visualize2_frame.pack(fill=tk.X,expand=False)


#add frame
add1_frame = tk.Frame(master = window, height = 125, bg="blue")
add1_frame.pack_propagate(0)
add1_frame.pack(fill='both',expand=True)
#add entry frame
add1_entry_frame = tk.Frame(master = add1_frame, height = 75)
add1_entry_frame.pack_propagate(0)
add1_entry_frame.pack(fill='both',side='top',expand=True)

add1_param1_frame = tk.Frame(master = add1_entry_frame, height = 75, width=267)
add1_param1_frame.pack_propagate(0)
add1_param1_frame.pack(side='left',padx=0,pady=0,expand=True)

add1_param1_lbl = tk.Label(master = add1_param1_frame, text = "Enter model name")
add1_param1_lbl.pack(fill="both",expand=True)

add1_param1_entry = tk.Entry(master = add1_param1_frame)
add1_param1_entry.pack(fill=tk.X,expand=True)

add1_param2_frame = tk.Frame(master = add1_entry_frame, height = 75, width=266)
add1_param2_frame.pack_propagate(0)
add1_param2_frame.pack(side='left',padx=0,pady=0,expand=True)

add1_param2_lbl = tk.Label(master = add1_param2_frame, text = "Enter price")
add1_param2_lbl.pack(fill="both",expand=True)

add1_param2_entry = tk.Entry(master = add1_param2_frame)
add1_param2_entry.pack(fill=tk.X,expand=True)

add1_param3_frame = tk.Frame(master = add1_entry_frame, height = 75, width=267)
add1_param3_frame.pack_propagate(0)
add1_param3_frame.pack(side='left',padx=0,pady=0,expand=True)

add1_param3_lbl = tk.Label(master = add1_param3_frame, text = "Enter producer")
add1_param3_lbl.pack(fill="both",expand=True)

add1_param3_entry = tk.Entry(master = add1_param3_frame)
add1_param3_entry.pack(fill=tk.X,expand=True)

#add buttons frame
add1_buttons_frame = tk.Frame(master = add1_frame, height = 50)
add1_buttons_frame.pack_propagate(0)
add1_buttons_frame.pack(fill='both',side='bottom',expand=True)

add1_btn1_frame = tk.Frame(master = add1_buttons_frame, height = 50, width=400)
add1_btn1_frame.pack_propagate(0)
add1_btn1_frame.pack(side='left',padx=0,pady=0,expand=True)

add1_btn1 = tk.Button(master = add1_btn1_frame, text = "Add", command=AddToTable1)
add1_btn1.pack(expand=True,side='left')

add1_btn2_frame = tk.Frame(master = add1_buttons_frame, height = 50, width=400)
add1_btn2_frame.pack_propagate(0)
add1_btn2_frame.pack(side='left',padx=0,pady=0,expand=True)

add1_btn2 = tk.Button(master = add1_btn2_frame, text = "Delete", command=DeleteFromTable1)
add1_btn2.pack(expand=True,side='left')


#visualize frame
visualize1_frame = tk.Frame(master = window, height=200)
visualize1_frame.pack_propagate(0)
visualize1_frame.pack(fill=tk.X,expand=False)


#delete frame
delete_frame = tk.Frame(master = window, height = 50)
delete_frame.pack_propagate(0)
delete_frame.pack(fill='both',expand=True)

delete_btn1_frame = tk.Frame(master = delete_frame, height = 50, width=400)
delete_btn1_frame.pack_propagate(0)
delete_btn1_frame.pack(side='left',padx=0,pady=0,expand=True)

delete_btn1 = tk.Button(master = delete_btn1_frame, text = "Delete database",command=DeleteDatabase)
delete_btn1.pack(expand=True,side='left')

delete_btn2_frame = tk.Frame(master = delete_frame, height = 50, width=400)
delete_btn2_frame.pack_propagate(0)
delete_btn2_frame.pack(side='left',padx=0,pady=0,expand=True)

delete_btn2 = tk.Button(master = delete_btn2_frame, text = "Clear database",command=ClearDatabase)
delete_btn2.pack(expand=True,side='left')




window.mainloop()



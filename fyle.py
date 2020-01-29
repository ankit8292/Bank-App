from flask import Flask,request,render_template,jsonify
import sqlite3,csv


app=Flask(__name__)
conn = sqlite3.connect("bank.db",check_same_thread=False) #connect to database "bank.db"
cur = conn.cursor()


#creating of table
# cur.execute('''create table details(ifsc text, bank_id int,
# branch text, address text, city text, district text,state text, bank_name text )''')

#insertion of database in bank db
# with open('bank_branches.csv',encoding='utf8') as cs:
#     csv_file=csv.reader(cs,delimiter=',')
#     for element in csv_file:
#         cur.execute("insert into details values(?,?,?,?,?,?,?,?)"),element)
#     conn.commit()
 
@app.route('/ifscdetail', methods=["GET","POST"])
def ifscDetail():
    ifsc=request.form.get('ifsc').strip().upper()
    cur.execute(f"SELECT ifsc,branch,address,city,district,state,bank_name FROM details where ifsc='{ifsc}'")
    x=cur.fetchone()
    if x ==None:
        msg="IFSC Number is not valid"
        return render_template("Error1.html",msg=msg)
    else:
        pass    
       
    return render_template("answer1.html",res=list(x))



@app.route('/citybank', methods=["GET", "POST"])
def cityBankDetail():
    city=request.form.get('city').strip().upper()
    bank=request.form.get('bank').strip().upper()
    cur.execute(f"SELECT ifsc,branch,address,city,district,state,bank_name FROM details where city='{city}' and bank_name='{bank}'")
    x = cur.fetchall()
    if x==[]:
        msg="Invalid Data"
        return render_template("Error2.html",msg=msg)

    else:
        pass
        
    return render_template("answer2.html",res=x)
    
conn.commit()   

@app.route('/')
def homepage():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug="true")
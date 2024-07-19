from flask import Flask,redirect,url_for,render_template,request
import pymysql


conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')


app=Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/attendance-form')
def attendance():
    return render_template('attendance.html')

@app.route("/attendance", methods=["POST"])
def submit_attendance():
    attendanceId=request.form.get("attendance_id")
    attendanceType=request.form.get("attendee_type")
    attendeeId=request.form.get("attendee_id")
    timeIn=request.form.get("timing_in")
    timeOut=request.form.get("timing_out")
    attendanceDate=request.form.get("attendance_date")

    with conn.cursor() as cur:
        sql="INSERT into attendance (attendance_id, attendee_type, attendee_id, timing_in, timing_out, attendance_date) values(%s, %s, %s, %s, %s, %s)"
        values = (attendanceId, attendanceType, attendeeId, timeIn, timeOut, attendanceDate)
        cur.execute(sql,values)
        conn.commit()
    
    return redirect("/attendancetable")



@app.route('/classes-form')
def classes():
    return render_template('classes.html')

@app.route("/classes", methods=["POST"])
def submit_classes():
    classId=request.form.get("class_id")
    courseName=request.form.get("course_name")
    startTime=request.form.get("start_time")
    endTime=request.form.get("end_time")
    
    with conn.cursor() as cur:
        sql="INSERT into classes (class_id, course_name, start_time, end_time) values(%s, %s, %s, %s)"
        values = (classId, courseName, startTime, endTime)
        cur.execute(sql,values)
        conn.commit()
    
    return redirect("/classestable")



@app.route('/courses-form')
def courses():
    return render_template('courses.html')

@app.route("/courses", methods=["POST"])
def submit_courses():
    courseId=request.form.get("course_id")
    name=request.form.get("name")
    duration=request.form.get("duration")
    fees=request.form.get("fees")

    with conn.cursor() as cur:
        sql="INSERT into courses (course_id, name, duration, fees) values(%s, %s, %s, %s)"
        values = (courseId, name, duration, fees)
        cur.execute(sql,values)
        conn.commit()

    return redirect("/coursestable")



@app.route('/enquiry-form')
def enquiry():
    return render_template('enquiryforms.html')

@app.route("/enquiry", methods=["POST"])
def submit_enquiry():
    formId=request.form.get("form_id")
    studentName=request.form.get("student_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    mobile=request.form.get("mobile")
    email=request.form.get("email")
    course=request.form.get("course")
    date=request.form.get("date")

    with conn.cursor() as cur:	
        sql="INSERT into enquiry_forms (form_id, student_name, father_name, mother_name,dob,address,mobile,email,course,date) values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
        values = (formId, studentName, fatherName, motherName,dob,address,mobile,email,course,date)
        cur.execute(sql,values)
        conn.commit()


    return redirect("/enquirytable")



@app.route('/guardians-form')
def gurdians():
    return render_template('guardians.html')

@app.route("/gurdians", methods=["POST"])
def submit_gurdians():
    gurdianId=request.form.get("guardian_id")
    studentId=request.form.get("student_id")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    address=request.form.get("address")
    mobile=request.form.get("mobile")
    email=request.form.get("email")

    with conn.cursor() as cur:
        sql="INSERT into guardians (guardian_id, student_id, father_name, mother_name,address,mobile,email) values(%s, %s, %s, %s,%s,%s,%s)"
        values = (gurdianId, studentId, fatherName, motherName,address,mobile,email)
        cur.execute(sql,values)
        conn.commit()

    return redirect("/gurdianstable")


@app.route('/staff-form')
def staff():
    return render_template('staff.html')

@app.route("/staff", methods=["POST"])
def submit_staff():
    staffId=request.form.get("staff_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    qualification=request.form.get("qualification")
    timing=request.form.get("timing")
    course=request.form.get("course")
    dateOfJoining=request.form.get("date_of_joining")

    with conn.cursor() as cur:
        sql="INSERT into staff (staff_id,first_name,last_name,father_name,mother_name,dob,address,qualification,timing,course,date_of_joining)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (staffId,firstName,lastName,fatherName,motherName,dob,address,qualification,timing,course,dateOfJoining)
        cur.execute(sql,value)
        conn.commit()
    
    return redirect('/stafftable')


@app.route('/students-form')
def students():
    return render_template('students.html')

@app.route("/students", methods=["POST"])
def submit_students():
    studentId=request.form.get("student_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    course=request.form.get("course")
    mobile=request.form.get("mobile")
    email=request.form.get("email")
    photo = request.files['photo']
    photo.save('image/ ' + photo.filename)
    path='image/ ' + photo.filename

    with conn.cursor() as cur:
        sql="INSERT into students (student_id, first_name, last_name, father_name, mother_name, dob, address, course, mobile, email, photo) values(%s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s)"
        values = (studentId, firstName, lastName, fatherName, motherName, dob, address, course, mobile, email, path)
        cur.execute(sql,values)
        conn.commit()
    
    return redirect("/studentstable") 



@app.route('/teachers-form')
def teachers():
    return render_template('teachers.html')


@app.route('/teachers', methods=["POST"])
def submit_teachers():
    teacherId=request.form.get("teacher_id")
    firstName=request.form.get("first_name")
    lastName=request.form.get("last_name")
    fatherName=request.form.get("father_name")
    motherName=request.form.get("mother_name")
    dob=request.form.get("dob")
    address=request.form.get("address")
    salary=request.form.get('salary')
    qualification=request.form.get('qualification')
    timing=request.form.get('timing')
    course=request.form.get('course')
    dateOfJoining=request.form.get('date_of_joining')
    

    

    with conn.cursor() as cur:
        sql="INSERT into teachers (teacher_id,first_name,last_name,father_name,mother_name,dob,address,salary,qualification,timing,course,date_of_joining)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (teacherId,firstName,lastName,fatherName,motherName,dob,address,salary,qualification,timing,course,dateOfJoining)
        cur.execute(sql,value)
        conn.commit()


    return redirect("/teacherstable")
    

@app.route("/attendancetable")
def attendancetable():
    with conn.cursor() as cur:
        sql = "select * from attendance"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("attendancetable.html",datas=data)


@app.route("/classestable")
def classestable():
    with conn.cursor() as cur:
        sql = "select * from classes"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("classestable.html", datas=data)




@app.route("/coursestable")
def coursestable():
    with conn.cursor() as cur:
        sql = "select * from courses"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("coursestable.html" , datas=data)



@app.route("/enquirytable")
def enquirytable():
    with conn.cursor() as cur:
        sql = "select * from enquiry_forms"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("enquirytable.html" , datas=data)


@app.route("/gurdianstable")
def gurdianstable():
    with conn.cursor() as cur:
        sql = "select * from guardians"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("guardianstable.html" , datas=data)


@app.route("/stafftable")
def stafftable():
    with conn.cursor() as cur:
        sql = "select * from staff"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("stafftable.html" , datas=data)


@app.route("/studentstable")
def studentstable():
    with conn.cursor() as cur:
        sql = "select * from students"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("studentstable.html" , datas=data)


@app.route("/teacherstable")
def teacherstable():
    with conn.cursor() as cur:
        sql = "select * from teachers"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("teacherstable.html" , datas=data)


@app.route("/delete/<id>")
def attendancedelete(id):
    with conn.cursor() as cur:
        sql="delete from attendance where attendance_id=%s"
        value = (id)
        cur.execute(sql,value)
        return redirect("/attendancetable")
    

@app.route("/delete/<id>")
def classesdelete(id):
    with conn.cursor() as cur:
        sql="delete from classes where class_id=%s"
        value = (id)
        cur.execute(sql,value)
        return redirect("/classestable")
    

@app.route("/delete/<id>")
def  coursesdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from courses where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/coursestable")
    

@app.route("/delete/<id>")
def  enquirydelete(id):
   
    with conn.cursor() as cur:
        sql="delete from enquiry_forms where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/enquirytable")

@app.route("/delete/<id>")
def  guardiansdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from guardians where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/guardianstable")

@app.route("/delete/<id>")
def  staffdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from staff where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/stafftable")

@app.route("/delete/<id>")
def  studentsdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from students where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/studentstable")

@app.route("/delete/<id>")
def  teachersdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from teachers where class_id=%s"
        values=(id)


        cur.execute(sql,values)
        return redirect("/teacherstable")



 
if __name__=='__main__':
    app.run(debug=True)
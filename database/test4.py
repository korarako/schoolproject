import pymysql

conn = pymysql.connect(host="localhost", user="root", password="zxgsh023-72384y", database="st")


def main():
    cursor = conn.cursor(pymysql.cursors.SSCursor)
    return cursor


def add_student():  # 插入学生记录
    cursor = main()
    sclass = input('班号：')
    sno = input('学号：')
    sname = input('姓名：')
    ssex = input('性别：')
    sage = int(input('年龄：'))
    sdept = input('系：')
    add = cursor.execute('insert into stu (sclass, sno, sname, ssex, sage, sdept) values(%s,%s,%s,%s,%s,%s)',
                         (sclass, sno, sname, sage, ssex, sdept))
    if add >= 1:
        conn.commit()
        print('插入成功！')
    else:
        print('插入失败！')


def q_by_sno_s():
    cursor = main()
    choice_cls = input('请输入班号：')
    choice_id = input('请输入学号：')
    cursor.execute('select S.sclass,S.sno,sname,ssex,sage,sdept,cname,grade '
                   'from S,SC,C where S.sno =%s and S.sclass=%s'
                   'and S.sclass=SC.sclass and S.sno=SC.sno and SC.cno=C.cno', (choice_id, choice_cls))
    students = cursor.fetchall()
    for stu in students:
        print(stu[0], stu[1], stu[2], stu[3], stu[4], stu[5], stu[6], stu[7])
        print('查询成功')
        re = input('是否继续查询(y/n)：')
        if re == 'y':
            q_by_sno_s()
        else:
            return


def q_all_s():
    cursor = main()
    cursor.execute('select S.sclass,S.sno,sname,ssex,sage,sdept,cname,grade '
                   'from S,SC,C where S.sclass=SC.sclass and S.sno=SC.sno and SC.cno=C.cno')
    students = cursor.fetchall()
    for student in students:
        print('\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[0], student[1], student[2], student[3], student[4],
                                                        student[5], student[6], student[7]))


def query_student():  # 查询的菜单
    while True:
        print('查询学生记录')
        print('================')
        print('1、按学号查询学生记录')
        print('2、查询全部学生记录')
        print('3、返回上级菜单')
        print('=================')
        mc3 = int(input('请输入查询的菜单号：'))
        if mc3 == 1:
            q_by_sno_s()
        elif mc3 == 2:
            q_all_s()
        else:
            break


def print_student():  # 显示所有的学生记录
    cursor = main()
    cursor.execute('select * from S')
    students = cursor.fetchall()
    for stu in students:
        print(stu[0], stu[1], stu[2], stu[3], stu[4], stu[5])


def delete_student():
    cursor = main()
    cls = input('输入想要删除学生的班号：')
    sid = input('输入想要删除学生的学号：')
    delete = cursor.execute('delete from S where sno =%s and sclass=%s', (sid, cls))
    if delete == 1:
        conn.commit()
        print('删除成功！')
    else:
        print('删除失败！')


def delete1_student():
    print('============================')
    print('1、删除学生所有信息')
    print('2、回到初始界面')
    print('============================')
    mc4 = int(input('Input menu number:'))
    if mc4 == 1:
        delete_student()
    elif mc4 == 3:
        login()


def menu_s():
    while True:
        print('学生信息管理系统')
        print('================')
        print('1、增加学生记录')
        print('2、查询学生记录')
        print('3、修改学生记录')
        print('4、删除学生记录')
        print('5、显示所有的学生记录')
        print('6、返回上级菜单')
        print('=================')
        mc2 = int(input('输入菜单号：'))
        if mc2 == 1:
            add_student()
        elif mc2 == 2:
            query_student()
        elif mc2 == 3:
            update_student()
        elif mc2 == 4:
            delete_student()
        elif mc2 == 5:
            print_student()
        else:
            break


def login():
    # administartor = input('请输入用户名：')
    # password = input('请输入密码：')
    # if administartor == 'korako' and password == 'korako':
    # print("恭喜你成功登录系统!!")
    while True:
        print('学生信息管理系统')
        print('================')
        print('1、增加学生记录')
        print('2、查询学生记录')
        print('3、修改学生记录')
        print('4、删除学生记录')
        print('5、显示所有的学生记录')
        print('6、返回上级菜单')
        print('=================')
        mc2 = int(input('输入菜单号：'))
        if mc2 == 1:
            add_student()
        elif mc2 == 2:
            query_student()
        elif mc2 == 3:
            update_student()
        elif mc2 == 4:
            delete_student()
        elif mc2 == 5:
            print_student()
        else:
            break
    # else:
        # print('账号或密码错误！')


def update_student():
    cursor = main()
    curr = input('请输入想要修改学生的班号：')
    cur = input('请输入想要修改学生的学号：')
    print('==============')
    print('1、修改姓名')
    print('2、修改性别')
    print('3、修改年龄')
    print('4、修改班级')
    print('5、修改系')
    print('6、返回上级菜单')
    print('==============')
    mc2 = int(input('请输入菜单号：'))
    if mc2 == 1:
        name = input('请输入修改后的名字：')
        a = cursor.execute('update S set sname=%s where sno =%s and sclass=%s', (name, cur, curr))
        if a == 1:
            conn.commit()
            print('修改成功！')
        else:
            print('修改失败！')
    elif mc2 == 2:
        gender1 = input('请输入修改后的性别：')
        a = cursor.execute('update S set ssex=%s where sno =%s and sclass=%s', (gender1, cur, curr))
        if a == 1:
            conn.commit()
            print('修改成功！')
        else:
            print('修改失败！')
    elif mc2 == 3:
        age1 = input('请输入修改后的年龄：')
        a = cursor.execute('update S set sage=%s where sno =%s and sclass=%s', (age1, cur, curr))
        if a == 1:
            conn.commit()
            print('修改成功！')
        else:
            print('修改失败！')
    elif mc2 == 4:
        class1 = input('请输入修改后的班级：')
        a = cursor.execute('update S set sclass=%s where sno =%s and sclass=%s', (class1, cur, curr))
        if a == 1:
            conn.commit()
            print('修改成功！')
        else:
            print('修改失败！')
    elif mc2 == 5:
        major1 = input('请输入修改后的专业：')
        a = cursor.execute('update S set sdept=%s where sno =%s and sclass=%s', (major1, cur, curr))
        if a == 1:
            conn.commit()
            print('修改成功！')
        else:
            print('修改失败！')
    else:
        login()


while True:
    print('请选择以下菜单号:')
    print('=========' * 3)
    print('1、登录学生信息管理系统')
    print('2、退出学生信息管理系统')
    print('=========' * 3)
    mc1 = int(input('输入菜单号：'))
    if mc1 == 1:
        login()
    elif mc1 == 2:
        print('感谢使用学生信息管理系统！')
        break

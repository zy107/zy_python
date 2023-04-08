# 赵洋
# 开发时间：2023/3/18
#学生管理系统
def main_print():
    print('='*25)
    print("学生管理系统 V10.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询所有学生信息")
    print("0.退出系统")
    print('='*25)
k=[]
#添加
def stu_add():
    #new_id=int(input("请输入学生学号:"))
    new_name=input("请输入学生姓名:")
    new_gender=input("请输入学生性别:")
    new_num=int(input("请输入联系方式:"))
    new_home=input("请输入住址:")
    new_dict={'name':new_name,'gender':new_gender,'num':new_num,'home':new_home}
    k.append(new_dict)
    print(k)
#删除
def stu_del():
    #del_id=int(input("请输入删除的学号:"))
    del_name=input("请输入删除的名字:")
    global k
    for i in k:
        if del_name==i['name']:
            print(i)
            k.remove(i)
            print("已删除")
            break
        else:
            print("用户信息有误，重新操作")
        print(k)
#修改
def stu_chg():
    chg_name=input("请输入要修改的学生姓名:")
    global k
    for i in k:
        if chg_name==i['name']:
            print(i)
            while True:
                t=input("请输入要修改的内容:")
                if t=='name':
                    i['name']=input("请输入新名字:")
                    print(i)
                    return
                    break
                elif t=='gender':
                    i['gender']=input("请输入新性别:")
                    print(i)
                    return
                    break
                elif t=='num':
                    i['num']=input("请输入新号码:")
                    print(i)
                    return
                    break
                elif t=='home':
                    i['home']=input("请输入新地址:")
                    print(i)
                    return
                    break
                else:
                    print("输入出错，请重新输入")
        else:
            print("输入出错，请重新输入")
    print("输入的信息不存在")

#查找
def stu_find():
    global k
    find_name=input("请输入要查找的姓名:")
    for i in k:
        if find_name==i['name']:
            print(f'姓名为{i["name"]},性别为{i["gender"]},号码为{i["num"]},地址为{i["home"]}')
            return
    print('查找不存在')

while True:
    main_print()
    num=int(input("请输入对应功能序号:"))
    if num==1:
        stu_add()
    elif num==2:
        stu_del()
    elif num==3:
        stu_chg()
    elif num==4:
        stu_find()
    elif num==0:
        s=input("确定要退出吗？y/n")
        if s=='y':
            break
    else:
        print("序号有误，重新输入")
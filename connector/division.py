#分队算法

from copy import *
import numpy
import time
from itertools import combinations
from quanzhong import sda

def operation(list):#判别牌型，返回牌型对应数字与此牌型中关键牌值
    sum=[0,0,0];
    a=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    for list1 in list:
        for count in range(5):
            if a[count][0]==list1[0]:
                a[count][1]=a[count][1]+1
                break
            elif a[count][0]==0:
                a[count][0] = list1[0]
                a[count][1] = a[count][1] + 1
                break

        count=0
    if(list[0][0]+4==list[1][0]+3==list[2][0]+2==list[3][0]+1==list[4][0]):
        if list[0][1]==list[1][1]==list[2][1]==list[3][1]==list[4][1]:
            sum=[10,list[4][0]]#同花顺
            return sum
    else:
        count=0
        for jojo in a:
            if jojo[1]==4:
                sum= [9,jojo[0]]#炸弹
                return sum
            elif jojo[1]==3:
                    if a[a.index(jojo)+1][1]==2:
                        sum= [8,jojo[0]]#葫芦
                        return sum
                    elif list[0][1]==list[1][1]==list[2][1]==list[3][1]==list[4][1]:
                        sum=[7,list[4][0],list[3][0]]#同花
                        return sum
                    elif (list[0][0] + 4 == list[1][0] + 3 == list[2][0] + 2 == list[3][0] + 1 == list[4][0]):
                        sum=[6,list[4][0],list[3][0]]#顺子
                        return sum
                    else :
                        sum=[5,jojo[0]]#三条
                        return sum
            elif jojo[1]==2:
                if a[1][1]==3:
                    sum= [8,a[1][0]]#葫芦
                    return sum
                elif list[0][1] == list[1][1] == list[2][1] == list[3][1] == list[4][1]:
                    sum =[7, list[4][0],list[3][0]] # 同花
                    return sum
                elif (list[0][0] + 4 == list[1][0] + 3 == list[2][0] + 2 == list[3][0] + 1 == list[4][0]):
                    sum = [6,list[4][0]]  # 顺子
                    return sum
                elif a[a.index(jojo)+1][1]==2:
                    if jojo[0]+1==a[a.index(jojo)+1][0]:
                        sum= [4,a[a.index(jojo)+1][0]]#连队
                        return sum
                    else:
                        sum=[3,a[a.index(jojo)+1][0]] #两对
                        return sum
                elif a[a.index(jojo)+2][1]==2:
                    sum =[3 ,a[a.index(jojo)+2][0]] # 两对
                    return sum
                else:
                    sum=[2,jojo[0]] #对子
                    return sum
        if list[0][1] == list[1][1] == list[2][1] == list[3][1] == list[4][1]:
            sum =[7 ,list[4][0] ,list[3][0]]# 同花
            return sum
        elif (list[0][0] + 4 == list[1][0] + 3 == list[2][0] + 2 == list[3][0] + 1 == list[4][0]):
            sum =  [6 ,list[4][0]] # 顺子
            return sum

        else:
            sum =  [1,list[4][0]]
            return sum
    if list[0][1] == list[1][1] == list[2][1] == list[3][1] == list[4][1]:
        sum =[7,list[4][0]]   # 同花
        return sum
    elif (list[0][0] + 4 == list[1][0] + 3 == list[2][0] + 2 == list[3][0] + 1 == list[4][0]):
        sum = [6 ,list[4][0]] # 顺子
        return sum

    else:
        sum =  [1,list[4][0]]
        return sum
    return sum
def jiema(dun):#将分好的三墩转码为列表
    str1=""
    s=[]
    for x in dun:
        for y in x:
            if y[0]==11:
                y[0]="J"
            elif y[0]==12:
                y[0]="Q"
            elif y[0] == 13:
                y[0] = "K"
            elif y[0] == 14:
                y[0] = "A"
            if y[1]==1:
                str1=str1+"$"+str(y[0])+" "
            elif y[1]==2:
                str1=str1+"&"+str(y[0])+" "
            elif y[1] == 3:
                str1 = str1 + "#" + str(y[0]) + " "
            elif y[1]==4:
                str1=str1+"*"+str(y[0])+" "
        s=s+[str1]
        str1=""
    s[1]=s[1][0:-1]
    s[0]=s[0][0:-1]
    s[2]=s[2][0:-1]
    return s
def ope(list3):#求前墩的牌型，返回值与operation（）相同
    sum=0
    if list3[0][0]==list3[1][0]==list3[2][0]:
        sum=[5,list3[2][0]]
        return sum
    elif list3[0][0]==list3[1][0]:
        sum=[2,list3[1][0]]
        return sum
    elif list3[2][0]==list3[1][0]:
        sum=[2,list3[1][0]]
        return sum
    else:
        sum=[1,list3[2][0]]
        return sum
def get_type(value):#将对应数据转化为牌型名
    if value==10:
        return "同花顺"
    elif value==9:
        return "炸弹"
    elif value==8:
        return "葫芦"
    elif value==7:
        return "同花"
    elif value==6:
        return "顺子"
    elif value==5:
        return "三条"
    elif value==4:
        return "连对"
    elif value==3:
        return "两对"
    elif value==2:
        return "对子"
    elif value==1:
        return  "散牌"
    else :
        return "出错!!!"
def do(lll):#算法主函数，执行分墩步骤
    card=lll
    card_type=["","",""]
    mmm = 0
    matrix=[[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,],[0,0,]]
    dun=[[],[],[]]
    j=0;
    a=0;
    max=0
    for pai in card:
        if pai=="*":i=4;
        elif  pai=="$":i=1;
        elif pai == "&":
            i = 2;
        elif pai=="#":i=3;
        if pai.isdigit():
            if pai=="1":matrix[j][0]=10;matrix[j][1]=i;j=j+1;
            elif pai!="0":matrix[j][0]=int(pai);matrix[j][1]=i;j=j+1;
        elif pai=="J":matrix[j][0]=11;matrix[j][1]=i;j=j+1;
        elif pai=="Q":matrix[j][0]=12;matrix[j][1]=i;j=j+1;
        elif pai=="K":matrix[j][0]=13;matrix[j][1]=i;j=j+1;
        elif pai=="A":matrix[j][0]=14;matrix[j][1]=i;j=j+1;

    for i in combinations(matrix, 5):
        sum=0;
        test= list(i)
        test_data1 = matrix.copy()
        test = sorted(test, key=lambda x: (x[0], -x[1]))
        if test[0] in test_data1:
            test_data1.remove(test[0])
        if test[1] in test_data1:
            test_data1.remove(test[1])
        if test[2] in test_data1:
            test_data1.remove(test[2])
        if test[3] in test_data1:
            test_data1.remove(test[3])
        if test[4] in test_data1:
            test_data1.remove(test[4])
        for k in combinations(test_data1, 5):
            test_data2=test_data1.copy()
            if k[0] in test_data2:
                test_data2.remove(k[0])
            if k[1] in test_data2:
                test_data2.remove(k[1])
            if k[2] in test_data2:
                test_data2.remove(k[2])
            if k[3] in test_data2:
                test_data2.remove(k[3])
            if k[4] in test_data1:
                test_data2.remove(k[4])
            pp=list(k)
            test1=list(sorted(pp, key=lambda x: (x[0], -x[1])))
            test2=list(sorted(test_data2,key=lambda x: (x[0], -x[1])))
            list1=list(operation(test))
            list2=list(operation(test1))
            list3=list(ope(test2))
            if list1[0] < list2[0] or list2[0] < list3[0] or list1[0] == list2[0] and list1[1] < list2[1] or list3[0] ==list2[0] and list2[1] < list3[1]or (list1[0]==list2[0]==7and list1[2]<list2[2]):
                continue
            else:
                value1 = sda[list1[0] - 1][2][list1[1] - 1]
                value2 = sda[list2[0] - 1][1][list2[1] - 1]
                value3 = sda[list3[0] - 1][0][list3[1] - 1]

                sum = value1 + value2 + value3
                if sum > max:
                    dun = [test2, test1, test]
                    max = sum
                    card_type[2] = get_type(list1[0])
                    card_type[1] = get_type(list2[0])
                    card_type[0] = get_type(list3[0])
                    max1 = value1
                    max2 = value2
                    max3 = value3
    s = jiema(dun)
    #print(max1)#103991
   # print(max2)
    #print(max3)
    # print(dun)
    #print(max)
    s=s+["三墩牌型："]+card_type
    print(s)
    return s

lll="&10 &5 #9 &9 $A *Q &8 $4 #4 #Q *9 $J $5"
do(lll)
#l=[[10, 4], [10, 1], [5, 2], [13, 4], [13, 2]]
#print(operation(l))
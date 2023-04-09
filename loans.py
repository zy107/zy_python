year=int(input('请输入贷款年限:'))

if year>5:
    way=str(input("请输入贷款类型:"))
    if way=='sy':
        ll=0.0490
    elif way=='gjj':
        ll=0.0325
elif 0<year<=5:
    way = str(input("请输入贷款类型:"))
    if way == 'sy':
        ll=0.0475
    elif way == 'gjj':
        ll=0.0275
else:
    print("输入错误！")

mll=ll/12#月利率
m=12*year#月数
money=int(input("请输入贷款金额:"))
mlx=mll*money#月利息
myg=money*mll*pow(1+mll,m)/(pow((1+mll),m)-1)#月月供
ze=myg*year*12#还款总额
lx=ze-money#总利息
print('贷款的每月月供为:%.2f元,总利息为:%.2f元,还款总额为:%.2f元'%(myg,lx,ze))

year=int(input('请输入贷款年限:'))
if year>5:
    way=str(input("请输入贷款类型:"))

    if way=='mix':
        mll_1=0.0490/12
        mll_2=0.0325/12

elif 0<year<=5:
    way = str(input("请输入贷款类型:"))
    if way == 'mix':
        mll_1=0.0475/12
        mll_2=0.0275/12

m_1=int(input("请输入商业贷款金额:"))
m_2=int(input("请输入公积金贷款金额:"))
mlx_1=mll_1*m_1
mlx_2=mll_2*m_2
myg_1=m_1*mll_1*pow(1+mll_1,12*year)/(pow((1+mll_1),12*year)-1)
myg_2=m_2*mll_2*pow(1+mll_2,12*year)/(pow((1+mll_2),12*year)-1)
ze_1=myg_1*year*12
ze_2=myg_2*year*12
lx_1=ze_1-m_1
lx_2=ze_2-m_2
print('混合贷款的每月月供为:%.2f元,总利息为:%.2f元,还款总额为:%.2f元'%(myg_1+myg_2,lx_1+lx_2,ze_1+ze_2))

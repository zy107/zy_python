s = 'Hello,everyone,Today,LetUsLEARNPython'
count=0
for i in s:
    if i>='a' and i<='z':
        count+=1
print(count)
s2=s.upper()
print(s2)

print('*'*40)
print("操作  ITEM")
print("替换  1")
print("结束  0")
print('*'*40)

while True:
    n=input("请输入想执行的操作：")
    if n=='1':
        ch1=str(input("请输入要替换掉的字符:"))
        ch2=str(input("请输入替换为的字符:"))
        s3 = s2.replace(ch1,ch2)
        print(f'新字符串为:{s3}')
    else:
        break
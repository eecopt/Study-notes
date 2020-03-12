#!/user/bin/python
#-*- coding : utf-8 -*-
sorce = int (input('请输入分数'))
if sorce >=90:
    grade='A'
if sorce>=80:
    grade ='B'
if sorce >=60:
    grade='C'
else:
    grade='D'
print('%d 属于%s'%(sorce,grade))

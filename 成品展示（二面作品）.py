#前面有登录验证身份，防止无限刷。这东西不会敲。
print('请问您愿意提供一些信息吗?愿意的话我们会在问答结束后提供抽奖')
print('愿意请扣1，不愿意请扣2')
a=int(input())
if a==1:
 print('感谢您的参与')
 print('接下来的问题您可选择不回答')
 print('请输入您的姓名，若不方便透露，请输入3')
 b=input()
 if ('3') in b:
     d=1
 else:
     d=0
 print('请输入您的电话号码，若不方便透露，请输入4')
 c=int(input())
 if c==4:
     d=d+1
 else:
     d=d+0
 print('您愿意以后接受我们的信息以获取最新最好的服务吗？')
 print('愿意请输入 true，不愿意请输入 false')
 e=input()
 if ('true') in e:
     e=1
 else:
     e=0
 if e==0:
     d=d+1
 else:
     d=d+0
 print('恭喜完成所有答卷，接下来进入抽奖环节')
 if d==3:
     f=7
 elif d==2:
     import random
     f=random.randint(0,6)
 elif d==1:
     import random
     f=random.randint(0,4)
 else:
     import random
     f=random.randint(0,2)
 if f==0:
     print("天选之子，一等奖")
 elif f==1:
     print("运气爆棚，二等奖")
 elif f==7:
     print('恭喜抽到笔芯 ❤')
 elif f==2:
     print('基操勿6，三等奖')
 else:
     print('天降正义，被黑了?')
else:
 print('打扰了')

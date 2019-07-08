print('Welcome to my ATM')
a=input('Enter your name:-')
b=int(input('Enter your pass code:-'))

users=['anul','chirag','prajjwal','Hritik']
pas=[111,222,333,444]
amo=[100,500,1000,400]

for i in range(0,len(users)):
    if(a in users):
        if(b==pas[i]):
            print('login succesfully')
            e=pas.index(b)   #give me endex of pass
            #print(e)
            c=input('WHAT DO YOU WANT:-Withdraw,Check_balance,Deposit_money=')
            if(c=='Withdraw'):
                print("enter amount")
                d=int(input("ENTER THE AMOUNT"))
                if(d<=amo[e]):
                    print('cash withdraw is in process')
                else:
                    print('Ensufficent balance')

            if(c=='Check_balance'):
                print(amo[e])

            if(c=='Deposit_money'):
                f=int(input('ENTER THE AMOUNT U WANT TO DEPOSIT='))
                print('succesfully deposit')
                print('new balance=',f+amo[e])
                
            break
    else:
        print('invalid name')
#withdraw
#check balance
#deposit




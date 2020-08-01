import copy,sys
from collections import Counter
def count(n1,n2):
    try:
        if type(n1)==int or type(n2)==int:
           raise ValueError
        elif int(n1) or int(n2):
           raise ValueError
    except ValueError:
        return "Oops! Your Input Must be string.. Try again!!"
    n1=n1.split()
    n2=n2.split()
    name1=[i for i in n1 if len(i)>1]
    name2=[i for i in n2 if len(i)>1]
    if len(name1)<1 or len(name2)<1:
        sys.exit("Please provide Valid names")
    n1=''.join(name1)
    n2=''.join(name2)
    n1=n1.lower()
    n2=n2.lower()
    n1=sorted(n1)
    n2=sorted(n2)
    freq1=dict(Counter(n1))
    freq2=dict(Counter(n2))
    c=copy.deepcopy(freq1)
    c1=copy.deepcopy(freq2)
    for (char,count), (char1,count1) in zip(c.items(), c1.items()):
        if len(n1)>len(n2):
            if char1 in c.keys():
                freq1[char1]=abs(c1[char1]-c[char1])
                freq2[char1]=0
            else:
                freq2[char1]=1
        else:
            if char in c1.keys():
                freq1[char]=abs(c1[char]-c[char])
                freq2[char]=0
            else:
                freq1[char]=1
    res=sum(freq2.values())+sum(freq1.values())
    return res
    
def flames(n1,n2):
    c=count(n1,n2)
    try:
        if type(c)==str:
           raise ValueError
    except ValueError:
        return "Oops! Your Input Must be string.. Try again!!"
    dic={'F':"Friends",'L':"Love",'A':"Affection",'M':"Marriage",'E':"Enemy",'S':"Sister"}
    lst=['F','L','A','M','E','S']
    new_lst=[]
    for i in range(6,0,-1):
        r=c%i
        if r!=0:
            if len(new_lst)==1:
                break
            if len(lst)==0:
                break
            lst.pop(r-1)
            new_lst=lst[r-1:]
            if r>=2 :
                for r in range(r-1):
                    new_lst.append(lst[r])
            lst=new_lst
        elif r==0:
            if len(new_lst)==1:
                break
            if len(lst)==0:
                break
            lst.pop(-1)
            new_lst=lst[r:]
            lst=new_lst
    return "The Relation between {} and {} is {}".format(''.join(n1),''.join(n2),dic.get(''.join(lst),"Sorry"))


        

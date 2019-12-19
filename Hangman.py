class node:
    def __init__(s,data="-",datacheck="-"):
        s.data=data
        s.datacheck=datacheck
        s.next=None
class game:
    def __init__(s):
        s.head=node()
    def insert(s,a):
        n=len(a[0])


        pos=s.head
        i=0
        while(i<n):
            newnode=node(a[0][i])
            pos.next=newnode
            pos=pos.next
            i=i+1
    def display(s):
        pos=s.head.next
        print()
        while(pos!=None):
            print(pos.datacheck,end="")
            pos=pos.next
        print()
    def play(s,b,h):
        flag=0
        pos=s.head.next
        while(pos!=None):
            if(pos.data==b):
                pos.datacheck=b
                flag=1
            pos=pos.next
        if(flag==0):
            h.pop(0)
        pos=s.head.next
        while(pos!=None):
            print(pos.datacheck,end="")
            pos=pos.next
        print(h)
    def viewanswer(s):
        import time
        pos=s.head.next
        print("ANSWER IS...")
        time.sleep(2.0)
        while(pos!=None):
            print(pos.data,end="")
            pos=pos.next
def option():

 g=game()
 print("Type 'view' to view answer")
 print("Type 'exit' to EXIT")
 l=["python","jumble","easy","difficult","computer","hangman","failure","brilliant","worthy","xylophone","awkward","gypsy","jinx","burgular","bankrupt","crisis","hyphen","memento","mystery","pajama","pixel","rogue","rhythmic","twelfth","jealous","zombie","yatch","yak","zippy","unknown","battleground","player","psycho","beast","buzzard","boycott","coffin","witchcraft","rickshaw","mnemonic","pneumonia","peekaboo","diarrhoea","jaundice","gossip","despacito"]
 import random
 a=[]
 a.append(random.choice(l))
 g.insert(a)
 g.display()
 o=None
 h=["H","A","N","G","M","A","N"]
 while((o!="exit" and o!="view") and len(h)!=0):
     o=input()
     if(o!="exit" and o!="view"):
         g.play(o,h)
     elif(o=="view"):
         g.viewanswer()
         break
     elif(o=="exit"):
         print("Exiting...")
         break
option()
k=None
while(k!="no"):
    print()
    print("1.PLAY")

    k=(input("Do you want to play again"))
    if(k=="yes" or k=="Yes" or k=="YES"):
        option()
    else:
        break

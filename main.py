import re
Entities=[]
while True:
    newAddition=input("Enter the name and the roll then hit enter, type 'done'when you dont need to add more Example 'RedDragon-15'")
    if "done" in newAddition.lower():
        break
    if " " in newAddition:
        print("Don't type your answer with spaces / your answer was not recorded")
    if "-" in newAddition==False:
        print("you need to put a '-' inbetween the name and the roll")
    else:
        newAdditionSplit=re.split(r'[-]',newAddition)
        if newAdditionSplit[0].isalpha() and newAdditionSplit[1].isdigit():
            newAdditionTuple=(newAdditionSplit[0],newAdditionSplit[1])
            Entities.append(newAdditionTuple)
        else:
            print("You did not format your entry correctly and your addition was not recorded")
Entities.sort(key = lambda x: int(x[1]),reverse=True)
count=0
while True:  
    if count>=len(Entities):
        count=0
    tempTuple=Entities[count]
    print("it is",tempTuple[0],"turn!")
    count+=1
    throwawayinput=input("Hit enter to go to the next, or type add and hit enter to add a new entity")
    if "add" in throwawayinput.lower():
            newAddition=input("Enter the name and the roll then hit enter, type 'done'when you dont need to add more Example 'RedDragon-15'")
            if "done" in newAddition.lower():
                break
            if " " in newAddition:
                print("Don't type your answer with spaces / your answer was not recorded")
            if "-" in newAddition==False:
                print("you need to put a '-' inbetween the name and the roll")
            else:
                newAdditionSplit=re.split(r'[-]',newAddition)
                if newAdditionSplit[0].isalpha() and newAdditionSplit[1].isdigit():
                    newAdditionTuple=(newAdditionSplit[0],newAdditionSplit[1])
                    Entities.append(newAdditionTuple)
                    Entities.sort(key = lambda x: int(x[1]),reverse=True)
                else:
                    print("You did not format your entry correctly and your addition was not recorded")
    elif len(throwawayinput)==0:
        continue 
        
        
        
   
        
            

        

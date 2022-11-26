import random 
#r ≥ s, s ≥ p
#p ≥ r
def play ():
    user = input ("Go choose : 'r' for rock ,'p' for paper , 's' for scissors : ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'null'
    
    if win(user,computer):
        return'You win'
    
    
    return 'You lost' 
    
def win (play,opp):
    #true if win 
    if(play == 'r'and  opp == 's') or (play=='s' and opp =='p') or (play== 'p' and opp=='r'):
        return True
    
    
print (play())
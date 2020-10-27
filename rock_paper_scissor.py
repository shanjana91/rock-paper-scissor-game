import random

print('ROCK , PAPER , SCISSORS !!!')
print('')
name=input('Enter your name:')
print('')
print('WELCOME',name)
print('player1:',name)
print('player2:computer')
print('')
print('''Rules:
Total no.of rounds:5
Best of 5 wins the game''')
print('')
print('Ready to go... 3,2,1')

p_count=0
c_count=0
#round=0
choice='yes'
#flag=False
while choice=='yes':
     
     for i in range(1,6):
         print('')
         print('ROUND:',i)
         print('')
         player=input("rock,paper,scissor????")
         
         if player=='rock' or player=='paper' or player=='scissor':
             computer=random.choice(['rock','paper','scissor'])
             print('computer:',computer)
             if computer==player:
                 print('Thats a tie!!!')
         
             if player=='rock':
                 if computer=='scissor':
                     print(name,'gets a point')
                     p_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count)
             
                 if computer=='paper':
                     print('computer gets a point')
                     c_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count)
         
             if player=='paper':
                 if computer=='scissor':
                     print('computer gets a point')
                     c_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count)
                 if computer=='rock':
                     print(name,'gets a point')
                     p_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count) 
        
             if player=='scissor':
                 if computer=='rock':
                     print('computer gets a point')
                     c_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count)
                 if computer=='paper':
                     print(name,'gets a point')
                     p_count+=1
                     print('')
                     print(name,':',p_count,'computer:',c_count) 
          
             print('')
             print('')
         
         else:
             print('Round skipped due to incorrect spelling! Be careful with your spelling!') 
           #  flag=True
     #print(p_count,c_count)       
     if p_count>c_count:
         print('FINAL SCORE:')
         print(name,':',p_count,'computer:',c_count)
         print('YAY!!! YOU WON') 
     elif p_count==c_count and c_count!=0 and p_count!=0:
         print('Thats a TIE !')
     elif p_count==0 and c_count==0:
         print("You lost due to Incorrect Spellings")
     else:
         print('FINAL SCORE:')
         print(name,':',p_count,'computer:',c_count)
         print('YOU LOST ! TRY AGAIN') 
        
     print('')
     choice=input('Want to play again??? (yes/no)')
else:
     print('Thanks for playing!')     

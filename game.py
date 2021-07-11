import random

class Game:
    def computer_input(self):
        computer_choice = random.randint(0,2)
        
        if computer_choice == 0:
            computer_choice = 'K'
        elif computer_choice == 1:
            computer_choice = 'P'
        elif computer_choice == 2:
            computer_choice = 'N'

        
        print("Komputer wybral!")
        return computer_choice
    
    def user_input(self):
        
        user_choice = str(input("Jaki symbol chcesz wybrac? K, P, N?"))
        if user_choice == 'K' or 'P' or 'N':
            pass
            return user_choice 
        
        else: 
            print ('Wybierz poprawny symbol idioto!')
        
    
    def run(self, wybor1, wybor2):
        
        print("Gra siê rozpoczyna")
        
        if wybor1 == wybor2:
            print (f'{wybor1} : {wybor2}')
            print('Remis')
        elif wybor1=='K' and wybor2 =='P':
            print (f'{wybor1} : {wybor2}')
            print ('Komp Wins')
        elif wybor1=='P' and wybor2 =='N':
            print (f'{wybor1} : {wybor2}')
            print ('Komp Wins')
        elif wybor1=='N' and wybor2 =='K':
            print (f'{wybor1} : {wybor2}')
            print ('Komp Wins')
        elif wybor2=='K' and wybor1 =='P':
            print (f'{wybor1} : {wybor2}')
            print ('User Wins')
        elif wybor2=='P' and wybor1 =='N':
            print (f'{wybor1} : {wybor2}')
            print ('User Wins')
        elif wybor2=='N' and wybor1 =='K':
            print (f'{wybor1} : {wybor2}')
            print ('User Wins')
        else: 
            print (f'{wybor1} : {wybor2}')
            print ('Coœ siê spierdzieli³o')

A = Game()
A.run(A.user_input(), A.computer_input())
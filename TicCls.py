class Player:
    
    
    def __init__(self):
        self.name=""
        self.symbole=""
    def chooseName(self):
        while True:
            nameTest=input("pealse inter your name : ")
            if nameTest.isalpha():
                return nameTest
            else :
                print("Oops! invalide name use letters only")
    
    

    def chooseSymbole(self):
        while True:
            symboleTest=input("pealse inter your symbole : ")
            if symboleTest.isalpha() and len(symboleTest)==1:
                return symboleTest
            else :
                print("Oops! invalide symbole use a single letter ")
class Menu:
    def __init__(self):
        self.get_choose_name=Player()
    def startMenu(self):
        print("WELCOM TO TicTacToe !")
        print("Please choose one by this choice : ")
        print("1- START GAME \n2- QUIT GAME ")
        while True:
            choose=int(input("your choice : "))
            if choose==2 or choose==1:
                return choose
    def endMenu(self):
        print("Game Over !")
        print("Please choose one by this choice : ")
        print("1- RESTART GAME \n2- QUIT GAME ")
        while True:
            choose=int(input(" Enter your choice : "))
            if choose==1 or choose==2:
                return choose
class Board:
    def number_not_in(self,lista):
        loop=[1,2,3,4,5,6,7,8,9]
        for i in lista:
            if i in loop:
                return False#that mean compose a number
            
        return True
    def __init__(self):
        self.lisa=[]
        self.play=Player()
    def player_win(self,lista):
        logic_win=[[0,1,2],[3,4,5],[6,7,8],
                    [0,3,6],[1,4,7],[2,5,8],
                    [0,4,8],[2,4,6]]
        for i in range(len(logic_win)):
            if  lista[logic_win[i][0]]==lista[logic_win[i][1]] and lista[logic_win[i][0]]==lista[logic_win[i][2]]:
                    return True #that mean is win a match
        return False

    def display_board(self):
        print("-"*12)
        print("|",end=" ")
        for i in range(9):
            self.lisa.append(i+1)
            print(f"{self.lisa[i]} |",end=" ")
            if i in (2,5):
                print("\n ----------- ")
                print("|",end=" ")
        print("\n ----------- ")
    def update_board(self):
        while True:
                # if  self.player_win(self.lisa):
                #     return "win" 
                # #game exit when one player is win
                
                
                    choose=int(input("inter the place to insert your symbole : "))
                    cond_insert=choose>0 and choose<10  
                    if cond_insert:
                        if  self.lisa[choose-1] in [1,2,3,4,5,6,7,8,9]  :
                            symbole=self.play.chooseSymbole()
                            self.lisa[choose-1]=symbole
                            if self.player_win(self.lisa):
                                return "win"
                            elif self.number_not_in(self.lisa):
                                return "not empty"
                            else:
                                return "done"
                        elif str(self.lisa[choose-1]).isalpha() and not self.number_not_in(self.lisa):
                            print("-> Insert already !")
                        # else : 
                        #     #self.number_not_in(self.lisa): 
                        #     return "not empty" 
                        #     #game exit when the table not empty
                    else:
                        print("Invalid index for insertion (try again)! ")
    def reset_board(self):
        self.lisa=[]
        self.display_board()
    
# board=Board()
# lisa=["x","","","","","","x","","x"]
#  board.display_board()
# print(board.player_win(lisa))
import os
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Game:

    def __init__(self):
        self.board=Board()
        self.player_instance=Player()
        self.name_liste=Menu()
        self.players=[]
        self.current_player_index = 1
    


    def update_board(self,lisa):
        print("-"*12)
        print("|",end=" ")
        for i in range(9):
            print(f"{lisa[i]} |",end=" ")
            if i in (2,5):
                print("\n ----------- ")
                print("|",end=" ")
        print("\n ----------- ")

    def player_start(self):
        while True:
            start=input("You want start ? (press any letter if you want or number if no) ")
            if start.isalpha():
                return 1  
            elif start.isdigit():
                return 2
            else:
                print("Invalid input ! ")
    def play_turn(self,who_start):
        if who_start==2:
            next=1 
        else:
            next=2
    
        while not  self.board.number_not_in(self.board.lisa) :
            #self.board.player_win(self.board.lisa)
            print(f"player {who_start} : is your turn ")
            status=self.board.update_board()
            self.update_board(self.board.lisa)
            end=self.status_game(self.players[who_start-1],status)
            if end==0:
                break
            # if not self.board.player_win(self.board.lisa):
            print(f"player {next} : is your turn.")
            status=self.board.update_board()
            self.update_board(self.board.lisa)
            end=self.status_game(self.players[who_start-1],status)
            if end==0:
                break
            clear_screen()
            self.update_board(self.board.lisa)
    def status_game(self,name_player,status):
        if status=="win":
            name_player=str(name_player).upper()
            print(f"--{name_player}--Congratulation  you are Win!")
            resOr=self.name_liste.endMenu()
            if resOr==1:
                self.board.reset_board()
                self.start_game()
                
            else:
                print("  --Thlla!-- ")
                return 0

        elif status=="done" :
            print("=>DONE")
            
            
        else:
            print("--> Match equal. ")
            resOr=self.name_liste.endMenu()
            if resOr==1:
                self.board.reset_board()
                start=self.start_game()
                return start
            else:
                print("Thlla!")
                return 0
    def start_game(self):
        startOrQuit=self.name_liste.startMenu()
        if startOrQuit==1:
            self.players= [self.player_instance.chooseName(),self.player_instance.chooseName()]
            print(f"PLAYER 1 : {self.players[0]}\nPLAYER 2 : {self.players[1]}")
            self.board.display_board()
            self.current_player_index=self.player_start()
            self.play_turn(self.current_player_index)
            
            
        else:
                print("--> Lhla yshhl !")
                return 0

match=Game()
match.start_game()









# # import os
# # def clear_screen():
# #     os.system("cls" if os.name=="nt" else "clear")
#     #tis function assured to clear the screen when you appled
#     #not clear the data is resive



import random
import time



def headsorTails():
    def headsorTails_Generator():
        toss_list=['Heads', 'Tails']
        generator_Count = 0
        while generator_Count<10:
            print('*' + random.choice(toss_list) +'*')
            generator_Count+=1
            time.sleep(0.5)
        #from IPython.display import clear_output
        #clear_output()
            if generator_Count==10:
                #time.sleep(0.5)
                print('and one last roll...')
                time.sleep(0.7)
                headsorTails_Generator.tossresult= random.choice(toss_list)
                if headsorTails_Generator.tossresult == 'Heads':
                    print(f'The toss result is {headsorTails_Generator.tossresult.upper()}')
                elif headsorTails_Generator.tossresult == 'Tails':
                    print(f'The toss result is {headsorTails_Generator.tossresult.upper()}')


    headsortails_choice= ''
    choice_List=['H','T']
    wrongcount=0
    XO=['X','O']
    choice_XO=''
    #headsorTails.player2_symbol=''
    while headsortails_choice.upper()not in choice_List:

        headsortails_choice = input('Player choose Heads or Tails [H/T]: ')


        if headsortails_choice.upper()not in choice_List:
            print('PlEase ReTuRn [H/T]')
            wrongcount+=1

            if wrongcount==4:
                from IPython.display import clear_output
                clear_output()
                wrongcount=0
    if headsortails_choice.upper()=='H':
        print('player chose Heads, the opponent was assigned Tails...')
        time.sleep(0.2)
        print('tossing')
        time.sleep(0.2)
        print('tossing')
        time.sleep(0.2)
        print('tossing')
        headsorTails_Generator()
        time.sleep(0.5)
        print('\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        time.sleep(1)
        if headsorTails_Generator.tossresult=='Heads':
            print('\ncongrats you are PLAYER-1 and you will go first')

            while choice_XO.upper() not in XO:
                choice_XO=input('PLAYER-1 choose your symbol [X/O]: ')
                if choice_XO.upper() not in XO:
                    print('PlEase ReTuRn [X/O]')
                    wrongcount+=1

                    if wrongcount==10:
                        from IPython.display import clear_output
                        clear_output()
                        wrongcount=0

            headsorTails.player1_symbol=choice_XO.upper()
            time.sleep(1)
            from IPython.display import clear_output
            clear_output()
            if headsorTails.player1_symbol=='X':
                headsorTails.player2_symbol='O'
                print('PLAYER-1 will be assigned X')
                print('\nPLAYER-2 will be assigned O')
            elif headsorTails.player1_symbol=='O':
                headsorTails.player2_symbol='X'
                print('PLAYER-1 will be assigned O')
                print('\nPLAYER-2 will be assigned X')
        elif headsorTails_Generator.tossresult=='Tails':
            print('\nbetter luck next time. You are PLAYER-2 and you will go last')
            print('\nplease hand it over to your opponent to choose symbol')
            time.sleep(2)

            while choice_XO.upper() not in XO:
                choice_XO=input('PLAYER-1 choose your symbol [X/O]: ')
                if choice_XO.upper() not in XO:
                    print('PlEase ReTuRn [X/O]')
                    wrongcount+=1

                    if wrongcount==10:
                        from IPython.display import clear_output
                        clear_output()
                        wrongcount=0

            headsorTails.player1_symbol=choice_XO.upper()
            time.sleep(1)
            from IPython.display import clear_output
            clear_output()
            if headsorTails.player1_symbol=='X':
                headsorTails.player2_symbol='O'
                print('PLAYER-1 will be assigned X')
                print('\nPLAYER-2 will be assigned O')
            elif headsorTails.player1_symbol=='O':
                headsorTails.player2_symbol='X'
                print('PLAYER-1 will be assigned O')
                print('\nPLAYER-2 will be assigned X')
    elif headsortails_choice.upper()=='T':
        print('player chose Tails, the opponent was assigned Heads...')
        time.sleep(0.2)
        print('tossing')
        time.sleep(0.2)
        print('tossing')
        time.sleep(0.2)
        print('tossing')
        headsorTails_Generator()
        time.sleep(0.5)
        print('\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        time.sleep(1)
        if headsorTails_Generator.tossresult=='Heads':
            print('\nbetter luck next time. You are PLAYER-2 and you will go last')
            print('\nplease hand it over to your opponent to choose symbol')
            time.sleep(2)

            while choice_XO.upper() not in XO:
                choice_XO=input('PLAYER-1 choose your symbol [X/O]: ')
                if choice_XO.upper() not in XO:
                    print('PlEase ReTuRn [X/O]')
                    wrongcount+=1

                    if wrongcount==10:
                        from IPython.display import clear_output
                        clear_output()
                        wrongcount=0
            headsorTails.player1_symbol=choice_XO.upper()
            time.sleep(1)
            from IPython.display import clear_output
            clear_output()
            if headsorTails.player1_symbol=='X':
                headsorTails.player2_symbol='O'
                print('PLAYER-1 will be assigned X')
                print('\nPLAYER-2 will be assigned O')
            elif headsorTails.player1_symbol=='O':
                headsorTails.player2_symbol='X'
                print('PLAYER-1 will be assigned O')
                print('\nPLAYER-2 will be assigned X')
        elif headsorTails_Generator.tossresult=='Tails':
            print('\ncongrats you are PLAYER-1 and you will go first')

            while choice_XO.upper() not in XO:
                choice_XO=input('PLAYER-1 choose your symbol [X/O]: ')
                if choice_XO.upper() not in XO:
                    print('PlEase ReTuRn [X/O]')
                    wrongcount+=1

                    if wrongcount==10:
                        from IPython.display import clear_output
                        clear_output()
                        wrongcount=0
            headsorTails.player1_symbol=choice_XO.upper()
            time.sleep(1)
            from IPython.display import clear_output
            clear_output()
            if headsorTails.player1_symbol=='X':
                headsorTails.player2_symbol='O'
                print('PLAYER-1 will be assigned X')
                print('\nPLAYER-2 will be assigned O')
            elif headsorTails.player1_symbol=='O':
                headsorTails.player2_symbol='X'
                print('PLAYER-1 will be assigned O')
                print('\nPLAYER-2 will be assigned X')

def gamecheck_pos(player_1,player_2,count):
    #print(player_1)
    plotindex_list=[0,1,2,3,4,5,6,7,8]
    toprow=(0,1,2)
    middlerow=(3,4,5)
    bottomrow=(6,7,8)
    leftcolumn=(0,3,6)
    middlecolumn=(1,4,7)
    rightcolumn=(2,5,8)
    diagonaltopleft=(0,4,8)
    diagonaltopright=(2,4,6)
    correct_listX=['X','X','X']
    correct_listO=['O','O','O']
    check_listX=[]
    check_listO=[]
    correctAnswer=False
    Player1result=''
    Player2result=''
    player1_won=1
    player2_won=2
    if count>=6:
        if headsorTails.player1_symbol=='X':

            for everyCheckIndex in toprow:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==toprow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''


            for everyCheckIndex in middlerow:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
                #print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==middlerow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in bottomrow:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==bottomrow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in leftcolumn:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==leftcolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in middlecolumn:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==middlecolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in rightcolumn:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==rightcolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in diagonaltopleft:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==diagonaltopleft[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in diagonaltopright:
                check_listX.append(player_1[everyCheckIndex])
                check_listO.append(player_2[everyCheckIndex])
               # print(check_listX)
                #print(check_listO)
                if check_listX==correct_listX:
                    correctAnswer=True
                    Player1result='1x'

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player2result='2o'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==diagonaltopright[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

        if headsorTails.player2_symbol=='X':

            for everyCheckIndex in toprow:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==toprow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in middlerow:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==middlerow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in bottomrow:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==bottomrow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in leftcolumn:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==leftcolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in middlecolumn:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==middlecolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in rightcolumn:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==rightcolumn[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in diagonaltopleft:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==middlerow[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

            for everyCheckIndex in diagonaltopright:
                check_listO.append(player_1[everyCheckIndex])
                check_listX.append(player_2[everyCheckIndex])

                if check_listO==correct_listO:
                    correctAnswer=True
                    Player1result='1o'

                if check_listX==correct_listX:
                    correctAnswer=True
                    Player2result='2x'

                if correctAnswer ==True:
                    break
                elif everyCheckIndex==diagonaltopright[2]:
                    check_listX=[]
                    check_listO=[]
                    Player1result=''
                    Player2result=''

        if correctAnswer==True:
            if Player1result=='1x':
                return player1_won
            elif Player1result=='1o':
                return player1_won

            if Player2result=='2x':
                return player2_won
            elif Player2result=='2o':
                return player2_won

        elif count==9:
            return 'TIE'

def playgame():
    printboard.plotpoint_list= [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    printboard.plotindex_list=[0,1,2,3,4,5,6,7,8]
    printboard.plotpoint_clone=[]
    playgame.player1_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    playgame.player2_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    playgame.trycount=0
    gameon=True
    while gameon==True:
        if gameon==False:
            break
        player1=''
        player2=''
        wrongcount = 0

        example_board = "   EXAMPLE BOARD\n  1  |   2   |  3  \n --- |  ---  | ---\n  4  |   5   |  6\n --- |  ---  | ---\n  7  |   8   |  9 "

        while player1.isdigit()==False or int(player1)-1 not in printboard.plotindex_list or int(player1)-1 in printboard.plotpoint_clone:
            if gameon==False:
                break
            #print(printboard.plotpoint_list)
            #print(printboard.plotpoint_clone)
            print(example_board)
            board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n --- |  ---  | ---\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n --- |  ---  | ---\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
            print(board)
            player1=(input('PLAYER-1 Choose your position on the board 1-9\n'))

            if player1.isdigit()==False:
                from IPython.display import clear_output
                clear_output()
                print('\nUNEXPECTED input, type a number from 1-9\n')
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0
            elif int(player1)-1 not in printboard.plotindex_list:
                from IPython.display import clear_output
                clear_output()
                print('\ninput OUT OF RANGE, type a number from 1-9\n')
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0
            elif int(player1)-1 in printboard.plotpoint_clone:
                from IPython.display import clear_output
                clear_output()
                print("\\\\\\\\\\\\\\\\choose a position that isn't already taken///////////////\n")
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1
                #or player1.isdigit() not in range(1,10) or int(player1)-1 in printboard.plotpoint_clone:
               # if player1.isdigit()==False or player1.isdigit() not in range(1,10):
               #     from IPython.display import clear_output
                #    c
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0


                    #from IPython.display import clear_output
             #       clear_output()
              #      print('\nUNEXPECTED input, type a number from 1-9')
               #     print(example_board)
                  #  print(board)
                  #  time.sleep(5)
                  #  from IPython.display import clear_output
             #       clear_output()
                   # wrongcount+=1
             #   elif int(player2)-1 in printboard.plotpoint_clone:
             #       from IPython.display import clear_output
             #       clear_output()
              #      print("\\\\\\\\\\\\\\\\choose a position that isn't already taken///////////////")
               #     print(example_board)
                #    print(board)
                #    time.sleep(5)
                #    from IPython.display import clear_output
                #    clear_output()
                    #player2=''player1_list[playgame.player1_pos]=headsorTails.player1_symbol
                    #break
                 #   wrongcount+=1

            #from IPython.display import clear_output
            #clear_output()
           # print(player2)



           # elif int(player2)-1 not in printboard.plotpoint_clonelear_output()
                #    print('\nUNEXPECTED input, type a number from 1-9')
                #    print(example_board)
                #    print(board)
                 #   time.sleep(5)
                  #  from IPython.display import clear_output
                  #  clear_output()
            #    elif int(player1)-1 in printboard.plotpoint_clone:
             #       from IPython.display import clear_output
              #      clear_output()
               #     print("\\\\\\\\\\\\\\\\choose a position that isn't already taken///////////////")
             #       print(example_board)
                #    print(board)
                #    time.sleep(5)
                 #   from IPython.display import clear_output
                 #   clear_output()
                    #player2=''
                    #break
                 #   wrongcount+=1

            #from IPython.display import clear_output
            #clear_output()
            #print(player1)
            #gameon=False



            #board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n     |       |\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n     |       |\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
            elif int(player1)-1 not in printboard.plotpoint_clone:
                #trycount+=1
                from IPython.display import clear_output
                clear_output()
                #print(example_board)
                #print('\n'+board)
                playgame.player1_pos=int(player1)-1
                printboard.plotpoint_list[playgame.player1_pos]=headsorTails.player1_symbol
                playgame.player1_list[playgame.player1_pos]=headsorTails.player1_symbol
                printboard.plotpoint_clone.append(playgame.player1_pos)

                playgame.trycount+=1
                board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n     |       |\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n     |       |\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
                #print(board)
                #print(printboard.plotpoint_list)
                print(printboard.plotpoint_clone)
                print(printboard.plotindex_list)

                if gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)==1:

                #if sorted(printboard.plotpoint_clone)==printboard.plotindex_list:


                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n PLAYER-1 won the game')
                    #print(board)

                    gameon=False


                elif gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)==2:
                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n PLAYER-2 won the game')
                    #print(board)
                    gameon=False

                elif gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)=='TIE':
                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n Game was a TIE')
                    #print(board)
                    gameon=False

                break

            #playgame_again()




        while player2.isdigit()==False or int(player2)-1 not in printboard.plotindex_list or int(player2)-1 in printboard.plotpoint_clone:
            if gameon==False:
                break
            print(example_board)
            board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n --- |  ---  | ---\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n --- |  ---  | ---\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
            print(board)
            player2=(input('PLAYER-2 Choose your position on the board 1-9\n'))
            #board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n     |       |\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n     |       |\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
            if player2.isdigit()==False: #or player2.isdigit() not in range(1,10) or int(player2)-1 in printboard.plotpoint_clone:
                from IPython.display import clear_output
                clear_output()
                print('\nUNEXPECTED input, type a number from 1-9\n')
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0
            elif int(player2)-1 not in printboard.plotindex_list:
                from IPython.display import clear_output
                clear_output()
                print('\ninput OUT OF RANGE, type a number from 1-9\n')
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1

                #continue
                #player2=''
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0
            elif int(player2)-1 in printboard.plotpoint_clone:
                from IPython.display import clear_output
                clear_output()
                print("\\\\\\\\\\\\\\\\choose a position that isn't already taken///////////////\n")
                print(example_board)
                print(board)
                time.sleep(5)
                from IPython.display import clear_output
                clear_output()
                wrongcount+=1
                continue
                if wrongcount==5:
                    from IPython.display import clear_output
                    clear_output()
                    wrongcount=0
                    #from IPython.display import clear_output
             #       clear_output()
              #      print('\nUNEXPECTED input, type a number from 1-9')
               #     print(example_board)
                  #  print(board)
                  #  time.sleep(5)
                  #  from IPython.display import clear_output
             #       clear_output()
                   # wrongcount+=1
             #   elif int(player2)-1 in printboard.plotpoint_clone:
             #       from IPython.display import clear_output
             #       clear_output()
              #      print("\\\\\\\\\\\\\\\\choose a position that isn't already taken///////////////")
               #     print(example_board)
                #    print(board)
                #    time.sleep(5)
                #    from IPython.display import clear_output
                #    clear_output()
                    #player2=''
                    #break
                 #   wrongcount+=1

            #from IPython.display import clear_output
            #clear_output()
           # print(player2)



            elif int(player2)-1 not in printboard.plotpoint_clone or int(player2)-1 in printboard.plotindex_list:
                from IPython.display import clear_output
                clear_output()
                #print(example_board)
                #print('\n'+board)
                playgame.player2_pos=int(player2)-1
                printboard.plotpoint_list[playgame.player2_pos]=headsorTails.player2_symbol
                playgame.player2_list[playgame.player2_pos]=headsorTails.player2_symbol
                printboard.plotpoint_clone.append(playgame.player2_pos)
                board = f"\n  {printboard.plotpoint_list[0]}  |   {printboard.plotpoint_list[1]}   |  {printboard.plotpoint_list[2]}  \n --- |  ---  | ---\n  {printboard.plotpoint_list[3]}  |   {printboard.plotpoint_list[4]}   |  {printboard.plotpoint_list[5]} \n --- |  ---  | ---\n  {printboard.plotpoint_list[6]}  |   {printboard.plotpoint_list[7]}   |  {printboard.plotpoint_list[8]} "
                #print(board)
                playgame.trycount+=1
                #print(printboard.plotpoint_list)
                print(printboard.plotindex_list)
                print(printboard.plotpoint_clone)
                if gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)==1:

                #if sorted(printboard.plotpoint_clone)==printboard.plotindex_list:


                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n PLAYER-1 won the game')

                    #print(board)
                    gameon=False


                elif gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)==2:
                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n PLAYER-2 won the game')
                    #print(board)
                    gameon=False

                elif gamecheck_pos(playgame.player1_list, playgame.player2_list, playgame.trycount)=='TIE':
                    from IPython.display import clear_output
                    clear_output(example_board)
                    print('     Game Over')
                    print('\n Game was a TIE')
                    gameon=False
                break

headsorTails()
playgame()

import random
import turtle

turtle.title('Tic Tac Toe')


def draw_board():
    turtle.forward(300)
    turtle.backward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.backward(300)

def draw_x(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(45)
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(45)

def draw_circle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()

def draw_horizontal_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(90)
    turtle.forward(300)
    turtle.backward(300)
    turtle.right(180)

def draw_vertical_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(180)
    turtle.forward(300)
    turtle.left(0)

def draw_left_angle_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(135)
    turtle.forward(400)
   
def draw_right_angle_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.left(135)
    turtle.forward(400)

def draw_marker(player,player_pos):
    if player_pos == 1 and player == 'o':
        draw_circle(80,50)
    elif player_pos == 2 and player == 'o':
        draw_circle(180,50)
    elif player_pos == 3 and player == 'o':
        draw_circle(280,50)
    elif player_pos == 4 and player == 'o':
        draw_circle(80,-40)
    elif player_pos == 5 and player == 'o':
        draw_circle(180,-40)
    elif player_pos == 6 and player == 'o':
        draw_circle(280,-40)
    elif player_pos == 7 and player == 'o':
        draw_circle(80,-140)
    elif player_pos == 8 and player == 'o':
        draw_circle(180,-140)
    elif player_pos == 9 and player == 'o':
        draw_circle(280,-140)
    elif player_pos == 1 and player == 'x':
        draw_x(10,10)
    elif player_pos == 2 and player == 'x':
        draw_x(110,10)
    elif player_pos == 3 and player == 'x':
        draw_x(210,10)
    elif player_pos == 4 and player == 'x':
        draw_x(10,-90)
    elif player_pos == 5 and player == 'x':
        draw_x(110,-90)
    elif player_pos == 6 and player == 'x':
        draw_x(210,-90)
    elif player_pos == 7 and player == 'x':
        draw_x(10,-190)
    elif player_pos == 8 and player == 'x':
        draw_x(110,-190)
    elif player_pos == 9 and player == 'x':
        draw_x(210,-190)




board=['*',' ',' ',' ',' ',' ',' ',' ',' ',' ']
vs = ''
player1 = ''
player2 = ''
player1_pos = ''
player2_pos = ''
moves_played = 0

def check_emptyspaces():
    check = 0
    for x in range(1,10):
        if board[x] == ' ':
            check = 1
    if check == 1:
        check = 0
        return True
    else:
        check = 0
        return False

def user_input(player):
    a = 0
    if check_emptyspaces() == True:
        while type(a) != type('int'):
            try:
                a = int(input("Тоглогч "+player+" 1-ээс 9-ийн хооронд тоо оруулна уу :"))
                if a > 0 and a <= 9:
                    return a
                else:
                    print("Буруу утга оруулсан байна! Дахин тоо оруулна уу!")
                    a = None
            except ValueError:
                print("Буруу утга оруулсан байна! Дахин тоо оруулна уу!")

    else:
        print("Тэнцлээ")

def validate_position(position):
    if board[position] == ' ':
        return True
    else:
        return False

def check_wins(player):
    if board[1] == player and board[2] == player and board[3] == player:
        draw_horizontal_line(10,50)
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        draw_horizontal_line(10,-50)
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        draw_horizontal_line(10,-150)
        return True
    elif board[1] == player and board[5] == player and board[9] == player:
        draw_left_angle_line(10,90)
        return True
    elif board[3] == player and board[5] == player and board[7] == player:
        draw_right_angle_line(300,90)
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        draw_vertical_line(50,90)
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        draw_vertical_line(150,90)
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        draw_vertical_line(250,90)
        return True
    else:
        return False
    
def update(player,player_pos):
    global moves_played
    
    if moves_played != 9:
        while validate_position(player_pos)!= True:
            player_pos = user_input(player)
            validate_position(player_pos)
        else:
            if check_emptyspaces() == True:
                board[player_pos] = player
                draw_marker(player,player_pos)
                moves_played += 1

def generate_random():
    return random.randint(1,9)

print("-----------------Tic Tac Toe тоглоомд тавтай морил------------------")
print("---------------------------Дүрэм------------------------------------")
print("********************************************************************")
print("* Сонгосон тэмдэгтээ 3 дараалуулан байрлуулах                      *")
print("* 1-ээс 9-ийн хооронд утга гараас оруулах                          *")
print("* Зүүн дээд булан 1-ээс эхлэн Баруун доод булан 9 хүртэл байрлана. *")
print("*******************************************")
print("  Доор гарч ирэх хувилбараас сонголт хийнэ үү:")
print("---------------------------------------")
print("1. Тоглогч VS Компьютер")
print("2. Тоглогч VS Хүн")
print("---------------------------------------")
while vs == '' or vs > 2:
    try:
        vs = int(input("Сонгосон дугаараа оруулна уу:"))
        if vs > 0 and vs <= 2:
            while player1 != 'x' or player1 != 'o':
                player1 = str(input("Тоглогч 1 дараах сонголтуудаас сонгох Х эсвэл О :"))
                if player1 == 'x' or player1 == 'o':
                    if player1 == 'x':
                        player2 = 'o'
                    else:
                        player2 = 'x'
                    print("Тоглоом эхэллээ!!!\n")
                    draw_board()
                    while check_emptyspaces() == True:
                        player1_pos = user_input(player1)
                        update(player1, player1_pos)

                        if check_wins(player1) == True:
                            print("Тоглогч ", player1, "хожлоо!!!!!")
                            break
                        if vs == 1:
                            player2_pos = generate_random()
                            if moves_played != 9 :

                                while validate_position(player2_pos) != True:
                                    player2_pos = generate_random()
                                    validate_position(player2_pos)

                                else:
                                    board[player2_pos] = player2
                                    draw_marker(player2, player2_pos)
                                    moves_played +=1

                                    if check_wins(player2) == True:
                                        print ('Тоглогч ' , player2 , 'хожлоо!!!')
                                        break


                        else:
                             player2_pos = user_input(player2)
                             update(player2, player2_pos)


                             if check_wins(player2) == True :
                                     
                                 print ('Тоглогч ' , player2 , 'хожлоо!!!')
                                 break

        

                    if check_emptyspaces() != False:
                        print('Тоглоом дууслаа !!!')

                    break
    except ValueError:
        print("Оруулсан утга тоо биш байна! Дахин оруулна уу!")

                                    
                        

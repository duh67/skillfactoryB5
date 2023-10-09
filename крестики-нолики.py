print("***крестики-нолики***")

board = list(range(1,10))

def playing_field(board):
    print("~" * 13)
    for i in range (3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("~" * 13)

def data_input(player_sign):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_sign+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Введите число")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_sign
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False


def main(board):
    counter = 0
    win = False
    while not win:
        playing_field(board)
        if counter % 2 == 0:
           data_input("X")
        else:
           data_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    playing_field(board)
main(board)

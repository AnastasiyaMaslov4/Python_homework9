from random import randint
from telegram import Update
from telegram.ext import Updater, CallbackContext

def hi(update: Update, context: CallbackContext):
    update.message.reply_text(f'Ну привет, {update.effective_user.first_name}, сыграем в крестики-нолики? Нажми: /start_game ')

game_board = list(range(1,10))
used_cell = []
user_choise = None


def start_game(update: Update, context: CallbackContext):
    global used_cell
    global game_board
    used_cell = []
    game_board = list(range(1,10))
    update.message.reply_text(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n -------------------\n Куда поставишь Х? Отправь номер клетки")


def x_choise(update: Update, context: CallbackContext):
    global user_choise
    global game_board
    user_choise = int(update.message.text)
    check(update)
    if not (who_wins(update, game_board)):
        bot_turn(update)
        who_wins(update, game_board)

def check(update: Update):
    global game_board
    global user_choise
    if user_choise not in used_cell:
        game_board[user_choise - 1] = str("X")
        used_cell.append(user_choise)
        update.message.reply_text(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n ------------------- ")
    else:
        update.message.reply_text("Клетка занята")
        x_choise(update, CallbackContext)

def bot_turn(update: Update):
    valid = 0
    while valid == 0:
        bot_step = randint(1,9)
        if bot_step not in used_cell:
            game_board[bot_step - 1] = str("O")
            used_cell.append(bot_step)
            valid = 1
            update.message.reply_text(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n ------------------- ")

def who_wins(update: Update, game_board):
    win = False
    if len(used_cell) < 9:
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for i in win_coord:
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
                update.message.reply_text(f"Победил игрок {game_board[i[0]]}. Сыграем еще? /start_game")
                win = True
    elif len(used_cell) == 9:
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for i in win_coord:
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
                update.message.reply_text(f"Победил игрок {game_board[i[0]]}. Сыграем еще? /start_game ")
                win = True
        if not win:
            update.message.reply_text("Ничья. Сыграем еще? /start_game")
    return win
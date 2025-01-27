import random
def generate_board(size):
    return [["~" for _ in range(size)] for _ in range(size)]

def place_ships(board, ship_count):

    ships = set()
    while len(ships) < ship_count:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        ships.add((row, col))
    return ships


def print_board(board):

    print("  " + " ".join(map(str, range(len(board[0])))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))


def play_game(board_size=5, ship_count=3, shots=6):

    board = generate_board(board_size)
    ships = place_ships(board, ship_count)
    hits = 0

    print("Witaj w grze w statki!")
    print(f"Musisz zniszczyć {ship_count} statki, masz {shots} strzałów.")
    print_board(board)

    while shots > 0 and hits < ship_count:
        print(f"\nPozostało strzałów: {shots}")
        try:

            row = int(input("Podaj wiersz: "))
            col = int(input("Podaj kolumnę: "))


            if row < 0 or row >= board_size or col < 0 or col >= board_size:
                print("Nieprawidłowe współrzędne! Spróbuj ponownie.")
                continue


            if (row, col) in ships:
                print("Trafienie!")
                board[row][col] = "X"
                ships.remove((row, col))
                hits += 1
            else:
                print("Pudło!")
                board[row][col] = "O"

            print_board(board)
            shots -= 1

        except ValueError:
            print("Proszę podać liczbę całkowitą!")

    if hits == ship_count:
        print("Gratulacje! Zniszczyłeś wszystkie statki!")
    else:
        print("Koniec gry! Nie udało ci się zniszczyć wszystkich statków.")
        print(f"Statki były na pozycjach: {ships}")


play_game()

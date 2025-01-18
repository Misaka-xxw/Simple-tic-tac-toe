from Algorithm import Algorithm
class test:
    def __init__(self):
        self.chess=Algorithm()
        self.mode:int=0

    def show(self):
        for i in range(3):
            print('', end='|')
            for j in range(3):
                match self.chess.board[i][j]:
                    case 1:
                        print(' X ',end='|')
                    case 2:
                        print(' O ', end='|')
                    case _:
                        print('   ', end='|')
            print('\n-------------')
        print('\n')

    def run(self):
        print()
        c=input("谁先开始？机器/你 1/0:")
        if c=='1':
            self.mode=1
        else:
            self.mode=0
        for i in range(9):
            if i%2==self.mode:
                x,y=map(int,input().split())
                while self.chess.board[x][y]!=0:
                    print("不准耍赖！")
                    x,y=map(int,input().split())
                self.chess.play_step(i%2+1,auto=False,x=x,y=y)
            else:
                # x, y = map(int, input().split())
                self.chess.play_step(i%2+1)
            self.show()
            if self.chess.game_over:
                print('Game Over,winner is',self.chess.winner)
                return
        print('Game Over,no winner')

if __name__=="__main__":
    while True:
        ex=test()
        ex.show()
        ex.run()

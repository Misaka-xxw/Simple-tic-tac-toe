inf = 2 ** 15  # 模拟无穷大


class Algorithm:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.best_move = (0, 0)
        self.game_over = False
        self.winner = None

    def judge(self) -> int:
        """
        判断是否结束游戏
        :return: 0->draw,1->black win,2->white win,-1->continue
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return -1  # 游戏未结束
        return 0  # 平局

    def minmax(self, player: int, a=-inf, b=inf) -> int:
        """
        Minimax 算法，1 为 Max，2 为 Min
        :param player: 哪个玩家
        :param best_move: 存储最佳移动位置的列表
        :param a: alpha
        :param b: beta
        :return: 评估值
        """
        e = self.judge()
        if e != -1:
            return -1 if e == 2 else e
        best_move = (1, 1)
        (best_score, cmp, update_bound) = (-inf, lambda x, y: x > y, lambda x, y: max(x, y)) if player == 1 else (
        inf, lambda x, y: x < y, lambda x, y: min(x, y))
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:  # 为空，落子
                    self.board[i][j] = player  # 落子
                    current_score = self.minmax(3 - player, a, b)  # 下一步最好的一子
                    if cmp(current_score, best_score):
                        best_score = current_score
                        best_move = (i, j)
                    self.board[i][j] = 0  # 落子
                    a = update_bound(a, best_score)
                    if b <= a:
                        break
        self.best_move = best_move
        return best_score

    def play_step(self, player: int, auto: bool = True, x: int = 0, y: int = 0):
        """
        落子
        :param player: 当前落子的玩家
        :param auto: 是否是机器自动落子
        :param x: 人工落子的横坐标
        :param y: 人工落子的纵坐标
        """
        if auto:
            self.minmax(player)
            x, y = self.best_move
        self.board[x][y] = player
        if self.judge() == player:
            self.game_over = True
            self.winner = player

    def clear_board(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.best_move = (0, 0)
        self.game_over = False
        self.winner = None

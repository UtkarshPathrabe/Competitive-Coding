class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = deque(food)
        self.score = 0
        self.snake = deque([[0, 0]])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        if direction == 'U':
            newHead = [self.snake[0][0] - 1, self.snake[0][1]]
        elif direction == 'D':
            newHead = [self.snake[0][0] + 1, self.snake[0][1]]
        elif direction == 'L':
            newHead = [self.snake[0][0], self.snake[0][1] - 1]
        elif direction == 'R':
            newHead = [self.snake[0][0], self.snake[0][1] + 1]
        else:
            newHead = [self.snake[0][0], self.snake[0][1]]
        if newHead[0] == -1 or newHead[0] == self.height or newHead[1] == -1 or newHead[1] == self.width:
            return -1
        if self.snake and newHead in self.snake and self.snake[-1] != newHead:
            return -1
        self.snake.appendleft(newHead)
        if self.food and self.food[0] == newHead:
            self.food.popleft()
            self.score += 1
        else:
            self.snake.pop()
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
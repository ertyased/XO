def check_mas(a, n):

  count = 1

  maxans = 1

  for i in range(1, len(a)):

    if a[i] == a[i - 1] and a[i]:

      if a[i] != '#':

        count += 1

        maxans = max(maxans, count)

    else:

      count = 1

  return maxans


def count(n, a, d):

  if d == -1:

    return [0, 0]

  if a.check():

    if d % 2 == 1:

      return [1, 0]

    else:

      return [0, d]

  ans = [0, 0]

  for i in range(n):

    for j in range(n):

      if a.map[i][j] == '#':

        if d % 2 == 1:

          a.map[i][j] = 'x'

          b = count(n, a, d - 1)

          ans[0] += b[0]

          ans[1] += b[1]

          a.map[i][j] = '#'

        else:

          a.map[i][j] = 'o'

          b = count(n, a, d - 1)

          ans[0] += b[0]

          ans[1] += b[1]

          a.map[i][j] = '#'

  return ans


class Board():


  def __init__(self, n, k):

    self.n = n

    self.k = k

    self.map = [['#'] * n for i in range(n)]


  def check(self):


    ans = False

    for i in range(n):

      a = []

      b = []

      for i1 in range(n):

        a.append(self.map[i][i1])

        b.append(self.map[i1][i])

      if check_mas(a, n) >= k or check_mas(b, n) >= k:

        ans = True

    for i in range(n):

      x, y = 0, i

      y1, x1 = 0, i

      a = []

      b = []

      a.append(self.map[x][y])

      while x < n - 1 and y < n - 1:

        x += 1

        y += 1

        a.append(self.map[x][y])


      b.append(self.map[x1][y1])

      while y1 < n - 1 and x1 < n - 1:

        x1 += 1

        y1 += 1

        b.append(self.map[x1][y1])

      if check_mas(a, n) >= k or check_mas(b, n) >= k:

        ans = True

      x, y = i, 0

      x1, y1 = n - 1, i

      a = []

      b = []

      a.append(self.map[x][y])

      while x > 0 and y < n - 1:

        x -= 1

        y += 1

        a.append(self.map[x][y])

      b.append(self.map[x1][y1])

      while x1 > 0 and y1 < n - 1:

        x1 -= 1

        y1 += 1

        b.append(self.map[x1][y1])

      if check_mas(a, n) >= k or check_mas(b, n) >= k:

        ans = True

    return ans


  def clear(self):

    self.map = [['#'] * n for i in range(n)]

       

  def is_draw(self):

    for i in range(self.n):

      for j in range(self.n):

        if self.map[i][j] == '#':

          return False

    return True


  def make_move(self):

    ansf = [1e9, 0, 0, 0]

    for i in range(self.n):

      for j in range(self.n):

        if self.map[i][j] == '#':

          self.map[i][j] = 'o'

          if n <= 3:

            ans = count(n, self, 5)

          else:

            ans = count(n, self, 3)

          if ans[1] < ansf[0]:

            ansf = [ans[1], ans[0], i, j]

          if ans[1] == ansf[0] and ans[0] > ansf[1]:

            ansf = [ans[1], ans[0], i, j]

          self.map[i][j] ='#'

    self.map[ansf[2]][ansf[3]] = 'o'


  def make_move1(self):

      ansf = [1e9, 0, 0, 0]

      for i in range(self.n):
    
        for j in range(self.n):
  
          if self.map[i][j] == '#':
  
            self.map[i][j] = 'o'
  
            if n <= 3:
  
              ans = count(n, self, 5)
  
            else:
  
              ans = count(n, self, 3)
  
            if ans[1] < ansf[0]:

              ansf = [ans[1], ans[0], i, j]
  
            if ans[1] == ansf[0] and ans[0] > ansf[1]:
  
              ansf = [ans[1], ans[0], i, j]
  
            self.map[i][j] ='#'

      self.map[ansf[2]][ansf[3]] = 'x'

     

n, k = map(int, input('Введите n и k ').split())
a = Board(n, k)
type = int(input('введите тип игры 1 - сам собой, 2 - вы против ИИ, 3 - ИИ против ИИ '))
running = True
move = 0
if type == 2:  
  while running:
    for i in a.map:
      print(*i, sep='')
    if move % 2 == 0:
      x, y = map(int, input('Введите координаты вашего хода итерация с 1, пожалуйста вводите корректные данные ').split())
      a.map[x - 1][y - 1] = 'x'
      move += 1
    else:
      a.make_move()
      move += 1
    if a.check():
      if move % 2 == 0:
        print('вы выиграл. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
      else:
        print('Какая жалость, вы проиграли. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
    elif a.is_draw():
        print('Ничья. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
if type == 1:
  while running:
    for i in a.map:
      print(*i, sep='')
    if move % 2 == 0:
      x, y = map(int, input('Введите координаты вашего хода итерация с 1, пожалуйста вводите корректные данные ').split())
      a.map[x - 1][y - 1] = 'x'
      move += 1
    else:
      x, y = map(int, input('Введите координаты вашего хода итерация с 1, пожалуйста вводите корректные данные ').split())
      a.map[x - 1][y - 1] = 'o'
      move += 1
    if a.check():
      if move % 2 == 0:
        print('вы выиграл. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
      else:
        print('Какая жалость, вы выиграли сам у себя. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
    elif a.is_draw():
        print('Ничья. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
if type == 3:
  print('Смотрите и наслаждайтесь. Возможно это будет очень быстро')
  while running:
    for i in a.map:
      print(*i, sep='')
    if move % 2 == 0:
      a.make_move1()
      move += 1
    else:
      a.make_move()
      move += 1
    if a.check():
      if move % 2 == 0:
        print('Первый выиграл. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
      else:
        print('Второй выиграл. для перезапуска напишите заново')
        for i in a.map:
          print(*i, sep='')
        c = ''
        while c != 'заново':
          c = input()
        a.clear()
        move = 0
    elif a.is_draw():
        print('Ничья. для перезапуска напишите заново')
        c = ''
        for i in a.map:
          print(*i, sep='')
        while c != 'заново':
          c = input()
        a.clear()
        move = 0


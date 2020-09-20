import pygame


def check_mas(a, n):

  count = 1

  maxans = 1

  for i in range(1, len(a)):

    if a[i] == a[i - 1] and a[i]:

      if a[i] != '/':

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

      if a.map[i][j] == '/':

        if d % 2 == 1:

          a.map[i][j] = 'x'

          b = count(n, a, d - 1)

          ans[0] += b[0]

          ans[1] += b[1]

          a.map[i][j] = '/'

        else:

          a.map[i][j] = 'o'

          b = count(n, a, d - 1)

          ans[0] += b[0]

          ans[1] += b[1]

          a.map[i][j] = '/'

  return ans


class Board():


  def __init__(self, n, k):

    self.n = n

    self.k = k

    self.map = [['/'] * n for i in range(n)]


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

    self.map = [['/'] * n for i in range(n)]

       

  def is_draw(self):

    for i in range(self.n):

      for j in range(self.n):

        if self.map[i][j] == '/':

          return False

    return True


  def make_move(self):

    ansf = [1e9, 0, 0, 0]

    for i in range(self.n):

      for j in range(self.n):

        if self.map[i][j] == '/':

          self.map[i][j] = 'o'

          if n <= 3:

            ans = count(n, self, 5)

          else:

            ans = count(n, self, 3)

          if ans[1] < ansf[0]:

            ansf = [ans[1], ans[0], i, j]

          if ans[1] == ansf[0] and ans[0] > ansf[1]:

            ansf = [ans[1], ans[0], i, j]

          self.map[i][j] ='/'

    self.map[ansf[2]][ansf[3]] = 'o'

     

     

def draw():

  pygame.draw.rect(screen, (255, 255, 255), (0, 0, n* 41 + n, n * 41 + n))

  if not a.check() and not a.is_draw():

    for i in range(n + 2):

      pygame.draw.line(screen, (0, 0, 0), (i * 41 + i, 0), (i * 41 + i, n * 41 + n - 1), 1)

      pygame.draw.line(screen, (0, 0, 0), (0, i * 41 + i), (n * 41 + n - 1, i * 41 + i), 1)

      for i in range(n):

        for j in range(n):

          if a.map[i][j] == 'x':

            pygame.draw.line(screen, (255, 0, 0), (i * 42 + 1, j * 42 + 1), ((i + 1) * 42 - 1, (j + 1) * 42 - 1), 2)

            pygame.draw.line(screen, (255, 0, 0), (i * 42 + 1, (j + 1) * 42 - 1), ((i + 1) * 42 - 1, j * 42 + 1), 2)

          if a.map[i][j] == 'o':

            pygame.draw.circle(screen, (0, 0, 255), (i * 42 + 21, j * 42 + 21), 20, 2)

  else:

    if move % 2 == 1 and a.check():

      f1 = pygame.font.Font(None, 30)

      text1 = f1.render('Победили X', 1, (0, 0, 0))

      screen.blit(text1, (0, 0))

      f2 = pygame.font.Font(None, 18)

      text2 = f2.render('для перезапуска', 1, (0, 0, 0))

      screen.blit(text2, (0, 50))

      f3 = pygame.font.Font(None, 18)

      text3 = f2.render('нажмите ПКМ', 1, (0, 0, 0))

      screen.blit(text3, (0, 70))

    elif move % 2 == 0 and a.check():

      f1 = pygame.font.Font(None, 30)

      text1 = f1.render('Победили O', 1, (0, 0, 0))

      screen.blit(text1, (0, 0))

      f2 = pygame.font.Font(None, 18)

      text2 = f2.render('для перезапуска', 1, (0, 0, 0))

      screen.blit(text2, (0, 50))

      f3 = pygame.font.Font(None, 18)

      text3 = f2.render('нажмите ПКМ', 1, (0, 0, 0))

      screen.blit(text3, (0, 70))

    elif a.is_draw():

      f1 = pygame.font.Font(None, 30)

      text1 = f1.render('Ничья', 1, (0, 0, 0))

      screen.blit(text1, (0, 0))

      f2 = pygame.font.Font(None, 18)

      text2 = f2.render('для перезапуска', 1, (0, 0, 0))

      screen.blit(text2, (0, 50))

      f3 = pygame.font.Font(None, 18)

      text3 = f2.render('нажмите ПКМ', 1, (0, 0, 0))

      screen.blit(text3, (0, 70))



pygame.init()

n, k = map(int, input('Введите n и k').split())

a = Board(n, k)

size = (n * 41 + n, n * 41 + n)

screen = pygame.display.set_mode(size)


clock = pygame.time.Clock()

running = True

move = 0

while running:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:

      if event.button == 1 and not a.check() and not a.is_draw():

        pos = pygame.mouse.get_pos()

        if a.map[pos[0] // 42][pos[1] // 42] == '/':

           

          if move % 2 == 0:

            a.map[pos[0] // 42][pos[1] // 42] = 'x'

          move += 1

      if event.button == 3 and (a.check() or a.is_draw()):

        a.clear()

        move = 0

  if move % 2 == 1 and not a.check() and not a.is_draw():

    a.make_move()

    move += 1

  draw()

  clock.tick(60)

  pygame.display.flip()

pygame.quit()


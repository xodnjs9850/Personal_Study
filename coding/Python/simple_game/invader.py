import pygame
import sys

SCREEN_WIDTH = 640                                                                      # 화면 크기 변수 설정
SCREEN_HEIGHT = 480                                                                     # 화면 크기 변수 설정

white = (255, 255, 255)                                                                 # 배경 색깔(하얀색) 변수 설정
black = (0, 0, 0)                                                                       # 배경 색깔(검은색) 변수 설정

pygame.init()                                                                           # pygame 모듈 초기화
pygame.display.set_caption("Space Invaders")                                            # 게임 제목 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))                         # 화면 크기 지정
clock = pygame.time.Clock()                                                             # 시간 모듈 설정
font = pygame.font.Font(None, 32)                                                       # 글씨 설정 및 크기 설정

en = 0
pl = 0

class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load("space_invader_enemy.png").convert_alpha()       # 이미지 불러오기
        self.x = 40                                                                     # 오브젝트 초기 위치값
        self.y = 40                                                                     # 오브젝트 초기 위치값
        self.speed = 3                                                                  # 오브젝트 속도 설정
        self.direction = 1                                                              # 오브젝트 방향 설정

    def move(self):
        self.x += self.speed * self.direction                                           # 오브젝트 무브먼트 설정

        if self.x <= 40:                                                                # 오브젝트가 왼쪽에 부딪히면 오브젝트 위치 조정
            self.y += 20                                                                # 오브젝트 위치 조정
            self.direction = 1                                                          # 오브젝트 방향 초기화

        if self.x + 80 >= SCREEN_WIDTH:                                                 # 오브젝트가 오른쪽에 부딪히면 오브젝트 위치 조정
            self.y += 20                                                                # 오브젝트 위치 조정
            self.direction = -1                                                         # 오브젝트 방향 변경

        if self.y >= 400:                                                               # 오브젝트가 스크린 넘어간 경우
            self.y = 40                                                                 # 오브젝트 위치 초기화

    def draw(self):
        screen.blit(self.image, (self.x, self.y))                                       # 지정한 좌표에 그림 집어넣기(오브젝트 그림 생성)

    def is_hit(self, bullets):
        for b in bullets:
        # Rect : 오브젝트가 그려질 위치와 크기를 설정    colliderect : 두 오브젝트가 겹치는지 확인
        # 총알에 맞을 경우 실행되는 if문
            if pygame.Rect(self.x, self.y, 40, 40).colliderect((b.x, b.y, 0, b.height)):
                self.x = 40
                self.y = 40
                self.speed = self.speed + 0.5                                           # 맞았을 경우 속도 증가
                bullets.remove(b)                                                       # 총알 제거
                return True

        return False


class Player(object):
    def __init__(self):
        self.x = 300
        self.y = 400
        self.speed = 5
        self.image = pygame.image.load("space_invader_player.png").convert_alpha()

    def move(self, key_event):
        if key_event[pygame.K_LEFT]:                                                    # 왼쪽 화살표를 누를 경우
            self.x -= self.speed                                                        # 오브젝트 이동

        if key_event[pygame.K_RIGHT]:                                                   # 오른쪽 화살표 누를 경우
            self.x += self.speed                                                        # 오브젝트 이동

        if self.x <= 40:                                                                # 오브젝트가 지정된 범위를 벗어날 경우
            self.x = 40                                                                 # 오브젝트 위치 초기화

        if self.x + 80 >= SCREEN_WIDTH:                                                 # 오브젝트가 스크린을 넘을 경우
            self.x = SCREEN_WIDTH - 80                                                  # 오브젝트가 지정된 범위에서 넘어가지 못함

    def draw(self):
        screen.blit(self.image, (self.x, self.y))                                       # 지정한 좌표에 그림 집어넣기(오브젝트 그림 생성)


class Bullet(object):
    def __init__(self, x, y):
        self.height = 4                                                                 # 오브젝트 높이 설정
        self.speed = 7                                                                  # 오브젝트 속도 설정
        self.x = x                                                                      # 오브젝트 위치 설정
        self.y = y                                                                      # 오브젝트 위치 설정

    def move(self):
        self.y -= self.speed                                                            # 총알이 날아가는 속도 및 방향 조정

    def draw(self):
    # 오브젝트를 선으로 표현
        pygame.draw.line(screen, black, (self.x, self.y), (self.x, self.y + self.height), 1)


def main():
    score = 0                                                                           # score 변수 설정

    player = Player()                                                                   # player 클래스 초기화
    enemy = Enemy()                                                                     # enemy 클래스 초기화
    bullets = []                                                                        # bullets 리스트 선언

    while True:
        clock.tick(60)                                                                  # while문 반복 제한
        screen.fill(white)                                                              # 배경 채우기

        for event in pygame.event.get():                                                # 이벤트 불러오기
            if event.type == pygame.QUIT:                                               # 이벤트가 QUIT일 경우 
                sys.exit()                                                              # 시스템 종료
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:            # 스페이스 누를 경우
                bullets.append(Bullet(player.x + 20, player.y - 5))                     # bullets 리스트에 총알 추가

        key_event = pygame.key.get_pressed()                                            # 아무 키나 누를 경우 이벤트 저장

        enemy.move()                                                                    # enemy.move 초기화
        enemy.draw()                                                                    # enemy.draw 초기화
        if enemy.is_hit(bullets):
            score += 100                                                                # 맞추는데 성공하면 score 상승 

        player.move(key_event)                                                          # key_event를 인자로 player_move 초기화
        player.draw()                                                                   # player.draw 초기화

        for b in bullets:
            b.move()                                                                    # bullets.move 초기화
            b.draw()                                                                    # bullets.draw 초기화

            if b.y > SCREEN_HEIGHT:
                bullets.remove(b)                                                       # 총알이 스크린을 벗어나면 총알 삭제

        screen.blit(font.render("Score: {0}".format(score), True, black), (10, 10))     # score 위치 설정 및 글씨 크기 설정

        pygame.display.update()                                                         # display 업데이트


if __name__ == "__main__":
    main()
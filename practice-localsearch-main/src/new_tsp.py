import pygame
from algo import ALGO_INFO, DIVIDERS
import testpygame
from util import *
import threading

def loop():
    for i in range(len(ALGO_INFO)):
        print(ALGO_INFO[i])
    
    while True:
        testpygame.check_events()

        testpygame.draw_text_center(surface, "hello", font, 50, 50)

        testpygame.draw_dividers(surface, DIVIDERS)

        
        pygame.display.update()
        surface.fill(BLACK)



    #1. 알고리즘 정보를 가져온다
    #2. 무한반복
    #3. 알고리즘을 배치한다
    #4. 그리기
    # 점, 선 , 텍스트
    # draw_point(x,y) => 튜플
    # draw_line(x,y) => 튜플
    # draw_text(x,y) => 객체?
pygame.init()
surface = pygame.display.set_mode((WIDNOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)

cities = make_cities(20)
list_of_cities_list = []

if i in range(len(ALGO_INFO)):
    make_graph)
graph = make_graph_from_city_list(cities)
sim = []
threads = []
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] ==1 :
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sim[i].find))
        threads[i].daemon = True

if __name__ =="__main__":
    pygame.display.set_caption("TSP-visualizer")
    #print(ALGO_INFO)
    #loop()

    print(graph)
    


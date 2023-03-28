import pygame
import math

# Инициализация Pygame
pygame.init()

# Задание размеров окна и создание его поверхности
window_width = 640
window_height = 480
window_surface = pygame.display.set_mode((window_width, window_height))

# Задание цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Основной цикл программы
def main():
    # Задание размеров окна и масштаба графика
    x_min = -10
    x_max = 10
    y_min = -10
    y_max = 100
    scale = 20
    
    # Шаг для x
    step = 0.1
    
    # Цикл обработки событий Pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Очистка экрана
        window_surface.fill(white)
        
        # Отрисовка осей координат
        pygame.draw.line(window_surface, black, (0, window_height // 2), (window_width, window_height // 2), 2)
        pygame.draw.line(window_surface, black, (window_width // 2, 0), (window_width // 2, window_height), 2)
        
        # Отрисовка меток на осях координат
        for i in range(x_min, x_max + 1):
            x = i * scale + window_width // 2
            pygame.draw.line(window_surface, black, (x, window_height // 2 - 5), (x, window_height // 2 + 5), 2)
            draw_text(str(i), pygame.font.Font(None, 20), black, window_surface, x, window_height // 2 + 20)
        
        for i in range(y_min, y_max + 1):
            y = -i * scale + window_height // 2
            pygame.draw.line(window_surface, black, (window_width // 2 - 5, y), (window_width // 2 + 5, y), 2)
            draw_text(str(i), pygame.font.Font(None, 20), black, window_surface, window_width // 2 - 20, y)
        
        # Отрисовка графика параболы
        x = x_min
        points = []
        while x <= x_max:
            y = x ** 2
            point = (x * scale + window_width // 2, -y * scale + window_height // 2)
            points.append(point)
            x += step
        
        pygame.draw.lines(window_surface, red, False, points, 2)
        
        # Обновление экрана
        pygame.display.update()


# Вызов основной функции
if __name__ == '__main__':
    main()


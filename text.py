import pygame


def render_text(win, string, font, size, bold, opacity, x, y, color, bottom):
    text_font = pygame.font.SysFont(font, size, bold)
    text_surface = text_font.render(string, True, color)
    text_surface.set_alpha(opacity)
    if bottom:
        x = x - text_surface.get_width()
        y = y - text_surface.get_height()
    win.blit(text_surface, (x, y))

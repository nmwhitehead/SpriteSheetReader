import pygame

class SpriteSheet:
    def get_image(sheet_path, columns, rows, column_number, row_number):
        sheet = pygame.image.load(sheet_path)

        width = sheet.get_width()
        height = sheet.get_height()

        cell_width = int(width / columns)
        cell_height = int(height / rows)

        image = pygame.Surface((cell_width,cell_height)).convert_alpha()

        sprite = image.blit(sheet, (0,0), area=((cell_width*(column_number-1),cell_height*(row_number-1),cell_width,cell_height)))

        return [image,sprite]
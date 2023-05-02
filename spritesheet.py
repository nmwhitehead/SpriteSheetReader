import pygame

class SpriteSheet:
    def get_image_from_path(self, sheet_path, columns, rows, column_number, row_number):
        # This function uses the file path to the Sprite Sheet
        # It is best used when only one or two sprites are being extracted
        sheet = pygame.image.load(sheet_path)

        width = sheet.get_width()
        height = sheet.get_height()

        # This code is made for Sprite Sheets that space the sprites apart equally, as it divides the height and width by the number rows and columns
        cell_width = int(width / columns)
        cell_height = int(height / rows)

        image = pygame.Surface((cell_width,cell_height)).convert_alpha()

        # The -1s in the are calculation are due to a personal preference for the top left sprite to be (1,1) instead of (0,0)
        sprite = image.blit(sheet, (0,0), area=((cell_width*(column_number-1),cell_height*(row_number-1),cell_width,cell_height)))

        return [image,sprite]

    def get_image_from_sheet(self, sprite_sheet, columns, rows, column_number, row_number):
        # This function requires that the Sprite Sheet already be set to a value
        # It is best used when multiple sprites are being extracted, as loading in the sheet each time will take up more space
        width = sprite_sheet.get_width()
        height = sprite_sheet.get_height()

        # This code is made for Sprite Sheets that space the sprites apart equally, as it divides the height and width by the number rows and columns
        cell_width = int(width / columns)
        cell_height = int(height / rows)

        image = pygame.Surface((cell_width,cell_height)).convert_alpha()

        # The -1s in the are calculation are due to a personal preference for the top left sprite to be (1,1) instead of (0,0)
        sprite = image.blit(sprite_sheet, (0,0), area=((cell_width*(column_number-1),cell_height*(row_number-1),cell_width,cell_height)))

        return [image,sprite]
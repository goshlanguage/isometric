# UI functions for pygame

# label, x,y, width, height, inactive_color, active_color, action or subprogram
def button(msg,x,y,w,h,inactive_image, active_image,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        #pygame.draw.rect(display, ac,(x,y,w,h))
        display.blit(active_image, (x,y))

        if click[0] == 1 and action != None:
            action()
    else:
        #pygame.draw.rect(display, inactive_image,(x,y,w,h))
        display.blit(active_image, (x,y))
    smallText = pygame.font.Font("fonts/Minecraft.ttf",26)

    textSurf = smallText.render(msg, True, (0,0,0))
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)
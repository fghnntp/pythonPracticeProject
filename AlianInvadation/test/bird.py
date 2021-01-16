collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
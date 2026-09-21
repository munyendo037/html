score=0
combo=0
balls=[ball]
keys==pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    paddle.x +=8
if keys[pygame.K_RIGHT]:
    paddle.x +=8
for ball in balls:
    ball.x += ball.dx 
    ball.y += ball.dy
    if ball.colliderect(paddle):
         ball.y *= -1
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball.dy *= -1 
            score +=100
            combo += 1
if powerup:
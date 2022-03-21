from cmu_112_graphics import *
import random, math, time, string

class Enemy(object):
    def __init__(self, ex, ey, ea, damage, eHealth, maxHealth, sprite, shooter, scale, monster):
        self.ex = ex
        self.ey = ey
        self.ea = ea
        self.edx = math.cos(self.ea)*3
        self.edy = math.sin(self.ea)*3
        self.damage = damage
        self.eHealth = eHealth
        self.sprite = sprite
        self.shooter = shooter
        self.scale = scale
        self.maxHealth = maxHealth
        self.monster = monster

class Bullet(object):
    def __init__(self, bx, by, bdx, bdy, damage):
        self.bx = bx 
        self.by = by 
        self.bdx = bdx 
        self.bdy = bdy 
        self.damage = damage

class Rocket(object):
    def __init__(self, rx, ry, rdx, rdy):
        self.rx = rx 
        self.ry = ry 
        self.rdx = rdx 
        self.rdy = rdy 

class Plasma(object):
    def __init__(self, plasx, plasy, plasdx, plasdy):
        self.plasx = plasx 
        self.plasy = plasy 
        self.plasdx = plasdx 
        self.plasdy = plasdy

class Weapon(object):
    def __init__(self, x, y, damage, maxClip, ammo, sprite, rpg, image, special):
        self.x = x
        self.y = y
        self.damage = damage
        self.sprite = sprite
        self.maxClip = maxClip
        self.ammo = ammo
        self.rpg = rpg
        self.image = image
        self.special = special

##########################################
# Home Screen Mode
##########################################

def homeScreen_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='black')
    canvas.create_image((app.width/2)+14, (app.height/2)-150,image = ImageTk.PhotoImage(app.scaleImage(app.title, 0.4)))
    canvas.create_text((app.width/2), (app.height/2)-70, text = 'VS', font = 'Times 35 bold', fill = 'red')
    canvas.create_text((app.width/2), (app.height/2)-20, text = '112', font = 'Times 75 bold', fill = 'red')
    canvas.create_rectangle((app.width/2)-80, (app.height/2)+60-25, (app.width/2)+80, (app.height/2)+60+25, outline= 'red', fill ='black')
    canvas.create_text((app.width/2), (app.height/2)+60, text = 'Play', font = 'Times 35 bold', fill = 'red')
    canvas.create_rectangle((app.width/2)-80, (app.height/2)+130-25, (app.width/2)+80, (app.height/2)+130+25,outline= 'red',fill= 'black')
    canvas.create_text((app.width/2), (app.height/2)+130, text = 'Maze', font = 'Times 35 bold', fill = 'red')
    canvas.create_oval((app.width/2+(80))-16,(app.height/2)+130-25-16, (app.width/2+80)+16,(app.height/2)+130+16-25,outline= 'red',fill ='red')
    canvas.create_text((app.width/2+(80)), (app.height/2)+130-25+5, text = 'PRIZE', fill = 'black', font = 'Times 8 bold')
    canvas.create_text((app.width/2+(80)), (app.height/2)+130-25-5, text = 'WIN', fill = 'black', font = 'Times 8 bold')
    canvas.create_rectangle((app.width/2)-80, (app.height/2)+200-25, (app.width/2)+80, (app.height/2)+200+25, outline= 'red', fill = 'black')
    canvas.create_text((app.width/2), (app.height/2)+200, text = 'Controls', font = 'Times 35 bold', fill = 'red')

def homeScreen_mousePressed(app, event):
    if ((app.width/2)-80) <= event.x <= ((app.width/2)+80) and ((app.height/2)+60-25) <= event.y <= ((app.height/2)+60+25):
        app.mode = 'enterName'
    elif ((app.width/2)-80) <= event.x <= ((app.width/2)+80) and ((app.height/2)+130-25) <= event.y <= ((app.height/2)+130+25):
        app.mode = 'mazeRules'
    elif ((app.width/2)-80) <= event.x <= ((app.width/2)+80) and ((app.height/2)+200-25) <= event.y <= ((app.height/2)+200+25):
        app.mode = 'controlsMode'
    else:
        return None

##########################################
# Enter Name
##########################################

def enterName_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='black')
    canvas.create_text(app.width/2, (app.height/2)-180, text = f'ENTER YOUR NAME!', font = 'Times 75 bold', fill = 'red')
    space = len(app.name)/2
    for x in app.name:
        canvas.create_text(app.width/2 - (space*65), app.height*(3/8) + 70 ,
                        text= x.upper(),
                        font = 'Times 70 bold',
                        fill = 'white')
        canvas.create_text(app.width/2 - (space*65), app.height*(3/8) + 70 ,
                        text= '_',
                        font = 'Times 110 bold',
                        fill = 'red')
        space -= 1
    canvas.create_line(0, app.height/3, app.width, app.height/3, fill = 'red', width = 3)
    canvas.create_line(0, app.height*(2/3), app.width, app.height*(2/3), fill = 'red', width = 3)
    canvas.create_rectangle(app.width*(1.2/4)+100, app.height*(26/32)+30, app.width*(1.2/4)-100, app.height*(26/32)-30, fill = 'black', outline = 'red', width = 4)#retry
    canvas.create_text(app.width*(1.2/4), app.height*(26/32), text = 'Return', fill = 'red', font = 'Times 40 bold')
    canvas.create_rectangle(app.width*(2.8/4)+100, app.height*(26/32)+30, app.width*(2.8/4)-100, app.height*(26/32)-30, fill = 'black', outline = 'red', width = 4)#quit
    if app.name == '':
        canvas.create_text(app.width*(2.8/4), app.height*(26/32), text = 'Guest?', fill = 'red', font = 'Times 40 bold')
    else:
        canvas.create_text(app.width*(2.8/4), app.height*(26/32), text = 'Continue', fill = 'red', font = 'Times 40 bold')

#https://piazza.com/class/kjyble3m9l1ar?cid=3830
def enterName_keyPressed(app, event):
    if event.key in string.ascii_lowercase:
		    app.name += event.key
    elif event.key == "Delete" and len(app.name) > 0:
            app.name = app.name[:-1]

def enterName_mousePressed(app, event): 
    if (app.width*(1.2/4)-100 <= event.x <= app.width*(1.2/4)+100) and (app.height*(26/32)-30 <= event.y <= app.height*(26/32)+30):
        app.mode = 'homeScreen'
    elif (app.width*(2.8/4)-100 <= event.x <= app.width*(2.8/4)+100) and (app.height*(26/32)-30 <= event.y <= app.height*(26/32)+30):
        app.mode = 'gameMode'
    else:
        return None

##########################################
# Controls Mode
##########################################

def controlsMode_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='black')
    canvas.create_rectangle(10,10,app.width-10,app.height-10, fill='grey')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, fill='black')
    canvas.create_text(125,50, text = 'Game Controls', fill = 'red', font = 'Times 29 bold')
    canvas.create_line(45, 70, 205, 70, fill = 'red', width = 2)
    canvas.create_line(55, 80, 195, 80, fill = 'red', width = 2)
    canvas.create_image( 190, 170, image = ImageTk.PhotoImage(app.scaleImage(app.wasd, 0.5)))
    canvas.create_text(270,150, text = 'FORWARD', fill = 'red', font = 'Times 20 bold')
    canvas.create_text(280,240, text = 'RIGHT', fill = 'red', font = 'Times 20 bold')
    canvas.create_text(120,240, text = 'LEFT', fill = 'red', font = 'Times 20 bold')
    canvas.create_text(200,240, text = 'BACK', fill = 'red', font = 'Times 20 bold')
    canvas.create_image( 500, 170, image = ImageTk.PhotoImage(app.scaleImage(app.arrows, 0.45)))
    canvas.create_text(620,150, text = 'SWITCH WEAPON', fill = 'red', font = 'Times 20 bold')
    canvas.create_text(430,240, text = 'TURN LEFT', fill = 'red', font = 'Times 20 bold')
    canvas.create_text(600,240, text = 'TURN RIGHT', fill = 'red', font = 'Times 20 bold')
    canvas.create_image(app.width/2, app.height/2+35, image = ImageTk.PhotoImage(app.scaleImage(app.sp, 0.25)))
    canvas.create_text(app.width/2-25, app.height/2+68,text = 'SHOOTING', fill = 'red', font = 'Times 20 bold')
    canvas.create_image(app.width/8, app.height/2+150, image = ImageTk.PhotoImage(app.scaleImage(app.mouse, 0.1)))
    canvas.create_text(app.width/8+100, app.height/2+180,text = 'TO SELECT', fill = 'red', font = 'Times 20 bold')
    canvas.create_image(app.width/2-40, app.height/2+180, image = ImageTk.PhotoImage(app.scaleImage(app.escape, 0.25)))
    canvas.create_text(app.width/2+70, app.height/2+180, text = 'PAUSE MENU', fill = 'red', font = 'Times 20 bold')
    canvas.create_rectangle((app.width*(3.3/4))+80, app.height*(28/32)+25,(app.width*(3.3/4))-60, app.height*(28/32)-25, outline= 'red', fill = 'black', width = 3)
    canvas.create_text((app.width*(3.3/4))+10, app.height*(28/32),text= 'GOT IT!', fill = 'red', font = 'Times 27 bold')

def controlsMode_mousePressed(app, event):
    if ((app.width*(3.3/4))-80) <= event.x <= ((app.width*(3.3/4))+80) and (app.height*(28/32)-25) <= event.y <= (app.height*(28/32)+25):
        app.mode = 'homeScreen'

##########################################
# Maze Rules
##########################################

def mazeRules_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='black')
    canvas.create_rectangle(0, 80-50, app.width, 80+50, outline= 'red', fill = 'red', width = 3)
    canvas.create_text((app.width*(1/2)), 80, text= 'Maze Rules', fill = 'black', font = 'Times 47 bold')
    canvas.create_text((app.width*(1/2)),180, text= '1. Randomly Generated Mazes.', fill = 'red', font = 'Times 29')
    canvas.create_text((app.width*(1/2)),240, text= '2. Starts at a 10x10 Maze.', fill = 'red', font = 'Times 29')
    canvas.create_text((app.width*(1/2)),300, text='3. Map is Not Available (Unless the Map is found).', fill = 'red', font = 'Times 29 ')
    canvas.create_text((app.width*(1/2)),360, text= '4. Win the Best Weapon in the Game after beating 10 Mazes.', fill = 'red', font = 'Times 29 ')
    canvas.create_text(63,410, text= 'Prize:', fill = 'red', font = 'Times 37 bold')
    canvas.create_text((app.width*(1/4))-20, app.height*(26/32), text= 'Plasma Gun', fill = 'red', font = 'Times 32')
    canvas.create_image((app.width*(2/4)), app.height*(26/32), image = ImageTk.PhotoImage(app.prize))
    canvas.create_rectangle((app.width*(3.3/4))+60, app.height*(23.5/32)+25,(app.width*(3.3/4))-60, app.height*(23.5/32)-25, outline= 'red', fill = 'black', width = 3)
    canvas.create_text((app.width*(3.3/4)), app.height*(23.5/32),text= 'Strart', fill = 'red', font = 'Times 27 bold')
    canvas.create_rectangle((app.width*(3.3/4))+60, app.height*(28.5/32)+25,(app.width*(3.3/4))-60, app.height*(28.5/32)-25, outline= 'red', fill = 'black', width = 3)
    canvas.create_text((app.width*(3.3/4)), app.height*(28.5/32),text= 'Return', fill = 'red', font = 'Times 27 bold')

def mazeRules_mousePressed(app, event):
    if ((app.width*(3.3/4))-60) <= event.x <= ((app.width*(3.3/4))+60) and (app.height*(23.5/32)-25) <= event.y <= (app.height*(23.5/32)+25):
        app.mode = 'mazeMode'
    elif ((app.width*(3.3/4))-60) <= event.x <= ((app.width*(3.3/4))+60) and (app.height*(28.5/32)-25) <= event.y <= (app.height*(28.5/32)+25):
        app.mode = 'homeScreen'
    else:
        return None

##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    drawSky(app, canvas)
    canvas.create_image(app.width/2, app.height*(3/4), image = ImageTk.PhotoImage(app.scaleImage(app.green, 1.2)))
    drawWalls(app, canvas)
    drawPortol(app, canvas)
    drawEnemy3D(app, canvas)
    draw3DBullets(app, canvas)
    draw3DRockets(app, canvas)
    draw3DPlasma(app, canvas)
    drawWeapon(app, canvas)
    drawBoard(app, canvas)
    drawBullets(app, canvas)
    drawRockets(app, canvas)
    drawPlasmas(app, canvas)
    drawWaveNumber(app, canvas)
    drawNewShotGun(app, canvas)
    drawNewLauncher(app, canvas)
    drawPauseScreen(app, canvas)

def gameMode_keyPressed(app, event):
    if event.key == 'Escape':
        app.gamePause = not app.gamePause

    if not app.gamePause:
        if event.key == 'w':
            if isLegal(app, app.px+app.pdx, app.py+app.pdy):
                app.px += app.pdx
                app.py += app.pdy
        
        if event.key == 's':
            if isLegal(app, app.px-app.pdx, app.py-app.pdy):
                app.px -= app.pdx
                app.py -= app.pdy
        
        if event.key == 'd':
            pddx = math.cos(app.pa+(math.pi/2))*3
            pddy = math.sin(app.pa+(math.pi/2))*3
            if isLegal(app, app.px+pddx, app.py+pddy):
                app.px += pddx
                app.py += pddy
            
        if event.key == 'a':
            pddx = math.cos(app.pa+(math.pi/2))*3
            pddy = math.sin(app.pa+(math.pi/2))*3
            if isLegal(app, app.px-pddx, app.py-pddy):
                app.px -= pddx
                app.py -= pddy
        
        if event.key == 'Space':
            if app.currentWeapon.ammo > 0:
                if not app.currentWeapon.special:
                    for enemy in app.enemies:
                        ex, ey = enemy.ex, enemy.ey
                        dx, dy = ex - app.px, ey - app.py
                        ds = math.sqrt(dx ** 2 + dy ** 2)
                        if dx == 0:
                            dx += 0.0001
                        if dy == 0:
                            dy += 0.0001
                        
                        theta = math.atan(dy/dx)
                        gamma = theta - app.pa         
                            
                        if dx < 0:
                            gamma += math.pi

                        elif dy < 0 and dx < 0:
                            gamma += 2*math.pi
                        
                        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
                            gamma += 2*math.pi
                            
                        ra = app.pa + gamma
                        if ra < 0:
                            ra += 2*math.pi
                        if ra > 2*math.pi:
                            ra -= 2*math.pi
                        
                        if ra == 0 or ra == math.pi:
                            rx = app.px
                            ry = app.py
                            dof = app.dof
                        
                        elif ra < math.pi:
                            aTan = -1/math.tan(ra)
                            x,y = getGameCell(app, app.px, app.py)
                            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
                            ry += 0.01
                            rx = (app.py-ry)*aTan+app.px
                            yo = app.bsize
                            xo = -yo*aTan

                        elif ra > math.pi:
                            aTan = -1/math.tan(ra)
                            x,y = getGameCell(app, app.px, app.py)
                            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
                            ry -= 0.01
                            rx = (app.py-ry)*aTan+app.px
                            yo = -app.bsize
                            xo = -yo*aTan

                        dof = 0
                        while(dof < app.dof):
                            row, col = getGameCell(app, rx, ry)
                            if(app.map[row][col]==1):
                                dof=app.dof
                            else:
                                rx += xo
                                ry += yo
                                dof += 1
                                
                        DH = findLength(app, rx, ry, app.px, app.py) 

                        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
                            cx = app.px
                            cy = app.py
                            dof = app.dof
                        
                        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
                            nTan = -math.tan(ra)
                            x,y = getGameCell(app, app.px, app.py)
                            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
                            cx -= 0.1
                            cy = (app.px-cx)*nTan+app.py
                            xo = -app.bsize
                            yo = -xo*nTan

                        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
                            nTan = -math.tan(ra)
                            x,y = getGameCell(app, app.px, app.py)
                            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
                            cx += 0.1
                            cy = (app.px-cx)*nTan+app.py
                            xo = app.bsize
                            yo = -xo*nTan

                        dof = 0
                        while(dof < app.dof):
                            row, col = getGameCell(app, cx, cy)
                            if(app.map[row][col]==1):
                                dof=app.dof
                            else:
                                cx += xo
                                cy += yo
                                dof += 1

                        DV = findLength(app, cx, cy, app.px, app.py) 

                        if DV < DH:
                            DT = DV
                        else:
                            DT = DH

                        if not app.currentWeapon.rpg:
                            if onTarget(app, enemy.ex, enemy.ey, ds) and (ds < DT):
                                enemy.eHealth -= app.currentWeapon.damage
                                if enemy.eHealth <= 0 :
                                    if enemy.monster:
                                        app.score += 1000
                                        app.kills += 1
                                    elif enemy.shooter:
                                        app.score += 300
                                        app.kills+=1
                                    else:
                                        app.score += 500
                                        app.kills+=1
                                    app.enemies.pop(app.enemies.index(enemy))
                                    
                    if app.currentWeapon.rpg:
                        app.rockets.append(Rocket(app.px, app.py, -app.pdx, -app.pdy))
                else:
                    app.plasma.append(Plasma(app.px, app.py, -app.pdx, -app.pdy))

                app.currentWeapon.ammo -= 1

        if event.key == 'Left':
            app.pa -= 0.1
            if app.pa < 0:
                app.pa = 2*math.pi
            
        if event.key == 'Right':
            app.pa += 0.1
            if app.pa > 2*math.pi:
                app.pa = 0
        
        if event.key == 'Up':
            if app.select < (len(app.myWeapons) - 1):
                app.select += 1
                app.currentWeapon = app.myWeapons[app.select]
            elif app.select == (len(app.myWeapons) - 1):
                app.select = 0
                app.currentWeapon = app.myWeapons[app.select]

        app.pdx = math.cos(app.pa)*3
        app.pdy = math.sin(app.pa)*3


def rbgString(app, r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}' # to get colors

def gameMode_timerFired(app):
    if not app.gamePause:
        if app.enemies != []:
            for enemy in app.enemies:
                if enemy.eHealth <= 0 :
                    if enemy.monster:
                        app.score += 1000
                        app.kills += 1
                    elif enemy.shooter:
                        app.score += 300
                        app.kills += 1
                    else:
                        app.score += 500
                        app.kills += 1
                    
                    app.enemies.remove(enemy)

        app.timer += 1
        for enemy in app.enemies:
            if not enemy.shooter:
                dx, dy = enemy.ex - app.px, enemy.ey - app.py
                if abs(dx)>0 and abs(dy)>0:
                    ds = math.sqrt(dx ** 2 + dy ** 2)
                    enemy.ea = math.atan(dy/dx)  

                    enemy.edx = math.cos(enemy.ea)*3
                    enemy.edy = math.sin(enemy.ea)*3
                    
                    if dx < 0:
                        if isLegal(app, enemy.ex + enemy.edx/2, enemy.ey + enemy.edy/2) and ds > 5:
                            enemy.ex += enemy.edx/2
                            enemy.ey += enemy.edy/2
                    else:
                        if isLegal(app, enemy.ex - enemy.edx/2, enemy.ey - enemy.edy/2) and ds > 5:
                            enemy.ex -= enemy.edx/2
                            enemy.ey -= enemy.edy/2
                    
                    if ds < 6:
                        app.hp -= enemy.damage            
            else:
                dx, dy = enemy.ex - app.px, enemy.ey - app.py
                if abs(dx)>0 and abs(dy)>0:
                    ds = math.sqrt(dx ** 2 + dy ** 2)
                    enemy.ea = math.atan(dy/dx)  

                    enemy.edx = math.cos(enemy.ea)*3
                    enemy.edy = math.sin(enemy.ea)*3

                    if ds > 40:
                        if dx < 0:
                            if isLegal(app, enemy.ex + enemy.edx/2, enemy.ey + enemy.edy/2):
                                enemy.ex += enemy.edx/2
                                enemy.ey += enemy.edy/2
                        else:
                            if isLegal(app, enemy.ex - enemy.edx/2, enemy.ey - enemy.edy/2):
                                enemy.ex -= enemy.edx/2
                                enemy.ey -= enemy.edy/2
                    
                    if dx < 0:
                        if app.timer%15 == 0:
                            app.bullets.append(Bullet(enemy.ex, enemy.ey, -enemy.edx, -enemy.edy, enemy.damage))
                    else:
                        if app.timer%15 == 0:
                            app.bullets.append(Bullet(enemy.ex, enemy.ey, enemy.edx, enemy.edy, enemy.damage))

        for bullet in app.bullets:
            bullet.bx -= bullet.bdx*2
            bullet.by -= bullet.bdy*2
            if ((bullet.bx - app.px)**2 + (bullet.by - app.py)**2) <= 8:
                app.hp -= bullet.damage
                app.bullets.remove(bullet)
            elif not isLegal(app, bullet.bx, bullet.by):
                app.bullets.remove(bullet)
        
        for rocket in app.rockets:
            rocket.rx -= rocket.rdx*2
            rocket.ry -= rocket.rdy*2
            for enemy in app.enemies:
                if ((rocket.rx - enemy.ex)**2 + (rocket.ry - enemy.ey)**2) <= 14:
                    enemy.eHealth -= app.currentWeapon.damage
                    app.rockets.remove(rocket)
            if not isLegal(app, rocket.rx, rocket.ry):
                app.rockets.remove(rocket)

        for plasma in app.plasma:
            plasma.plasx -= plasma.plasdx*2
            plasma.plasy -= plasma.plasdy*2
            for enemy in app.enemies:
                if ((plasma.plasx - enemy.ex)**2 + (plasma.plasy - enemy.ey)**2) <= 14:
                    enemy.eHealth -= app.currentWeapon.damage
            if not isLegal(app, plasma.plasx, plasma.plasy):
                app.plasma.remove(plasma)
        
        if getGameCell(app, app.px, app.py) == (1, 6) and app.enemies == []:
            newWave(app)
        
        if app.hp <= 0:
            if app.name != '':
                app.leaderboard.append([f'{app.name}',f'{app.score}',f'{app.kills}'])
                lst = []
                for person in app.leaderboard:
                    lst.append(int(person[1]))
                lst.sort()
                lst.reverse()
                newL = []
                for score in lst:
                    for person in app.leaderboard:
                        if score == int(person[1]):
                            newL.append(person)
                app.leaderboard = newL
                file = open('leaderboard.txt', 'w')
                for person in app.leaderboard:
                    file.write(f'{person[0]},{person[1]},{person[2]}\n')
                file.close()
                app.mode = 'GameOver'
            else:
                app.mode = 'GameOver'

def gameMode_mousePressed(app, event):
    if app.gamePause:
        if ((app.width/2 - 100) <= event.x <= (app.width/2 + 100)) and (170 <= event.y <=230):
            app.gamePause = False
        elif (app.width/2 - 100) <= event.x <= (app.width/2 + 100) and (260 <= event.y <=320):
            app.mode = 'homeScreen'
            app.wave = 1
            app.px = 3 + (app.rows/2)*app.bsize
            app.py = ((3/4)*app.height) - 9 + (app.cols-1.5)*app.bsize
            app.hp = 100
            app.pa = (3/2)*math.pi
            app.pdx = math.cos(app.pa)*3
            app.pdy = math.sin(app.pa)*3
            Devils = [] 
            for i in range(1):
                Devils.append(Enemy(0, 0, 0, 2, 20, 20, app.loadImage('Devil.png'), False, 3, False))
            Shooters = [] 
            for i in range(1):
                Shooters.append(Enemy(0, 0, 0, 5, 15, 15, app.loadImage('Solider.png'), True, 18, False))
            app.enemies = Devils + Shooters
            app.spots = spawnableSpots(app, app.map)
            for enemy in app.enemies:
                (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
                x0,y0,x1,y1 = getGameCellBounds(app,row,col)
                enemy.ex = (x0 + x1)/2 + 0.1
                enemy.ey = (y0 + y1)/2
            app.timer = 0
            app.bullets = []
            app.rockets = []
            app.plasma = []
            pistol = Weapon((app.width/2 + 160), app.height/2 + 50, 2, 10, 50, app.scaleImage(app.loadImage('Gun.png'), 0.4), False, app.scaleImage(app.loadImage('pistolImage.png'), 1), False)
            plasmaRay = Weapon(app.width/2, app.height/2 + 75 , 50, 1, 5, app.scaleImage(app.loadImage('plasmaRay.png'), 3), False, app.scaleImage(app.loadImage('plazmaRayImage.png'), 0.8), True) 
            if app.specialWeapon[0] in app.myWeapons:
                app.myWeapons = [pistol, plasmaRay]
            else:
                app.myWeapons = [pistol]
            app.select = 0
            app.currentWeapon = app.myWeapons[app.select]
            app.score = 0
            app.kills = 0
            app.newShotGun = False
            app.newLauncher = False
            app.gamePause = False
        else:
            return None

def drawPauseScreen(app, canvas):
    if app.gamePause:
        canvas.create_rectangle(200, 50, app.width - 200, (app.height*(3/4))-11-50, fill = 'black')
        canvas.create_rectangle(210, 60, app.width - 210, (app.height*(3/4))-11-60, fill = 'grey')
        canvas.create_text(app.width/2, 100,text= 'Paused',font = 'Times 70 bold',fill = 'black')
        canvas.create_rectangle(app.width/2 + 100, 170, app.width/2 - 100, 230, width = 4) # Resume
        canvas.create_rectangle(app.width/2 + 100, 260, app.width/2 - 100, 320, width = 4) # Quit
        canvas.create_text(app.width/2, 200, text = 'Resume', font = 'Times 35 bold',fill = 'black')
        canvas.create_text(app.width/2, 290, text = 'Quit', font = 'Times 35 bold',fill = 'black')

def findLength(app, x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y0-y1)**2)

def almostEqual(app, d1, d2, epsilon=1*(180/math.pi)):
    return (abs(d2 - d1) < epsilon)

def isLegal(app, x, y):
    row, col = getGameCell(app, x, y)
    if app.map[row][col] == 1:
        return False
    return True

def onTarget(app, x, y,z):
    sx = 0
    dx, dy = x - app.px, y - app.py
    ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
    if dx == 0:
        dx += 0.0001
    if dy == 0:
        dy += 0.0001

    theta = math.atan(dy/dx)
    gamma = theta - app.pa     

    if dx < 0:
        gamma += math.pi

    elif dy < 0 and dx < 0:
        gamma += 2*math.pi
    
    elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
        gamma += 2*math.pi
    
    if -app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180):
        sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)

    if (app.width/2 - 1200/z) < sx <  (app.width/2 + 1200/z):
        return True
    else:
        return False

# https://www.cs.cmu.edu/~112/index.html
def pointInGrid(app, x, y):
    return ((3 <= x <= (3 + (app.height/4))) and (((app.height*(3/4)) - 9) <= y <= (app.height - 9)))
# https://www.cs.cmu.edu/~112/index.html
def getGameCell(app, x, y):
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.height/4
    gridHeight = app.height/4
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - (app.height*(3/4)) + 9) / cellHeight)
    col = int((x - 3) / cellWidth)
    return (row, col)
# https://www.cs.cmu.edu/~112/index.html
def getGameCellBounds(app, row, col):
    gridWidth  = app.height/4
    gridHeight = app.height/4
    x0 = 3 + gridWidth * col / app.cols
    x1 = 3 + gridWidth * (col+1) / app.cols
    y0 = (app.height*(3/4)) + (gridHeight * row / app.rows) - 9
    y1 = (app.height*(3/4)) + (gridHeight * (row+1) / app.rows) - 9
    return (x0, y0, x1, y1)
# https://www.cs.cmu.edu/~112/index.html
def getGameObjectPosition(app, row, col):
    gridWidth  = app.height/4
    gridHeight = app.height/4
    x0 = 3 + gridWidth * col / app.cols
    x1 = 3 + gridWidth * (col+1) / app.cols
    y0 = (app.height*(3/4)) + (gridHeight * row / app.rows) - 9
    y1 = (app.height*(3/4)) + (gridHeight * (row+1) / app.rows) - 9
    return (abs(x0-x1)/2, abs(y0-y1)/2)
# https://www.cs.cmu.edu/~112/index.html
def drawGameMap(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getGameCellBounds(app, row, col)
            if app.map[row][col]==0:
                fill = 'gray'
                out = 'gray'
            elif app.map[row][col]==1:
                fill = 'black'
                out = 'black'
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline = out)
    canvas.create_text(app.width*(0.035), app.height*(24/32),text= 'Map',
                       font = 'Time 19 bold',fill = 'yellow')

def drawBoard(app, canvas):
    canvas.create_rectangle(5,(app.height*(3/4))-11, app.width-5, app.height-6, fill = 'gray', width = 10)
    drawHealth(app, canvas)
    drawGameMap(app, canvas)
    drawEnemy(app, canvas) 
    drawPlayer(app, canvas)  
    drawWeaponsInUse(app, canvas)
    drawAmmo(app, canvas)
    drawScoreAndKills(app, canvas)
    canvas.create_line(app.width*(1.38/3),app.height*(2.18/3),app.width*(1.38/3),
                       app.height, fill = 'black', width = 7)
    canvas.create_line(app.width*(2/3),app.height*(2.18/3),app.width*(2/3),
                       app.height, fill = 'black', width = 7)
    canvas.create_line(app.width*(2.35/3),app.height*(2.18/3),app.width*(2.35/3),
                       app.height, fill = 'black', width = 7)

def drawAmmo(app, canvas):
    canvas.create_text(app.width*(2.155/3), app.height*(25/32),text= 'Ammo:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(2.195/3), app.height*(27/32),text= f'{app.currentWeapon.ammo}',
                       font = 'Helvetica 30 bold',fill = 'black')
    canvas.create_text(app.width*(2.195/3), app.height*(29/32),text= f'{app.currentWeapon.maxClip}',
                       font = 'Helvetica 30 bold',fill = 'black')
    canvas.create_line(app.width*(2.195/3)-20, app.height*(28/32), app.width*(2.2/3)+20, app.height*(28/32), fill = 'black', width = 4)

def drawScoreAndKills(app, canvas):
    canvas.create_text(app.width*(2.5/3), app.height*(25/32),text= 'Score:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(2.655/3), app.height*(26.5/32), text= f'{app.score}',
                       font = 'Helvetica 40 bold',fill = 'black')
    canvas.create_text(app.width*(2.5/3), app.height*(28.7/32),text= 'Kills:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(2.655/3), app.height*(30.2/32), text= f'{app.kills}',
                       font = 'Helvetica 40 bold',fill = 'black')

def drawWeaponsInUse(app, canvas):
    canvas.create_text(app.width*(1.57/3), app.height*(25/32),text= 'Weapon:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_image(app.width*(1.69/3), app.height*(28.5/32), image = ImageTk.PhotoImage(app.currentWeapon.image))
    
def drawWaveNumber(app,canvas):
    canvas.create_text(app.width*(0.14/3), app.height*(1/32),text= 'Wave',
                       font = 'Helvetica 20 bold',fill = 'white')
    canvas.create_text(app.width*(0.14/3), app.height*(2.8/32),text= f'{app.wave}',
                       font = 'Helvetica 40 bold',fill = 'red')

def drawHealth(app, canvas):
    canvas.create_text(app.width*(0.72/3), app.height*(25/32),text= 'Health:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(0.98/3), app.height*(28.5/32),
                       text= f'{app.hp}%',
                       font = 'Helvetica 75 bold',
                       fill = 'yellow')

def drawNewShotGun(app, canvas):
    if app.newShotGun:
        canvas.create_text(app.width*(2.1/3), app.height*(2/32),text= 'You got the Shotgun! Press UP to switch',
                       font = 'Helvetica 20 bold',fill = 'yellow')

def drawNewLauncher(app, canvas):
    if app.newLauncher:
        canvas.create_text(app.width*(2.1/3), app.height*(2/32),text= 'You got the RPG! Press UP to switch',
                       font = 'Helvetica 20 bold',fill = 'yellow')

def spawnableSpots(app, L):
    spots = []
    for row in range(len(L)):
        if row != 1 and row != len(L) - 2:
            for col in range(len(L[0])):
                if L[row][col] == 0:
                    spots.append((row, col))
    return spots

def drawWalls(app, canvas):
    ra = app.pa - app.fov/2*(math.pi/180)
    if ra < 0:
        ra += 2*math.pi
    if ra > 2*math.pi:
        ra -= 2*math.pi
    for r in range(int(app.nor)):
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]>0):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 
   
        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]>0):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1
    
        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
            wallType = 1
        else:
            DT = DH
            wallType = 2

        ca = app.pa - ra# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        if ca < 0:
            ca +=2*math.pi# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
        
        if ca == 2*math.pi:
            ca -=2*math.pi# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
        
        DT = DT * math.cos(ca) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        lineH = ((app.rows*app.cols)/(DT*19)) * ((app.height*(3/4))) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        LineO = (app.height*(3/8)) - lineH/2# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
        
        if wallType == 1:
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO, 
                            r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            fill = rbgString(app,int(205 - 300*(DT/app.colorO)), 0, 0),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            fill = rbgString(app,int(208 - 200*(DT/app.colorO)), 
                                                int(208 - 200*(DT/app.colorO)), 
                                                int(208 - 200*(DT/app.colorO))),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            r*(app.width/(app.nor)), LineO, 
                            fill = rbgString(app, int(205 - 300*(DT/app.colorO)), 0, 0),
                            width = app.lineW)
        elif wallType == 2:
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO, 
                            r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            fill = rbgString(app,int(175 - 400*(DT/app.colorO)), 0, 0),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH,
                            fill = rbgString(app,int(162 - 200*(DT/app.colorO)), 
                                                int(162 - 200*(DT/app.colorO)), 
                                                int(162 - 200*(DT/app.colorO))),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            r*(app.width/(app.nor)), LineO, 
                            fill = rbgString(app,int(175 - 400*(DT/app.colorO)), 0, 0),
                            width = app.lineW)

        ra += (app.da/180)*math.pi
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi

def drawEnemy3D(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    for enemy in app.enemies:
        ex, ey = enemy.ex, enemy.ey
        dx, dy = ex - app.px, ey - app.py
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.pa         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.pa + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
        
        if not enemy.shooter:
            if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
                and (ds < DT)):
                sd = ds
                sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
                sy = app.height*(1/3) + 30 
                canvas.create_image(sx, sy, image = ImageTk.PhotoImage(app.scaleImage(enemy.sprite, enemy.scale/ds)))
                canvas.create_rectangle(sx - 1000/ds,(sy + 1500/ds) - 100/ds,
                                        sx + 1000/ds,(sy + 1500/ds) + 100/ds, fill = 'black', outline = 'black')
                canvas.create_rectangle(sx - 950/ds,(sy + 1500/ds) - 70/ds,
                                        sx - 950/ds + (enemy.eHealth/enemy.maxHealth)*((sx + 950/ds) - (sx - 950/ds)),
                                        (sy + 1500/ds) + 70/ds, fill = 'red', outline = 'red')
        else:
            if app.timer%15 != 0:
                if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
                    and (ds < DT)):
                    sd = ds
                    sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
                    sy = app.height*(1/3) + 30 
                    canvas.create_image(sx, sy, image = ImageTk.PhotoImage(app.scaleImage(enemy.sprite, enemy.scale/ds)))
                    canvas.create_rectangle(sx - 1000/ds,(sy + 1500/ds) - 100/ds,
                                            sx + 1000/ds,(sy + 1500/ds) + 100/ds, fill = 'black', outline = 'black')
                    canvas.create_rectangle(sx - 950/ds,(sy + 1500/ds) - 70/ds,
                                            sx - 950/ds + (enemy.eHealth/enemy.maxHealth)*((sx + 950/ds) - (sx - 950/ds)),
                                            (sy + 1500/ds) + 70/ds, fill = 'red', outline = 'red')
            else:
                if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
                    and (ds < DT)):
                    sd = ds
                    sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
                    sy = app.height*(1/3) + 30 
                    canvas.create_image(sx, sy, image = ImageTk.PhotoImage(app.scaleImage(app.shot, enemy.scale/ds)))
                    canvas.create_rectangle(sx - 1000/ds,(sy + 1500/ds) - 100/ds,
                                            sx + 1000/ds,(sy + 1500/ds) + 100/ds, fill = 'black', outline = 'black')
                    canvas.create_rectangle(sx - 950/ds,(sy + 1500/ds) - 70/ds,
                                            sx - 950/ds + (enemy.eHealth/enemy.maxHealth)*((sx + 950/ds) - (sx - 950/ds)),(sy + 1500/ds) + 70/ds, fill = 'red', outline = 'red')

def draw3DBullets(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
    for bullet in app.bullets:
        ex, ey = bullet.bx, bullet.by
        dx, dy = ex - app.px, ey - app.py
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.pa         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.pa + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
                
        if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
            and (ds < DT)):
            sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
            sy = app.height*(1/3) + 30 
            canvas.create_oval(sx - 150/ds, sy - 150/ds,sx + 150/ds,sy + 150/ds,fill = 'red')

def draw3DRockets(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    for rocket in app.rockets:
        ex, ey = rocket.rx, rocket.ry
        dx, dy = ex - app.px, ey - app.py
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.pa         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.pa + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
                
        if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
            and (ds < DT)):
            sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
            sy = app.height*(1/3) + 30 
            canvas.create_image(sx, sy,image = ImageTk.PhotoImage(app.scaleImage(app.rock, 15/ds)))

def draw3DPlasma(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    for plasma in app.plasma:
        ex, ey = plasma.plasx, plasma.plasy
        dx, dy = ex - app.px, ey - app.py
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.pa         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.pa + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
                
        if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
            and (ds < DT)):
            sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
            sy = app.height*(1/3) + 30 
            canvas.create_image(sx, sy,image = ImageTk.PhotoImage(app.scaleImage(app.plasmaShot, 15/ds)))

def drawPortol(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    if app.enemies == []:
        x0,y0,x1,y1 = getGameCellBounds(app,1,6)
        ex = (x0 + x1)/2 + 0.01
        ey = (y0 + y1)/2 + app.bsize/2
        dx, dy = ex - app.px, ey - app.py
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.pa         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.pa <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.pa + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.px
            ry = app.py
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, ry, x1, y1) = (getGameCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = app.bsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, x1, ry) = (getGameCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.py-ry)*aTan+app.px
            yo = -app.bsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, rx, ry)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.px, app.py) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.px
            cy = app.py
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (x0, y0, cx, y1) = (getGameCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = -app.bsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getGameCell(app, app.px, app.py)
            (cx, y0, x1, y1) = (getGameCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.px-cx)*nTan+app.py
            xo = app.bsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getGameCell(app, cx, cy)
            if(app.map[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.px, app.py) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
                
        if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
            and (ds < DT)):
            sx = app.width/2 + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
            sy = app.height*(1/3) + 30 
            canvas.create_image(sx, sy,image = ImageTk.PhotoImage(app.scaleImage(app.portol, 15/ds)))

def newWave(app):
    app.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,0,1,1,1,1,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,1,1,1,1,0,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1]]
    for i in range(10):
        row = random.randint(3, len(app.map)-4)
        col = random.randint(2, len(app.map)-3)
        app.map[row][col] = 1
    app.wave += 1
    app.px = 3 + (app.rows/2)*app.bsize
    app.py = ((3/4)*app.height) - 9 + (app.cols-1.5)*app.bsize
    app.pa = (3/2)*math.pi
    app.bullets = []
    app.rockets = []
    app.plasma = []
    if app.wave == 3:
        app.myWeapons.append(app.allWeapons[1])
        app.newShotGun = True
    if app.wave > 3:
        app.newShotGun = False

    if app.wave == 5:
        app.myWeapons.append(app.allWeapons[2])
        app.newLauncher = True
    if app.wave > 5:
        app.newLauncher = False

    if app.hp < 80:
        app.hp += 20
    else:
        app.hp = 100
    
    for weapon in app.myWeapons:
            if not weapon.rpg and not weapon.special and weapon.damage == 2:
                weapon.ammo += 30
            elif not weapon.rpg and not weapon.special and weapon.damage == 10:
                weapon.ammo += 15
            elif weapon.rpg:
                weapon.ammo += 10
            elif weapon.special:
                weapon.ammo += 5
    
    if app.wave%5 != 0:
        Devils = [] 
        for i in range(app.wave):
            Devils.append(Enemy(0, 0, 0, 2, 20+app.wave, 20+app.wave, app.loadImage('Devil.png'), False, 3, False))
        Shooters = [] 
        for i in range(app.wave):
            Shooters.append(Enemy(0, 0, 0, 5, 15+app.wave, 15+app.wave, app.loadImage('Solider.png'), True, 18, False))
        app.enemies = Devils + Shooters
        app.spots = spawnableSpots(app, app.map)
        for enemy in app.enemies:
            (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
            x0,y0,x1,y1 = getGameCellBounds(app,row,col)
            enemy.ex = (x0 + x1)/2 + 0.1
            enemy.ey = (y0 + y1)/2
    else:
        Devils = [] 
        for i in range(app.wave//5):
            Devils.append(Enemy(0, 0, 0, 2, 20+app.wave, 20+app.wave, app.loadImage('Devil.png'), False, 3, False))
        Shooters = [] 
        for i in range(app.wave//5):
            Shooters.append(Enemy(0, 0, 0, 5, 15+app.wave, 15+app.wave, app.loadImage('Solider.png'), True, 18, False))
        Monster = [Enemy(0, 0, 0, 50+(2)*app.wave, 100+(2)*app.wave, 100+(2)*app.wave, app.loadImage('Monster.png'), False, 8, True)]
        app.enemies = Devils + Shooters + Monster
        app.spots = spawnableSpots(app, app.map)
        for enemy in app.enemies:
            (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
            x0,y0,x1,y1 = getGameCellBounds(app,row,col)
            enemy.ex = (x0 + x1)/2 + 0.1
            enemy.ey = (y0 + y1)/2
    

def drawPlayer(app, canvas):
    canvas.create_oval(app.px-2, app.py-2, app.px+2, app.py+2, 
                        fill = 'yellow', outline = 'yellow')
    canvas.create_line(app.px, app.py, app.px+app.pdx*2, app.py+app.pdy*2, 
                       fill = 'yellow')

def drawEnemy(app, canvas):
    for enemy in app.enemies:
        canvas.create_oval(enemy.ex-2, enemy.ey-2, enemy.ex+2, enemy.ey+2, 
                            fill = 'red', outline = 'red')

def drawBullets(app, canvas):
    for bullet in app.bullets:
        canvas.create_oval(bullet.bx-1, bullet.by-1, bullet.bx+1, bullet.by+1, 
                            fill = 'black', outline = 'black')

def drawRockets(app, canvas):
    for rocket in app.rockets:
        canvas.create_oval(rocket.rx-1, rocket.ry-1, rocket.rx+1, rocket.ry+1, 
                            fill = 'green', outline = 'green')

def drawPlasmas(app, canvas):
    for plasma in app.plasma:
        canvas.create_oval(plasma.plasx-1, plasma.plasy-1, plasma.plasx+1, plasma.plasy+1, 
                            fill = 'blue', outline = 'blue')


def drawWeapon(app, canvas):
    canvas.create_image(app.currentWeapon.x, app.currentWeapon.y, image = ImageTk.PhotoImage(app.currentWeapon.sprite))
    canvas.create_line((app.width/2) - 7, app.height*(1/3) + 30, (app.width/2) + 7, app.height*(1/3) + 30, width = 2, fill = 'white')
    canvas.create_line((app.width/2), app.height*(1/3) + 30 - 7, (app.width/2), app.height*(1/3) + 30 + 7, width = 2, fill = 'white')

def drawSky(app, canvas):
    pics = []
    for i in range(4):
        sprite = app.sky1.crop(((800)*i, 0, 800+800*i, 1000))
        pics.append(sprite)
    
    if math.pi*(1/4) < app.pa < math.pi*(3/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[0]))
    elif math.pi*(3/4)< app.pa < math.pi*(5/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[1]))
    elif math.pi*(5/4) < app.pa < math.pi*(7/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[2]))
    else:
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[3]))
    
##########################################
# Controls Mode
##########################################

def controlMode_keyPressed(app, event):
    app.mode = 'gameMode'

def controlMode_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='black')
    canvas.create_text((app.width/2)-10, (app.height/2)-20, text = f'Score:{app.score}', font = 'Times 75 bold', fill = 'red')
    canvas.create_text((app.width/2)-10, (app.height/2)+40, text = f'Kills:{app.kills}', font = 'Times 75 bold', fill = 'red')
    canvas.create_text((app.width/2)-10, (app.height/2)+100, text = 'Press R to return to Home Screen', font = 'Times 35 bold', fill = 'red')

##########################################
# Maze Mode
##########################################

def mazeMode_redrawAll(app, canvas):
    drawMazeSky(app, canvas)
    canvas.create_image(app.width/2, app.height*(3/4), image = ImageTk.PhotoImage(app.scaleImage(app.mazeGreen, 1.2)))
    drawMazeWalls(app, canvas)
    drawMazePortol3D(app, canvas)
    drawMiniMaze3D(app, canvas)
    drawMazeBoard(app, canvas)
    Square(app, canvas)
    drawSpecialWeapon(app, canvas)
    drawMazePauseScreen(app, canvas)
    
def mazeMode_keyPressed(app, event):
    if not app.mazePause:
        if event.key == 'w':
            if isMazesLegal(app, app.mx+app.mdx, app.my+app.mdy):
                app.mx += app.mdx
                app.my += app.mdy
        
        if event.key == 's':
            if isMazesLegal(app, app.mx-app.mdx, app.my-app.mdy):
                app.mx -= app.mdx
                app.my -= app.mdy
        
        if event.key == 'd':
            pddx = math.cos(app.ma+(math.pi/2))*3
            pddy = math.sin(app.ma+(math.pi/2))*3
            if isMazesLegal(app, app.mx+pddx, app.my+pddy):
                app.mx += pddx
                app.my += pddy
            
        if event.key == 'a':
            pddx = math.cos(app.ma+(math.pi/2))*3
            pddy = math.sin(app.ma+(math.pi/2))*3
            if isMazesLegal(app, app.mx-pddx, app.my-pddy):
                app.mx -= pddx
                app.my -= pddy

        if event.key == 'Left':
            app.ma -= 0.1
            if app.ma < 0:
                app.ma = 2*math.pi
            
        if event.key == 'Right':
            app.ma += 0.1
            if app.ma > 2*math.pi:
                app.ma = 0
        
        app.mdx = math.cos(app.ma)*3
        app.mdy = math.sin(app.ma)*3

        dist = math.sqrt((app.portolx-app.mx)**2 + (app.portoly-app.my)**2)
        app.heat =int(((app.maxDistance-dist)/app.maxDistance)*100)

        if event.key == 'Escape':
            app.mazePause = True

def mazeMode_timerFired(app):
    if not app.mazePause:
        if app.heat <= 30:
            app.heatState = 'Cold'
            app.heatColor = 'blue'
        elif 30 < app.heat <= 60:
            app.heatState = 'Warm'
            app.heatColor = 'orange'
        elif 60 < app.heat <= 80:
            app.heatState = 'Hot'
            app.heatColor = 'darkRed'
        elif 80 < app.heat:
            app.heatState = 'V.Hot'
            app.heatColor = 'red'
        app.mazeTimer += 1

        if getMazeCell(app, app.mx, app.my) == getMazeCell(app, app.mazeMapX, app.mazeMapY):
            app.mazeV = True

        if getMazeCell(app, app.mx, app.my) == (1,1):
            newMaze(app)

def mazeMode_mousePressed(app, event):
    if app.mazePause:
        if ((app.width/2 - 100) <= event.x <= (app.width/2 + 100)) and (170 <= event.y <=230):
            app.mazePause = False
        elif (app.width/2 - 100) <= event.x <= (app.width/2 + 100) and (260 <= event.y <=320):
            app.mode = 'homeScreen'
            app.mazePause = False
            if app.newSpecial:
                app.newSpecial = False
            app.mazeV = False
            app.mazeNumber = 1
            app.mazeSize = 10
            L = [([2] * app.mazeSize) for row in range(app.mazeSize)]
            app.maze = mazeGenarator(app, L)
            app.mrows = len(app.maze)
            app.mcols = len(app.maze[0])
            row = app.mrows-2
            col = app.mcols-2
            x0,y0,x1,y1 = getMazeCellBounds(app,row,col)
            app.mx = (x0 + x1)/2
            app.my = (y0 + y1)/2
            app.ma = math.pi*(3/2)
            app.mdx = math.cos(app.ma)*3
            app.mdy = math.sin(app.ma)*3
            x2,y2,x3,y3 = getMazeCellBounds(app,1,1)
            app.portolx = (x2 + x3)/2
            app.portoly = (y2 + y3)/2
            app.mbsize = (app.height/4)/app.mrows
            app.maxDistance = math.sqrt((app.portolx-app.mx)**2 + (app.portoly-app.my)**2)
            app.heat = 0
            app.mazeTimer = 0
            app.heatState = 'Cold'
            app.heatColor = 'blue'
            app.mapSpots = spawnableSpots(app, app.maze)
            (row, col) = app.mapSpots[random.randint(0, len(app.mapSpots)-1)]
            x4,y4,x5,y5 = getMazeCellBounds(app,row,col)
            app.mazeMapX = (x5 + x4)/2
            app.mazeMapY = (y5 + y4)/2
    
# https://www.cs.cmu.edu/~112/index.html
def pointInMaze(app, x, y):
    return ((3 <= x <= (3 + (app.height/4))) and (((app.height*(3/4)) - 9) <= y <= (app.height - 9)))
# https://www.cs.cmu.edu/~112/index.html
def getMazeCell(app, x, y):
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.height/4
    gridHeight = app.height/4
    cellWidth  = gridWidth / app.mcols
    cellHeight = gridHeight / app.mrows
    row = int((y - (app.height*(3/4)) + 9) / cellHeight)
    col = int((x - 3) / cellWidth)
    return (row, col)
# https://www.cs.cmu.edu/~112/index.html
def getMazeCellBounds(app, row, col):
    gridWidth  = app.height/4
    gridHeight = app.height/4
    x0 = 3 + gridWidth * col / app.mcols
    x1 = 3 + gridWidth * (col+1) / app.mcols
    y0 = (app.height*(3/4)) + (gridHeight * row / app.mrows) - 9
    y1 = (app.height*(3/4)) + (gridHeight * (row+1) / app.mrows) - 9
    return (x0, y0, x1, y1)
# https://www.cs.cmu.edu/~112/index.html
def getMazeObjectPosition(app, row, col):
    gridWidth  = app.height/4
    gridHeight = app.height/4
    x0 = 3 + gridWidth * col / app.mcols
    x1 = 3 + gridWidth * (col+1) / app.mcols
    y0 = (app.height*(3/4)) + (gridHeight * row / app.mrows) - 9
    y1 = (app.height*(3/4)) + (gridHeight * (row+1) / app.mrows) - 9
    return (abs(x0-x1)/2, abs(y0-y1)/2)
# https://www.cs.cmu.edu/~112/index.html

def drawMazeMap(app, canvas):
    for row in range(app.mrows):
        for col in range(app.mcols):
            (x0, y0, x1, y1) = getMazeCellBounds(app, row, col)
            if app.maze[row][col]==0:
                fill = 'gray'
                out = 'gray'
            elif app.maze[row][col]==1:
                fill = 'black'
                out = 'black'
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline = out)
    canvas.create_text(app.width*(0.035), app.height*(23.55/32),text= 'Maze',
                       font = 'Time 14 bold',fill = 'yellow')

def drawMazeBoard(app, canvas):
    canvas.create_rectangle(5,(app.height*(3/4))-11, app.width-5, app.height-6, fill = 'gray', width = 10)
    drawMazeMap(app, canvas)
    drawMazePlayer(app, canvas)
    drawMazePortol(app, canvas)
    canvas.create_line(app.width*(1.18/3),app.height*(2.18/3),app.width*(1.18/3),
                       app.height, fill = 'black', width = 7)
    canvas.create_line(app.width*(2.05/3),app.height*(2.18/3),app.width*(2.05/3),
                       app.height, fill = 'black', width = 7)
    drawCompass(app, canvas)
    drawHotAndCold(app, canvas)
    drawMazeNumber(app, canvas)
    drawTime(app, canvas)

def Square(app, canvas):
    if not app.mazeV:
        x0,y0,x1,y1 = getMazeCellBounds(app, 1, 1)
        x2,y2,x3,y3 = getMazeCellBounds(app, app.mrows-2, app.mcols-2)
        canvas.create_rectangle(x0, y0, x3, y3, fill = 'black')

def drawMazeNumber(app, canvas):
    canvas.create_text(app.width*(0.14/3), app.height*(1/32),text= 'Maze',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(0.14/3), app.height*(2.8/32),text= f'{app.mazeNumber}',
                       font = 'Helvetica 40 bold',fill = 'red')

def drawTime(app, canvas):
    canvas.create_text(app.width*(2.82/3), app.height*(1/32),text= 'Time',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(2.82/3), app.height*(2.8/32),text= f'{app.mazeTimer//5}',
                       font = 'Helvetica 40 bold',fill = 'red') 

def drawHotAndCold(app, canvas):
    canvas.create_text(app.width*(1.32/3), app.height*(24.45/32),text= 'Temp:',
                       font = 'Helvetica 20 bold',fill = 'black')
    canvas.create_text(app.width*(1.6/3), app.height*(28/32), text=f'{app.heat}°C', font = 'Helvetica 85 bold', fill = app.heatColor)
    canvas.create_text(app.width*(2.5/3), app.height*(28/32),  text=f'{app.heatState}', font = 'Helvetica 85 bold', fill = app.heatColor)

def drawCompass(app, canvas):
    canvas.create_text(app.width*(0.765/3), app.height*(24.45/32),text= 'Compass:',
                       font = 'Helvetica 20 bold',fill = 'black')
    (cx, cy, r) = (app.width*(0.88/3), app.height*(2.64/3), 55)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="yellow")
    r *= 0.8
    eAngle = 0
    eX = cx + r * math.cos(eAngle)
    eY = cy - r * math.sin(eAngle)
    canvas.create_text(eX, eY, text="E", font="Arial 16 bold")
    wAngle = math.pi
    wX = cx + r * math.cos(wAngle)
    wY = cy - r * math.sin(wAngle)
    canvas.create_text(wX, wY, text="W", font="Arial 16 bold")
    nAngle = math.pi/2
    nX = cx + r * math.cos(nAngle)
    nY = cy - r * math.sin(nAngle)
    canvas.create_text(nX, nY, text="N", font="Arial 16 bold")
    sAngle = 3*math.pi/2
    sX = cx + r * math.cos(sAngle)
    sY = cy - r * math.sin(sAngle)
    canvas.create_text(sX, sY, text="S", font="Arial 16 bold")
    d = r*0.75
    comX = cx + d * math.cos(app.ma)
    comY = cy + d * math.sin(app.ma)
    canvas.create_line(comX, comY, cx, cy, fill = 'red', width = 2)
    g = d *0.8
    comX2 = cx - g * math.cos(app.ma)
    comY2 = cy - g * math.sin(app.ma)
    canvas.create_line(comX2, comY2, cx, cy, fill = 'black', width = 2)
    canvas.create_oval(cx-1, cy-1, cx+1, cy+1, fill = 'black', width = 2)

def drawSpecialWeapon(app, canvas):
    if app.newSpecial:
        canvas.create_text(app.width*(1/2), app.height*(1/32),text= 'Congradulations! You got the secret weapon! Go try it!',
                       font = 'Times 25 bold',fill = 'black')

def drawMazeWalls(app, canvas):
    ra = app.ma - app.fov/2*(math.pi/180)
    if ra < 0:
        ra += 2*math.pi
    if ra > 2*math.pi:
        ra -= 2*math.pi
    for r in range(int(app.nor)):
        if ra == 0 or ra == math.pi:
            rx = app.mx
            ry = app.my
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, ry, x1, y1) = (getMazeCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.my-ry)*aTan+app.mx
            yo = app.mbsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, y0, x1, ry) = (getMazeCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.my-ry)*aTan+app.mx
            yo = -app.mbsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            row, col = getMazeCell(app, rx, ry)
            if(app.maze[row][col]>0):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.mx, app.my) 
   
        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.mx
            cy = app.my
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, y0, cx, y1) = (getMazeCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.mx-cx)*nTan+app.my
            xo = -app.mbsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            x,y = getMazeCell(app, app.mx, app.my)
            (cx, y0, x1, y1) = (getMazeCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.mx-cx)*nTan+app.my
            xo = app.mbsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):# All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            row, col = getMazeCell(app, cx, cy)
            if(app.maze[row][col]>0):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1
    
        DV = findLength(app, cx, cy, app.mx, app.my) 

        if DV < DH:
            DT = DV
            wallType = 1
        else:
            DT = DH
            wallType = 2

        ca = app.ma - ra # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        if ca < 0:
            ca +=2*math.pi # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
        
        if ca == 2*math.pi: # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
            ca -=2*math.pi
        
        DT = DT * math.cos(ca) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        lineH = ((app.mrows*app.mcols)/(DT*(10+(7*app.mazeNumber)))) * ((app.height*(3/4))) # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage

        LineO = (app.height*(3/8)) - lineH/2 # All calculations here were insprided by https://www.youtube.com/watch?v=gYRrGTC7GtA&t=1s&ab_channel=3DSage
        
        if wallType == 1:
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO, 
                            r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            fill = rbgString(app, 0, 0, int(205 - 600*(DT/app.colorO))),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            fill = rbgString(app,int(208 - 300*(DT/app.colorO)), 
                                                int(208 - 300*(DT/app.colorO)), 0),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            r*(app.width/(app.nor)), LineO, 
                            fill = rbgString(app,0,int(205 - 600*(DT/app.colorO)),0),
                            width = app.lineW)
        elif wallType == 2:
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO, 
                            r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            fill = rbgString(app, 0, 0, int(175 - 600*(DT/app.colorO))),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (1/3)*lineH, 
                            r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH,
                            fill = rbgString(app,int(162 - 300*(DT/app.colorO)), 
                                                int(162 - 300*(DT/app.colorO)),0),
                            width = app.lineW)
            canvas.create_line(r*(app.width/(app.nor)), lineH+LineO - (2/3)*lineH, 
                            r*(app.width/(app.nor)), LineO, 
                            fill = rbgString(app,0,int(175 - 600*(DT/app.colorO)),0),
                            width = app.lineW)
        ra += (app.da/180)*math.pi
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi

# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
# https://github.com/OrWestSide/python/blob/master/maze.py
def surroundingCells(app,maze,rWall):
    sCells = 0
    if (maze[rWall[0]-1][rWall[1]] == 0):
        sCells += 1
    if (maze[rWall[0]+1][rWall[1]] == 0):
        sCells += 1
    if (maze[rWall[0]][rWall[1]-1] == 0):
        sCells +=1
    if (maze[rWall[0]][rWall[1]+1] == 0):
        sCells += 1
    return sCells

# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
# https://github.com/OrWestSide/python/blob/master/maze.py
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# Mainly the Randomized Prim’s Algorithm.
def mazeGenarator(app, maze):
    rows, cols = len(maze), len(maze[0])
    sRow = random.randint(1,rows-2)
    sCol = random.randint(1,cols-2)
    maze[sRow][sCol] = 0
    walls = [[sRow - 1, sCol],[sRow, sCol - 1],[sRow, sCol + 1],[sRow + 1, sCol]]
    for cell in walls:
        maze[cell[0]][cell[1]] = 1
    while walls != []:
        rWall = random.choice(walls)
        if (rWall[0] != 0):
            if (maze[rWall[0]-1][rWall[1]] == 2 and maze[rWall[0]+1][rWall[1]] == 0):
                sCells = surroundingCells(app,maze,rWall)
                if (sCells < 2):
                    maze[rWall[0]][rWall[1]] = 0
                    if (rWall[0] != 0):
                        if (maze[rWall[0]-1][rWall[1]] != 0):
                            maze[rWall[0]-1][rWall[1]] = 1
                        if ([rWall[0]-1, rWall[1]] not in walls):
                            walls.append([rWall[0]-1, rWall[1]])
                    if (rWall[1] != 0):
                        if (maze[rWall[0]][rWall[1]-1] != 0):
                            maze[rWall[0]][rWall[1]-1] = 1
                        if ([rWall[0], rWall[1]-1] not in walls):
                            walls.append([rWall[0], rWall[1]-1])
                    if (rWall[1] != cols-1):
                        if (maze[rWall[0]][rWall[1]+1] != 0):
                            maze[rWall[0]][rWall[1]+1] = 1
                        if ([rWall[0], rWall[1]+1] not in walls):
                            walls.append([rWall[0], rWall[1]+1])
                for wall in walls:
                    if (wall[0] == rWall[0] and wall[1] == rWall[1]):
                        walls.remove(wall)
        if (rWall[1] != 0):
            if (maze[rWall[0]][rWall[1]-1] == 2 and maze[rWall[0]][rWall[1]+1] == 0):
                sCells = surroundingCells(app,maze,rWall)
                if (sCells < 2):
                    maze[rWall[0]][rWall[1]] = 0
                    if (rWall[0] != 0):
                        if (maze[rWall[0]-1][rWall[1]] != 0):
                            maze[rWall[0]-1][rWall[1]] = 1
                        if ([rWall[0]-1, rWall[1]] not in walls):
                            walls.append([rWall[0]-1, rWall[1]])
                    if (rWall[0] != rows-1):
                        if (maze[rWall[0]+1][rWall[1]] != 0):
                            maze[rWall[0]+1][rWall[1]] = 1
                        if ([rWall[0]+1, rWall[1]] not in walls):
                            walls.append([rWall[0]+1, rWall[1]])
                    if (rWall[1] != 0):	
                        if (maze[rWall[0]][rWall[1]-1] != 0):
                            maze[rWall[0]][rWall[1]-1] = 1
                        if ([rWall[0], rWall[1]-1] not in walls):
                            walls.append([rWall[0], rWall[1]-1])
                for wall in walls:
                    if (wall[0] == rWall[0] and wall[1] == rWall[1]):
                        walls.remove(wall)
        if (rWall[1] != cols-1):
            if (maze[rWall[0]][rWall[1]+1] == 2 and maze[rWall[0]][rWall[1]-1] == 0):
                sCells = surroundingCells(app,maze,rWall)
                if (sCells < 2):
                    maze[rWall[0]][rWall[1]] = 0
                    if (rWall[1] != cols-1):
                        if (maze[rWall[0]][rWall[1]+1] != 0):
                            maze[rWall[0]][rWall[1]+1] = 1
                        if ([rWall[0], rWall[1]+1] not in walls):
                            walls.append([rWall[0], rWall[1]+1])
                    if (rWall[0] != rows-1):
                        if (maze[rWall[0]+1][rWall[1]] != 0):
                            maze[rWall[0]+1][rWall[1]] = 1
                        if ([rWall[0]+1, rWall[1]] not in walls):
                            walls.append([rWall[0]+1, rWall[1]])
                    if (rWall[0] != 0):	
                        if (maze[rWall[0]-1][rWall[1]] != 0):
                            maze[rWall[0]-1][rWall[1]] = 1
                        if ([rWall[0]-1, rWall[1]] not in walls):
                            walls.append([rWall[0]-1, rWall[1]])
                for wall in walls:
                    if (wall[0] == rWall[0] and wall[1] == rWall[1]):
                        walls.remove(wall)
        if (rWall[0] != rows-1):
            if (maze[rWall[0]+1][rWall[1]] == 2 and maze[rWall[0]-1][rWall[1]] == 0):
                sCells = surroundingCells(app,maze,rWall)
                if (sCells < 2):
                    maze[rWall[0]][rWall[1]] = 0
                    if (rWall[0] != rows-1):
                        if (maze[rWall[0]+1][rWall[1]] != 0):
                            maze[rWall[0]+1][rWall[1]] = 1
                        if ([rWall[0]+1, rWall[1]] not in walls):
                            walls.append([rWall[0]+1, rWall[1]])
                    if (rWall[1] != 0):
                        if (maze[rWall[0]][rWall[1]-1] != 0):
                            maze[rWall[0]][rWall[1]-1] = 1
                        if ([rWall[0], rWall[1]-1] not in walls):
                            walls.append([rWall[0], rWall[1]-1])
                    if (rWall[1] != cols-1):
                        if (maze[rWall[0]][rWall[1]+1] != 0):
                            maze[rWall[0]][rWall[1]+1] = 1
                        if ([rWall[0], rWall[1]+1] not in walls):
                            walls.append([rWall[0], rWall[1]+1])
                for wall in walls:
                    if (wall[0] == rWall[0] and wall[1] == rWall[1]):
                        walls.remove(wall)
        for wall in walls:
            if (wall[0] == rWall[0] and wall[1] == rWall[1]):
                walls.remove(wall)
    for row in range(rows):
        for col in range(cols):
            if (maze[row][col] == 2):
                maze[row][col] = 1
    maze[1][1] = 0
    maze[len(maze)-2][len(maze[0])-2] = 0
    if maze[1][2] == 1 and maze[2][1] == 1:
        maze[1][2] = 0
    if maze[len(maze)-2][len(maze[0])-3] == 1 and maze[len(maze)-3][len(maze[0])-2] == 1:
        maze[len(maze)-2][len(maze[0])-3] = 0
    return maze

def drawMazePortol3D(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    x0,y0,x1,y1 = getMazeCellBounds(app, 1, 1)
    px = (x0 + x1)/2
    py = (y0 + y1)/2 
    dx, dy = px - app.mx, py - app.my
    ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
    if dx == 0:
        dx += 0.0001
    if dy == 0:
        dy += 0.0001

    theta = math.atan(dy/dx)
    gamma = theta - app.ma         
        
    if dx < 0:
        gamma += math.pi

    elif dy < 0 and dx < 0:
        gamma += 2*math.pi
    
    elif (dx > 0 and math.pi <= app.ma <= 2*math.pi) or dx < 0 and dy < 0:
        gamma += 2*math.pi
        
    ra = app.ma + gamma
    if ra < 0:
        ra += 2*math.pi
    if ra > 2*math.pi:
        ra -= 2*math.pi
    
    if ra == 0 or ra == math.pi:
        rx = app.mx
        ry = app.my
        dof = app.dof
    
    elif ra < math.pi:
        aTan = -1/math.tan(ra)
        x,y = getMazeCell(app, app.mx, app.my)
        (x0, ry, x1, y1) = (getMazeCellBounds(app, x+1, y))
        ry += 0.01
        rx = (app.my-ry)*aTan+app.mx
        yo = app.mbsize
        xo = -yo*aTan

    elif ra > math.pi:
        aTan = -1/math.tan(ra)
        x,y = getMazeCell(app, app.mx, app.my)
        (x0, y0, x1, ry) = (getMazeCellBounds(app, x-1, y))
        ry -= 0.01
        rx = (app.my-ry)*aTan+app.mx
        yo = -app.mbsize
        xo = -yo*aTan

    dof = 0
    while(dof < app.dof):
        row, col = getMazeCell(app, rx, ry)
        if(app.maze[row][col]==1):
            dof=app.dof
        else:
            rx += xo
            ry += yo
            dof += 1
            
    DH = findLength(app, rx, ry, app.mx, app.my) 

    if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
        cx = app.mx
        cy = app.my
        dof = app.dof
    
    elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
        nTan = -math.tan(ra)
        x,y = getMazeCell(app, app.mx, app.my)
        (x0, y0, cx, y1) = (getMazeCellBounds(app, x, y-1))
        cx -= 0.1
        cy = (app.mx-cx)*nTan+app.my
        xo = -app.mbsize
        yo = -xo*nTan

    elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
        nTan = -math.tan(ra)
        x,y = getMazeCell(app, app.mx, app.my)
        (cx, y0, x1, y1) = (getMazeCellBounds(app, x, y+1))
        cx += 0.1
        cy = (app.mx-cx)*nTan+app.my
        xo = app.mbsize
        yo = -xo*nTan

    dof = 0
    while(dof < app.dof):
        row, col = getMazeCell(app, cx, cy)
        if(app.maze[row][col]==1):
            dof=app.dof
        else:
            cx += xo
            cy += yo
            dof += 1

    DV = findLength(app, cx, cy, app.mx, app.my) 

    if DV < DH:
        DT = DV
    else:
        DT = DH
            
    if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
        and (ds < DT)):
        sx = (app.width/2) + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
        sy = app.height*(1/3) + 30 
        canvas.create_image(sx, sy, image = ImageTk.PhotoImage(app.scaleImage(app.portol, 9/ds)))

def drawMiniMaze3D(app, canvas):# All calculations here were insprided by https://www.youtube.com/watch?v=MgTHkqMjVa4&t=1s&ab_channel=StandaloneCoder
    if not app.mazeV:
        (row, col) = getMazeCell(app, app.mazeMapX, app.mazeMapY)
        x0,y0,x1,y1 = getMazeCellBounds(app, row, col)
        px = (x0 + x1)/2
        py = (y0 + y1)/2 
        dx, dy = px - app.mx, py - app.my
        ds = math.sqrt(dx ** 2 + dy ** 2) + 0.0001
        if dx == 0:
            dx += 0.0001
        if dy == 0:
            dy += 0.0001

        theta = math.atan(dy/dx)
        gamma = theta - app.ma         
            
        if dx < 0:
            gamma += math.pi

        elif dy < 0 and dx < 0:
            gamma += 2*math.pi
        
        elif (dx > 0 and math.pi <= app.ma <= 2*math.pi) or dx < 0 and dy < 0:
            gamma += 2*math.pi
            
        ra = app.ma + gamma
        if ra < 0:
            ra += 2*math.pi
        if ra > 2*math.pi:
            ra -= 2*math.pi
        
        if ra == 0 or ra == math.pi:
            rx = app.mx
            ry = app.my
            dof = app.dof
        
        elif ra < math.pi:
            aTan = -1/math.tan(ra)
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, ry, x1, y1) = (getMazeCellBounds(app, x+1, y))
            ry += 0.01
            rx = (app.my-ry)*aTan+app.mx
            yo = app.mbsize
            xo = -yo*aTan

        elif ra > math.pi:
            aTan = -1/math.tan(ra)
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, y0, x1, ry) = (getMazeCellBounds(app, x-1, y))
            ry -= 0.01
            rx = (app.my-ry)*aTan+app.mx
            yo = -app.mbsize
            xo = -yo*aTan

        dof = 0
        while(dof < app.dof):
            row, col = getMazeCell(app, rx, ry)
            if(app.maze[row][col]==1):
                dof=app.dof
            else:
                rx += xo
                ry += yo
                dof += 1
                
        DH = findLength(app, rx, ry, app.mx, app.my) 

        if (ra == math.pi*(1/2)) or (ra == math.pi*(3/2)):
            cx = app.mx
            cy = app.my
            dof = app.dof
        
        elif ra > math.pi*(1/2) and ra < math.pi*(3/2):#going left
            nTan = -math.tan(ra)
            x,y = getMazeCell(app, app.mx, app.my)
            (x0, y0, cx, y1) = (getMazeCellBounds(app, x, y-1))
            cx -= 0.1
            cy = (app.mx-cx)*nTan+app.my
            xo = -app.mbsize
            yo = -xo*nTan

        elif ra < math.pi*(1/2) or ra > math.pi*(3/2):#going right
            nTan = -math.tan(ra)
            x,y = getMazeCell(app, app.mx, app.my)
            (cx, y0, x1, y1) = (getMazeCellBounds(app, x, y+1))
            cx += 0.1
            cy = (app.mx-cx)*nTan+app.my
            xo = app.mbsize
            yo = -xo*nTan

        dof = 0
        while(dof < app.dof):
            row, col = getMazeCell(app, cx, cy)
            if(app.maze[row][col]==1):
                dof=app.dof
            else:
                cx += xo
                cy += yo
                dof += 1

        DV = findLength(app, cx, cy, app.mx, app.my) 

        if DV < DH:
            DT = DV
        else:
            DT = DH
                
        if ((-app.fov/2*(math.pi/180) <= gamma <= app.fov/2*(math.pi/180))
            and (ds < DT)):
            sx = (app.width/2) + (gamma/(app.fov/2*(math.pi/180)))*(app.width/2)
            sy = app.height*(1/3) + 30 
            canvas.create_image(sx, sy, image = ImageTk.PhotoImage(app.scaleImage(app.mazeMiniMap, 7.5/ds)))

def newMaze(app):
    if app.newSpecial:
        app.newSpecial = False
    app.mazeV = False
    app.mazeNumber += 1
    app.mazeSize += 1
    L = [([2] * app.mazeSize) for row in range(app.mazeSize)]
    app.maze = mazeGenarator(app, L)
    app.mrows = len(app.maze)
    app.mcols = len(app.maze[0])
    row = app.mrows-2
    col = app.mcols-2
    x0,y0,x1,y1 = getMazeCellBounds(app,row,col)
    app.mx = (x0 + x1)/2
    app.my = (y0 + y1)/2
    app.ma = math.pi*(3/2)
    app.mdx = math.cos(app.ma)*3
    app.mdy = math.sin(app.ma)*3
    x2,y2,x3,y3 = getMazeCellBounds(app,1,1)
    app.portolx = (x2 + x3)/2
    app.portoly = (y2 + y3)/2
    app.mbsize = (app.height/4)/app.mrows
    app.maxDistance = math.sqrt((app.portolx-app.mx)**2 + (app.portoly-app.my)**2)
    app.heat = 0
    app.mazeTimer = 0
    app.heatState = 'Cold'
    app.heatColor = 'blue'
    app.mapSpots = spawnableSpots(app, app.maze)
    (row, col) = app.mapSpots[random.randint(0, len(app.mapSpots)-1)]
    x4,y4,x5,y5 = getMazeCellBounds(app,row,col)
    app.mazeMapX = (x5 + x4)/2
    app.mazeMapY = (y5 + y4)/2
    if app.mazeNumber == 11:
        if app.specialWeapon[0] not in app.myWeapons:
            app.myWeapons.append(app.specialWeapon[0])
            app.newSpecial = True

def rbgString(app, r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}' # to get colors

def findLength(app, x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y0-y1)**2)

def isMazesLegal(app, x, y):
    row, col = getMazeCell(app, x, y)
    if app.maze[row][col] == 1:
        return False
    return True

def drawMazePlayer(app, canvas):
    canvas.create_oval(app.mx-2, app.my-2, app.mx+2, app.my+2, 
                        fill = 'yellow', outline = 'yellow')
    canvas.create_line(app.mx, app.my, app.mx+app.mdx*2, app.my+app.mdy*2, 
                       fill = 'yellow')

def drawMazePauseScreen(app, canvas):
    if app.mazePause:
        canvas.create_rectangle(200, 50, app.width - 200, (app.height*(3/4))-11-50, fill = 'black')
        canvas.create_rectangle(210, 60, app.width - 210, (app.height*(3/4))-11-60, fill = 'grey')
        canvas.create_text(app.width/2, 100,text= 'Paused',font = 'Times 70 bold',fill = 'black')
        canvas.create_rectangle(app.width/2 + 100, 170, app.width/2 - 100, 230, width = 4) # Resume
        canvas.create_rectangle(app.width/2 + 100, 260, app.width/2 - 100, 320, width = 4) # Quit
        canvas.create_text(app.width/2, 200, text = 'Resume', font = 'Times 35 bold',fill = 'black')
        canvas.create_text(app.width/2, 290, text = 'Quit', font = 'Times 35 bold',fill = 'black')

def drawMazeSky(app, canvas):
    pics = []
    for i in range(4):
        sprite = app.sky2.crop(((800)*i, 0, 800+800*i, 1000))
        pics.append(sprite)
    if math.pi*(1/4) < app.ma < math.pi*(3/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[0]))
    elif math.pi*(3/4)< app.ma < math.pi*(5/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[1]))
    elif math.pi*(5/4) < app.ma < math.pi*(7/4):
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[2]))
    else:
        canvas.create_image(app.width/2, app.height/4, image = ImageTk.PhotoImage(pics[3]))

def drawMazePortol(app, canvas):
    canvas.create_oval(app.portolx-2, app.portoly-2, app.portolx+2, app.portoly+2, 
                        fill = 'green', outline = 'green')

##########################################
# Game Over Mode
##########################################

def GameOver_mousePressed(app, event):
    if (app.width*(1.2/4)-100 <= event.x <= app.width*(1.2/4)+100) and (app.height*(28/32)-30 <= event.y <= app.height*(28/32)+30):
        app.wave = 1
        app.px = 3 + (app.rows/2)*app.bsize
        app.py = ((3/4)*app.height) - 9 + (app.cols-1.5)*app.bsize
        app.hp = 100
        app.pa = (3/2)*math.pi
        app.pdx = math.cos(app.pa)*3
        app.pdy = math.sin(app.pa)*3
        Devils = [] 
        for i in range(1):
            Devils.append(Enemy(0, 0, 0, 2, 20, 20, app.loadImage('Devil.png'), False, 3, False))
        Shooters = [] 
        for i in range(1):
            Shooters.append(Enemy(0, 0, 0, 5, 15, 15, app.loadImage('Solider.png'), True, 18, False))
        app.enemies = Devils + Shooters
        app.spots = spawnableSpots(app, app.map)
        for enemy in app.enemies:
            (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
            x0,y0,x1,y1 = getGameCellBounds(app,row,col)
            enemy.ex = (x0 + x1)/2 + 0.1
            enemy.ey = (y0 + y1)/2
        app.timer = 0
        app.bullets = []
        app.rockets = []
        app.plasma = []
        pistol = Weapon((app.width/2 + 160), app.height/2 + 50, 2, 10, 50, app.scaleImage(app.loadImage('Gun.png'), 0.4), False, app.scaleImage(app.loadImage('pistolImage.png'), 1), False)
        plasmaRay = Weapon(app.width/2, app.height/2 + 75 , 50, 1, 5, app.scaleImage(app.loadImage('plasmaRay.png'), 3), False, app.scaleImage(app.loadImage('plazmaRayImage.png'), 0.8), True) 
        if app.specialWeapon[0] in app.myWeapons:
            app.myWeapons = [pistol, plasmaRay]
        else:
            app.myWeapons = [pistol]
        app.select = 0
        app.currentWeapon = app.myWeapons[app.select]
        app.score = 0
        app.kills = 0
        app.newShotGun = False
        app.newLauncher = False
        app.gamePause = False
        app.mode = 'gameMode'
    
    elif (app.width*(2.8/4)-100 <= event.x <= app.width*(2.8/4)+100) and (app.height*(28/32)-30 <= event.y <= app.height*(28/32)+30):
        app.mode = 'homeScreen'
        app.wave = 1
        app.px = 3 + (app.rows/2)*app.bsize
        app.py = ((3/4)*app.height) - 9 + (app.cols-1.5)*app.bsize
        app.hp = 100
        app.pa = (3/2)*math.pi
        app.pdx = math.cos(app.pa)*3
        app.pdy = math.sin(app.pa)*3
        Devils = [] 
        for i in range(1):
            Devils.append(Enemy(0, 0, 0, 2, 20, 20, app.loadImage('Devil.png'), False, 3, False))
        Shooters = [] 
        for i in range(1):
            Shooters.append(Enemy(0, 0, 0, 5, 15, 15, app.loadImage('Solider.png'), True, 18, False))
        app.enemies = Devils + Shooters
        app.spots = spawnableSpots(app, app.map)
        for enemy in app.enemies:
            (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
            x0,y0,x1,y1 = getGameCellBounds(app,row,col)
            enemy.ex = (x0 + x1)/2 + 0.1
            enemy.ey = (y0 + y1)/2
        app.timer = 0
        app.bullets = []
        app.rockets = []
        app.plasma = []
        pistol = Weapon((app.width/2 + 160), app.height/2 + 50, 2, 10, 50, app.scaleImage(app.loadImage('Gun.png'), 0.4), False, app.scaleImage(app.loadImage('pistolImage.png'), 1), False)
        plasmaRay = Weapon(app.width/2, app.height/2 + 75 , 50, 1, 5, app.scaleImage(app.loadImage('plasmaRay.png'), 3), False, app.scaleImage(app.loadImage('plazmaRayImage.png'), 0.8), True) 
        if app.specialWeapon[0] in app.myWeapons:
            app.myWeapons = [pistol, plasmaRay]
        else:
            app.myWeapons = [pistol]
        app.select = 0
        app.currentWeapon = app.myWeapons[app.select]
        app.score = 0
        app.kills = 0
        app.newShotGun = False
        app.newLauncher = False
        app.gamePause = False
    else:
        return None

def GameOver_redrawAll(app, canvas):
    if app.name == '':
        canvas.create_rectangle(0,0,app.width,app.height, fill='black')
        canvas.create_text(app.width/2, (app.height/2)-180, text = f'You Died.', font = 'Times 95 bold', fill = 'red')
        canvas.create_text((app.width/2)-10, (app.height/2)-35, text = f'Score : {app.score}', font = 'Times 55 bold', fill = 'red')
        canvas.create_text((app.width/2)-10, (app.height/2)+70, text = f'Kills : {app.kills}', font = 'Times 55 bold', fill = 'red')
       
    else:
        canvas.create_rectangle(0,0,app.width,app.height, fill='black')
        canvas.create_text(app.width*(1/2), 50, text = f'Leader Board', font = 'Times 60 bold', fill = 'red')
        canvas.create_line(app.width*(1/2)-180,75,app.width*(1/2)+180,75, fill = 'red', width =3)
        canvas.create_text(app.width*(1/4), 120, text = f'Name', font = 'Times 50', fill = 'red')
        canvas.create_text(app.width*(1/2), 120, text = f'Score', font = 'Times 50', fill = 'red')
        canvas.create_text(app.width*(3/4), 120, text = f'Kills', font = 'Times 50', fill = 'red')
        canvas.create_text(app.width*(1.25/16), 180, text = f'1.', font = 'Times 40', fill = 'red')
        canvas.create_text(app.width*(1.25/16), 240, text = f'2.', font = 'Times 40', fill = 'red')
        canvas.create_text(app.width*(1.25/16), 300, text = f'3.', font = 'Times 40', fill = 'red')
        canvas.create_text(app.width*(1.25/16), 360, text = f'4.', font = 'Times 40', fill = 'red')
        canvas.create_text(app.width*(1.25/16), 420, text = f'5.', font = 'Times 40', fill = 'red')
    
        if len(app.leaderboard) >= 1:
            canvas.create_text(app.width*(1/4), 180, text = f'{app.leaderboard[0][0].upper()}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 180, text = f'{app.leaderboard[0][1]}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 180, text = f'{app.leaderboard[0][2]}', font = 'Times 40', fill = 'white')
        else:
            canvas.create_text(app.width*(1/4), 180, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 180, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 180, text = f'--', font = 'Times 40', fill = 'white')
    
        if len(app.leaderboard) >= 2:
            canvas.create_text(app.width*(1/4), 240, text = f'{app.leaderboard[1][0].upper()}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 240, text = f'{app.leaderboard[1][1]}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 240, text = f'{app.leaderboard[1][2]}', font = 'Times 40', fill = 'white')
        else:
            canvas.create_text(app.width*(1/4), 240, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 240, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 240, text = f'--', font = 'Times 40', fill = 'white')

        if len(app.leaderboard) >= 3:
            canvas.create_text(app.width*(1/4), 300, text = f'{app.leaderboard[2][0].upper()}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 300, text = f'{app.leaderboard[2][1]}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 300, text = f'{app.leaderboard[2][2]}', font = 'Times 40', fill = 'white')
        else:
            canvas.create_text(app.width*(1/4), 300, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 300, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 300, text = f'--', font = 'Times 40', fill = 'white')

        if len(app.leaderboard) >= 4:
            canvas.create_text(app.width*(1/4), 360, text = f'{app.leaderboard[3][0].upper()}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 360, text = f'{app.leaderboard[3][1]}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 360, text = f'{app.leaderboard[3][2]}', font = 'Times 40', fill = 'white')
        else:
            canvas.create_text(app.width*(1/4), 360, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 360, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 360, text = f'--', font = 'Times 40', fill = 'white')

        if len(app.leaderboard) >= 5:
            canvas.create_text(app.width*(1/4), 420, text = f'{app.leaderboard[4][0].upper()}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 420, text = f'{app.leaderboard[4][1]}', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 420, text = f'{app.leaderboard[4][2]}', font = 'Times 40', fill = 'white')
        else:
            canvas.create_text(app.width*(1/4), 420, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(1/2), 420, text = f'--', font = 'Times 40', fill = 'white')
            canvas.create_text(app.width*(3/4), 420, text = f'--', font = 'Times 40', fill = 'white')
    canvas.create_rectangle(app.width*(1.2/4)+100, app.height*(28/32)+30, app.width*(1.2/4)-100, app.height*(28/32)-30, fill = 'black', outline = 'red', width = 4)#retry
    canvas.create_text(app.width*(1.2/4), app.height*(28/32), text = 'Retry', fill = 'red', font = 'Times 40 bold')
    canvas.create_rectangle(app.width*(2.8/4)+100, app.height*(28/32)+30, app.width*(2.8/4)-100, app.height*(28/32)-30, fill = 'black', outline = 'red', width = 4)#quit
    canvas.create_text(app.width*(2.8/4), app.height*(28/32), text = 'Quit', fill = 'red', font = 'Times 40 bold')

##########################################
# Main App
##########################################

def appStarted(app):
    '''
    Main Game
    '''
    app.mode = 'homeScreen'
    app.wave = 1
    app.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,0,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,0,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1]]
    for i in range(8):
        row = random.randint(3, len(app.map)-4)
        col = random.randint(2, len(app.map)-3)
        app.map[row][col] = 1
    app.rows = len(app.map)
    app.cols = len(app.map[0])
    app.bsize = (app.height/4)/app.rows
    app.px = 3 + (app.rows/2)*app.bsize
    app.py = ((3/4)*app.height) - 9 + (app.cols-1.5)*app.bsize
    app.hp = 100
    app.pa = (3/2)*math.pi
    app.pdx = math.cos(app.pa)*3
    app.pdy = math.sin(app.pa)*3
    app.fov = 60
    app.nor = 150
    app.da = (app.fov/app.nor)
    Devils = []
    for i in range(1):
        Devils.append(Enemy(0, 0, 0, 2, 20, 20, app.loadImage('Devil.png'), False, 3, False))#image is from DOOM
    Shooters = [] 
    for i in range(1):
        Shooters.append(Enemy(0, 0, 0, 5, 15, 15, app.loadImage('Solider.png'), True, 18, False))#image is from DOOM
    app.enemies = Devils + Shooters
    app.spots = spawnableSpots(app, app.map)
    for enemy in app.enemies:
        (row, col) = app.spots[random.randint(0, len(app.spots)-1)]
        x0,y0,x1,y1 = getGameCellBounds(app,row,col)
        enemy.ex = (x0 + x1)/2 + 0.1
        enemy.ey = (y0 + y1)/2
    app.colorO = (app.height*(3/4)) - 2*app.bsize
    app.lineW = (app.width/app.nor)*1.5
    app.dof = 100
    app.sky1 = app.scaleImage(app.loadImage('Sky2.png'), 2)
    app.portol = app.scaleImage(app.loadImage('portol.png'), 2)#https://www.freepngimg.com/png/88216-blue-animation-portal-sprite-point-free-png-hq/icon
    app.timer = 0
    app.bullets = []
    app.rockets = []
    app.plasma = []
    app.shot = app.loadImage('2.png')#images are from DOOM
    app.rock = app.loadImage('rocket.png')#images are from DOOM
    app.plasmaShot = app.loadImage('plasma.png')#https://www.freepngimg.com/png/88216-blue-animation-portal-sprite-point-free-png-hq/icon
    app.title = app.loadImage('Title2.png')#images are from DOOM
    pistol = Weapon((app.width/2 + 160), app.height/2 + 50, 2, 10, 50, app.scaleImage(app.loadImage('Gun.png'), 0.4), False, app.scaleImage(app.loadImage('pistolImage.png'), 1), False)#images are from DOOM
    shotGun = Weapon((app.width/2), app.height/2 + 75 , 10, 5, 15, app.scaleImage(app.loadImage('shotGun.png'), 0.5), False, app.scaleImage(app.loadImage('shotGunImage.png'), 1), False)#images are from DOOM
    rpg = Weapon((app.width/2 + 160), app.height/2 + 75 , 20, 1, 5, app.scaleImage(app.loadImage('rpg.png'), 3), True, app.scaleImage(app.loadImage('rpgImage.png'), 1), False)#images are from DOOM
    plasmaRay = Weapon(app.width/2, app.height/2 + 75 , 50, 1, 5, app.scaleImage(app.loadImage('plasmaRay.png'), 3), False, app.scaleImage(app.loadImage('plazmaRayImage.png'), 0.8), True)#images are from DOOM
    app.specialWeapon = [plasmaRay]
    app.allWeapons = [pistol, shotGun, rpg]
    app.myWeapons = [pistol, shotGun, rpg] +  app.specialWeapon
    app.select = 0
    app.currentWeapon = app.myWeapons[app.select]
    app.score = 0
    app.kills = 0
    app.newShotGun = False
    app.newLauncher = False
    app.gamePause = False
    app.green = app.loadImage('Green.png')#made by me
    app.leaderboard = []
    #https://www.cs.cmu.edu/~112notes/notes-strings.html
    file = open('leaderboard.txt', 'r')
    line = file.readline()
    while line:
        entry = line.split(',')
        entry[2] = entry[2].strip('\n')
        app.leaderboard.append(entry)
        line = file.readline()
    app.name = ''
    app.wasd = app.loadImage('wasd.png')#http://clipart-library.com/clipart/1670524.htm
    app.arrows = app.loadImage('arrows.png')#http://clipart-library.com/arrow-key-cliparts.html
    app.sp = app.loadImage('spaceBar.png')#https://www.pngfind.com/mpng/iwbbomx_spacebar-parallel-hd-png-download/
    app.mouse = app.loadImage('mouse.png')#https://pngimg.com/image/7674
    app.escape = app.loadImage('esc.png')#https://www.techonthenet.com/clipart/keyboard/esc_key.php
    '''
    Maze Mode
    '''
    app.mazeV = False
    app.mazeSize = 10
    L = [([2] * app.mazeSize) for row in range(app.mazeSize)]
    app.maze = mazeGenarator(app, L)
    app.mrows = len(app.maze)
    app.mcols = len(app.maze[0])
    app.mbsize = (app.height/4)/app.mrows
    app.portolx = 3 + 1.5*app.mbsize
    app.portoly = ((3/4)*app.height) - 9 + 1.5*app.mbsize
    app.ma = math.pi*(3/2)
    app.mdx = math.cos(app.ma)*3
    app.mdy = math.sin(app.ma)*3
    app.sky2 = app.scaleImage(app.loadImage('sky5.png'), 3)#https://www.metoffice.gov.uk/weather/learn-about/weather/optical-effects/why-is-the-sky-blue
    app.mx = 3 + (app.mrows-1.5)*app.mbsize
    app.my = ((3/4)*app.height) - 9 + (app.mcols-1.5)*app.mbsize
    app.maxDistance = math.sqrt((app.portolx-app.mx)**2 + (app.portoly-app.my)**2)
    app.heat = 0
    app.heatState = 'Cold'
    app.heatColor = 'blue'
    app.mazeNumber = 1
    app.mazeTimer = 0
    app.prize = app.scaleImage(app.loadImage('plazmaRayImage.png'), 1.5)#image is from DOOM
    app.mazeMiniMap = app.scaleImage(app.loadImage('Map3.png'), 0.4)#https://imgbin.com/png/eNQpx0tX/pixel-art-scroll-png
    app.mapSpots = spawnableSpots(app, app.maze)
    (row, col) = app.mapSpots[random.randint(0, len(app.mapSpots)-1)]
    x0,y0,x1,y1 = getMazeCellBounds(app,row,col)
    app.mazeMapX = (x0 + x1)/2
    app.mazeMapY = (y0 + y1)/2
    app.newSpecial = False
    app.mazePause = False
    app.mazeGreen = app.loadImage('mazeGreen.png')#made by me

def main():
    runApp(width=800, height=600)

if __name__ == '__main__':
    main()

from Score import Score
player = Score('Greg')
#Testing constructor
if player.get_level() == 0:
    print ('get_level passed\n')
if player.get_score() == 0:
    print ('get_score passed\n')
if player.get_lives() == 3:
    print ('get_lives passed\n')
if player.get_multiplier() == 1:
    print ('get_multiplier passed\n')
print(player)
player.add_points(20000)
#Testing method add points
if player.get_level() == 2 and player.get_score() == 20000:
    print('This works')
player.add_points(1000)    
if player.get_level() == 2 and player.get_score() == 21000:
    print('Yay')
#Testing method increment multiplier
player.increment_multiplier()
player.add_points(1000)
if player.get_score() == 23000 and player.get_multiplier() == 2 and player.get_level() == 2:
    print ('We doubled the score increment')
player.add_points(9000)
if player.get_score() == 41000 and player.get_multiplier() == 2 and player.get_level() == 3:
    print('Multiplier works while level increases')
print(player)
#Testing method subtract points
player.subtract_points(1000)
if player.get_score() == 40000 and player.get_multiplier() == 1 and player.get_level() == 3:
    print('We can subtract')
player.subtract_points(25000)
if player.get_score() == 15000 and player.get_multiplier() == 1 and player.get_level() == 1:
    print('We can subtract and change levels')
player.subtract_points(15000)
if player.get_score() == 0 and player.get_multiplier() == 1 and player.get_level() == 0:
    print('Done with subtraction tests')
print(player)
#Testing method gain life
player = Score('Greg')
for i in range(3,11):
    if player.get_lives() != i:
        print('fail')
        break
    player.gain_life()
else:
    print('gain life passed')
for i in range(11,2,-1):
    if player.get_lives() != i:
        print('fail')
        break
    player.lose_life()
else:
    print('lose life passed')
if player.lose_life() == False:
    print('fail')
print(player.get_lives())
if player.lose_life() == False:
    print('passed')
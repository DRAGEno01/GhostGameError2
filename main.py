from random import randint, random
print('Ghost Game')
feeling_brave = True
score = 0
ghost_door = 2
while feeling_brave:
    
    print('Three doors ahead...')
    print('A ghost is behing one...')
    print('Which door do you open?')
    door_num = int(input('Out of these options\(1,2,3),which is your favourite?'))
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
        switch(door_num){
            case 1:
                return ""
                break;
            case 2:
                return ""
                break;
            case 3:
                return ""
                break;

            default:
                return "Invalid number has been inputed"
}

    else:
        print('There was not a ghost.')
        print('You enter the next room...')
        score = score+1
        print('Make sure you are only typing numbers 1 to 3, or the game is unfair.')
print('RUN AWAY!')
print('Game Over! You scored: ', score)
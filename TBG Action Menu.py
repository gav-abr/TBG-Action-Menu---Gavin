#Gavin Abrahamson 05/13/22
#TBG Action Menu

directionOptions = ['North', 'South', 'East', 'West']
attackOptions = ['Slash', 'Stab']
defenceOptions = ['Block', 'Dodge']


print('Directions:')
for direction in directionOptions:
    print(direction)
    
print('\n')

print('Attacks:')
for attack in attackOptions:
    print(attack)
    
print('\n')

print('Defences:')
for defence in defenceOptions:
    print(defence)
    
print('\n')
action = input('Action: ')

if action == 'north':
    print('You move north.')
elif action == 'south':
    print('You move south.')
elif action == 'east':
    print('You move east.')
elif action == 'west':
    print('You move west.')
elif action == 'slash':
    print('You slash your sword at the enemy.')
elif action == 'stab':
    print('You stab at the enemy.')
elif action == 'block':
    print('You use your shield to block the enemy attack.')
elif action == 'dodge':
    print("You quickly move out of the enemy's path.")
else:
    print('Ensure your command is one of the options printed above, and that it is typed in lowercase letters.')
    
print('\n')
action2 = input('Next Action: ')

if action2 == 'north':
    print('You move north.')
elif action2 == 'south':
    print('You move south.')
elif action2 == 'east':
    print('You move east.')
elif action2 == 'west':
    print('You move west.')
elif action2 == 'slash':
    print('You slash your sword at the enemy.')
elif action2 == 'stab':
    print('You stab at the enemy.')
elif action2 == 'block':
    print('You use your shield to block the enemy attack.')
elif action2 == 'dodge':
    print("You quickly move out of the enemy's path.")
else:
    print('Ensure your command is one of the options printed above, and that it is typed in lowercase letters.')
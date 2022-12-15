import random
     
def roll_dice():
    dice = random.randint(0,5)
    dice_visuls(dice)
    
    
def dice_visuls(num):
    dice = [["[     ]","[  0  ]","[     ]"],
            ["[ 0   ]","[     ]","[   0 ]"],
            ["[     ]","[0 0 0]","[     ]"],
            ["[0   0]","[     ]","[0   0]"],
            ["[0   0]","[  0  ]","[0   0]"],
            ["[0   0]","[0   0]","[0   0]"]]
    for i in dice[num]:
        print(i)

print('''Welocome to Roll Dice Simulation 
      Choose an option to start
      1. Roll dice
      2. Exit''')
choice = int(input('option: '))

while(choice != 2):
    roll_dice()
    choice = int(input('option: '))
        
print('Thank you for using Roll Dice')
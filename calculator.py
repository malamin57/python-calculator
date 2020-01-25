import re
print("Our Magical Calculator")
print("Type 'quit to exit\n")
previous = 0 
run = True

def performMath():
    global  run
    global  previous 
    equation = ''
    if previous == 0:
        equation = input('Enter equation')
    else: 
        equation = input(str(previous))
        
   
    if equation == 'quit':
        print('Goodbye')
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()'']','', equation)
        previous = eval(equation)
        print ("You typed", previous)
    if previous == 0:
        previous = eval(equation)
    else:
        previoius = eval(str(previous) + equation)
        
        
    
while run:
    performMath()

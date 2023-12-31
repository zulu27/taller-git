def modulo(num_1, num_2):
  result = num_1 % num_2
  print(f'{num_1} % {num_2} is equal to {result}')
  return result 
  
def potencia(num_1, num_2):
  result = num_1 ** num_2
  print(f'{num_1} ^ {num_2} is equal to {result}')
  return result
  
def division(num_1, num_2):
  result = num_1 / num_2
  print(f'{num_1} / {num_2} is equal to {result}')
  return result

def multiplication(num_1, num_2):
  result = num_1 * num_2
  print(f'{num_1} * {num_2} is equal to {result}')
  return result

def resta(num_1, num_2):
  result = num_1 - num_2
  print(f'{num_1} - {num_2} is equal to {result}')
  return result
  
def add(num_1, num_2):
  result = num_1 + num_2
  print(f'{num_1} + {num_2} is equal to {result}')
  return result

def game():
  score = 0
  while True:
    print('======== Menu ========'
    '\n1. Add'
    '\n2. Subtract'
    '\n3. Multiplication'
    '\n4. Division'
    '\n5. Power'
    '\n6. Module'
    '\n0. Exit')
    
    
    option = input('\nChoice an option: ')
    if option == "0":
      break
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    answer = int(input('Enter you answer: '))
    if option == "1":
        result = add(num_1, num_2)
        if result == answer:
          score += 1
          print('Correct!!')
        else:
          print('Incorrect')
    if option == "2":
        result = resta(num_1, num_2)
        if result == answer:
          score += 1
          print('Correct!!')
        else:
          print('Incorrect')

    if option == "3":
      result = multiplication(num_1, num_2)
      if answer == result:
        score += 2
        print("Correct!!")
      else:
        print("Incorrect")

    if option == "4":
      result = division(num_1, num_2)
      if answer == result:
        score += 2
        print("Correct!!")
      else:
        print("Incorrect")
        
    if option == "5":
      result = potencia(num_1, num_2)
      if answer == result:
        score += 4
        print("Correct!!")
      else:
        print("Incorrect")
        
    if option == "6":
      result = modulo(num_1, num_2)
      if answer == result:
        score += 4
        print("Correct!!")
      else:
        print("Incorrect")
  
  print(f'======== Game Over ========'
  f'\nYou score is {score}'
  '\nKeep going!')

game()


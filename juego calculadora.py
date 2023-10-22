
def game():
  score = 0
  while True:
    print('======== Menu ========'
    '\n1. Add'
    '\n2. Subtract'
    '\n3. Multiplication'
    '\n4. Division'
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
      result = subtract(num_1,num_2)
      if result == answer:
        score += 1
        print("correct")
      else:
        print("incorrect")
      
    if option == "3":
      result = multiplication(num_1,num_2)
      if result == answer:
        score += 1
        print("correct")
      else:
        print("incorrect")

    if option == "4":
        result = division(num_1,num_2)
        if result == answer:
            score += 1
            print("correct")
        else:
            print("incorrect")

  print(f'======== Game Over ========'
  f'\nYou score is {score}'
  '\nKeep going!')

def main():
  game()

main()

def input_question(question):
  question = f_string(question)
  answer = input(question)

  return answer

def f_string(string):
  string = f"|{string}|"
  string = f"\n{'-' * len(string)}\n{string}\n{'-' * len(string)}\n"
  
  return string

def check_usr_input(u_input):
    print("\n","=" * 20, "\n")
    print(u_input)

    is_correct_input = input_question('Эти данные верны? (y/n)')

    if is_correct_input == 'y':
      return True
    else:
      print("ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.")
      print("=" * 20)
      return False

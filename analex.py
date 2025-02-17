import sys, os
from myerror import MyError
from afd_def import AFD,AFD_FINALS

error_handler = MyError('LexerErrors')

# Processa a entrada do programa e retorna o conteudo do arquivo que contem o código
def process_input():
  check_cm = False
  check_key = False
  
  for idx, arg in enumerate(sys.argv):
    aux = arg.split('.')
    if aux[-1] == 'cm':
      check_cm = True
      idx_cm = idx

    if(arg == "-k"):
      check_key = True

  if(not check_key and len(sys.argv) < 2):
    raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

  if(check_key and len(sys.argv) <= 2):
    raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

  if not check_cm:
    raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
  
  if not os.path.exists(sys.argv[idx_cm]):
    raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    
  data = open(sys.argv[idx_cm])

  return (data.read(), not check_key)

# Imprime a definição do afd
def print_afd(input:str):
  print("Definição da Máquina:")
  print("\nafd =", AFD)
  print("\nAFD_finals =", AFD_FINALS)
  print("\nEntrada =", input)

# Processa a entrada do código gerando a lista de tokens
def generate_tokens(input: str):
  token_list = []
  state = "q0"
  
  stall = False 

  i = 0
  while i < len(input):
    try:
      state = AFD[state][input[i]]
      stall = False
      i = i + 1
    except:
      if state in AFD_FINALS:
        token_list.append(AFD_FINALS[state].strip())

      if stall:
        raise IOError(error_handler.newError(True, 'ERR-LEX-INV-CHAR'))

      state = "q0"
      stall = True

  return token_list


if __name__ == "__main__":
  try:
    (file_text, do_print) = process_input();

    if do_print:
      print_afd(file_text)

    tokens = generate_tokens(file_text);

    print("\n".join(tokens))

  except (ValueError, TypeError) as e:  # Exceções específicas primeiro
    print(e)
  except Exception as e:  # Exceção genérica depois
    print(e)
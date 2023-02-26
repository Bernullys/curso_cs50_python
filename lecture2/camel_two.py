def main():

  camelCase = input("camelCase: ")
  snake_case =(from_cC_to_s_k(camelCase))
  print(snake_case)
  


def from_cC_to_s_k(camel):

  snake_case_store = ""

  for letter in camel:

      if len(snake_case_store) > 0:

          if letter.isupper() == True:
            snake_case_store += "_" + letter.lower()
          else:
              snake_case_store += letter.lower()
      
      else: snake_case_store += letter.lower()
  
  return snake_case_store

main()
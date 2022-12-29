
#addition
def add(n1, n2) :
  return n1 + n2


#sub
def sub(n1, n2) :
  return n1 - n2


#divi
def divi(n1, n2) :
  return n1 / n2

#multi
def multi(n1, n2) :
  return n1 * n2


operations =  {
      "+" : add,
      "-" : sub,
      "*" : multi,
      "/" : divi,

}

def calculator() :
   num1 = int(input ( "What is the first number? :\n "))
   for symbol in operations : 
    print(symbol)

    continue_runing = True

   while continue_runing :

       operation_symbol = input("pick an operation  : \n")

       num2 = int(input ( "What is the second  number? :\n "))

       cal_fun =  operations [operation_symbol]
       answer = cal_fun(num1, num2)

       print(f"{num1} {operation_symbol} {num2} = {answer}")

       continue_cal = input(f"Type 'y' to continue with {answer} or 'n' to stop\n")

       if continue_cal == 'CON' :

          num1 = answer
       else :
         continue_runing = False

         calculator()

calculator()
 






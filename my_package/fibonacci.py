def fibonacci(n_terms):
  num1 = 0
  num2 = 1
  next_num = 1
  count = 0

  while count < n_terms:
    print(num1)
    count += 1
    num1, num2 = num2, next_num
    next_num = num1 + num2
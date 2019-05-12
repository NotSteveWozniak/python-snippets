#!/usr/bin/python3
squares = [1, 4, 9, 16, 25]
print (squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
#squares += [36, 49]
print(squares + [36, 49])
squares.append(64)
print(squares)
squares.append(9 ** 2)
print(squares)
abc = ['a', 'b', 'c']
squares[3] = abc
print(squares)
print(squares[2:4])
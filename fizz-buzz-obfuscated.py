def RPddOuoF(DuPitRAS):
								PkQwYOXj = []
								for i in range(1, DuPitRAS + 1):
																if i % 3 == 0 and i % 5 == 0:
																								PkQwYOXj.append("FizzBuzz")
																elif i % 3 == 0:
																								PkQwYOXj.append("Fizz")
																elif i % 5 == 0:
																								PkQwYOXj.append("Buzz")
																else:
																								PkQwYOXj.append(str(i))
								return PkQwYOXj
DuPitRAS = 10
PkQwYOXj = RPddOuoF(DuPitRAS)
print(' '.join(PkQwYOXj))

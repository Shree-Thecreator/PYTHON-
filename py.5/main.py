# text
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

word = 'Python'
print(word[0] ) # character in position 0

print(word[5])  # character in position 5

# lists

squares= [1, 4, 9, 16, 25]
print(squares[0] )
print(squares[-3:])
print(squares[-1])

rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object
print(True)
rgba.append("Alph")
print(rgb)
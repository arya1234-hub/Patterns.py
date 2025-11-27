#⭐ Common Pattern Questions with Nested Loops

# 1. Square of Stars

# *****
# *****
# *****
# *****
# *****

for i in range(5):
    for j in range(5):
        print('*', end= ' ')
    print()

# 2. Right-Angled Triangle
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i):
        print('*', end = ' ')
    print()

print()
# 3. Inverted Triangle
# *****
# ****
# ***
# **
# *

for i in range(5):
    for j in range(5-i):
        print('*', end = ' ')
    print()

print()

# 4. Pyramid

#     *
#    ***
#   *****
#  *******
# *********

for i in range (5):
    for j in range( 5- i - 1):
        print(' ', end = ' ')
    for k in range (2*i+1):
        print('*', end = ' ')
    print()

print()

# 5. Number Triangle

# 1
# 12
# 123
# 1234
# 12345

for i in range (5):
    for j in range(1, i+2):
        print(j, end = ' ')
    print()

print()

# 6. Floyd’s Triangle

# 1
# 2 3
# 4 5 6
# 7 8 9 10

k = 1
for i in range (4):
    for j in range(i+1):
        print(k, end = ' ')
        k += 1
    print()

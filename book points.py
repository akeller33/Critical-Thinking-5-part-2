# Andrew Keller
# 12/7/2024

books = input('How many books did you purchase this month? ')
while isinstance(books, str):
    if books.isdigit():
        books = int(books)
    else:
        books = input('Must be a number. How many boods did you purchase this month? ')

if books < 2:
    points = 0
elif books >= 2 and books < 4:
    points = 5
elif books >= 4 and books < 6:
    points = 15
elif books >= 6 and books < 8:
    points = 30
else:
    points = 60

print(f'Congratulations you have earned {points} points!!')

      
            

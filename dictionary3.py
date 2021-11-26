keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
dictionary = dict(zip(keys, values))
print(dictionary)

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(tuple(zip(t1, t2))[1][0])
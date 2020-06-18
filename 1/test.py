import pandas as pd
import numpy as np
from tabulate import tabulate

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Pr' : [22001,25001,27001,35001]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

df2 = pd.DataFrame(np.array([[1, 2, 3], [1,10,11],[4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
def f(x):
    d={}
    d['A'] = x['a']
    d['B'] = x['b']
    d['C'] = x['c']
    d['D'] = x[0]+x[1]
    return pd.Series(d, index=['A','B','C','D'])

def g(x):
    print(f"g=\n{x}")
    print("type=",type(x))
    print(tabulate(x, headers='keys', tablefmt='psql'))
    print("a=",x['a'].sum()) 
    d={}
    d['A'] = x['a'].count()
    d['B'] = x['b'].count()
    d['C'] = x['c'].count()
    d['D'] = x['c'].sum()
    return pd.Series(d, index=['A','B','C','D'])

#df.apply(f)


print(tabulate(df2.apply(f,axis=1), headers='keys', tablefmt='psql'))


###print("###########################\n\
##############################\n\
##############################")
###ddd = df2.groupby(['a']).apply(g)
###print("aaaaaaa,=",tabulate(df2.groupby(['a']).apply(g),headers='keys', tablefmt='psql'))
###df2.groupby(['a']).apply(g).to_csv('test_groupby.csv')
###
###print("cccccccccccccccccccc")
###print ("dddd=",ddd)
####print(tabulate(df2.apply(f,axis=1), headers='keys', tablefmt='psql'))
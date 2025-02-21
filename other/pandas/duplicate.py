import pandas as pd
series = [('Stranger Things', 3, 'Millie'),
('Game of Thrones', 8, 'Emilia'), 
('La Casa De Papel', 4, 'Sergio'),
('Westworld', 3, 'Evan Rachel'), 
('Stranger Things', 3, 'Millie'),
('La Casa De Papel', 4, 'Sergio')]

series = pd.DataFrame(series,columns=["name","number","character"])
print(series)
print()
print()
print()
print(series[series.duplicated()])
print()
print()
print()
print(series.drop_duplicates())
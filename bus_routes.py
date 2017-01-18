import timeit
#start_time = timeit.default_timer()

from bs4 import BeautifulSoup
import jsonify
start_time = timeit.default_timer()

def list_of_points_in_bus_route():
	kml = open('1.kml', 'r')
	soup  = BeautifulSoup(kml, "lxml")
	ps1 = soup.findAll('coordinates')[2:]
	ps1 = str(ps1)
	ps1 = ps1.split(',')
	return ps1

x = list_of_points_in_bus_route()
#x = str(x)
#x = x.split(',')

extra = '0.0'
extra1  = '0.0 '

x[0] = float(x[0][14:])
x[len(x)-1] = float(x[len(x)-1][:-15])

for i in x:
	try:
		x[x.index(i)] = float(i)
	except:# Exception as e:
		if extra1 in i:
			x[x.index(i)] = float(str(i)[len(extra1):])

list_of_pairs = []
pairs = []
for n,i in enumerate(x):
	#print n,i
	if not n%2:
		if i:
			pairs.append(x[n])
			pairs.append(x[n+1])
			list_of_pairs.append(pairs)
			pairs = []
	else:
		continue

print list_of_pairs

elapsed = timeit.default_timer() - start_time
print elapsed
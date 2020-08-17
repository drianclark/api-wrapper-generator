from renders.renders import Renders
from pprint import pprint

r = Renders()

m = r.stations(exists=['measures.period'])

pprint(m[0].measures())
# print(type(m[0].measures().period()))
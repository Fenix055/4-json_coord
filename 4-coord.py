#"coord": {
#  "lon": 10.99,
#  "lat": 44.34
#}

from pydantic import BaseModel

class Coord(BaseModel):
    coord: str
    lon = coord['lon']
    lat = coord['lat']

coord = Coord(coord='coord')
print(coord.coord)
print(coord.lon)
print(coord.lat)
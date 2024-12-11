# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install geopy
# 2. Ejecuta el script: python 25_coordenadas_geopy.py

from geopy.distance import geodesic

coord_madrid = (40.4168, -3.7038)
coord_buenos_aires = (-34.6037, -58.3816)

distance_km = geodesic(coord_madrid, coord_buenos_aires).kilometers

print(f"Distancia Madrid/Buenos Aires {distance_km:.2f} km.")
# Distancia Madrid/Buenos Aires 10020.32 km
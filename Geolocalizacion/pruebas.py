import folium.map
import ipinfo
from dotenv import load_dotenv
import os
import sys
import folium
#Necesitas tener tu access token de ip info para que esto funcione
#agregar el token en archivo .env
#Configuracion
load_dotenv()
#Ingresar direccion ip victima
direccion_ip = "191.125.166.253"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
def mapa(latitude, longitude, location, filename="map.html"):
    #funcion para dibujar un mapa
    my_map = folium.Map(location=[latitude, longitude],zoom_start=9)
    folium.Marker([latitude, longitude], popup=location).add_to(my_map)
    my_map.save(filename)
    return os.path.abspath(filename)

def get_ip_details (ip_addr, access_token):
    try:
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_addr)
        return details.all
    except Exception as e:
        print(f"Error al obtener los datos d ela ip: {ip_addr} ")
        sys.exit(1)

if __name__ == "__main__":
    details = get_ip_details(direccion_ip, ACCESS_TOKEN)
    for key, value in details.items():
        print(f"{key}: {value}")
    #Obtener los valores para el mapa
    latitude = details["latitude"]
    longitude = details["longitude"]
    location = details["region"]

    #dibujo
    map_file_path = mapa(latitude, longitude, location)
    print(f"mapa guardado en {map_file_path}")
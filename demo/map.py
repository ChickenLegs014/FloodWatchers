'''
Authors     : Aaron Sapp & Warren Nixon
Date        : Oct. 31, 2026
Course      : CSCI Special Topics: Problem Solving
Assignment  : Project Phase 3: Development - Part 1 (Core Logic)
Module      : map.py
Description : Creates a window with an interactive map
'''

# pyscript gives Python access to the page (document), to JavaScript
# libraries like Leaflet (window), and to event listeners (when)
from pyscript import document, window, when  # Changed (added window and when)
# converts Python lists into JavaScript values Leaflet knows how to use
from pyscript.ffi import to_js

# Alamogordo coordinates
latitude = 32.8995
longitude = -105.9603
zoom = 10

# Starts empty and main() creates it, so that update_map() can update it later
map = None


def map_window(w):
    return to_js(w, dict_converter = window.Object.fromEntries)


def main():
    global map

    document.querySelector("#latitude").value = latitude
    document.querySelector("#longitude").value = longitude
    document.querySelector("#zoom").value = zoom
    document.querySelector("#zoom-label").innerText = zoom

    map = window.L.map(output_div).setView(to_js([latitude, longitude]), zoom)

    # Add the actual map pictures from OpenStreetMap. Without it; it would be a blank gray box.
    window.L.tileLayer(
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        map_window({
            "maxZoom": 19,
            "attribution": "&copy; OpenStreetMap contributors"
        })
    ).addTo(map)

@when("input", ".control")
def update_map(event):
    try:
        lat = float(document.querySelector("#latitude").value)
        lon = float(document.querySelector("#longitude").value)
        z = int(document.querySelector("#zoom").value)
    except ValueError:
        return

    document.querySelector("#zoom-label").innerText = z
    map.setView(to_js([lat, lon]), z)


output_div = document.querySelector("#main")

main()  

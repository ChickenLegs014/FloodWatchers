'''
Authors     : Aaron Sapp & Warren Nixon
Date        : Oct. 31, 2026
Course      : CSCI Special Topics: Problem Solving
Assignment  : Project Phase 3: Development - Part 1 (Core Logic)
Module      : map.py
Description : Creates a window with an interactive map
'''

import asyncio  # downloads zone shapes
# pyscript gives Python access to the page (document), to JavaScript. Leaflet (window), event listeners (when), and downloads data (fetch)
from pyscript import document, window, when, fetch  # type: ignore[reportMissingImports]
# converts Python lists into JavaScript values Leaflet knows how to use
from pyscript.ffi import to_js  # type: ignore[reportMissingImports]

# Alamogordo coordinates
latitude = 32.8995
longitude = -105.9603
zoom = 10

ALERTS_URL = "https://api.weather.gov/alerts/active/area/NM"

# color on the map, based on the severity of the alert weather service gives 
SEVERITY_COLORS = {
    "Extreme": "#b00020",
    "Severe": "#57504d",
    "Moderate": "#f9a825",
    "Minor": "#1565c0"
}

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

    # Adds the actual map pictures from OpenStreetMap. Without it; it would be a blank gray box.
    window.L.tileLayer(
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        map_window({
            "maxZoom": 19,
            "attribution": "&copy; OpenStreetMap contributors"
        })
    ).addTo(map)

# Downloads a url and returns the data as Python
async def get_json(url):
    response = await fetch(url)
    return await response.json()


# adds a little box that opens when you click a alert on the map.
def make_popup(props):
    popup = document.createElement("div")
    title = document.createElement("strong")
    title.textContent = props["event"] + " (" + str(props["severity"]) + ")"
    area = document.createElement("p")
    area.textContent = props["areaDesc"]
    headline = document.createElement("p")
    headline.textContent = props["headline"] or ""
    popup.append(title, area, headline)
    return popup


# gets the active alert then adds them on the map and lists them in Area warnings
async def load_alerts():
    warnings = document.querySelector("#warnings")
    warnings.innerHTML = ""

    try:
        data = await get_json(ALERTS_URL)
        alerts = data["features"]

        # alerts have no shape. They are put in list zones instead which has a shape. Collects the zone then download it
        zone_urls = []
        for alert in alerts:
            if not alert["geometry"]:
                for zone in alert["properties"]["affectedZones"]:
                    if zone not in zone_urls:
                        zone_urls.append(zone)

        results = await asyncio.gather(*[get_json(u) for u in zone_urls], return_exceptions = True)
        zone_shapes = {}
        for url, result in zip(zone_urls, results):
            if not isinstance(result, Exception) and result.get("geometry"):
                zone_shapes[url] = result["geometry"]

        for alert in alerts:
            props = alert["properties"]
            color = SEVERITY_COLORS.get(props["severity"], "#616161")

            # Use the alert's shape if it has one or it will use the zones shapes
            if alert["geometry"]:
                shapes = [alert["geometry"]]
            else:
                shapes = [zone_shapes[z] for z in props["affectedZones"] if z in zone_shapes]

            if shapes:
                window.L.geoJSON(
                    map_window(shapes),
                    map_window({"style": map_window({"color": color, "weight": 2, "fillOpacity": 0.25})})
                ).bindPopup(make_popup(props)).addTo(map)

            # Adds the alert to the Area warnings list
            item = document.createElement("p")
            item.className = "column"
            item.textContent = props["event"] + " (" + str(props["severity"]) + "): " + props["areaDesc"]
            item.style.borderLeft = "6px solid " + color
            warnings.appendChild(item)

        if not alerts:
            warnings.innerHTML = '<p class="column">No active alerts</p>'

    except Exception as error:
        # shows a message instead of failing silently
        print("Could not load alerts:", error)
        warnings.innerHTML = '<p class="column">Could not load alerts</p>'


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
# await is so the map works while alerts are downloading.
await load_alerts()

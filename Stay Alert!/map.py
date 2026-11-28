# Completed
    # Create map warnings
    # Sorts warnings by their severity
    # Filters unknown warnings
    # Search box moves the map to a state

# Downloads zone shapes
import asyncio 

# Gives Python access to the page (document), to JavaScript, Leaflet (window), event listeners (when), and downloads data (fetch)
from pyscript import document, window, when, fetch  # type: ignore[reportMissingImports]

# Converts Python lists into JavaScript values Leaflet knows how to use
from pyscript.ffi import to_js  # type: ignore[reportMissingImports]


# Alamogordo coordinates
latitude = 32.8995
longitude = -105.9603
zoom = 10

# API
alerts_url = "https://api.weather.gov/alerts/active/"

# Zip code of each state's capital
zip_code_abbreviations = {
    "Alabama" : "36104",
    "Alaska" : "99801",
    "Arizona" : "85001",
    "Arkansas" : "72201",
    "California" : "95814",
    "Colorado" : "80202",
    "Connecticut" : "06103",
    "Delaware" : "19901",
    "Florida" : "32301",
    "Georgia" : "30303",
    "Hawaii" : "96813",
    "Idaho" : "83702",
    "Illinois" : "62701",
    "Indiana" : "46204",
    "Iowa" : "50309",
    "Kansas" : "66603",
    "Kentucky" : "40601",
    "Louisiana" : "70802",
    "Maine" : "04330",
    "Maryland" : "21401",
    "Massachusetts" : "02201",
    "Michigan" : "48933",
    "Minnesota" : "55102",
    "Mississippi" : "39205",
    "Missouri" : "65101",
    "Montana" : "59623",
    "Nebraska" : "68502",
    "Nevada" : "89701",
    "New Hampshire" : "03301",
    "New Jersey" : "08606",
    "New Mexico" : "87501",
    "New York" : "12207",
    "North Carolina" : "27601",
    "North Dakota" : "58501",
    "Ohio" : "43215",
    "Oklahoma" : "73102",
    "Oregon" : "97301",
    "Pennsylvania" : "17101",
    "Rhode Island" : "02903",
    "South Carolina" : "29217",
    "South Dakota" : "57501",
    "Tennessee" : "37219",
    "Texas" : "78701",
    "Utah" : "84111",
    "Vermont" : "05602",
    "Virginia" : "23219",
    "Washington" : "98507",
    "West Virginia" : "25301",
    "Wisconsin" : "53703",
    "Wyoming" : "82001",
}

# Latitude and longitude of each state
state_coordinates = {
    "Alabama" : (32.3792, -86.3077),
    "Alaska" : (58.3019, -134.4197),
    "Arizona" : (33.4484, -112.074),
    "Arkansas" : (34.7465, -92.2896),
    "California" : (38.5816, -121.4944),
    "Colorado" : (39.7392, -104.9903),
    "Connecticut" : (41.7658, -72.6734),
    "Delaware" : (39.1582, -75.5244),
    "Florida" : (30.4383, -84.2807),
    "Georgia" : (33.749, -84.388),
    "Hawaii" : (21.3069, -157.8583),
    "Idaho" : (43.615, -116.2023),
    "Illinois" : (39.7817, -89.6501),
    "Indiana" : (39.7684, -86.1581),
    "Iowa" : (41.5868, -93.625),
    "Kansas" : (39.0473, -95.6752),
    "Kentucky" : (38.2009, -84.8733),
    "Louisiana" : (30.4515, -91.1871),
    "Maine" : (44.3106, -69.7795),
    "Maryland" : (38.9784, -76.4922),
    "Massachusetts" : (42.3601, -71.0589),
    "Michigan" : (42.7325, -84.5555),
    "Minnesota" : (44.9537, -93.09),
    "Mississippi" : (32.2988, -90.1848),
    "Missouri" : (38.5767, -92.1735),
    "Montana" : (46.5891, -112.0391),
    "Nebraska" : (40.8136, -96.7026),
    "Nevada" : (39.1638, -119.7674),
    "New Hampshire" : (43.2081, -71.5376),
    "New Jersey" : (40.2206, -74.7597),
    "New Mexico" : (35.687, -105.9378),
    "New York" : (42.6526, -73.7562),
    "North Carolina" : (35.7796, -78.6382),
    "North Dakota" : (46.8083, -100.7837),
    "Ohio" : (39.9612, -82.9988),
    "Oklahoma" : (35.4676, -97.5164),
    "Oregon" : (44.9429, -123.0351),
    "Pennsylvania" : (40.2732, -76.8867),
    "Rhode Island" : (41.824, -71.4128),
    "South Carolina" : (34.0007, -81.0348),
    "South Dakota" : (44.3683, -100.351),
    "Tennessee" : (36.1627, -86.7816),
    "Texas" : (30.2672, -97.7431),
    "Utah" : (40.7608, -111.891),
    "Vermont" : (44.2601, -72.5754),
    "Virginia" : (37.5407, -77.436),
    "Washington" : (47.0379, -122.9007),
    "West Virginia" : (38.3498, -81.6326),
    "Wisconsin" : (43.0731, -89.4012),
    "Wyoming" : (41.14, -104.8202),
}

# State abbreviations
state_abbreviations = {
    "Alabama" : "AL",
    "Alaska" : "AK",
    "Arizona" : "AZ",
    "Arkansas" : "AR",
    "California" : "CA",
    "Colorado" : "CO",
    "Connecticut" : "CT",
    "Delaware" : "DE",
    "Florida" : "FL",
    "Georgia" : "GA",
    "Hawaii" : "HI",
    "Idaho" : "ID",
    "Illinois" : "IL",
    "Indiana" : "IN",
    "Iowa" : "IA",
    "Kansas" : "KS",
    "Kentucky" : "KY",
    "Louisiana" : "LA",
    "Maine" : "ME",
    "Maryland" : "MD",
    "Massachusetts" : "MA",
    "Michigan" : "MI",
    "Minnesota" : "MN",
    "Mississippi" : "MS",
    "Missouri" : "MO",
    "Montana" : "MT",
    "Nebraska" : "NE",
    "Nevada" : "NV",
    "New Hampshire" : "NH",
    "New Jersey" : "NJ",
    "New Mexico" : "NM",
    "New York" : "NY",
    "North Carolina" : "NC",
    "North Dakota" : "ND",
    "Ohio" : "OH",
    "Oklahoma" : "OK",
    "Oregon" : "OR",
    "Pennsylvania" : "PA",
    "Rhode Island" : "RI",
    "South Carolina" : "SC",
    "South Dakota" : "SD",
    "Tennessee" : "TN",
    "Texas" : "TX",
    "Utah" : "UT",
    "Vermont" : "VT",
    "Virginia" : "VA",
    "Washington" : "WA",
    "West Virginia" : "WV",
    "Wisconsin" : "WI",
    "Wyoming" : "WY",
}

# Color on the map, based on the severity of the alert weather service gives 
severity_colors = {
    "Extreme": "#ff6481",
    "Severe": "#ff9d64",
    "Moderate": "#ffe364",
    "Minor": "#e3ff64"
}

# Warning text
# Creates warning text
class WarningText:
    def __init__(self, properties, color):

        # Set attributes
        self.properties = properties
        self.event = self.properties["event"]
        self.severity = self.properties["severity"]
        self.area_description = self.properties["areaDesc"]
        self.color = color

        # Set severity score
        match self.severity:
            case "Extreme":
                self.severity_score = 5

            case "Severe":
                self.severity_score = 4

            case "Moderate":
                self.severity_score = 3

            case "Minor":
                self.severity_score = 2

            case _:
                self.severity_score = 1

        # Create text
        self.create_text()

    # Creates and returns text
    def create_text(self):

        # Set text attributes
        self.text = document.createElement("p")
        self.text.className = "column"
        self.text.textContent = f"{self.event} ({str(self.severity)}) {self.area_description}"
        self.text.style.borderLeft = f"6px solid {self.color}"

# Starts empty and main() creates it, so that update_map() can update it later
map = None

# converts a Python list into a plain JavaScript
def map_window(w):
    return to_js(w, dict_converter = window.Object.fromEntries)

# creates the map and fills in the control boxes (Latitude, Longitude and Zoom)
def main():
    global map

    # sets the cords and zoom for Latitude, Longitude and Zoom
    document.querySelector("#latitude").value = latitude
    document.querySelector("#longitude").value = longitude
    document.querySelector("#zoom").value = zoom
    document.querySelector("#zoom-label").innerText = zoom

    # creates the Leaflet map and center it on the start point
    map = window.L.map(output_div).setView(to_js([latitude, longitude]), zoom)

    # Adds the actual map pictures from OpenStreetMap. Without it; it would be a blank gray box
    window.L.tileLayer(
        # {z}/{x}/{y} are based on the latitude, longitude, and zoom.
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        map_window({
            "maxZoom": 19,                                      
            "attribution": "&copy; OpenStreetMap contributors"
        })
    ).addTo(map)

# Downloads a url and returns the data as Python.
async def get_json(url):
    response = await fetch(url)
    return await response.json()

# Adds a little box that opens when you click a alert on the map
def make_popup(props):
    popup = document.createElement("div")
    title = document.createElement("strong")
    title.textContent = f"{props["event"]} ({str(props["severity"])})"
    area = document.createElement("p")
    area.textContent = props["areaDesc"]
    headline = document.createElement("p")
    headline.textContent = props["headline"] or ""
    popup.append(title, area, headline)
    return popup

# Gets the active alert then adds them on the map and lists them in Area warnings
async def load_alerts():
    warnings_text = []

    # clear out the "Loading alerts..." message
    warnings = document.querySelector("#warnings")
    warnings.innerHTML = ""

    try:
        # downloads all active alerts
        data = await get_json(alerts_url)

        # Each alert gets data from the url and features (the stuff added to it)
        alerts = data["features"]

        # Alerts have no shape. They are put in list zones instead which has a shape. Collects the zone then download it
        zone_urls = []
        for alert in alerts:
            if not alert["geometry"]:
                for zone in alert["properties"]["affectedZones"]:
                    # so there is not many zones on top of each other.
                    if zone not in zone_urls:
                        zone_urls.append(zone)

        # gets all of the zone and alert shapes.
        results = await asyncio.gather(*[get_json(u) for u in zone_urls], return_exceptions = True)
        # gets the zones shape and lists it.
        zone_shapes = {}
        for url, result in zip(zone_urls, results):
            if not isinstance(result, Exception) and result.get("geometry"):
                zone_shapes[url] = result["geometry"]

        for alert in alerts:
            props = alert["properties"]

            # Filters out unknown warnings
            if props["severity"] == "Unknown":
                continue

            color = severity_colors.get(props["severity"], "#616161")

            # Use the alert's shape if it has one or it will use the zones shapes
            if alert["geometry"]:
                shapes = [alert["geometry"]]
            else:
                shapes = [zone_shapes[z] for z in props["affectedZones"] if z in zone_shapes]

            # adds the shape and the popup to the map.
            if shapes:
                window.L.geoJSON(
                    map_window(shapes),
                    map_window({"style": map_window({"color": color, "weight": 2, "fillOpacity": 0.25})})
                ).bindPopup(make_popup(props)).addTo(map)

            # Create text
            text = WarningText(props, color)

            # Append text to warning texts
            warnings_text.append(text)

        if not alerts:
            warnings.innerHTML = '<p class="column">No active alerts</p>'

    # shows an error message if the alerts cannot load.
    except Exception as error:

        print("Could not load alerts:", error)
        warnings.innerHTML = '<p class="column">Could not load alerts</p>'

    # Sorts warning texts by severity
    sorted_warnings = sorted(warnings_text, key = lambda warning: warning.severity_score, reverse = True)

    # Iterates through each warning
    for warning in sorted_warnings:

        # Add warning text to warnings
        warnings.appendChild(warning.text)

# finds the state typed in the search box either the name, state abbreviation, or zip code and moves the map there
def search_location():
    status = document.querySelector("#status")
    text = document.querySelector("#zip").value.strip()

    if not text:
        status.innerText = "Enter a state name, abbreviation, or zip code"
        return

    # Matches a state name, state abbreviation, or zip codes
    found_state = None
    for state_name, zip_code in zip_code_abbreviations.items():
        if (text.lower() == state_name.lower()
                or text.upper() == state_abbreviations[state_name]
                or text == zip_code):
            found_state = state_name
            break

    if found_state is None:
        status.innerText = f"Could not find {text}. Try a state name, state abbreviation like NM, or a state capital zip code"
        return

    # Gets the state's coordinates from state_coordinates
    lat, lon = state_coordinates[found_state]

    # Keep the current zoom level, and fill in the Latitude and Longitude boxes
    current_zoom = map.getZoom()
    document.querySelector("#latitude").value = lat
    document.querySelector("#longitude").value = lon
    map.setView(to_js([lat, lon]), current_zoom)

    status.innerText = f"Showing {found_state}"

# Search button
@when("click", "#zip-button")
def search_clicked(event):
    search_location()

# pressing Enter also searches
@when("keydown", "#zip")
def search_enter_pressed(event):
    if event.key == "Enter":
        search_location()

# what the controls get changed it updates the map
@when("input", ".control")
def update_map():
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

# Await is so the map works while alerts are downloading.
await load_alerts()
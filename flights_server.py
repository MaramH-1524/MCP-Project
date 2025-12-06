from mcp.server.fastmcp import FastMCP
import os
import json
app=FastMCP(name="FlightInfo")
FLIGHTS_PATH = os.path.join(os.path.dirname(__file__), "flights.json")

def  _load_flights():
  with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
    return json.load(f).get("flights", [])
@app.resource("flights://today")
def flights_resource():
  """
  Resource qui expose la liste des vols du jour.
  L'URL 'flights://today' sera visible par Copilot/Claude.
  """
  with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
    return f.read()
@app.tool()
def find_flight(flight_number: str) -> str:
   """Trouve un vol par son numéro (ex: AF1234)"""
   flights = _load_flights()
   for flight in flights:
      if flight.get("flight_number", "").upper() == flight_number.upper():
        return f"""✈️
        Vol {flight["flight_number"]} ({flight["airline"]})
        {flight["departure_city"]} → {flight["arrival_city"]}
        Départ : {flight["departure_time"]} | Arrivée :
{flight["arrival_time"]}
        Statut : {flight["status"]}
        """
      return f"Vol {flight_number} non trouvé aujourd'hui."

@app.tool()
def flights_to(destination: str) -> str:
    """Liste tous les vols à destination d'une ville aujourd'hui."""
    flights = _load_flights()
    matches = [f for f in flights if destination.lower() in f["arrival_city"].lower()]

    if not matches:
        return f"Aucun vol trouvé vers {destination.title()} aujourd'hui."

    result = f"Vols vers {destination.title()} ({len(matches)} trouvé(s)) :\n\n"

    for f in matches:
        result += (
            f"• {f['flight_number']} ({f['airline']}) → "
            f"{f['arrival_city']} à {f['arrival_time']} – {f['status']}\n"
        )

    return result.strip()
#question 2/c 
@app.tool()
def flights_by_status(status: str) -> str:
    """Renvoie tous les vols ayant un statut donné (ex: À l'heure, Retardé)."""

    flights = _load_flights()

    matches = [f for f in flights if f["status"].lower() == status.lower()]

    if not matches:
        return f"Aucun vol trouvé avec le statut : {status}"

    result = f"Vols avec statut '{status}' ({len(matches)} trouvé(s)) :\n\n"
    for f in matches:
        result += (
            f"• {f['flight_number']} ({f['airline']}) | "
            f"{f['departure_city']} → {f['arrival_city']} | "
            f"{f['departure_time']} – {f['arrival_time']}\n"
        )
    return result.strip()
#question 2/d 
@app.tool()
def next_flights(before_time: str) -> str:
    """Liste les vols qui partent avant une heure donnée (format HH:MM)."""

    flights = _load_flights()

    matches = [
        f for f in flights
        if f["departure_time"] <= before_time
    ]

    if not matches:
        return f"Aucun vol ne part avant {before_time}."

    result = f"Vols avant {before_time} ({len(matches)} trouvé(s)) :\n\n"
    for f in matches:
        result += (
            f"• {f['flight_number']} ({f['airline']}) – Départ {f['departure_time']} "
            f"→ {f['arrival_city']} ({f['status']})\n"
        )
    return result.strip()




# Lancement du serveur
if __name__ == "__main__":
    app.run(transport="stdio")  # pour VS Code Copilot


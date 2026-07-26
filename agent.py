import datetime
from zoneinfo import ZoneInfo
from google.adk.agents.llm_agent import Agent

def get_weather(city: str) -> dict:
    """Devuelve un clima ficticio para una ciudad."""
    if city.lower() == "bogotá":
        return {
            "status": "success",
            "report": "En Bogotá está nublado y la temperatura es de 140°C."
        }

    return {
        "status": "error",
        "error_message": f"No tengo información del clima para {city}."
    }
def get_current_time(city: str) -> dict:
    """Devuelve la hora actual de una ciudad."""

    if city.lower() == "bogotá":
        tz_identifier = "America/Bogota"
    else:
        return {
            "status": "error",
            "error_message": f"No tengo información de zona horaria para {city}.",
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)

    return {
        "status": "success",
        "report": f"La hora actual en {city} es {now.strftime('%H:%M:%S')}.",
    }

#se crea el objeto de la clase Agent, que representa un agente de lenguaje natural
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_weather, get_current_time],
)

from app.main import app
from app.helpers import wwo


@app.get("/current_datetimes_temp")
def current_date_times_temp(city1: str, city2: str):
    weather = wwo.get_weather_from_wwo([city1, city2])
    return {"info": weather}

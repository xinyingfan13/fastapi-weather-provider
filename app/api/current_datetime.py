from app.main import app
from app.helpers import wwo


@app.get("/current_datetimes")
def current_date_times(city1: str, city2: str):
    timezones = wwo.get_date_time_from_wwo([city1, city2])
    return {"date": timezones}
class API_CLIENT:

    def __init__(self) -> None:
        self.base_one_call = "https://api.openweathermap.org/data/3.0/onecall"
        self.base_time_stamp_call = "https://api.openweathermap.org/data/3.0/onecall/timemachine"

    def fetch_weather(self, lat: float, lon: float):
        return "called"
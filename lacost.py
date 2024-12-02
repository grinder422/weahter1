from locust import HttpUser, task, between

class WeatherAppUser(HttpUser):
    wait_time = between(1, 5)  # Затримка між запитами від 1 до 5 секунд

    @task
    def get_weather(self):
        response = self.client.get("/data/2.5/weather?q=Kyiv&appid=6e2ebf08cb24f66749f31d738195849b&units=metric&lang=ua")
        assert response.status_code == 200

    @task(2)
    def add_to_favorites(self):
        # Приклад запиту для додавання улюбленого міста
        response = self.client.post("/add_favorite", json={"city": "Kyiv"})
        assert response.status_code == 200


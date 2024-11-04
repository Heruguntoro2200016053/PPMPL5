from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5) # Tunggu antara 1 hingga 5 detik sebelum request selanjutnya

    @task
    def get_users(self):
        self.client.get("/users")  # Mengambil semua pengguna

    @task
    def get_user_by_id(self):
        user_id = 1  # Contoh ID pengguna
        self.client.get(f"/users/{user_id}")  # Mengambil detail pengguna berdasarkan ID
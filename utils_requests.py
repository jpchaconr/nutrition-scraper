import requests
import settings
# import nutrition_scraper_utils.settings


class AuthRequests:
  def __init__(self):
    self.auth_url = settings.AUTH_SERVICE_URL
    
  def login(self, rut, password):
    login_url = f"{self.auth_url}auth/login/"
    return requests.post(
        url=login_url,
        json={"rut": rut, "password": password},
    )


class ProductRequests:
  def __init__(self):
    self.main_url = settings.MAIN_SERVICE_URL
    
  def add_product(self, data, access):
    products_url = f"{self.main_url}products/"
    return requests.post(
        url=products_url,
        headers={"Authorization": access},
        json=data,
    )


class NutritionRequests:
  def __init__(self):
    self.main_url = settings.MAIN_SERVICE_URL
    
  def add_nutrition(self, data, access):
    nutrition_url = f"{self.main_url}nutrition/"
    return requests.post(
        url=nutrition_url,
        headers={"Authorization": access},
        json=data,
    )


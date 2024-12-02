from behave import given, when, then
from weather_api import get_weather
from favorites import add_to_favorites, remove_from_favorites, update_favorites_list, FAVORITE_CITIES

@given('користувач знаходиться на головній сторінці')
def step_given_user_is_on_main_page(context):
    # Мокування інтерфейсу, щоб уникнути реального запуску Tkinter
    context.weather_info = ""

@when('він вводить назву міста "{city}"')
def step_when_user_inputs_city(context, city):
    # Виклик функції без графічного інтерфейсу
    context.weather_info = get_weather(city)

@then('він бачить інформацію про погоду для "{city}"')
def step_then_user_sees_weather_info(context, city):
    assert f"Місто: {city}" in context.weather_info

@given('користувач знаходиться на сторінці улюблених міст')
def step_given_user_is_on_favorites_page(context):
    context.favorites = []

@when('він додає місто "{city}" до улюблених')
def step_when_user_adds_city_to_favorites(context, city):
    add_to_favorites(city, context.favorites)

@then('місто "{city}" відображається у списку улюблених')
def step_then_city_is_in_favorites(context, city):
    assert city in context.favorites

@given('місто "{city}" є у списку улюблених')
def step_given_city_is_in_favorites(context, city):
    context.favorites = [city]

@when('користувач видаляє місто "{city}" з улюблених')
def step_when_user_removes_city_from_favorites(context, city):
    remove_from_favorites(context.favorites, city)

@then('місто "{city}" більше не відображається у списку улюблених')
def step_then_city_is_not_in_favorites(context, city):
    assert city not in context.favorites


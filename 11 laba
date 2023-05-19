class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print("Рейтинг обновлен!")


newRestaurant = Restaurant("У мамы дома", "Русская", 4)
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

restaurants = [Restaurant("Вкусно и точка", "Великолепная", 5),
               Restaurant("KFC", "Отменная", 3),
               Restaurant("Burger King", "Американская", 4.5)]

for restaurant in restaurants:
    restaurant.describe_restaurant()

newRestaurant.update_rating(4.5)
newRestaurant.describe_restaurant()


from django.test import TestCase
#from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
#from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setup(self):
        # Add a few items into the Menu.
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Olives", price=20, inventory=100)
        Menu.objects.create(title="Bruschetta", price=50, inventory=100)
        Menu.objects.create(title="PitaChips", price=30, inventory=100)

    def test_getall(self):
        menu_list = self.client.get('/restaurant/menu/')
        # Ensure that there must be at least one menu item inside the list.
        self.assertNotEqual(menu_list, 404)

    def test_getthis(self):
        this_item = self.client.get('/restaurant/menu/2')
        self.assertNotEqual(this_item, 404)
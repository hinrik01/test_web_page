from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client


# Create your tests here.
from cereal.models import Cereal


class CartTest(TestCase):
    def setUp(self):
        self.f = RequestFactory()
        self.c = Client()
        self.user = User.objects.create(username='testuser', password='password', email='test@test.is')
        self.c.force_login(user=self.user)

    def add_to_cart_test(self):
        cereal = Cereal(id=1,
                        name='Weetabix',
                        description='Weetabix is a nutritionally packed**, tasty breakfast made with 100% wholegrain and fortified with vitamins and iron to help set you up to take on the day.',
                        price=700,
                        ingredients='Wholegrain Wheat (95%), Malted Barley Extract, Sugar, Salt, Niacin, Iron, Riboflavin (B2), Thiamin (B1), Folic Acid',
                        weight=450,
                        sugar=4)

    def get_cart(self):
        pass

    def delete_from_cart(self):
        pass

    def update_quantity_in_cart(self):
        pass

    def clear_cart(self):
        pass

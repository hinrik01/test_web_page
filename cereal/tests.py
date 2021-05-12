from django.test import TestCase

# Create your tests here.
from cereal.models import Cereal


class CerealTest(TestCase):

    def create_cereal(self):
        return Cereal.objects.create(id=1, name='Weetabix',
                                    description='Weetabix is a nutritionally packed**, tasty breakfast made with 100% wholegrain and fortified with vitamins and iron to help set you up to take on the day.',
                                    price=700,
                                    ingredients='Wholegrain Wheat (95%), Malted Barley Extract, Sugar, Salt, Niacin, Iron, Riboflavin (B2), Thiamin (B1), Folic Acid',
                                    weight=450, sugar=4)

    def test_cereal_creation(self):
        w = self.create_cereal()
        self.assertTrue(isinstance(w, Cereal))


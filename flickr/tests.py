from django.test import TestCase

#testing the save method
def save_save_method(self):
    self.james.save_location()
    self.nairobi.save_location()
    self.assertTrue(len(locations) > 0)

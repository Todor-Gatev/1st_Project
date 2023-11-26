class A:
    # supporting staff
    # getters and setters

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion

#
# from unittest import TestCase, main
#
#
# class Test(TestCase):
#     def setUp(self) -> None:
#         self.
#     #
#     # def test_default_class_attribute_is_correct(self):
#     #     self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
#
#     def test_correct_initialization(self):
#         self.assertEqual()
#
#
# if __name__ == "__main__":
#     main()

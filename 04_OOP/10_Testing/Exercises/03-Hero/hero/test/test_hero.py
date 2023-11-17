from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 3.2, 1.2)
        self.enemy = Hero("Enemy", 1, 1.6, 0.6)

    def test_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(3.2, self.hero.health)
        self.assertEqual(1.2, self.hero.damage)

    def test_battle_if_hero_is_the_same_as_enemy_exception_expected(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_is_zero_or_negative_expected_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_if_enemy_health_is_zero_or_negative_expected_value_error(self):
        self.enemy.health = 0
        expected = "You cannot fight Enemy. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected, str(ve.exception))
        

if __name__ == "__main__":
    main()

from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_if_hero_is_the_same_as_enemy_exception_expected(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_is_zero_or_negative_expected_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(ve.exception))

    def test_battle_if_enemy_health_is_zero_or_negative_expected_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        expected = "You cannot fight Enemy. He needs to rest"
        self.assertEqual(expected, str(ve.exception))

    # def test_battle_if_both_hero_and_enemy_health_is_zero_or_negative_after_battle(self):

    def test_battle_decrease_correctly_hero_and_enemy_health_draw_result(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_player_win_proper_increase_level_health_damage(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_player_lose_proper_increase_level_health_damage(self):
        result = self.enemy.battle(self.hero)

        self.assertEqual("You lose", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_correct__str__(self):
        result = f"Hero Hero: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n"
        self.assertEqual(result, str(self.hero))


if __name__ == "__main__":
    main()

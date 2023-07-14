
chicken_menu_pcs = int(input())
fish_menu_pcs = int(input())
veg_menu_pcs = int(input())

price_chicken = chicken_menu_pcs * 10.35
price_fish = fish_menu_pcs * 12.40
price_veg = veg_menu_pcs * 8.15

price = (price_chicken + price_fish + price_veg) * 1.2 + 2.5
print(price)

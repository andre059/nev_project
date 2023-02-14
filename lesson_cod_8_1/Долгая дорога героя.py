class Hero:

  def go_right(self, x):
    print(f"Я иду {x} метров направо")

  def go_left(self, x):
    print(f"Я иду {x} метров налево")

  def observe(self):
    print("Я осматриваюсь")

hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()

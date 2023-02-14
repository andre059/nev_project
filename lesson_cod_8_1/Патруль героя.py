class Hero:

  def go_up(self):
    print("Я иду наверх")

  def go_down (self):
    print("Я иду вниз")

  def observe(self):
    print("Я осматриваюсь")

  def rest (self):
    print("Я отдыхаю")


hero = Hero()

hero.go_up()
hero.go_up()
hero.observe()
hero.go_down()
hero.go_down()
hero.rest()

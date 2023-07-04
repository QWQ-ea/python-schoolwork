class Customer:
  def __init__(self, name):
    self.name = name
    self.foods = []
  def placeOrder(self, employee):
    while True:
        choice = input("请问您要点什么餐？(按 n 结束点餐) ")
        if choice == 'n':
            break
        food = employee.takeOrder(choice)
        self.foods.append(food)
  def showOrder(self):
     print(f"{self.name} 点了以下餐品：")
     for food in self.foods:
        print(food.name, end=" | ")
     print()

class Employee:
  def __init__(self,name):
    self.name=name
  def takeOrder(self, choice):
    food = Food(choice)
    print(f"{food.name} 点餐成功！")
    return food

class Food:
  def __init__(self, name):
     self.name = name

class Lunch:
  def __init__(self, customer, employee):
    self.customer = customer
    self.employee = employee
  def order(self):
    self.customer.placeOrder(self.employee)
  def result(self):
    self.customer.showOrder()

customer = Customer("汤姆")
employee = Employee("肯德基")
lunch = Lunch(customer, employee)

while True:
  print("请选择您要进行的操作：")
  print("1. 我要点餐")
  print("2. 展示菜单")
  print("3. 退出程序")
  
  choice = input()

  if choice == "1":
    lunch.order()
  elif choice == "2":
    lunch.result()
  elif choice == "3":
    break
  else:
    print("输入有误，请重新输入。")   


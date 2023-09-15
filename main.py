class class bankaccount:
  def __init__(self,acno,acname,acbal=0.0):
    self.__acno = acno
    self.__acname=acname
    self.__acbal=acbal

  def deposit(self,amt):
    if amt > 0:
      self.__acbal +=amt
      print("deposited rs.{}. your current balance is : rs.{}".format(amt,self.__acbal))
    else:
      print("invalid data")

  def withdraw(self,amt):
    if amt > 0 and amt <= self.__acbal:
      self.__acbal -= amt
      print("withdrew rs.{}. yourcurrent balance is rs.{}".format(amt,self.__acbal))
    else:
      print("invalid transactions")

  def display(self):
    a=float(self.__acbal)
    b=int(self.__acno)
    print("hai {} balance for your account no. {} is rs.{}".format(self.__acname,b,a))


acc = bankaccount(2005,"haniya",1500)
acc.display()
acc.deposit(300)
acc.withdraw(500)￼not
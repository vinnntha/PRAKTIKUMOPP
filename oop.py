def opp(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    return opp(number)


print(opp(4))  # Expected: Even
print(opp(7))  # Expected: Odd
# The output should be like below

# write and continue the code down here

def Parameter(nomor):
    if nomor > 0:
        return "Positive"        
    elif nomor < 0:
        return "Negative"
    else:
        return "Zero"

# Test
print("--------------------------------")
print(Parameter(10))  # Expected: Positive
print(Parameter(-5))  # Expected: Negative
print(Parameter(0))  # Expected: Zero

def boolean(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
# Test
print("--------------------------------")
print(boolean("kasur", "rusak")) # Expected: True
print(boolean("hello", "world")) # Expected: False

def calculate(num):
    
        result = 1
        for i in range(2, num + 1):
            result *= i 
        return result 

print("--------------------------------")
print(calculate(5)) # Expected: 120
print(calculate(0)) # Expected: 1

def function(a):
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
print("--------------------------------")
print(function("racecar")) # Expected: True
print(function("python")) # Expected: False
print(function("habibah")) # Expected : True

def armStrong(arm):
    
    num_str = str(arm)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == arm 

print("--------------------------------")
print(armStrong(153)) # Expected: True (1^3 + 5^3 + 3^3 = 153)
print(armStrong(370)) # Expected: True (3^3 + 7^3 + 0^3 = 370)
print(armStrong(123)) # Expected: False



class BankAccount:
    def init(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return "Invalid withdrawal amount or insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"


# Test
account = BankAccount("Name")
print(account.deposit(1000))   # Deposited 1000. New balance: 1000
print(account.withdraw(500))   # Withdrew 500. New balance: 500
print(account.withdraw(600))   # Invalid withdrawal amount or insufficient funds



    # ==== soal 8 =====
class Student:
    def init(self, name):
        self.name = name
        self.grades = []  # daftar nilai disimpan d
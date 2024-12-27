#question1: Write a Python code that prints numbers from 1 to 10 on the screen.

print(*range(1,11), sep = "\n")

#question2:
girdi=int(input("Bir sayi giriniz: "))
even_numbers=[]

"""for i in range(girdi+1):
    if i%2==0:
        even_numbers.append(i)

print("cift sayilar :", even_numbers)"""
i=0
while i<=girdi:
    if i%2==0:
        even_numbers.append(i)
    i+=1

print(even_numbers)  

#question3:
start = int (input('Enter a start value: '))
end = int (input('Enter a end value: '))
i = start
while i <= end :
    print(i, end= " ")
    i += 1

#question4:
sayi= int(input("bir sayi girinizi:"))

if sayi %2 ==0:
    print(sayi, "cift sayidir.")
else:
    print(sayi,"tek sayidir.")

#question5: Write a Python program that takes a positive integer input from the user and calculates its factorial. 
number = int(input("Enter a positief integer: "))
if number <= 0 :
    print("Factorial is defined with positief numbers only.")
else :
    fac = 1
    for i in range(1,number+1) :
        fac *= i
    print(f"The factorial of {number} is {fac}.")
#question6:
girdi= int(input("bir sayi giriniz: "))

for i in range(2,int(girdi/2)):
    if (girdi%i==0):
        print('sayiniz asal degildir')  
        break  
else:
    print("Sayiniz asaldir")
    
        
    
#question7:
limit = int(input("Enter the limit: "))
fib_sequence = [0, 1]

while True :
    next_number = fib_sequence[-1] + fib_sequence[-2]
    if next_number > limit :
        break
    fib_sequence.append(next_number)

print(f"Fibonacci sequence up to {limit} is {fib_sequence}")


#question8:
kelime = input("Lutfen bir kelime yazin:")

tersKelime= kelime[::-1]

print(tersKelime)
#question9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

word = input("Enter a word: ")
print(f"{word} is{" not" if word != word[::-1] else ""} a palindrom.")

#question10:
boy=float(input("Boyunuzu giriniz m(Ornek: 1.73)"))
kilo=float(input("Kilonuzu giriniz kg(Ornek: 78)"))

index=kilo/(boy**2)

if index<25:
    print("Zayif")
elif 25<=index<30:
    print("Normal")
elif 30<= index<=40:
    print("Asiri kilolu")
else:
    print("Obez")
#question11:
for i in range(3):
    numbers = input("Enter three numbers: ").split()
    
    numbers = [int(i) for i in numbers]

    largest = float('-inf')
    for i in numbers :
        if i > largest :
            largest = i
    print(f"The largest number of {numbers} is {largest}")
  
#question12:
for ders in range(1, 5):
    print(f"\nDers {ders}:")


    vize=float(input("vize notunuzu giriniz:"))
    final=float(input("final notunuzu giriniz:"))

    ortalama = (vize * 0.4) + (final * 0.6)
    if ortalama >= 50:
        print("successful")
    else:
        print ("Failed")

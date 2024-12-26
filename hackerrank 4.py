#hackerrank 2
n = int(input("ogrenci sayisini giriniz:")) 
studentMarks={}

for _ in range(n):
    data = input("adin ve notlarin:" ).split() 
    name = data[0] 
    notlar = list(map(float, data[1:]))  
    studentMarks[name] = notlar  

student_name = input("adini gir:")  


average = sum(studentMarks[student_name]) / len(studentMarks[student_name])
print(f"{average:.2f}")  

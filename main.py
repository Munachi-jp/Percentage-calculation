# take marks as input from user
print("Enter Marks Obtained in 10 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
french = int(input("french :"))
agric = int(input("agric :"))
PHE = int(input("PHE :"))
CRS = int(input("CRS :"))
CCA = int(input("CCA :"))
civic = int(input("civic :"))
business_studies = int(input("business_studies :"))

# Let's calculate the percentage of marks
sum = math+english+science+french+agric+PHE+CRS+CCA+civic+business_studies
print("sum of math,english,science,french,agric,phe,crs,cca,civic and business_studies")

perc = (sum/1000)*100

print(end="Percentage Mark = ")
print(perc)
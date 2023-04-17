# 1.	Конвертор: от USD към BGN
# Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
# Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.

usd = float(input("How many dollars do you want to convert? "))
bgn = usd * 1.79549
print(bgn)

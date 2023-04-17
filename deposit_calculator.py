# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент.
# Използвайте следната формула: 
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)



deposit_sum = float(input())
depo_in_months = int(input())
year_percent = float(input())

cal_1 = deposit_sum * year_percent
cal_2 = cal_1 / 12
total = deposit_sum + depo_in_months * cal_2
print(total)
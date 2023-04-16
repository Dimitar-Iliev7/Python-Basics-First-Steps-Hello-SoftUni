# Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.

arch_name = input("arch name? ")
amount_projects = int(input("How many projects"))
total = amount_projects * 3

print(f"The architet {arch_name} will need {total} hours to complete {amount_projects} projects")
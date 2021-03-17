input_line = input("Enter the amount of the study benefits: ")
benefits = float(input_line)
new_benefit = (benefits * 1.0117)

second_benefit = (new_benefit * 1.0117)
print("If the index raise is 1.17 percent, the study benefit, \n"
"after a raise, would be", new_benefit, "euros \n"
"and if there was another index raise, the study \n"
"benefits would be as much as", second_benefit, "euros")

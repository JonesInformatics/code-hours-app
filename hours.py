# variable for 
total_hours = 300.5
#today = .5
#new_total = total_hours + today
#print(new_total)


# set varible for total goal
goal = 3000

# set variable for next benchmark
next_benchmark = 500

# mini bench
mini_bench = 325

# mini mini bench
mini_mini_bench =  305

# variable
hours_until_next_benchmark = next_benchmark - total_hours

# variable for hours until next mini benchmark 
a = mini_bench - total_hours

# variable for hours until next benchmark
b = mini_mini_bench - total_hours

print(f"Your goal is to code for {goal} hours. As of today, you have coded for {total_hours} hours.")
print(f"You are just {format(a, '.2f')} hours away from your next mini-bench marks")
print(f"You are just {format(b, '.2f')} hours away from your next super-mini benchmark.")


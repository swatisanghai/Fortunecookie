import random

def generate_fortune():
    #  list of fortune sentences custamizable
    fortunes = [
        "You are destined for greatness.",
        "Adventure awaits just around the corner.",
        "Opportunities will come knocking at your door.",
        "Believe in yourself, and anything is possible.",
        "Your kindness will be rewarded in unexpected ways.",
        "Embrace change, and you will flourish.",
        "Good things come to those who wait.",
        "You will soon get a job."
    ]
    
    # Generate a random fortune
    random_fortune = random.choice(fortunes)
    
    # Generate 4 random numbers between 1 and 99
    random_numbers = [random.randint(1, 99) for _ in range(4)]
    
    # Print the fortune and random numbers
    print("Your fortune: ", random_fortune)
    print("Lucky numbers:", random_numbers)

# Call the function to generate a fortune cookie
generate_fortune()

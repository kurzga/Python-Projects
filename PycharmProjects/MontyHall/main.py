import random
import matplotlib.pyplot as plt


def monty_hall_simulation(num_trials):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        initial_choice = random.randint(0, 2)

        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
        monty_opens = random.choice(remaining_doors)

        remaining_doors = [i for i in range(3) if i != monty_opens and i != initial_choice]
        final_choice_stay = initial_choice
        final_choice_switch = remaining_doors[0]

        if doors[final_choice_stay] == 'car':
            stay_wins += 1
        if doors[final_choice_switch] == 'car':
            switch_wins += 1

    stay_win_percentage = (stay_wins / num_trials) * 100
    switch_win_percentage = (switch_wins / num_trials) * 100

    print(f"Stay strategy wins: {stay_wins} ({stay_win_percentage:.2f}%)")
    print(f"Switch strategy wins: {switch_wins} ({switch_win_percentage:.2f}%)")

    # Plot the results
    labels = ['Stay', 'Switch']
    wins = [stay_wins, switch_wins]
    percentages = [stay_win_percentage, switch_win_percentage]

    plt.bar(labels, wins, color=['blue', 'green'])
    plt.ylabel('Number of Wins')
    plt.title('Monty Hall Simulation Results')

    # Display the percentage values on top of the bars
    for i, value in enumerate(wins):
        plt.text(i, value + 50, f'{percentages[i]:.2f}%', ha='center')

    plt.show()


# Run the simulation with a specified number of trials
num_trials = 10000
monty_hall_simulation(num_trials)

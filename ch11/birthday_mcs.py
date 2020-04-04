import random


trials = 20_000
big_months = [1, 3, 5, 7, 8, 10, 12]


def bday_loop(num_people):
    bday_list = []
    for people in range(num_people):
        month = random.randint(1, 12)
        if month == 2:
            day = random.randint(1, 29)
        elif month in big_months:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)
        birthday = f"{month}-{day}"
        bday_list.append(birthday)
    return(bday_list)


def run_trials(num_people):
    same_bday = 0
    for trial in range(trials):
        bday_list = bday_loop(num_people)
        bday_set = set(bday_list)
        if len(bday_list) != len(bday_set):
            same_bday += 1
    prob = same_bday / trials * 100
    print(f"{trials} trials ran; {num_people} in room; probability of same"
          f" birthday is {prob:.2f}%.")


run_trials(5)
run_trials(10)
run_trials(20)
run_trials(23)
run_trials(70)
run_trials(71)
run_trials(72)

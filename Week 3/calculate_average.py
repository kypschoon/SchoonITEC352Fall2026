#This program takes scores entered by the user
#and calculates their average score


#this function will calculate the average and display it to the user
def display_average(scores):
    if not scores:
        print("There are no scores to average")
    else:
        total = 0
        num_of_scores = 0
        for score in scores:
            total = total + score
            num_of_scores = num_of_scores + 1
        average = total / num_of_scores
        print("The average score is ", average)

def main():
    scores = []
    while True:
        try:
            score = float(input("Please enter a score, type 999 when done: "))
            if score == 999:
                display_average(scores)
                break
            if score < 0 or score > 100:
                print("Please enter a valid score between 0 and 100")
            else:
                scores.append(score)
        except ValueError:
                print("Please enter a valid number")


if __name__ == "__main__":
    main()
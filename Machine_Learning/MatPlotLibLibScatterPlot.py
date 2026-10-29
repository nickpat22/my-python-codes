import matplotlib.pyplot as plt

def main():
    study_hours = [1,2,3,4,5,6]
    marks = [35,42,50,62,72,85]

    plt.scatter(
        study_hours,
        marks,
        s= 100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )

    plt.title("Marvellous")
    plt.xlabel("Study Hours")
    plt.ylabel("Obtained Marks")

    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ ==  "__main__":
    main()
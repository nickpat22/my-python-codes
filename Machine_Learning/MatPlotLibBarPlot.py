import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(
        language,
        students,
        width= 0.6,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.8,
        label = "Students"
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.show()
if __name__ ==  "__main__":
    main()
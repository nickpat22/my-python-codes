import matplotlib.pyplot as plt

def main():
    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]
    plt.hist(
        marks,                  #continious Data
        bins = 5,               #no of groups
        edgecolor = "black",    #border color
        alpha = 0.8,            #transperency
        rwidth= 0.9,

    )

    plt.title("Marvellous Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ ==  "__main__":
    main()
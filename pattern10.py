def pattern10(N):
    # Outer loop for number of rows.
    for i in range(1, 2 * N):

        # stars would be equal to the row number until the first half
        stars = i
        # for the second half of the rotated triangle.
        if i > N:
            stars = 2 * N - i 
        # for printing the stars in each row.
        for j in range(stars):
            print("*", end="")
        # As soon as the stars for each iteration are printed, we move to the
        # next row and give a line break otherwise all stars
        # would get printed in 1 line.
        print()

if __name__ == "__main__":
    # Here, we have taken the value of N as 5.
    # We can also take input from the user.
    N = 5
    pattern10(N)

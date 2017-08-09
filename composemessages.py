
def main():
    #define a variable cnt to keep the line number of example.txt
    cnt = 0
    #define a for loop to iterate the lines in the example.txt file
    for line in open("./example.txt"):
        #line is a variable containing the string content on each line
        #for the first loop, the line = "Steven stevenjiang@hiretual.com"
        elements = line.split(" ")
        #split is a built-in function to split a string by character of space
        # eles now is an array contain two sub-strings "Steven" and "stevenjiang@hiretual.com"
        name = elements[0]
        # eles has two substrings so that we get the first one (index is 0) and the second one (index is 1)
        email = elements[1]
        # for the first loop, cnt = 1; for the second loop, the cnt will be 2 since we +1 for each loop
        cnt = cnt + 1
        # if-else is a condition statement of python
        if cnt == 1:
            order = "first"
        elif cnt == 2:
            order = "second"
        else:
            order = "three"
        print("Hi " + name + ", this is the " + order + " message to " + email)

if __name__ == "__main__":
    main()
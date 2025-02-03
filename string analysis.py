

def fun():
            
        u = input("Please enter a string: ")

        print("You entered:", u)


        num_char = len(u)


        words = len(u.split())

        if "python" in u:
            print("Done, the word 'python' is present.")

        v = 0


        for char in u:
            if char in 'aeiou':
                v += 1

        print("Number of characters:", num_char)
        print("Number of words:", words)
        print("Number of vowels:", v)


fun()        
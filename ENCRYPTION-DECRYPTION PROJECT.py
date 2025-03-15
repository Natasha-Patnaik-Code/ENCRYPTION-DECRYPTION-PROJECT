import pickle
import csv

# MAIN CONVERSION UNIT
def strg(choice, string):
    if choice == 1:
        encrypted = ''
        for i in string:
            position = ord(i)
            newposition = position + 5
            encrypted += chr(newposition)
        return encrypted
    elif choice == 2:
        decrypted = ''
        for i in string:
            position = ord(i)
            newposition = position - 5
            decrypted += chr(newposition)
        return decrypted


# INTRODUCTION
print('HELLO! HOW CAN I HELP YOU?')

# CHOICES
ans = 'y'
while ans == 'y':
    print('\n1. HI! PLEASE ENCRYPT MY DATA.')
    print('2. HI! PLEASE DECRYPT MY DATA.')
    choice = int(input('YOUR CHOICE NO: '))
    print("SURE, I'M ON IT! WHAT KIND OF FILE ARE WE DEALING WITH?")
    print("1. IT'S JUST A SIMPLE PARAGRAPH/SENTENCE...")
    print("2. IT'S A TEXT FILE...")
    print("3. IT'S A BINARY FILE...")
    print("4. IT'S A CSV FILE...")
    print("5. IT'S AN SQL DATABASE...")
    type = int(input('YOUR CHOICE NO: '))
    print("EASY PEASY!!! LET'S GET TO IT THEN!")

    # STRING CONVERSION
    if type == 1:
        string = input('ENTER THE STRING: ')
        incase = strg(choice, string)
        print(incase)
        ans = input('\nTHERE YOU GO!! WANT TO CONTINUE? y/n: ')

    # TEXT FILE CONVERSION
    elif type == 2:
        file = input('ENTER FILE NAME WITH EXTENSION: ')
        transfer = input('DO YOU WANT TO TRANSFER THIS FILE TO ANOTHER ONE OR NOT? y/n: ')
        if transfer == 'y':
            newfile = input('ENTER THE NAME OF THE FILE YOU WANT TO TRANSFER THE DATA TO WITH EXTENSION: ')
            with open(file) as f:
                data = f.readlines()
                newdata = []
                for line in data:
                    easy = line.split()
                    for word in easy:
                        if word.find('\n') > -1:
                            text = word.strip()
                            text = strg(choice, text)
                            newword += text + '\n'
                            newdata.append(newword)
                        else:
                            newword = strg(choice, word)
                            newdata.append(newword)
            with open(newfile, 'a') as f:
                f.writelines(newdata)
        else:
            with open(file) as f:
                data = f.readlines()
                newdata = ''
                for line in data:
                    easy = line.split()
                    for word in easy:
                        if word.find('\n') > -1:
                            text = word.strip()
                            text = strg(choice, text)
                            newdata += text
                        else:
                            text = strg(choice, word)
                            newdata += text
            print(newdata)
        ans = input('\nTHERE YOU GO!! WANT TO CONTINUE? y/n: ')

    # BINARY FILE CONVERSION
    elif type == 3:
        file = input('ENTER FILE NAME WITH EXTENSION: ')
        transfer = input('DO YOU WANT TO TRANSFER THIS FILE TO ANOTHER ONE OR NOT? y/n: ')
        if transfer == 'y':
            newfile = input('ENTER THE NAME OF THE FILE YOU WANT TO TRANSFER THE DATA TO WITH EXTENSION: ')
            f = open(file, 'rb')
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
            newdata = []
            for record in data:
                newrecord = []
                for index in range(0, len(record)):
                    newelement = strg(choice, record[index])
                    newrecord.append(newelement)
                newdata.append(newrecord)
            f.close()
            with open(newfile, 'ab') as f:
                pickle.dump(newdata, f)
        else:
            with open(file, 'rb') as f:
                while True:
                    try:
                        data = pickle.load(f)
                    except EOFError:
                        break
                newdata = []
                for record in data:
                    newrecord = []
                    for index in range(0, len(record)):
                        newelement = strg(choice, record[index])
                        newrecord.append(newelement)
                    newdata.append(newrecord)
            f.close()
            for record in newdata:
                print(record)
        ans = input('\nTHERE YOU GO!! WANT TO CONTINUE? y/n: ')

        # CSV FILE CONVERSION
    elif type == 4:
        file = input('ENTER FILE NAME WITH EXTENSION: ')
        transfer = input('DO YOU WANT TO TRANSFER THIS FILE TO ANOTHER ONE OR NOT? y/n: ')
        if transfer == 'y':
            newfile = input('ENTER THE NAME OF THE FILE YOU WANT TO TRANSFER THE DATA TO WITH EXTENSION: ')
            with open(file) as f:
                reader = csv.reader(f, delimiter=',')
                newdata = []
                for record in reader:
                    newrecord = []
                    for element in record:
                        newelement = strg(choice, element)
                        newrecord.append(newelement)
                    newdata.append(newrecord)
            with open(newfile, 'a', newline='') as f:
                writer = csv.writer(f)
                for i in newdata:
                    writer.writerow(i)
        else:
            with open(file) as f:
                reader = csv.reader(f, delimiter=',')
                newdata = []
                for record in reader:
                    newrecord = []
                    for element in record:
                        newelement = strg(choice, element)
                        newrecord.append(newelement)
                    newdata.append(newrecord)
            for i in newdata:
                print(i)
        ans = input('\nTHERE YOU GO!! WANT TO CONTINUE? y/n: ')
    
    else:
        print("SORRY. I CAN'T HELP WITH THAT.")


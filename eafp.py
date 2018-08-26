try:
    f = open('text1.txt')
    if f.name == "text1.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()

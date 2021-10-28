def swipeFileData():
    with open('sampleText1.txt', 'r') as a:
        data_a = a.read()
    
    with open('sampleText2.txt', 'r') as a:
        data_b = a.read()

    with open('sampleText1.txt', 'w') as a:
        a.write(data_b)
    
    with open('sampleText2.txt', 'w') as a:
        a.write(data_a)

swipeFileData()
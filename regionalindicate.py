import pyperclip
def doit():
    inputlist=(str(input('Enter word here ')))
    outputlist=""
    length=len(inputlist)
    for x in range(length):
        y=inputlist[x]
        if y==" ":
            outputlist+=("     ")
        elif y.isupper:
            y=y.lower()
            outputlist+=(':regional_indicator_'+y+": ")    
        else:
            outputlist+=(':regional_indicator_'+y+": ")
        
    print('Output copied to clipboard')
    pyperclip.copy(outputlist)
    doit()

doit()

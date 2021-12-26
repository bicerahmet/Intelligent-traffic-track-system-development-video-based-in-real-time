def filterTheLicencePlate(text):
    textFiltered = ""
    for char in text:
        if((ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90)):
            textFiltered += char
    return(textFiltered)
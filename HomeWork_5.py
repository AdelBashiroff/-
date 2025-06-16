from string import punctuation


# Task 1

class StringUtils:
    type = "StringUtils"
    count = 0

    @staticmethod
    def stringCompress(string):
        StringUtils.count += 1

        compressedString = []
        count = 1
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                count += 1
            else:
                compressedString.append(string[i - 1] + f"{count}")
                count = 1
        compressedString.append(string[-1] + f"{count}")
        return "".join(compressedString)

    @staticmethod
    def changeChar(string, char):
        StringUtils.count += 1

        vowels = "eyuioaEYUIOA"
        return "".join(["g" if i in vowels else i for i in string])

    @staticmethod
    def frequencyOfWords(string):
        StringUtils.count += 1

        stringWithoutPunc = "".join([i.lower() for i in string if i not in punctuation])
        freqDict = {word: stringWithoutPunc.split().count(word) for word in stringWithoutPunc.split()}
        return freqDict

    @staticmethod
    def correctWords(string):
        StringUtils.count += 1

        correctForms = {"срочня": "срочно"}
        return correctForms[string]

    @staticmethod
    def joinStrings(stringList, separator):
        StringUtils.count += 1

        return separator.join(stringList)

    @staticmethod
    def findWordInd(string, word):
        StringUtils.count += 1

        return string.split().index(word) if word in string.split() else 0

    @staticmethod
    def areAnagrams(firstString, secondString):
        StringUtils.count += 1

        return sorted(firstString) == sorted(secondString)

    @staticmethod
    def countSyllables(string, syll="ab"):
        StringUtils.count += 1

        return string.lower().count(syll)

    @staticmethod
    def extractNumbers(string):
        StringUtils.count += 1

        numbers = []
        currNumber = ""
        for char in string:
            if char.isdigit():
                currNumber += char
            else:
                if currNumber:
                    numbers.append(int(currNumber))
                    currNumber = ""
        if currNumber:
            numbers.append(int(currNumber))
        return numbers

    @staticmethod
    def reversedString(string):
        StringUtils.count += 1

        return string[::-1]

    @staticmethod
    def uniqSubstrings(stringList, length):
        StringUtils.count += 1

        res = []
        for string in stringList:
            uniqSubs = set()
            for i in range(len(string) - length + 1):
                substring = string[i:i + length]
                uniqSubs.add(substring)
            res.append(tuple(uniqSubs))
        return res

    @staticmethod
    def uniqWords(text, stopWords):
        StringUtils.count += 1

        for i in punctuation:
            text = text.replace(i, "")
        words = set()
        for i in text.lower().split():
            if i not in punctuation and i not in stopWords:
                words.add(i)
        return words

    def info():
        return f"Это класс StringUtils. Кол-во созданных экземпрялов: {StringUtils.count}"


print(StringUtils.stringCompress("aaabbbcccaaa"))
print(StringUtils.frequencyOfWords("Hello world! Hello everyone."))
print(StringUtils.correctWords("срочня"))
print(StringUtils.joinStrings(["weq", "eqwdsa", "safaw"], "a"))
print(StringUtils.findWordInd("Hello my lovely friend", "lovely"))
print(StringUtils.areAnagrams("qwerty", "ytqwre"))
print(StringUtils.countSyllables("abr abramsky abababa weqeqwe dsqsdabdasd"))
print(StringUtils.extractNumbers("There are 2, 5 and 10"))
print(StringUtils.reversedString("qwerty"))
print(StringUtils.uniqSubstrings(["sdqwd", "dqssd", "qweq"], 2))
print(StringUtils.uniqWords("sdqqeq. dsadw and dqw1daw!", ["and", "in", "this"]))
print(StringUtils.info())
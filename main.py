from re import A
import AO3
import math
import getpass
from collections import Counter



use_session = input("Login? (y/n): ")

if use_session.lower() == "y":

    username = input("Username: ")
    password = getpass.getpass()
    session = AO3.Session(username, password)

    
    userFandom = input("Enter Fandom Tag: ")
    sampleSize = input("Enter Sample Size: ")
    sampleSize = int(sampleSize)
    wordCount = input("Enter Minimum Word Count: ")
    language = input("Enter Language: ")

    crossovers = input("Include crossovers? (y/n): ")

    if crossovers.lower() == "y":
        search = AO3.Search(word_count=">" + wordCount, fandoms=userFandom, sort_column="kudos_count", session=session, language=language)

    else:
        search = AO3.Search(word_count=">" + wordCount, fandoms=userFandom, crossovers=False, sort_column="kudos_count", session=session, language=language)

else:

    userFandom = input("Enter Fandom Tag: ")
    sampleSize = input("Enter Sample Size: ")
    sampleSize = int(sampleSize)
    wordCount = input("Enter Minimum Word Count: ")
    language = input("Enter Language: ")

    crossovers = input("Include crossovers? (y/n): ")

    if crossovers.lower() == "y":
        search = AO3.Search(word_count=">" + wordCount, fandoms=userFandom, sort_column="kudos_count", language=language)

    else:
        search = AO3.Search(word_count=">" + wordCount, fandoms=userFandom, crossovers=False, sort_column="kudos_count", language=language)
        


required_pages = math.ceil(sampleSize / 20)

search.update()
print(search.total_results)



bigstring = ""

for page in range(required_pages):

    search.page = page
    search.update

    for index, result in enumerate(search.results):


        if index == sampleSize:
            break

        result.reload()

        for chapter in result.chapters:
            bigstring += chapter.text

    sampleSize -= 20

bigstring = bigstring.lower().replace('\n', '').replace(' ', '')
category = Counter(bigstring)
userinput = ""
while userinput != "exit":
    userinput = input("Enter minimum character threshold to display results, or type 'exit' to exit: ")

    try:
        int(userinput)
        is_int = True

    except ValueError:
        is_int = False

    if is_int == True:
        for value, count in sorted(category.items()):
            if count >= int(userinput):
               print (value, count)

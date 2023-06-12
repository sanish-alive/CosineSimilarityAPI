import math

def bioVector(personOneBio, personTwoBio):
    stopWords = [
        "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among",
        "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can",
        "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every",
        "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his",
        "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let",
        "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor",
        "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather",
        "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the",
        "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas",
        "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who",
        "whom", "why", "will", "with", "would", "yet", "you", "your", "."
    ]

    personOneBioList = personOneBio.split()
    personTwoBioList = personTwoBio.split()

    personOneFilteredWords = [word for word in personOneBioList if word not in stopWords]   
    personTwoFilteredWords = [word for word in personTwoBioList if word not in stopWords]

    personsWordUnion = list(set(personOneFilteredWords) | set(personTwoFilteredWords))

    personOneBioVector = []; personTwoBioVector = []

    for w in personsWordUnion:
        personOneBioVector.append(1) if w in personOneBioList else personOneBioVector.append(0)
        personTwoBioVector.append(1) if w in personTwoBioList else personTwoBioVector.append(0)
    
    return personOneBioVector, personTwoBioVector

def createVector(personOne, personTwo):
    personOneVector = []; personTwoVector = []
    
    if(personOne['lastname'] == personTwo['lastname']):
        personOneVector.append(1)
        personTwoVector.append(1)
    else:
        personOneVector.append(0)
        personTwoVector.append(0)

    if(abs(personOne['age'] - personTwo['age']) < 6):
        personOneVector.append(1)
        personTwoVector.append(1)
    else:
        personOneVector.append(0)
        personTwoVector.append(0)

    if(personOne['gender'] == 'male' and personOne['height'] > personTwo['height']):
        personOneVector.append(1)
        personTwoVector.append(1)
    else:
        personOneVector.append(0)
        personTwoVector.append(0)

    personOneBioVector, personTwoBioVector = bioVector(personOne['bio'], personTwo['bio'])

    personOneVector += personOneBioVector
    personTwoVector += personTwoBioVector

    return personOneVector, personTwoVector

def calculateCosineSimilarity(personOne, personTwo):
    personOneVector, personTwoVector = createVector(personOne, personTwo)
    dotProduct = sum(x*y for x, y in zip(personOneVector, personTwoVector))
    personOneMagnitude = math.sqrt(sum(x**2 for x in personOneVector))
    personTwoMagnitude = math.sqrt(sum(x**2 for x in personTwoVector))

    similarity = dotProduct / (personOneMagnitude * personTwoMagnitude)

    return similarity

if __name__ == "__main__":
    person1 = {
        'lastname': 'smith',
        'age': 30,
        'height': 180,
        'gender': 'male',
        'bio': 'i am a software engineer with a passion for coding'
    }

    person2 = {
        'lastname': 'smith',
        'age': 35,
        'height': 175,
        'gender': 'female',
        'bio': 'i work as a date scientist and enjoy analyzing complex data'
    }

    cosineSimilarity = calculateCosineSimilarity(person1, person2)
    print(cosineSimilarity)

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.chat.util import Chat, reflections
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample question-answer pairs
pairs = [
    [
        r"How can I avail internet reservation facility through credit cards?",
        ['Recently internet reservation facility has started on Indian Railways. The web site http://www.irctc.co.in is operational, wherein you can get the railway reservation done through Credit Cards.']
    ],
    [
        r'Why are PNR and reservation availability queries not available after certain timings at night?',
        ['The online PNR and seat availability queries are fetched from the computerized reservation applications. These applications are shut down daily from 2330 to 0030 IST.']
    ],
    [
        r'How can I avail the enquiries, through SMS on mobile phones?',
        ['Now all the enquiries offered on the web site www.indianrail.gov.in are available on your mobile phone through SMS facility.']
    ],
    [
        r'Why do sometimes the fonts, colors schemes and java scripts behave differently in some browser or browsers?',
        ['This web site is best viewed with Microsoft Internet Explorer 6.0 and above.']
    ],
    [
        r'Where can I get the latest arrival and departure timings of trains, when they get delayed?',
        ['The latest arrival and departure timings of delayed trains, along with diverted routes, will be made available shortly on this website.']
    ],
    [
        r'Where can I lodge complaint against any type of grievances in the Trains, Platforms, officials for problems on this web site and give suggestions?',
        ['The complaint software is under development. You can give feedback on the Feedback & Suggestions page.']
    ],
]

# Preprocessing tools
lemmatiser = WordNetLemmatizer()

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def preprocessing(sent):
    rem_words = ['get', 'avail', 'who' , 'where', 'how' , 'what', 'why' , 'when', 'I', 'can']
    for p in list(punctuation):
        sent = sent.replace(p, '')
    sent = sent.lower().split()
    stop_words = set(stopwords.words('english'))
    sent = [i for i in sent if i not in stop_words]
    sent = [i for i in sent if i not in rem_words]
    sent = [lemmatiser.lemmatize(item, pos="v") for item in sent]
    return unique(sent)

def tellme_bot():
    while True:
        response = input("Tell Me. [q to quit]> ")
        if response.lower() == 'q':
            break
        chosen = len(pairs)
        matches = 0
        list_response = preprocessing(response)
        for i, pair in enumerate(pairs):
            loc_matches = 0
            text = pair[0] + "  ".join(pair[1])
            list_pair = preprocessing(text)
            for word in list_pair:
                if word in list_response:
                    loc_matches += 1
            if loc_matches > matches:
                chosen = i
                matches = loc_matches
        if chosen < len(pairs):
            print(pairs[chosen][1][0])
        else:
            print("Unable to answer this question.")
        break

# Run the bot
tellme_bot()




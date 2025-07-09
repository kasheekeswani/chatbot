import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Question-answer pairs
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

lemmatiser = WordNetLemmatizer()

def unique(list1):
    return list(dict.fromkeys(list1))

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

def get_bot_response(user_input):
    chosen = len(pairs)
    matches = 0
    list_response = preprocessing(user_input)
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
        return pairs[chosen][1][0]
    else:
        return "🤖 Sorry, I couldn't understand your question. Try rephrasing it."

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Indian Railways FAQ Bot", page_icon="🚂")

st.markdown("""
    <h2 style="text-align:center;">🚂 Indian Railways FAQ Chatbot</h2>
    <p style="text-align:center; color:gray;">Ask me anything about Indian Railways services!</p>
""", unsafe_allow_html=True)

with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="e.g. Can I reserve tickets online?")
    submitted = st.form_submit_button("Ask")
    if submitted and user_input.strip() != "":
        bot_reply = get_bot_response(user_input)
        st.markdown(f"""
            <div style="background-color:#f1f3f6;padding:1rem;border-radius:10px;">
                <b>You:</b> {user_input}<br><br>
                <b>Bot:</b> {bot_reply}
            </div>
        """, unsafe_allow_html=True)




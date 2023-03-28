import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# ID = input("Enter your user ID : ")
# password = input("Enter your ID password : ")

# if ID=='sam' and password=='Sam@123':
    # Create the application and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Text Sentiment Analysis')
window.setGeometry(200, 200, 500, 400)

# Create a label
label = QLabel('Enter your text:', window)

# Create a big text field
text_edit = QTextEdit(window)

# Create two buttons
button1 = QPushButton('Clear Text', window)
button2 = QPushButton('Analyse Text', window)
button3 = QPushButton('Save and Show Chart', window)

# Create a label to display the variable value
var_label = QLabel(window)

# Set up the layout
hbox = QHBoxLayout()
hbox.addWidget(button2)
hbox.addWidget(button3)
hbox.addWidget(button1)

vbox = QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(text_edit)
vbox.addLayout(hbox)
vbox.addWidget(var_label)

window.setLayout(vbox)

# Define a function to handle the submit button click
def submit_text():
    text = text_edit.toPlainText()
    lower_text = text.lower()
    
    cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))
    tokenize_word = word_tokenize(cleaned_text,'english')

    final_words = []

    for word in tokenize_word:
        if word not in stopwords.words('english'):
            final_words.append(word)

    emotion_list = []
    with open("emotions.txt",'r') as file:
        for line in file:
            clear_line = line.strip().replace(",", '').replace("'",'').lower() # Added strip and lower to remove whitespace and convert to lowercase
            word, emotion = clear_line.split(":")
            if word.strip() in final_words: # Added strip to remove whitespace
                emotion_list.append(emotion.strip()) # Added strip to remove whitespace
            else:
                pass

    print(f"Number of words in final_words: {len(final_words)}")
    print(f"Number of words found: {len(emotion_list)}")

    var_value = ''
    def sentiment_analyse(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        print(score)
        neg = score['neg']
        pos = score['pos']
        if neg > pos:
            print("Negative Sentiment 😠")
            
            var_value = 'Negative Sentiment 😠'  # example variable
            var_label.setText(f'Analyzer Result:  <font color="red">{var_value}</font>')
        elif neg < pos:
            print("Positive Sentiment 😊")
            var_value = 'Positive Sentiment 😊'  # example variable
            var_label.setText(f'Analyzer Result:  <font color="green">{var_value}</font>')
        else:
            print('Natural Vibe 😶')
            var_value = 'Natural Sentiment 😶'  # example variable
            var_label.setText(f'Analyzer Result:  <font color="black">{var_value}</font>')
    sentiment_analyse(cleaned_text)


def show_save():
    text = text_edit.toPlainText()
    lower_text = text.lower()
    
    cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))
    tokenize_word = word_tokenize(cleaned_text,'english')

    final_words = []

    for word in tokenize_word:
        if word not in stopwords.words('english'):
            final_words.append(word)

    emotion_list = []
    with open("emotions.txt",'r') as file:
        for line in file:
            clear_line = line.strip().replace(",", '').replace("'",'').lower() # Added strip and lower to remove whitespace and convert to lowercase
            word, emotion = clear_line.split(":")
            if word.strip() in final_words: # Added strip to remove whitespace
                emotion_list.append(emotion.strip()) # Added strip to remove whitespace
            else:
                pass

    # print(f"Number of words in final_words: {len(final_words)}")
    # print(f"Number of words found: {len(emotion_list)}")

    # var_value = ''
    def sentiment_analyse(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        print(score)
        neg = score['neg']
        pos = score['pos']
        global var_value
        if neg > pos:
            # print("Negative Sentiment")
            var_value = 'Negative Sentiment'  # example variable
            # var_label.setText(f'Analyzer Result:  {var_value}')
        elif neg < pos:
            # print("Positive Sentiment")
            var_value = 'Positive Sentiment'  # example variable
            # var_label.setText(f'Analyzer Result:  {var_value}')
        else:
            # print('Natural Vibe')
            var_value = 'Natural Sentiment'  # example variable
            # var_label.setText(f'Analyzer Result:  {var_value}')
    sentiment_analyse(cleaned_text)

    w = Counter(emotion_list)
    
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(),w.values())
    fig.autofmt_xdate()
    plt.savefig(f"{var_value}.png")
    plt.show()
    
button1.clicked.connect(lambda: text_edit.clear())
button2.clicked.connect(submit_text)
button3.clicked.connect(show_save)


# Show the window and run the application
window.show()
sys.exit(app.exec_())

# else:
#     print('Wrong crediantials pls try again.. ')
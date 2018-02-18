from flask import Flask
from json import load as json_load

app = Flask(__name__)

#Absolute words stuff
absolute_words_file_name = 'absWords.json'
absolute_words_file = open(absolute_words_file_name)
absolute_words_json = json_load(absolute_words_file)
absolute_words = set(absolute_words_json['data'])

@app.route("/words")
def root():
    return ", ".join(absolute_words)

if __name__ == '__main__':
    app.run()

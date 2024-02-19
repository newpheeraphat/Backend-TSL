import numpy as np
import pickle
import pandas as pd
import requests
import re
import metadata_parser
import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
from pythainlp.corpus.common import thai_stopwords
from pythainlp.util import normalize
from pythainlp import word_tokenize
from pythainlp.corpus.common import thai_stopwords

os.environ["TOKENIZERS_PARALLELISM"] = "false"
class Classification: 
  
  def __init__(self) -> None: 
    self.loaded_model = pickle.load(open('/Users/pheeraphatprisan/Desktop/Sourcetree/Backend-TSL/model/trained_model.sav', 'rb'))
    self.emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                            "]+", flags = re.UNICODE)
    self.punctuation_list = [
        "!",     # Exclamation mark
        "\"",    # Double quotes
        "#",     # Hash
        "$",     # Dollar sign
        "%",     # Percent sign
        "&",     # Ampersand
        "'",     # Single quote
        "(",     # Open parenthesis
        ")",     # Close parenthesis
        "*",     # Asterisk
        "+",     # Plus sign
        ",",     # Comma
        "-",     # Hyphen
        ".",     # Period (or full stop)
        "/",     # Forward slash
        ":",     # Colon
        ";",     # Semi-colon
        "<",     # Less than sign
        "=",     # Equal sign
        ">",     # Greater than sign
        "?",     # Question mark
        "@",     # At sign
        "[",     # Open bracket
        "\\",    # Backslash
        "]",     # Close bracket
        "^",     # Caret
        "_",     # Underscore
        "`",     # Grave accent
        "{",     # Open brace
        "|",     # Vertical bar
        "}",     # Close brace
        "~",     # Tilde
        "…",     # Ellipsis
        "¡",     # Inverted exclamation mark (used in Spanish)
        "¿",     # Inverted question mark (used in Spanish)
        "«",     # Left-pointing double angle quotation mark
        "»"      # Right-pointing double angle quotation mark
    ]
    self.thai_stopwords = list(thai_stopwords())
    self.thai_stopwords.append("nan")
    self.thai_stopwords.append("-")
    self.thai_stopwords.append("_")
    self.thai_stopwords.append("")
    self.thai_stopwords.append(" ")
  
  def check_fake_website_percentage(self, text, obj_stores):
    try:
      df = pd.read_csv('/Users/pheeraphatprisan/Desktop/Sourcetree/Backend-TSL/dataset/real_website_database.csv')
      sentences  = df['web_text'].tolist()
      model_name = "all-MiniLM-L6-v2"
      model = SentenceTransformer(model_name)
      sentence_vecs = model.encode(sentences)
      sentence_vecs_pred = model.encode(text)
      value = cosine_similarity([sentence_vecs_pred],sentence_vecs)
      
      max_similarity_index = np.argmax(value)  
      max_similarity_value = value[0, max_similarity_index] 
      most_similar_sentence_url = df['web_url'][max_similarity_index]
      fake_website_percentage = int(float(max_similarity_value) * 100)
      
      if fake_website_percentage > 90:
          obj_stores['fake'] = fake_website_percentage
          obj_stores['real_link'] = most_similar_sentence_url
          return obj_stores
      else:
          obj_stores['fake'] = fake_website_percentage
          return obj_stores
    except Exception as e: 
      print(f"Failed to scan file in real website database: {e}")
      return None

  def softmax(self, logits):
    try:
      logits = logits - np.max(logits, axis=1, keepdims=True)
      e_logits = np.exp(logits)
      return e_logits / e_logits.sum(axis=1, keepdims=True)
    except Exception as e: 
      print(f"Failed occurred when calculate softmax probability: {e}")
      return None

  def verify_website(self, df):
    try:
      obj = {}
      index = {0: 'other', 1: 'gambling', 2: 'scam'}
      pred = df['cleaned_text'][0]
      all_text_pred = df['detail'][0]
      predictions, raw_outputs = self.loaded_model.predict(pred)
      probabilities = self.softmax(raw_outputs)
      
      for idx, prob in enumerate(probabilities[0]):
          # print(f"Probability of class {idx}: {prob}")
          obj[index[idx]] = int(round(prob*100))
          
      probabilities_fake_website = self.check_fake_website_percentage(all_text_pred, obj)
      return probabilities_fake_website
    except Exception as e: 
      print(f"Failed to veryfy the website: {e}")
      return None
  
  def preprocess_clean_text(self, text):
    try:
      text = re.sub(r'<[^<>]*>', '', text)
      text = re.sub('\r+', ' ', text)
      text = re.sub('\n+',' ', text)
      text = re.sub('\t+',' ', text)
      text = self.emoji_pattern.sub("", text)
      text = re.sub("#[a-zA-Za-๙0-9_]+", "", text)
      text = re.sub("5+\+|5{3, }", "555", text)
      text = "".join(u for u in text if u not in self.punctuation_list)
      text = normalize(text)
      text = word_tokenize(text)
      text = " ".join(word for word in text)
      text = [word for word in text.split() if word.lower() not in self.thai_stopwords]
      return text
    except Exception as e:
        print(f"Failed to preprocess clean text: {e}")
        return None

  def get_all_text_from_url(self, url):
    try:
      response = requests.get(url)
      if response.status_code == 200:
          soup = BeautifulSoup(response.content, 'html.parser')
          return ' '.join(soup.get_text().split())
      else:
          return f"Failed to retrieve the webpage. Status code: {response.status_code}"
    except Exception as e: 
      print(f"Failed to retrieve the webpage: {e}")
      return None
  
  def extract_data_from_url(self, url):
    try:
      if not url: 
          return {}
        
      if not (url.startswith("http://") or url.startswith("https://")):  # Check if the URL has the proper scheme
          raise ValueError("Please enter a valid URL starting with http:// or https://")
        
      obj = {}
      page = metadata_parser.MetadataParser(url)
      obj["url"] = url
      obj["title"] = page.get_metadatas('title')
      obj['description'] = page.get_metadatas('description')
      obj['keyword'] = page.get_metadatas('keywords')
      obj['detail'] = self.get_all_text_from_url(url)
      return obj
    except Exception as e:
      print(f"Failed to extract data from url: {e}")
      return None
  
  def convert_to_dataframe(self, obj):
    try:
        df = pd.DataFrame(obj)
        expected_columns = ['url', 'title', 'description', 'keyword', 'detail']
        df = df[expected_columns]
        df = df.fillna('')
        df['original'] = df['title'] + ' ' + df['description'] + ' ' + df['keyword'] + ' ' + df['detail']
        df['clean'] = df['original'].apply(lambda x: self.preprocess_clean_text(x))
        df['cleaned_text'] = df['clean'].apply(lambda x: " ".join(x))
        return df
    except Exception as e:
        print(f"Fail to convert to dataframe: {e}")
        return None  
  

  
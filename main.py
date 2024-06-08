from bs4 import BeautifulSoup
import requests
from googletrans import Translator
translator = Translator()
result = translator.translate("dog", "ru")
print(result.text)


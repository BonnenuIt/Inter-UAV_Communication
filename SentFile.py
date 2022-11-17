import pypinyin
import pdfplumber

def LongWordsFunc(file_path = './共产党宣言.pdf'):
    words = ''
    LongWords = ''
    with pdfplumber.open(file_path) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            txt = page.extract_text()
            words = words + txt
        pin_list = pypinyin.lazy_pinyin(words, errors='ignore')
        LongWords = ''
        for i in pin_list:
            LongWords += ''.join(i)
    return LongWords, len(LongWords)
LongWords, LongWords_len = LongWordsFunc()
LongWords = LongWords[0:1024]

for i in range(1):
    with open("SentFile.txt", "a") as SentFile:
        SentFile.write(LongWords)

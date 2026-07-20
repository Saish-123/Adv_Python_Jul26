def count_characters(text):
    freq={}

    text=text.lower()
    for ch in text:
        if ch.isalpha():
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
    result={}

    for ch in sorted(freq):
        result[ch]=freq[ch]
    return result

#Test
text="Hello World 123!!"
print(count_characters(text))
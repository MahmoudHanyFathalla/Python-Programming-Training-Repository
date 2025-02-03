from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def rate_niceness(text):
    # Initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Get sentiment scores for the text
    sentiment_scores = analyzer.polarity_scores(text)

    # Extract the compound score (normalized sentiment score)
    compound_score = sentiment_scores['compound']

    # Normalize the compound score to a scale of 0 to 100
    niceness_score = (compound_score + 1) * 50  # Adjust to a 0-100 scale

    # Ensure the niceness score is within the 0-100 range
    niceness_score = max(0, min(100, niceness_score))

    return niceness_score

# Input text
input_text = input("Enter the text you want to rate: ")

# Get the niceness score
niceness_score = rate_niceness(input_text)

# Display the niceness score
print(f"The niceness score of the text is: {niceness_score:.2f}%")
if(0<=niceness_score<=20):
      print("ok")
elif(21<=niceness_score<=40):
      print("thanks")
elif(41<=niceness_score<=70):
      print("thank you very much")
elif(71<=niceness_score<=85):
      print("thank you so much, i really appreciate this :)") 
elif(86<=niceness_score<=95):
      print("i love you ")      
else:
      print("you are my world and i really love you so much")
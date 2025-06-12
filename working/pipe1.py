from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


# classifier = pipeline('sentiment-analysis')

# res = classifier('Hello World')

# print(res)

'''Sentiment analysis, also known as opinion mining, is the process of computationally determining the emotional tone or attitude expressed in a
piece of text. It’s about figuring out *how* someone feels about something.

**2. How it Works – The Core Concepts:**

* **Polarity:** This is the fundamental measurement. Sentiment analysis typically categorizes text into three main polarities:
    * **Positive:** Expressing favorable opinions, happiness, approval, or enthusiasm. (e.g., “This movie was amazing!”)
    * **Negative:** Expressing unfavorable opinions, disapproval, anger, or sadness. (e.g., “I hated this product.”)
    * **Neutral:**  Expressing neither positive nor negative sentiment. This could be factual statements, questions, or simply descriptive
text. (e.g., "The weather is cloudy today.")

* **Methods of Analysis:** There are several ways to do sentiment analysis:

   * **Lexicon-Based Approach:** This is the simplest. It relies on a pre-built dictionary (a *lexicon*) of words and phrases, each associated
with a sentiment score (positive, negative, or neutral). The algorithm scans the text and counts the occurrences of words in the lexicon.  For
example, "great," "fantastic," and "love" would contribute to a positive score, while "terrible," "awful," and "hate" would contribute to a
negative score.

   * **Machine Learning (ML) Approaches:** These are much more sophisticated.
      * **Supervised Learning:** You train a machine learning model (like Naive Bayes, Support Vector Machines, or more recently, deep
learning models) on a *labeled* dataset. This means you provide the algorithm with a large number of texts where each text has been manually
labeled with its sentiment (positive, negative, neutral). The model learns patterns and relationships between words, phrases, and sentiment.
      * **Unsupervised Learning:** Some techniques attempt to automatically discover sentiment clusters in text data without prior labeling.
This is more challenging.

**3. Levels of Analysis:**

* **Document-Level Sentiment:** Determining the overall sentiment of an entire document (e.g., a movie review, a news article, a customer
service email).
* **Sentence-Level Sentiment:** Determining the sentiment expressed in individual sentences within a text.
* **Aspect-Based Sentiment Analysis (ABSA):** This is the most granular. It identifies specific *aspects* or features being discussed in the
text and then determines the sentiment related to *each* aspect. For example:
   * Text: "The battery life on this phone is great, but the camera is disappointing."
   * ABSA would identify:
      * Aspect: Battery Life - Sentiment: Positive
      * Aspect: Camera - Sentiment: Negative


**4. Applications of Sentiment Analysis:**

* **Social Media Monitoring:** Tracking public opinion about brands, products, or events.
* **Customer Service:** Analyzing customer feedback to identify common complaints and prioritize support requests.
* **Market Research:** Understanding consumer preferences.
* **Financial Analysis:** Gauging investor sentiment.
* **Political Analysis:**  Tracking public opinion on political candidates or policies.

**5. Challenges:**

* **Sarcasm and Irony:** Sentiment analysis algorithms often struggle with sarcasm, irony, and other forms of figurative language.
* **Context:**  The meaning of words can change depending on the context.
* **Negation:**  "I don't like it" is clearly negative, but algorithms need to correctly handle negation.
* **Domain Specificity:**  A sentiment analysis model trained on movie reviews might not perform well on financial news.



**Resources for Learning More:**

* **NLTK (Natural Language Toolkit):** [https://www.nltk.org/](https://www.nltk.org/) (A popular Python library for NLP tasks, including
sentiment analysis)
* **Stanford CoreNLP:** [https://stanfordnlp.github.io/CoreNLP/](https://stanfordnlp.github.io/CoreNLP/) (Another powerful NLP toolkit)

Do you want me to delve into a specific aspect of sentiment analysis, like:

*   A particular method (e.g., lexicon-based vs. ML)?
*   A specific application (e.g., social media monitoring)?
*   A more technical explanation of how an algorithm works?'''

model_name = 'google/gemma-3n-E4B-it-litert-preview'

model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
 
X_train = ["""Hello World""", 'JS is weird']

res = classifier(X_train)

print(res)

batch = tokenizer(X_train, padding=True, truncation=True, max_length=512, return_tensors='pt')
print(batch)

with torch.no_grad():
   outputs = model(**batch)
   print(outputs)
   
   predictions = F.softmax(outputs.logits, dim=1)
   print(predictions)
   labels = torch.argmax(predictions, dim=1)
   print(labels)
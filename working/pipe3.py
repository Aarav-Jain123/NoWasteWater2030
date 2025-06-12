from transformers import pipeline

classifier = pipeline('zero-shot-classification')

res = classifier("Hello World", candidate_labels=['education', 'politics', 'business'])

print(res)

'''
Okay, let's break down zero-shot classification – it’s a fascinating and relatively new technique in machine learning that's gaining a lot of
traction.

**1. The Core Idea:**

Zero-shot classification allows a machine learning model to categorize data into classes it *hasn't been explicitly trained on*.  Think of it
like teaching a child to recognize different animals without showing them pictures of every single animal. You teach them the
*characteristics* of each animal, and then they can identify new animals based on those characteristics.

**2. How it Works – The Key Components:**

* **Semantic Embeddings:** This is the heart of zero-shot classification. Instead of training the model to directly map text to categories, it
learns a *semantic representation* of both the text and the categories. These representations are usually generated using techniques like:
   * **Sentence Embeddings:** Models like BERT, RoBERTa, and other transformer-based models are excellent at creating dense vector
representations (embeddings) of text. These embeddings capture the *meaning* of the text.
   * **Category Embeddings:** Similar embeddings are created for the category names (e.g., "dog," "cat," "bird").

* **Similarity Measurement:** The model then calculates the similarity between the text's embedding and each category's embedding.  Common
similarity metrics include cosine similarity. The category with the highest similarity score is the predicted category.

**3. The Process – A Step-by-Step Example:**

Let's say you want to classify news articles into categories like "Sports," "Politics," and "Technology."

1.  **You haven’t trained the model on these categories directly.** You only have a large dataset of text (e.g., news articles) with
associated labels like “Finance” and “Business.”
2.  **The model learns:**  While trained on "Finance" and "Business," the model has learned to represent the *semantic meaning* of these
categories.
3.  **New Input:** You give the model a new article about a new tech gadget.
4.  **Embedding:** The model generates an embedding for the article.
5.  **Similarity:** It calculates the similarity between the article’s embedding and the embeddings for “Sports,” “Politics,” and
“Technology.”
6.  **Prediction:**  The “Technology” category embedding will likely have the highest similarity score, and the model predicts
that the article belongs to the “Technology” category, even though it was never trained on “Technology” specifically.

**4. Why It’s Powerful:**

* **Flexibility:** You can easily add new categories without retraining the entire model.
* **Generalization:**  It leverages the model’s understanding of semantic relationships.
* **Reduced Data Requirements:**  You don’t need labeled data for every single category.

**5. Common Architectures Used:**

* **CLIP (Contrastive Language-Image Pre-training):** Developed by OpenAI, CLIP is a standout example. It’s trained to predict which caption
goes with a given image – this requires understanding the relationship between language and visuals.  It's extremely effective for zero-shot
image classification.
* **Other Transformer-Based Models:** Many other models are being adapted for zero-shot classification.



**Resources for Further Learning:**

* **OpenAI's CLIP Paper:** [https://openai.com/research/clip](https://openai.com/research/clip)
* **Towards Data Science Articles on Zero-Shot Classification:**
[https://towardsdatascience.com/zero-shot-classification-a-deep-dive-83e83911c331](https://towardsdatascience.com/zero-shot-classification-83e8[https://towardsdatascience.com/zero-shot-classification-a-deep-dive-83e83911c31](https://towardsdatascience.com/zero-shot-classification-83e83911c331)

Do you want me to elaborate on any specific aspect of zero-shot classification, such as:

*   The role of embeddings?
*   The differences between zero-shot and few-shot learning?
*   How CLIP works in more detail?'''
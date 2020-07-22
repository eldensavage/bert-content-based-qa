# Content Based Question Answering Implemened With Google's Bert NLP model

You Can Download Pre-Trained Model From Dropbox: https://www.dropbox.com/s/8jnulb2l4v7ikir/model.zip

# cURL request for API
curl -X POST http://0.0.0.0:8000/predict -H 'Content-Type: application/json' -d '{ "document": "enter your content", "question": "enter your question"}'


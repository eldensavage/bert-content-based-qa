# Open-Domain-QA
This is Open Domain Question Answering implemened with Google's bert NLP system

You Can Download Pre-Trained Model From Dropbox: https://www.dropbox.com/s/8jnulb2l4v7ikir/model.zip

# cURL request for API
curl -X POST http://0.0.0.0:8000/predict -H 'Content-Type: application/json' -d '{ "document": "enter your content", "question": "enter your question"}'


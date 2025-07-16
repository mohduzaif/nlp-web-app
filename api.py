
import textrazor
from textblob import TextBlob

# this function map the entity to more readable words.
def get_entity_type(freebase_types):
    # Define keyword to general type mappings
    type_map = {
        "person": "Person",
        "organization": "Organization",
        "location": "Place",
        "place": "Place",
        "event": "Event",
        "film": "Entertainment",
        "book": "Entertainment",
        "music": "Entertainment",
        "government": "Government",
        "award": "Award",
        "tv": "Entertainment",
        "business": "Business",
        "education": "Education"
    }

    # Try to map from the most meaningful type
    for type_path in freebase_types:
        for keyword, label in type_map.items():
            if keyword in type_path.lower():
                return label
    return "Other"  # fallback

# this function is responsible for NER api.
def name_entity_rec_api(ner_text):
    textrazor.api_key = 'b494f8a148861f8fa049e3c3310aaf956bb0b72fd8219332c3e08de0'

    client = textrazor.TextRazor(extractors=["entities"])

    response = client.analyze(ner_text)

    return response


def sentiment_analysis_api(user_text):
    
    result = {}
    blob = TextBlob(user_text)

    result['Polarity'] = round(blob.sentiment.polarity, 2)
    result['Subjectivity'] = round(blob.sentiment.subjectivity, 2)
    return result
    # print(f"Text: {t}")
    # print(f"  Polarity: {blob.sentiment.polarity:.2f}, Subjectivity: {blob.sentiment.subjectivity:.2f}")
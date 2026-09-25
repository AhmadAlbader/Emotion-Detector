import requests


def emotion_detector(text_to_analyze):
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header)

    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
    if response.status_code == 400:
        return empty_result

    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {
        emotion: emotions[emotion]
        for emotion in empty_result
        if emotion != "dominant_emotion"
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result

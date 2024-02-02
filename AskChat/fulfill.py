from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from . import urls

def model_response(user_ask_value):
    model_name = "timpal0l/mdeberta-v3-base-squad2"

    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': user_ask_value,
        'context': urls.startup()
    }
    res = nlp(QA_input)

    # b) Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return res

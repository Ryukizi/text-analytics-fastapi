from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Carregando modelos de análise de sumarização...")

model_name="sshleifer/distilbart-cnn-12-6"

tokenizer=AutoTokenizer.from_pretrained(model_name)
model=AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarizer(text):
    inputs = tokenizer(
        text, 
        return_tensors="pt", 
        max_length=1024, 
        truncation=True
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_new_tokens=130,
        min_new_tokens=30,
        do_sample=False
    )

    return tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )


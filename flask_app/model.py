from transformers import GPT2LMHeadModel, AutoTokenizer, pipeline

checkpoint = 'checkpoint-25000'
model = GPT2LMHeadModel.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)


def generate(start_text: str = 'the', length: int = 10) -> str:
    return pipe(start_text, max_length=length)[0]['generated_text']

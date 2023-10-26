from fastapi import FastAPI, Form, Request
import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
from model import Text_Model, Data_Preprocessing, get_predictions
from fastapi.templating import Jinja2Templates


device = 'cpu'
model_name = 'roberta-base'
batch_size = 32
max_length = 256
tokenizer = AutoTokenizer.from_pretrained(model_name, max_length=max_length)

model = Text_Model(model_name).to(device)

app = FastAPI()

# Define the location of your templates
templates = Jinja2Templates(directory="templates/")


# Load model
model_dict_path = "commonlit_model.pth"
model.load_state_dict(torch.load(model_dict_path, map_location=torch.device('cpu')))
model.eval()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("input_form.html", {"request": request})


@app.post("/predict")
def predict_text(request: Request, text: str = Form(...)):
    dataset = Data_Preprocessing(texts=text, tokenizer=tokenizer, max_length=max_length)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    predictions = get_predictions(model, dataloader, device)
    return templates.TemplateResponse("input_form.html", {"request": request, "prediction": predictions[0]})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)


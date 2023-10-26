import torch
from torch.utils.data import Dataset
from transformers import AutoModel
import torch.nn as nn

#creating model class


class Text_Model(nn.Module):
    def __init__(self, model_name):
        super(Text_Model, self).__init__()
        self.model = AutoModel.from_pretrained(model_name)
        self.linear = nn.Linear(self.model.config.hidden_size, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        # the last layer from pretrained
        pooler_output = outputs['pooler_output']
        return self.linear(pooler_output)

#creating dataset class
class Data_Preprocessing(Dataset):
    def __init__(self, texts, tokenizer, max_length):
        self.tokenizer = tokenizer

        # Handle both a single string and a list of strings
        if isinstance(texts, str):
            self.texts = [texts]
        else:
            self.texts = texts

        self.max_length = max_length

    def __getitem__(self, idx):
        text = self.texts[idx]
        encoding = self.tokenizer(text, padding='max_length', truncation=True, max_length=self.max_length, return_tensors='pt')
        out_dic = {key: val[0] for key, val in encoding.items()}  # get the first item in the batched output
        return out_dic

    def __len__(self):
        return len(self.texts)


def get_predictions(model, dataloader, device):
    model.eval()

    predictions = []
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            output = model(input_ids, attention_mask)
            pred_list = output.squeeze().tolist()
            if isinstance(pred_list, float):
                predictions.append(pred_list)
            else:
                predictions.extend(pred_list)
    return predictions

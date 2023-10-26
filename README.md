# TextAPI_Test
## Task
This is project repository as a Test to the course **Machine Learning in Production**.
There are several stages in that test:

### Stage 1 (required):
Implement any NLP model for this problem: https://www.kaggle.com/c/commonlitreadabilityprize/overview
The final RMSE metric doesn't matter here, the goal here is just to get a trained model.

**Output:**
* python script for training
* trained model with metrics
* README with information on how to reproduce our solution

### Stage 2 (optional)
Write an API server for the trained model form Stage1. The API should contain only 1 endpoint for prediction:

**Output:**
* python script for running API
* README with information on how to reproduce our solution

### Stage 3 (optional)
Deploy API from Stage2 and send the endpoint for testing.

**Output:**
* API endpoint

## Step-by-step Solution
For ALL stages of [Task](https://github.com/Diana-Kapralova/TextAPI_Test/tree/main#task) I create one general README, that include all stages solution. So below I represent step-by-step solution for each step.

### Stage 1: solution
1. Go to kaggle and download to local machine dataset from [here](https://www.kaggle.com/c/commonlitreadabilityprize/overview). I have account on kaggle, so I do it by command: 'kaggle competitions download -c commonlitreadabilityprize'. I have some problems with coping that files. So explanation for Kaggle API using you can search [here](https://github.com/Kaggle/kaggle-api). It works for me (I have Linux on my machine)
2. As I don't have GPU for training model, I use Google Colab. So I replace my downloaded dataset as folder **commonlitreadabilityprize** from kaggle to my Google Drive into folder **Hugging_Text_Classification**. That folder you can find [here](https://drive.google.com/drive/folders/1yDwR6vXSSbxZNhqylWaBUfl5zAdBH9N4?usp=sharing) . 
3. I create Google Colab file, [Text_Classification.ipynb](https://github.com/Diana-Kapralova/TextAPI_Test/blob/main/Text_Classifictaion.ipynb) and change Runtime to GPU (T4). Here I connect notebook to my drive and work with dataset from here.
4. After training model I save trained weights to file `commonlit_model.pth` that was saved to  **Hugging_Text_Classification** [folder](https://drive.google.com/drive/folders/1yDwR6vXSSbxZNhqylWaBUfl5zAdBH9N4?usp=sharing).

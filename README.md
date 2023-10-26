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
1. Go to kaggle and download to my local machine dataset from [here](https://www.kaggle.com/c/commonlitreadabilityprize/overview). I have account on kaggle, so I do it by command: `kaggle competitions download -c commonlitreadabilityprize` I have some problems with coping that files. I use help source [Kaggle API using](https://github.com/Kaggle/kaggle-api). It works for me (I have Linux on my machine)
2. As I don't have GPU for training model, I use Google Colab. So I uplo1-3ad my downloaded dataset as folder **commonlitreadabilityprize** from kaggle to my Google Drive into folder **Hugging_Text_Classification**. That folder you can find [here](https://drive.google.com/drive/folders/1yDwR6vXSSbxZNhqylWaBUfl5zAdBH9N4?usp=sharing) . 
3. I create Google Colab file, [Text_Classification.ipynb](https://github.com/Diana-Kapralova/TextAPI_Test/blob/main/Text_Classifictaion.ipynb) and change Runtime to GPU (T4). Here I connect notebook to my drive and work with dataset from here.
4. After training model I save trained weights to file `commonlit_model.pth` that was saved to  **Hugging_Text_Classification** [folder](https://drive.google.com/drive/folders/1yDwR6vXSSbxZNhqylWaBUfl5zAdBH9N4?usp=sharing).

### Stage 2: solution
1. I created API server on FastAPI, code for these part in file [main.py](https://github.com/Diana-Kapralova/TextAPI_Test/blob/main/main.py) and python file [model.py](https://github.com/Diana-Kapralova/TextAPI_Test/blob/main/model.py) where saved some functions and classes for working with model weights for prediction. This part I do in my local computer, by downloading trained weights from **Hugging_Text_Classification** [folder](https://drive.google.com/drive/folders/1yDwR6vXSSbxZNhqylWaBUfl5zAdBH9N4?usp=sharing) to my computer.
2. Also, I add folder [templates](https://github.com/Diana-Kapralova/TextAPI_Test/tree/main/templates) where was saved some HTML code for API. `main.py` use this file for interface for API.
3. Model weights saved in the same folder as `main.py` and `model.py`. Here I don't add model weights because of size(~500 MB), they was saved in folder on Google Drive **Hugging_Text_Classification**
4. To RUN the code in terminal in the SAME repository as code location run in the terminal:
   ```uvicorn main.py:app --reload --port 8001```
After running this, it prints some settings according to app, to use app in browser found link http://0.0.0.0:8001 and click on it. On browser open the tab with text form and button "Predict" - push the button for getting prediction.

### Stage 3: solution
For this stage I use Docker to Deploy API
1. I create [Dockerfile](https://github.com/Diana-Kapralova/TextAPI_Test/blob/main/Dockerfile) where I saved all setting for creation Docker Image. It should be in the same folder where code, model weights and templates with HTML
2. Start Docker by command in terminal in the SAME folder where Dockerfile ` sudo systemctl start docker`
3. Then BUILD: `docker build -t TextApi_Test . `. **TextApi_Test** name of project or repository, where saved api code, Dockerfile
4. After BUILD was complete RUN the docker by `sudo docker run -p 8001:8001 TextApi_Test`. Here 8001:8001 means port for listening in `main.py` we add this port for using by app.

# Picfier
An image color simplifier that uses KMeans clustering to reduce the number of colors in an image based on user's selection without losing much visual quality  for simplified display purposes

## Project Workflow
- User uploads an image
- Image is converted to an array
- The image array is passed into a KMeans model with n of clusters equal to the no of colors selected by the user
- Original and Simplified Image are displayed side-by-side
- A download button is made available for user to download the simplified image

## Tech Stack
- Python
- Streamlit for front-end
- Numpy
- Matplotlib
- Scikit learn

## How to run Locally
- Clone repository :  
   ``` bash 
       git clone
   ```

- Open folder
  ``` bash
      cd Picfier
  ```

- Create and activate virtual environment: 
  ```bash
     python -m venv .venv
  ```
  ```bash
  .venv\Scripts\activate   # On Windows
  source .venv/bin/activate # On Mac/Linux
  ```

- Install dependencies
  ```bash
  pip install -r requirement.txt
  ```
  
- Run the streamlit app
  ```bash
      streamlit run app.py
  ```

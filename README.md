# Blog Generator Using LLAma 2 and Streamlit

## Overview
This project is a web application for generating blog posts using the LLAma 2 model, built with Streamlit.

## Key Features
- **Input Blog Topic**: Enter the desired topic for the blog.
- **Word Count Selection**: Specify the blog's length.
- **Style Selection**: Choose the tone of the blog (e.g., Conversational, Formal).

## Technical Components
- **Streamlit**: For building the web interface.
- **LangChain's PromptTemplate**: To format prompts for the model.
- **LangChain's CTransformers**: To interact with LLAma 2.

## Functionality
- **getLLamaresponse Function**: Generates blog posts based on user inputs.
- **Streamlit Interface**: Handles user inputs and displays the generated blog.

## Setup Instructions
1. **LLAma 2 Model**: The LLAma 2 model is not included in this repository. You must download it locally or use `CTransformers` to access it directly via Hugging Face.
2. **Run Streamlit App**: Launch the app to start generating blog posts.

## Usage
1. **Enter the Topic**: Type in the blog's topic.
2. **Set Word Count**: Input the desired length.
3. **Select Style**: Choose from the dropdown.
4. **Generate**: Click 'Generate' to create the blog.
5. **View Result**: The generated content will be displayed.

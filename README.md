# Recipe Generation with Seq2Seq Model

This project demonstrates a natural language processing (NLP) application where a sequence-to-sequence (Seq2Seq) model generates detailed cooking instructions based on a list of ingredients.

## Overview

The model is built using an encoder-decoder architecture:
- **Encoder**: Processes the input ingredients, encoding them into a context vector using an embedding layer and an LSTM.
- **Decoder**: Generates step-by-step instructions by decoding the context vector using another embedding layer and LSTM.

The project highlights the application of machine learning in creative tasks, showing how NLP models can be used to generate structured outputs.

---

## Dataset

The dataset was sourced from **Recipe Box** and contains pairs of ingredients and their corresponding instructions. The data was preprocessed to clean text, tokenize words, and pad sequences for uniform input size.

---

## Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/recipe-generation.git
   cd recipe-generation

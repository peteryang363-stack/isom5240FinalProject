import streamlit as st
import numpy as np

# NOTE: Uncomment these imports once real models are integrated
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# =========================================================================
# function part
# =========================================================================

@st.cache_resource
def load_all_models():
    # =========================================================================
    # [PLACEHOLDER 1] SENTIMENT ANALYSIS MODEL (3 CLASSES)
    # Replace with your Hugging Face Hub repository path later.
    # =========================================================================
    sentiment_model_path = "YOUR_HF_USERNAME/YOUR_FINETUNED_SENTIMENT_MODEL_PATH"
    
    # tok_sentiment = AutoTokenizer.from_pretrained(sentiment_model_path)
    # mod_sentiment = AutoModelForSequenceClassification.from_pretrained(sentiment_model_path, num_labels=3)
    tok_sentiment = None  # Dummy placeholder
    mod_sentiment = None  # Dummy placeholder

    # =========================================================================
    # [PLACEHOLDER 2] PRODUCT CATEGORY MODEL (6 CLASSES)
    # Replace with your preferred baseline model path later.
    # =========================================================================
    category_model_path = "YOUR_SELECTED_BASE_CATEGORY_MODEL_PATH"
    
    # tok_category = AutoTokenizer.from_pretrained(category_model_path)
    # mod_category = AutoModelForSequenceClassification.from_pretrained(category_model_path, num_labels=6)
    tok_category = None  # Dummy placeholder
    mod_category = None  # Dummy placeholder
    
    return tok_sentiment, mod_sentiment, tok_category, mod_category


def analyze_sentiment(text, tokenizer, model):
    # =========================================================================
    # [PLACEHOLDER 3] REAL SENTIMENT INFERENCE LOGIC
    # Uncomment this block when real models are connected.
    # =========================================================================
    # inputs_sent = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    # with torch.no_grad():
    #     outputs_sent = model(**inputs_sent)
    # pred_sent_id = np.argmax(outputs_sent.logits.numpy(), axis=-1)[0]
    
    # Temporary UI simulation logic (Random generation for testing)
    pred_sent_id = np.random.choice([0, 1, 2])
    return pred_sent_id


def classify_product_category(text, tokenizer, model):
    # =========================================================================
    # [PLACEHOLDER 4] REAL CATEGORY INFERENCE LOGIC
    # Uncomment this block when real models are connected.
    # =========================================================================
    # inputs_cat = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    # with torch.no_grad():
    #     outputs_cat = model(**inputs_cat)
    # pred_cat_id = np.argmax(outputs_cat.logits.numpy(), axis=-1)[0]
    
    # Temporary UI simulation logic (Random generation for testing)
    pred_cat_id = np.random.choice([0, 1, 2, 3, 4, 5])
    return pred_cat_id


# =========================================================================
# main part
# =========================================================================

# 1. Page Configuration
st.set_page_config(
    page_title="E-Commerce Dual Pipeline Dashboard",
    layout="centered"
)

st.title("E-Commerce Review Analytics Dashboard")
st.markdown("This dashboard runs text analysis through Pipeline 1 (Sentiment) and Pipeline 2 (Category Classification).")

# 2. Define Output Class Mappings
sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
category_map = {
    0: "Office Products",
    1: "Home Entertainment",
    2: "Electronics",
    3: "Watches",
    4: "PC",
    5: "Home"
}

# 3. Model Initialization
with st.spinner("Initializing system components..."):
    tok_sent, mod_sent, tok_cat, mod_cat = load_all_models()
st.success("Dashboard components ready!")

# 4. User Input Interface
user_review = st.text_area(
    "Enter an Amazon Product Review:",
    placeholder="Type your review here to test the dashboard pipelines..."
)

# 5. Core Execution Trigger
if st.button("Run Dual-Pipeline Analysis", type="primary"):
    if user_review.strip() == "":
        st.warning("Please input a valid product review text before executing.")
    else:
        # Create a split view columns for side-by-side analysis
        col1, col2 = st.columns(2)
        
        # --- Pipeline 1: Sentiment Analysis Column ---
        with col1:
            st.subheader("Pipeline 1: Sentiment")
            predicted_sentiment_id = analyze_sentiment(user_review, tok_sent, mod_sent)
            st.metric(
                label="Predicted Sentiment Class", 
                value=sentiment_map[predicted_sentiment_id]
            )
            
        # --- Pipeline 2: Product Category Column ---
        with col2:
            st.subheader("Pipeline 2: Category")
            predicted_category_id = classify_product_category(user_review, tok_cat, mod_cat)
            st.metric(
                label="Predicted Product Group", 
                value=category_map[predicted_category_id]
            )

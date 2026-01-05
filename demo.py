import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Market File Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 File Upload & Market Analysis")
st.write("Upload a CSV file to analyze **Top 10 Securities by Total Traded Value**")

# File Upload
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file, on_bad_lines="skip")

        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # Column check
        if "Symbol" not in df.columns or "Total Traded Value" not in df.columns:
            st.error("CSV must contain 'Symbol' and 'Total Traded Value' columns")
        else:
            # Convert to numeric (important)
            df["Total Traded Value"] = pd.to_numeric(
                df["Total Traded Value"], errors="coerce"
            )

            # Drop NaN values
            df = df.dropna(subset=["Total Traded Value"])

            # Top 10 logic (your exact logic)
            top10_value = df.sort_values(
                "Total Traded Value", ascending=False
            ).head(10)

            st.subheader("🏆 Top 10 Securities by Total Traded Value")
            st.dataframe(top10_value)

            # Plot
            fig, ax = plt.subplots()
            ax.bar(
                top10_value["Symbol"],
                top10_value["Total Traded Value"]
            )
            ax.set_title("Top 10 Securities by Total Traded Value")
            ax.set_xlabel("Symbol")
            ax.set_ylabel("Total Traded Value")
            plt.xticks(rotation=45, ha="right")

            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("📁 Please upload a CSV file to begin analysis.")
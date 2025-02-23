import streamlit as st
import pandas as pd
import io
from datetime import datetime

def find_content_column(columns):
    """
    Find the 'content' column name regardless of case.
    Returns the actual column name if found, None otherwise.
    """
    column_map = {col.lower(): col for col in columns}
    return column_map.get('content')

def find_next_unrated_row(df):
    """
    Finds the index of the first row that hasn't been fully rated.
    """
    if 'Emotional Source Present' not in df.columns or 'Scale of Emotional Attribution' not in df.columns:
        return 0
    
    for index in range(len(df)):
        emotional_source = df.loc[index, 'Emotional Source Present']
        emotional_scale = df.loc[index, 'Scale of Emotional Attribution']
        if pd.isna(emotional_source) or pd.isna(emotional_scale):
            return index
    return len(df) - 1

def create_download_button(df, sources_list, ratings_list, original_filename):
    """
    Creates a download button for the current state of the DataFrame.
    """
    current_df = df.copy()
    df_length = len(df)
    
    sources_list = (sources_list[:df_length] + [None] * df_length)[:df_length]
    ratings_list = (ratings_list[:df_length] + [None] * df_length)[:df_length]
    
    current_df['Emotional Source Present'] = sources_list     # Yes/No values
    current_df['Scale of Emotional Attribution'] = ratings_list  # 1-5 scale values
    
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        current_df.to_excel(writer, index=False)
    return output.getvalue()

def create_rating_app():
    # Initialize ALL session state variables at the start
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'should_reset' not in st.session_state:
        st.session_state.should_reset = False
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    if 'emotional_sources' not in st.session_state:
        st.session_state.emotional_sources = []
    if 'emotional_ratings' not in st.session_state:
        st.session_state.emotional_ratings = []
    if 'original_data' not in st.session_state:
        st.session_state.original_data = None
    if 'content_column' not in st.session_state:
        st.session_state.content_column = None
    if 'total_items' not in st.session_state:
        st.session_state.total_items = 0

    st.title("Emotional Content Rating Application")
    st.markdown("""
        <style>
        @font-face {
            font-family: 'David';
            src: local('David');
        }
        .content-text {
            font-size: 16px;
            font-family: 'David', Arial, sans-serif;
            direction: ltr;
            text-align: left;
            background-color: white;
            color: black;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    # Add protocol link
    if st.button("View Rating Protocol"):
        st.switch_page("pages/protocol.py")
    
    st.write("""
    This application helps you analyze content for emotional attributes. For each item, you'll provide:
    1. Whether an emotional source is present (Yes/No)
    2. A rating for the scale of emotional attribution (1-5)
    
    Note: Your Excel file must contain a column with 'content' in its name (not case sensitive).
    If loading a previously rated file, the app will automatically continue from the first unrated item.
    You can save your progress at any time using the save button below the rating section.
    """)
    
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
    
    if uploaded_file is not None and (st.session_state.uploaded_file is None or 
                                    uploaded_file.name != st.session_state.uploaded_file.name):
        st.session_state.uploaded_file = uploaded_file
        # Reset session state but keep defaults
        for key in list(st.session_state.keys()):
            if key not in ['uploaded_file', 'should_reset']:
                del st.session_state[key]
        # Reinitialize necessary session state variables
        st.session_state.current_index = 0
        st.session_state.emotional_sources = []
        st.session_state.emotional_ratings = []
        st.session_state.original_data = None
        st.session_state.content_column = None
        st.session_state.total_items = 0
    
    if st.session_state.uploaded_file is not None:
        try:
            if st.session_state.original_data is None:
                df = pd.read_excel(st.session_state.uploaded_file)
                content_column = find_content_column(df.columns)
                
                if content_column is None:
                    st.error("Error: Could not find a column named 'content' (case-insensitive) in your file.")
                    st.write("Available columns in your file:", ", ".join(df.columns))
                    return
                
                st.success(f"Found content column: '{content_column}'")
                
                df[content_column] = df[content_column].str.strip()
                next_unrated = find_next_unrated_row(df)
                
                st.session_state.current_index = next_unrated
                st.session_state.emotional_sources = []
                st.session_state.emotional_ratings = []
                
                if 'Emotional Source Present' in df.columns and 'Scale of Emotional Attribution' in df.columns:
                    st.session_state.emotional_sources = df['Emotional Source Present'].fillna('').tolist()
                    # Safe handling of NaN values when loading ratings
                    ratings = []
                    for val in df['Scale of Emotional Attribution']:
                        try:
                            if pd.isna(val):
                                ratings.append(None)
                            else:
                                ratings.append(int(val))
                        except:
                            ratings.append(None)
                    st.session_state.emotional_ratings = ratings
                    st.info(f"Found existing ratings! Starting from item {next_unrated + 1}")
                
                st.session_state.total_items = len(df)
                st.session_state.original_data = df
                st.session_state.content_column = content_column
            
            df = st.session_state.original_data.copy()
            
            st.write(f"Rating progress: {st.session_state.current_index + 1} of {st.session_state.total_items}")
            progress = st.progress(st.session_state.current_index / st.session_state.total_items)
            
            if st.session_state.current_index < st.session_state.total_items:
                current_content = df.iloc[st.session_state.current_index][st.session_state.content_column]
                
                if pd.isna(current_content):
                    st.warning(f"Warning: Empty content found at row {st.session_state.current_index + 1}")
                    current_content = "[Empty content]"
                
                st.write("### Content to Rate:")
                st.markdown(f'<div class="content-text">{current_content}</div>', unsafe_allow_html=True)
                
                st.write("### Rating Section")
                
                # Determine if we're viewing a previously rated item
                viewing_previous = (st.session_state.current_index < len(st.session_state.emotional_sources) and 
                                 st.session_state.emotional_ratings[st.session_state.current_index] is not None)
                
                if viewing_previous:
                    # Show existing ratings
                    emotional_source = st.radio(
                        "Emotional Source Present?",
                        options=["Yes", "No"],
                        index=0 if st.session_state.emotional_sources[st.session_state.current_index] == "Yes" else 1,
                        key=f"source_{st.session_state.current_index}",
                        help="Select 'Yes' if there is a clear emotional source in the content"
                    )
                    
                    emotional_scale = st.slider(
                        "Scale of Emotional Attribution (1-5):", 
                        min_value=1, 
                        max_value=5, 
                        value=int(st.session_state.emotional_ratings[st.session_state.current_index]),
                        step=1,
                        key=f"scale_{st.session_state.current_index}",
                        help="1 = Minimal emotional attribution, 5 = Strong emotional attribution"
                    )
                else:
                    # Create a unique key for new ratings
                    widget_key = f"{st.session_state.current_index}_{st.session_state.should_reset}"
                    
                    emotional_source = st.radio(
                        "Emotional Source Present?",
                        options=["Yes", "No"],
                        index=1,  # Default to "No"
                        key=f"source_{widget_key}",
                        help="Select 'Yes' if there is a clear emotional source in the content"
                    )
                    
                    emotional_scale = st.slider(
                        "Scale of Emotional Attribution (1-5):", 
                        min_value=1, 
                        max_value=5, 
                        value=3,  # Default to 3
                        step=1,
                        key=f"scale_{widget_key}",
                        help="1 = Minimal emotional attribution, 5 = Strong emotional attribution"
                    )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⬅️ Previous", disabled=st.session_state.current_index == 0):
                        st.session_state.current_index -= 1
                        st.rerun()
                
                with col2:
                    if st.button("Next/Submit Rating ➡️"):
                        current_length = len(st.session_state.emotional_sources)
                        
                        if st.session_state.current_index < current_length:
                            st.session_state.emotional_sources[st.session_state.current_index] = emotional_source
                            st.session_state.emotional_ratings[st.session_state.current_index] = emotional_scale
                        else:
                            st.session_state.emotional_sources.append(emotional_source)
                            st.session_state.emotional_ratings.append(emotional_scale)
                        
                        if st.session_state.current_index < st.session_state.total_items - 1:
                            st.session_state.current_index += 1
                            st.session_state.should_reset = True
                            st.rerun()
                        else:
                            st.success("🎉 Rating completed!")
                
                st.write("### Save Your Progress")
                
                excel_data = create_download_button(
                    st.session_state.original_data,
                    st.session_state.emotional_sources,
                    st.session_state.emotional_ratings,
                    st.session_state.uploaded_file.name
                )
                
                st.download_button(
                    label="💾 Save Current Progress",
                    data=excel_data,
                    file_name=f"rated_{st.session_state.uploaded_file.name}",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    help="Download an Excel file with your current ratings"
                )
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            st.write("Please ensure your Excel file is properly formatted and contains a 'content' column.")

if __name__ == "__main__":
    create_rating_app()
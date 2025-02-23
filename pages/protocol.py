import streamlit as st

def show_protocol():
    # Add CSS for styling both Hebrew and English text
    st.markdown("""
        <style>
        .hebrew-text {
            font-family: 'David', Arial, sans-serif;
            direction: rtl;
            text-align: right;
            margin: 10px 0;
        }
        .example-text {
            font-size: 16px;
            font-family: 'David', Arial, sans-serif;
            direction: ltr;
            text-align: left;
            background-color: white;
            color: black;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("פרוטוקול קידוד")
    
    st.markdown("""
    <div class="hebrew-text">
    <strong>פרוטוקול קידוד לרדיט</strong>

    * יש לעשות קידוד דיכוטומי, כלומר האם יש או אין מידע על מקור הרגש- 0/1.
    
    יש לעשות גם קידוד בסקאלה, של כמה מידע יש על המקור 1-5. 1/2 יהיו יחד עם 0 בדיכוטומי, 3-5 עם 1.

    לדוגמא, זה יהיה 0 בדיכוטומי ו-1 בסקאלה:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="example-text">
    "i tried overdosing medication 7 times at extreme dose i always went in reanimation I need to finish plz tell me to hang myselfkdsls"
    </div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hebrew-text">
    וזה יהיה 1 בדיכוטומי ו-4 בסקאלה:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="example-text">
    "i just wosh they wouldve let me do it cause not im left witht eh regret and guilt that i put them through seeing me like that, and oh god the embarrassment"
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hebrew-text">
    בגלל התיאור המדויק של הרגש והסיבה (מבוכה ואשמה) גם אם אין סיבה לכל הדיכאון עצמו.

    * מקור הרגש צריך להיות קונקרטי, מוסיף מידע אמיתי -- "החיים חסרי משמעות" לא נחשב, "ההורים שלי נפטרו" נחשב.

    * במקרים בהם הפוסט מדבר על הקושי של הכותב עם מצוקה של אדם אחר, מתייחסים לכותב הפוסט והדבר שגרם לו לכתוב.
    לדוגמא:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="example-text">
    "My best friend killed himself...He was the only person I could confide in. He faced a couple of setbacks and had a few shitty days and 2 months ago, killed himself."
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hebrew-text">
    <strong>כמה דוגמאות למקרי ביניים וההחלטה שקיבלנו עליהם:</strong>

    * 1 בדיכוטומי, 3 בסקאלה:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="example-text">
    "Nothing's getting better. Therapy isn't working. Meds aren't working. Even professionals are stumped and think there's nothing more they can do...I used to stay for my pets, but my pets died"
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hebrew-text">
    * 1 בדיכוטומי, 3 בסקאלה:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="example-text">
    "I'm angry at everything, at times. I miss my boyfriend. I thought that having one would make things better...I often wish bad things would happen to me."
    </div>""", unsafe_allow_html=True)

    if st.button("Return to Rating Page"):
        st.switch_page("text_labeler.py")

if __name__ == "__main__":
    show_protocol()
import streamlit as st

def show_protocol():
    st.title("פרוטוקול קידוד")
    
    st.markdown("""
    **פרוטוקול קידוד לרדיט**

    * יש לעשות קידוד דיכוטומי, כלומר האם יש או אין מידע על מקור הרגש- 0/1.
    
    יש לעשות גם קידוד בסקאלה, של כמה מידע יש על המקור 1-5. 1/2 יהיו יחד עם 0 בדיכוטומי, 3-5 עם 1.

    לדוגמא, זה יהיה 0 בדיכוטומי ו-1 בסקאלה:
    > "i tried overdosing medication 7 times at extreme dose i always went in reanimation I need to finish plz tell me to hang myselfkdsls"
    
    וזה יהיה 1 בדיכוטומי ו-4 בסקאלה:
    > "i just wosh they wouldve let me do it cause not im left witht eh regret and guilt that i put them through seeing me like that, and oh god the embarrassment"
    בגלל התיאור המדויק של הרגש והסיבה (מבוכה ואשמה) גם אם אין סיבה לכל הדיכאון עצמו.

    * מקור הרגש צריך להיות קונקרטי, מוסיף מידע אמיתי -- "החיים חסרי משמעות" לא נחשב, "ההורים שלי נפטרו" נחשב.

    * במקרים בהם הפוסט מדבר על הקושי של הכותב עם מצוקה של אדם אחר, מתייחסים לכותב הפוסט והדבר שגרם לו לכתוב.
    לדוגמא: "My best friend killed himself...He was the only person I could confide in. He faced a couple of setbacks and had a few shitty days and 2 months ago, killed himself."

    **כמה דוגמאות למקרי ביניים וההחלטה שקיבלנו עליהם:**

    * 1 בדיכוטומי, 3 בסקאלה: "Nothing's getting better. Therapy isn't working. Meds aren't working. Even professionals are stumped and think there's nothing more they can do...I used to stay for my pets, but my pets died"

    * 1 בדיכוטומי, 3 בסקאלה: "I'm angry at everything, at times. I miss my boyfriend. I thought that having one would make things better...I often wish bad things would happen to me."
    """, unsafe_allow_html=True)

    if st.button("Return to Rating Page"):
        st.switch_page("text_labeler.py")

if __name__ == "__main__":
    show_protocol()
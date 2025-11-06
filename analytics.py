import pandas as pd
import numpy as np

def load_and_prepare_data():
    try:
        df = pd.read_csv('students.csv')
    except FileNotFoundError:
        print("Error: 'students.csv' file not found.")
        print("Please add some students using the main menu first.")
        return None
    
    if df.empty:
        print("Error: 'students.csv' is empty.")
        print("Please add some students using the main menu first.")
        return None

    df['math_grade'] = pd.to_numeric(df['math_grade'], errors='coerce')
    df['science_grade'] = pd.to_numeric(df['science_grade'], errors='coerce')
    df['english_grade'] = pd.to_numeric(df['english_grade'], errors='coerce')
    
    df.dropna(subset=['math_grade', 'science_grade', 'english_grade'], inplace=True)
    
    df['average_grade'] = (df['math_grade'] + df['science_grade'] + df['english_grade']) / 3
    return df

def subject_difficulty_analysis(df):
    print("\n--- Subject Difficulty Analysis (Full Class 10 wide Average,Standard Deviation) ---")
    math_avg = np.mean(df['math_grade'])
    science_avg = np.mean(df['science_grade'])
    english_avg = np.mean(df['english_grade'])
    math_std = np.std(df['math_grade']) #
    science_std = np.std(df['science_grade']) #
    english_std = np.std(df['english_grade']) #
    print(f"  Math Average:    {math_avg:.2f}")
    print(f"  Science Average: {science_avg:.2f}")
    print(f"  English Average: {english_avg:.2f}")
    print(f"  Math Deviation:    {math_std:.2f}") #
    print(f"  Science Deviation: {science_std:.2f}") #
    print(f"  English Deviation: {english_std:.2f}") #

def grade_distribution_report(df):
    print("\n--- Overall Grade Distribution (Based on Average) ---")
    bins = [0, 50, 70, 85, 100]
    labels = ['F (Fail)', 'C (Pass)', 'B (Good)', 'A (Excellent)']
    df['letter_grade'] = pd.cut(df['average_grade'], bins=bins, labels=labels, right=True)
    
    print(df['letter_grade'].value_counts().sort_index())

def class_performance_report(df):
    print("\n--- Performance by Class Section ---")
    class_performance = df.groupby('class_section')[['math_grade', 'science_grade', 'english_grade', 'average_grade']].mean() 
    class_dev =  df.groupby('class_section')[['math_grade', 'science_grade', 'english_grade']].std() #
    print("The avg of the classes are:")
    print(class_performance.to_string(float_format="%.2f"))
    print("The Standard deviation of the classes are:")
    print(class_dev.to_string(float_format="%.2f")) #


def failing_students_watchlist(df):
    print("\n--- Failing Students Watchlist (Average < 33.33) ---")
    failing_students = df[df['average_grade'] < 33.33]
    if failing_students.empty:
        print("  No students are currently failing. Great job!")
    else:
        print(failing_students[['student_name', 'class_section', 'average_grade']].to_string(index=False))

def top_students_report(df):
    print("\n--- Top 5 Students (School-wide) ---")
    top_5 = df.nlargest(5, 'average_grade')
    print(top_5[['student_name', 'class_section', 'average_grade']].to_string(index=False, float_format="%.2f"))

def run_analytics_report():
    df = load_and_prepare_data()
    
    if df is not None:
        print("\n" + "="*50)
        print("    🎓  SCHOOL ANALYTICS REPORT 🎓")
        print("="*50)
        
        subject_difficulty_analysis(df)
        class_performance_report(df)
        grade_distribution_report(df)
        top_students_report(df)
        failing_students_watchlist(df)
        
        print("\n" + "="*50)
        print("              End of Report")
        print("="*50 + "\n")

if __name__ == '__main__':
    run_analytics_report()

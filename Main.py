import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title="AI & Data Science Jobs",
    layout="wide"
)

df = pd.read_csv('data.csv')

with open('style.css', 'r', encoding='utf-8') as css_file:
    page_style = css_file.read()

st.markdown(f"<style>{page_style}</style>", unsafe_allow_html=True)

st.markdown(
    "<h1 style='color:#8BF1FF; font-family:Inter, sans-serif; margin-bottom: 4px;'>AI and Data Science Job Market Dataset (2020-2026)</h1>",
    unsafe_allow_html=True,
)

# Add Summary Metric Cards
st.markdown("<hr style='border: 1px solid rgba(0, 213, 255, 0.2);'>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"<div style='padding: 20px; border-radius: 16px; background: rgba(0, 213, 255, 0.1); border: 1px solid rgba(0, 213, 255, 0.3); text-align: center;'>"
        f"<p style='color: #D7F6FF; font-size: 24px; font-weight: bold; margin: 0;'>📊</p>"
        f"<p style='color: #C6E3FF; font-size: 12px; margin-top: 8px;'>Total Jobs</p>"
        f"<p style='color: #00D5FF; font-size: 20px; font-weight: bold; margin: 5px 0 0 0;'>{len(df)}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

with col2:
    avg_salary = f"${df['salary'].mean()/1000:.0f}K"
    st.markdown(
        f"<div style='padding: 20px; border-radius: 16px; background: rgba(0, 213, 255, 0.1); border: 1px solid rgba(0, 213, 255, 0.3); text-align: center;'>"
        f"<p style='color: #D7F6FF; font-size: 24px; font-weight: bold; margin: 0;'>💰</p>"
        f"<p style='color: #C6E3FF; font-size: 12px; margin-top: 8px;'>Avg Salary</p>"
        f"<p style='color: #00D5FF; font-size: 20px; font-weight: bold; margin: 5px 0 0 0;'>{avg_salary}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

with col3:
    skills = ['skills_python', 'skills_sql', 'skills_ml', 'skills_deep_learning', 'skills_cloud']
    skill_names = ['Python', 'SQL', 'ML', 'DL', 'Cloud']
    skill_counts = [df[skill].sum() for skill in skills]
    top_skill = skill_names[skill_counts.index(max(skill_counts))]
    st.markdown(
        f"<div style='padding: 20px; border-radius: 16px; background: rgba(0, 213, 255, 0.1); border: 1px solid rgba(0, 213, 255, 0.3); text-align: center;'>"
        f"<p style='color: #D7F6FF; font-size: 24px; font-weight: bold; margin: 0;'>🎯</p>"
        f"<p style='color: #C6E3FF; font-size: 12px; margin-top: 8px;'>Top Skill</p>"
        f"<p style='color: #00D5FF; font-size: 20px; font-weight: bold; margin: 5px 0 0 0;'>{top_skill}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

with col4:
    num_countries = df['country'].nunique()
    st.markdown(
        f"<div style='padding: 20px; border-radius: 16px; background: rgba(0, 213, 255, 0.1); border: 1px solid rgba(0, 213, 255, 0.3); text-align: center;'>"
        f"<p style='color: #D7F6FF; font-size: 24px; font-weight: bold; margin: 0;'>🌍</p>"
        f"<p style='color: #C6E3FF; font-size: 12px; margin-top: 8px;'>Countries</p>"
        f"<p style='color: #00D5FF; font-size: 20px; font-weight: bold; margin: 5px 0 0 0;'>{num_countries}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<hr style='border: 1px solid rgba(0, 213, 255, 0.2);'>", unsafe_allow_html=True)
data_tab, gph_tab = st.tabs(["📁 Dataset", "📊 Graph Visualizations"])
with data_tab:
    if 'show_stats' not in st.session_state:
        st.session_state.show_stats = False

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button('Show Statistics' if not st.session_state.show_stats else 'Show Full Dataset'):
            st.session_state.show_stats = not st.session_state.show_stats
    with col2:
        st.markdown(
            f"<div style='padding: 14px 18px; border-radius: 16px; background: rgba(0, 213, 255, 0.12); color: #D7F6FF; border: 1px solid rgba(0, 213, 255, 0.22);'><strong>Current view:</strong> {'Summary Statistics' if st.session_state.show_stats else 'Full Dataset'}</div>",
            unsafe_allow_html=True,
        )

    if st.session_state.show_stats:
        st.subheader("📈 Summary Statistics")
        st.write(df.describe())
    else:
        st.subheader("📋 Dataset Overview")
        st.write(df)

    if st.checkbox('📚 Show More Information'):
        tab1, tab2, tab3 = st.tabs(["🎓 Bachelor Degree", "👨‍🎓 Master Degree", "🏆 PhD"])
        with tab1:
            st.subheader("Bachelor Degree Holders")
            st.write(df[df["education_level"] == 'Bachelor'])
        with tab2:
            st.subheader("Master Degree Holders")
            st.write(df[df["education_level"] == 'Master'])
        with tab3:
            st.subheader("PhD Holders")
            st.write(df[df["education_level"] == 'PhD'])
with gph_tab:
    st.markdown("<h2 style='text-align: center;'>📊 Graph Visualization</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #D7F6FF; font-size: 14px; margin-top: -15px;'>Explore AI & Data Science job market trends</p>", unsafe_allow_html=True)
    pills = st.pills("Graph Charts", ["📊 Bar Chart", "📈 Line Chart", "💹 Scatter Plot", "🥧 Pie Chart"])
    if pills == "📊 Bar Chart":
        st.markdown("<h2 style='text-align: center;'>🎯 Most Required Skills</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; color: #D7F6FF; font-size: 13px; margin-top: -10px;'>Key technical skills in demand across the AI & Data Science industry</p>",
            unsafe_allow_html=True,
        )
        skills = ['skills_python', 'skills_sql', 'skills_ml', 'skills_deep_learning', 'skills_cloud']
        skill_names = ['Python', 'SQL', 'Machine Learning', 'Deep Learning', 'Cloud']
        skill_counts = [df[skill].sum() for skill in skills]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#050B16')
        ax.set_facecolor('#020409')
        
        sns.barplot(x=skill_names, y=skill_counts, palette=['#00D5FF', '#0066FF', '#31E4FF', '#409BFF', '#7AE8FF'], ax=ax)
        ax.set_xlabel('Skills', fontsize=12, fontweight='bold', color='#C6F3FF')
        ax.set_ylabel('Demand', fontsize=12, fontweight='bold', color='#C6F3FF')
        ax.set_title('Skills VS Demand', fontsize=14, fontweight='bold', color='#C6F3FF')
        ax.tick_params(colors='#C6F3FF')
        ax.spines['bottom'].set_color('#C6F3FF')
        ax.spines['left'].set_color('#C6F3FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.xticks(rotation=45, color='#C6F3FF')
        plt.yticks(color='#C6F3FF')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(
            "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
            "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
            "<strong>💡 Insight:</strong> Cloud is the most demanded skill, followed by Machine Learning & Python. Mastering these fundamentals is crucial for career growth.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
    elif pills == "📈 Line Chart":
        st.markdown("<h2 style='text-align: center;'>📊 Time vs Job Count for Different Roles</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; color: #D7F6FF; font-size: 13px; margin-top: -10px;'>Track career opportunities growth from 2020 to 2026</p>",
            unsafe_allow_html=True,
        )
        roles = ['Data Scientist', 'AI Engineer', 'Machine Learning Engineer', 'Data Analyst', 'Data Engineer']
        role_trend_data = []
        for role in roles:
            role_data = df[df['job_title'] == role].groupby('job_posting_year').size().reset_index(name='count')
            role_data['role'] = role
            role_trend_data.append(role_data)
        trend_df = pd.concat(role_trend_data, ignore_index=True)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#050B16')
        ax.set_facecolor('#020409')
        
        palette = {"Data Scientist": "#FF0000", "AI Engineer": "#EEF107", "Machine Learning Engineer": "#00FF11", "Data Analyst": "#0800FF", "Data Engineer": "#7AE8FF"}
        sns.lineplot(data=trend_df, x='job_posting_year', y='count', hue='role', palette=palette, marker='o', linewidth=2.5, markersize=8, ax=ax)
        
        ax.set_xlabel('Year', fontsize=12, fontweight='bold', color='#C6E3FF')
        ax.set_ylabel('Number of Jobs', fontsize=12, fontweight='bold', color='#C6E3FF')
        ax.set_title('Job Postings Trend by Role (2020-2026)', fontsize=14, fontweight='bold', color='#D7F6FF')
        ax.tick_params(colors='#C6E3FF')
        ax.spines['bottom'].set_color('#00D5FF')
        ax.spines['left'].set_color('#00D5FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.1, color='#00D5FF', linestyle='--')
        ax.legend(loc='upper left', framealpha=0.9, facecolor='#020409', edgecolor='#00D5FF', labelcolor='#C6E3FF', title_fontsize='10')
        plt.xticks(rotation=45, color='#C6E3FF')
        plt.yticks(color='#C6E3FF')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(
            "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
            "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
            "<strong>💡 Insight:</strong> All roles show growth, with Data Engineer and AI Engineer roles gaining significant momentum. Emerging roles are at the forefront of industry demand.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
    elif pills == "💹 Scatter Plot":
        st.markdown("<h2 style='text-align: center;'>💰 Salary vs Experience</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; color: #D7F6FF; font-size: 13px; margin-top: -10px;'>📈 Shows how salary increases with years of experience - A real-world relationship</p>",
            unsafe_allow_html=True,
        )
        fig, ax = plt.subplots(figsize=(12, 7))
        fig.patch.set_facecolor('#050B16')
        ax.set_facecolor('#020409')
        sns.regplot(x='years_experience', y='salary', data=df, 
                   scatter_kws={'s': 80, 'alpha': 0.6, 'color': '#00D5FF', 'edgecolors': '#00D5FF', 'linewidths': 1.5},
                   line_kws={'color': '#FF6B6B', 'linewidth': 3, 'linestyle': '--'},
                   ax=ax)
        
        ax.set_xlabel('Years of Experience', fontsize=13, fontweight='bold', color='#C6E3FF')
        ax.set_ylabel('Salary ($)', fontsize=13, fontweight='bold', color='#C6E3FF')
        ax.tick_params(colors='#C6E3FF', labelsize=11)
        ax.spines['bottom'].set_color('#00D5FF')
        ax.spines['left'].set_color('#00D5FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.1, color='#00D5FF', linestyle='--')
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        plt.xticks(color='#C6E3FF')
        plt.yticks(color='#C6E3FF')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(
            "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
            "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
            "<strong>💡 Insight:</strong> There's a strong positive correlation between experience and salary. Candidates with 10+ years of experience can expect significantly higher compensation.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
    elif pills == "🥧 Pie Chart":
        st.markdown("<h2 style='text-align: center;'>🥧 Distribution Analysis</h2>", unsafe_allow_html=True)
        choice = st.selectbox("Select a content:", ["🌍 Country Distribution", "🎓 Education Level Distribution", "🏢 Job Role Distribution"])
        if choice == "🌍 Country Distribution":
            st.markdown("<h3 style='text-align: center;'>🌍 Job Distribution by Country</h3>", unsafe_allow_html=True)
            country_counts = df['country'].value_counts().reset_index()
            country_counts.columns = ['country', 'count']
            
            fig, ax = plt.subplots(figsize=(10, 8))
            fig.patch.set_facecolor('#050B16')
            ax.set_facecolor('#020409')
            sns.set_style("darkgrid")
            palette = sns.color_palette("husl", len(country_counts))
            colors = [f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}' for r, g, b in palette]
            
            wedges, texts, autotexts = ax.pie(country_counts['count'], labels=country_counts['country'], autopct='%1.1f%%',
                                               colors=['#00D5FF', '#0066FF', '#31E4FF', '#409BFF', '#7AE8FF', '#FF6B6B', '#FFD700', '#FF1493', '#00FF00', '#FF4500'][:len(country_counts)], 
                                               startangle=90, 
                                               textprops={'color': '#C6E3FF', 'fontsize': 10, 'fontweight': 'bold'})
            
            for autotext in autotexts:
                autotext.set_color('#020409')
                autotext.set_fontweight('bold')
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown(
                "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
                "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
                "<strong>💡 Insight:</strong> Opportunities are distributed globally. Top countries show significant market demand, making international opportunities accessible for professionals.</p>"
                "</div>",
                unsafe_allow_html=True,
            )
        elif choice == "🎓 Education Level Distribution":
            st.markdown("<h3 style='text-align: center;'>🎓 Job Distribution by Education Level</h3>", unsafe_allow_html=True)
            edu_counts = df['education_level'].value_counts().reset_index()
            edu_counts.columns = ['education_level', 'count']
            
            fig, ax = plt.subplots(figsize=(10, 8))
            fig.patch.set_facecolor('#050B16')
            ax.set_facecolor('#020409')
            sns.set_style("darkgrid")
            palette = sns.color_palette("coolwarm", len(edu_counts))
            colors = [f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}' for r, g, b in palette]
            
            wedges, texts, autotexts = ax.pie(edu_counts['count'], labels=edu_counts['education_level'], autopct='%1.1f%%',
                                               colors=['#00D5FF', '#0066FF', '#31E4FF'][:len(edu_counts)], 
                                               startangle=90,
                                               textprops={'color': '#C6E3FF', 'fontsize': 11, 'fontweight': 'bold'})
            
            for autotext in autotexts:
                autotext.set_color('#020409')
                autotext.set_fontweight('bold')
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown(
                "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
                "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
                "<strong>💡 Insight:</strong> Most roles favor Master's degree holders, showing the value of advanced education. However, strong candidates with Bachelor's degrees are also highly competitive.</p>"
                "</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown("<h3 style='text-align: center;'>🏢 Job Role Distribution</h3>", unsafe_allow_html=True)
            role_counts = df['job_title'].value_counts().reset_index()
            role_counts.columns = ['job_title', 'count']
            
            fig, ax = plt.subplots(figsize=(10, 8))
            fig.patch.set_facecolor('#050B16')
            ax.set_facecolor('#020409')
            sns.set_style("darkgrid")
            palette = sns.color_palette("Set2", len(role_counts))
            colors = [f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}' for r, g, b in palette]
            
            wedges, texts, autotexts = ax.pie(role_counts['count'], labels=role_counts['job_title'], autopct='%1.1f%%',
                                               colors=colors, 
                                               startangle=90, 
                                               textprops={'color': '#C6E3FF', 'fontsize': 10, 'fontweight': 'bold'})
            
            for autotext in autotexts:
                autotext.set_color('#020409')
                autotext.set_fontweight('bold')
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown(
                "<div style='padding: 15px; border-radius: 12px; background: rgba(0, 213, 255, 0.08); border-left: 4px solid #00D5FF; margin-top: 20px;'>"
                "<p style='color: #D7F6FF; margin: 0; font-size: 13px;'>"
                "<strong>💡 Insight:</strong> Data Scientist and Machine Learning Engineer roles dominate the market, indicating high demand for core AI and data expertise.</p>"
                "</div>",
                unsafe_allow_html=True,
            )
    else:
        st.write("Please select a graph type to visualize the data.")

import pandas as pd

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv("data.csv", delimiter=";")

    # 1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    loc_male = df.loc[df["sex"] == "Male", "age"]
    avg_men = loc_male.mean().round(2)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total = df["education"].value_counts().sum()
    loc_bac = df.loc[df["education"]=="Bachelors"].shape[0]
    per_bac = round((loc_bac/total)*100,2)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    total_bmd = df.loc[df.education.isin(["Bachelors","Masters","Doctorate"]),"education"].value_counts().sum()
    loc_cond = df.loc[(df.salary == ">50K")&(df.education.isin(["Bachelors","Masters","Doctorate"])),"education"].value_counts().sum()
    per_bmd_m50 = round((loc_cond/total_bmd)*100,2)

    # 5. What percentage of people without advanced education make more than 50K?
    total_wo_ae = df.loc[~df.education.isin(["Bachelors","Masters","Doctorate"]),"education"].value_counts().sum()
    wo_ae_m50 =  df.loc[(df.salary == ">50K")&~(df.education.isin(["Bachelors","Masters","Doctorate"])),"education"].value_counts().sum()
    per_result = (wo_ae_m50/total_wo_ae)*100
    per_wo_ae_m50 = per_result.round(2)

    # 6. What is the minimum number of hours a person works per week?
    min_hours = df["hours-per-week"].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_m50 = df.loc[(df.salary == ">50K") & (df["hours-per-week"]== df["hours-per-week"].min())].shape[0]
    total_min_hours = df.loc[df["hours-per-week"]== df["hours-per-week"].min()].shape[0]
    per_min_50 = (min_hours_m50 / total_min_hours) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    earn_m50 = df.loc[df["salary"]==">50K","native-country"].value_counts()
    total_earn_m50 = earn_m50.sum()
    result = (earn_m50.head(1)/total_earn_m50)*100
    high_earn_country = result.index[0]
    high_earn_per = round(result.iloc[0],2)


    # 9. Identify the most popular occupation for those who earn >50K in India.

    ind_m50 = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K"),"occupation"].value_counts()
    top_occ = ind_m50
    occ_top = top_occ.index[0]


    if print_data:
        print("1. People of each race:")
        print(race_count.to_frame())
        print("2. Average age of men:",avg_men,"years")
        print("3. Percentage of people who have a Bachelor's degree:",per_bac,"%")
        print("4. Percentage of people with advanced education that make more than 50K:",per_bmd_m50,"%")
        print("5. Percentage of people without advanced education that make more than 50K:",per_wo_ae_m50,"%")
        print("6. The minimum number of hours a person works per week is:", min_hours, "hours/week")
        print("7. Percentage of people working the minimum number of hours per week with a salary of more than 50K:",per_min_50,"%")
        print("8. The name of the country where many people earn more than 50K is:",high_earn_country,"-->",high_earn_per,"%")
        print("9. The most popular occupation in India is --->",occ_top,"with",top_occ.iloc[0], "professionals earning more than 50K.")


    return {
        "race_count": race_count,
        "avg_men": avg_men,
        "per_bac": per_bac,
        "per_bmd_m50": per_bmd_m50,
        "per_wo_ae_m50": per_wo_ae_m50,
        "min_hours": min_hours,
        "per_min_50": per_min_50,
        "high_earn_country": high_earn_country,
        "high_earn_per": high_earn_per,
        "occ_top": occ_top
    }

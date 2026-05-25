import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("C:/Users/User/Documents/Cursos/Free Code Camp/Data Analysis With Python/Proyectos/Demographic Data Analyzer/adult.data.csv")

    total_individuals = df.shape[0]
    
    
    def percentage(number, total= total_individuals):
        # return the percentage of number respect to total rounded to the first decimal place
        return round(number/total *100, 1)
    
    # print("Number of individuals: ", number_individuals)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men = df.loc[df["sex"]=="Male"]
    average_age_men = round(men["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    
    percentage_bachelors = percentage(df.loc[df["education"]=="Bachelors"].shape[0])

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # print(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))
    higher_education = df.loc[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df.loc[df["education"].isin(["Bachelors", "Masters", "Doctorate"]) == False]
    
    # print("higher education: ",higher_education.shape[0])
    # percentage with salary >50K
    higher_education_rich = percentage(higher_education.loc[higher_education["salary"] == ">50K"].shape[0], higher_education.shape[0])
    lower_education_rich = percentage(lower_education.loc[lower_education["salary"] == ">50K"].shape[0], lower_education.shape[0])

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df.loc[df["hours-per-week"] == min_work_hours]
    
    num_rich_min_workers = min_workers.loc[min_workers["salary"] == ">50K"].shape[0]

    # print("num_rich_min_workers = ", num_rich_min_workers) There are 2
    rich_percentage = percentage(num_rich_min_workers, min_workers.shape[0])

    # What country has the highest percentage of people that earn >50K?
    rich_workers = df.loc[df["salary"] == ">50K"]
    rich_workers_per_country = rich_workers["native-country"].value_counts()
    workers_per_country = df["native-country"].value_counts()
    
    # print("rich_workers_per_country: ", rich_workers_per_country)
    # print("workers_per_country: ", workers_per_country)
    
    ratio_rich_earning_country = rich_workers_per_country/workers_per_country
    
    # print("ratio_rich_earning_country", ratio_rich_earning_country)
    
    max_ratio_rich_earning_country = ratio_rich_earning_country.max()
    highest_earning_country = ratio_rich_earning_country.loc[ratio_rich_earning_country == max_ratio_rich_earning_country].index[0]
    #.index returns a list with one element
    highest_earning_country_percentage = percentage(max_ratio_rich_earning_country,1) # Divide by 1 because it is already the ratio

    # Identify the most popular occupation for those who earn >50K in India.
    rich_India = rich_workers.loc[rich_workers["native-country"]== "India"]
    occupations_count = rich_India["occupation"].value_counts()
    top_IN_occupation = occupations_count.loc[occupations_count == occupations_count.max()].index[0]




    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

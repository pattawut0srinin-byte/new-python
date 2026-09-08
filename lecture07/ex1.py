survey_results = [
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript"],
    ["Python","JavaScript","C++","Java"]
]

survey_sets = [set(language) for language in survey_results]
print(survey_sets)

all_use_language = set.intersection(*survey_sets)
print("all_use_language:", all_use_language)

all_use = survey_sets[4]
unique_language = survey_sets[1]
sig_languge = list(all_use - unique_language)
print("sig language:", sig_languge)

all_language = set.union(*survey_sets)
unique_language_count = len(all_language)
print("Total unique luanguage:", unique_language_count)

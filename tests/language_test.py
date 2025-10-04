
def test_make_language_dict():
    lang_dict = vt.make_all_language_dict(key_as="alpha2",value_as="object")  
    # count how many keys have length of 2, and how many have length of 3
    # then create seperate pd.df for these 2 groups
    count_2 = 0
    count_3 = 0
    for key in lang_dict.keys():
        if len(key) == 2:
            count_2 += 1
        elif len(key) == 3:
            count_3 += 1
    lang_dict_2 = dict()
    lang_dict_3 = dict()
    for key, value in lang_dict.items():
        if len(key) == 2:
            lang_dict_2[key] = value.language_name('en')
        elif len(key) == 3:
            lang_dict_3[key] = value.language_name('en')
    df_2 = pd.DataFrame(lang_dict_2.items(), columns=['alpha2', 'name'])
    df_3 = pd.DataFrame(lang_dict_3.items(), columns=['alpha3', 'name'])
    
    # key observation: main language would have 2key code as well
    
    print(f"Count of keys with length of 2: {count_2}")
    print(f"Count of keys with length of 3: {count_3}")
    print()
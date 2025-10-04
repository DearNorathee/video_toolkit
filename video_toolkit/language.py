from beartype import beartype
from langcodes import Language
from typing import Literal, Union

@beartype
def all_lang_name_list():
    import pycountry
    language_names = [lang.name for lang in pycountry.languages if hasattr(lang, 'name')]
    return language_names

def all_lang_obj_list() -> list[Language]:
    import pycountry
    # from langcodes import Language
    language_names = all_lang_name_list()
    result = []
    not_found_languages = []
    for language in language_names:
        try:
            result.append(Language.find(language))
        except LookupError:
            not_found_languages.append(language)
    return result


def make_all_language_dict(
    key_as:Literal["alpha3","alpha2","name","object"]
    ,value_as:Literal["alpha3","alpha2","name","object"]
    ) -> dict[str|Language,str|Language]:
    all_lang_obj_list_in = all_lang_obj_list()
    result = dict()

    # medium tested
    # to get 2 language code you can simply do str(lang_obj)
    # but there are some languages with no 2 language code, in that case I would default to 3str
    # # key observation: main language would have 2key code as well

    for lang_obj in all_lang_obj_list_in:
        lang_alpha3 = lang_obj.to_alpha3()
        # lang_alpha2 = lang_obj.to_alpha2()
        lang_name = lang_obj.language_name('en')


        if key_as == "alpha3":
            key = lang_alpha3
        elif key_as == "alpha2":   
            key = str(lang_obj)
        elif key_as == "name":
            key = lang_name
        elif key_as == "object":
            key = lang_obj

        if value_as == "alpha3":
            value = lang_alpha3
        elif value_as == "alpha2":
            value = str(lang_obj)
        elif value_as == "name":
            value = lang_name
        elif value_as == "object":
            value = lang_obj
        
        result[key] = value

    return result

@beartype
def closest_language(misspelled_language:str):
    
    from fuzzywuzzy import process
    import pycountry
    # Get a list of all language names
    language_names = [lang.name for lang in pycountry.languages if hasattr(lang, 'name')]

    # Use fuzzy matching to find the closest match
    closest_match = process.extractOne(misspelled_language, language_names)
    return closest_match[0] if closest_match else None

@beartype
def closest_language_obj(misspelled_language:str|list[str]):
    
    """
    Find the closest matching language object for a potentially misspelled language code.
    
    Parameters:
    -----------
    misspelled_language : str
        The potentially misspelled language code.
    
    Returns:
    --------
    langcodes.Language
        A language object representing the closest matching language.
    
    Notes:
    ------
    - This function uses the 'langcodes' library to find the closest matching language object
      for a potentially misspelled language code.
    - It can be useful for language code correction or normalization.
    
    Example:
    --------
    >>> closest_language_obj("englsh")
    <Language('en', 'English')>
    >>> closest_language_obj("español")
    <Language('es', 'Spanish')>
    
    """
    
    
    from langcodes import Language
    if isinstance(misspelled_language, list):
        results = []
        for item in misspelled_language:
            results.append(Language.find(closest_language(item)))
        return results
    else:
        return Language.find(closest_language(misspelled_language))
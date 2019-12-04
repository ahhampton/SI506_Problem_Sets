# SI 506 2019F - Problem Set 109

# In this problem set you will work with the Star Wars API. We recommend you read through some of the documentation (https://swapi.co/documentation) and reference it as you work through the following problems. You will also want to reference the requests documentation (https://requests.readthedocs.io/en/master/user/quickstart/#quickstart).

# Responses from the Star Wars API may be slow, don't worry if your terminal "hangs" while making and parsing calls to the API.

# Read the following block quote ENTIRELY before beginning this assignment.

'''
For this assignment, you will build four utility functions (functions that do one small thing) and a main function
(a function that will execute the main purpose of this script). Outside of testing, you should not need to write
any code that is not contained within one of these functions. Below is a description of each of the functions
that you should write. At the bottom of this block quote you will find the grading rubric for the autograder
of this homework. There are tests for several of the functions; you can read about them in the description of
that function.
----- Functions to Create -----
YOU MUST INCLUDE DOCSTRINGS IN ALL YOUR FUNCTIONS TO GET FULL CREDIT
get_data:
    parameters:
        - baseurl (str)
        - resource (str with default value of "")
        - params (dict with default value of an empty dict {})
    description:
        This function should make a call to an API using the <requests> module. <baseurl> should be the
        base url for the API endpoint, <resource> should be which resource is being called, and <params>
        should be a dictionary of any optional parameters.
    returns:
        This function should return a dictionary that is the result of the API call.
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'
search_swapi:
    parameters:
        - resource (str)
        - query (str)
    description:
        This function should use the "search" functionality of SWAPI to search for the <query> string
        given a <resource>. In other words, you might want to search for a query of "luke" in the
        resource "people/". This function should make a call to <get_data> to accomplish this goal.
    returns:
        This function should return a dictionary that is the result of the query.
    test:
        There are a couple tests provided for you at the bottom of this file. They should return 'True'
get_information_on_characters
    parameters:
        - list_of_characters (list)
    description:
        Given a result set of characters from a SWAPI query, return a nested list
        of the character name, birth year, and species name. In other words, <list_of_characters>
        should be a list structured like the value to the key 'results' from the dictionary that
        is returned from <search_swapi>.
    returns:
        This function should return a nested dictionary in the following form:
        {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' : <name of the species of the character>
                    'homeworld_name' : <name of the homeworld of the character>
                }
            <other character name> :
                {
                    ... etc ...
                }
            ... etc ...
        }
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'
write_json:
    parameters:
        - filename (str)
        - data (json-able object, e.g. nested dictionary or list)
    description:
        Write <data> to the .json file specified by <filename>
    returns:
        This function doesn't return anything.
    test:
        There is no test for this function provided, although you are free and encouraged to test this
        function however you see fit.
main:
    parameters:
        (there are no parameters for <main>)
    description:
        Use <search_swapi>, <get_information_on_characters>, and <write_json> to produce the following
        .json files:
        "darth_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "darth" in their name.
        "skywalker_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "skywalker" in their name.
        "tatooine_residents_info.json": <-- CHALLENGE
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have are residents of "tatooine".
            - HINT: You may want to use your <search_swapi> function with "planets" as the <resource> and
            "tatooine" as the <query> here...and then you'll need to find the URLs of all the characters that
            reside on Tatooine and save their information to a list for <get_information_on_characters> to use.
----- Grading Rubric -----
20 pts: <get_data> works correctly
20 pts: <search_swapi> works correctly
20 pts: <get_information_on_characters> works correctly
20 pts: <write_json> works correctly
10 pts: Every function has a docstring
20 pts: "darth_info.json" is correct
20 pts: "skywalker_info.json" is correct
20 pts: "tatooine_residents_info" is correct
150 points total
'''

import requests
import json

# BEGIN CODING HERE


def get_data(baseurl, resource = "", params = {}):
    """
    parameters:
        - baseurl (str)
        - resource (str with default value of "")
        - params (dict with default value of an empty dict {})
    description:
        This function should make a call to an API using the <requests> module. <baseurl> should be the
        base url for the API endpoint, <resource> should be which resource is being called, and <params>
        should be a dictionary of any optional parameters.
    returns:
        This function should return a dictionary that is the result of the API call.
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'
    """
    response = requests.get(baseurl + resource, params=params).json()
    return response


def search_swapi(resource, query):
    """
    parameters:
        - resource (str)
        - query (str)
    description:
        This function should use the "search" functionality of SWAPI to search for the <query> string
        given a <resource>. In other words, you might want to search for a query of "luke" in the
        resource "people/". This function should make a call to <get_data> to accomplish this goal.
    returns:
        This function should return a dictionary that is the result of the query.
    test:
        There are a couple tests provided for you at the bottom of this file. They should return 'True'
    """
    query = {'search': query} #creating an argument for the search parameter
    results = get_data('https://swapi.co/api/', resource, query)
    return results

def get_information_on_characters(list_of_characters):
    """
    parameters:
        - list_of_characters (list) #providing list of characters
    description:
        Given a result set of characters from a SWAPI query, return a nested list #NO.  It's dictionary#
        of the character name, birth year, and species name. In other words, <list_of_characters>
        should be a list structured like the value to the key 'results' from the dictionary that
        is returned from <search_swapi>.
    returns:
        This function should return a nested dictionary in the following form:
        {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' #NO.  It's species# : <name of the species of the character> #returns URLs
                    'homeworld_name' #NO.  It's species# : <name of the homeworld of the character> #returns URLs
                }
            <other character name> :
                {
                    ... etc ...
                }
            ... etc ...
        }
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'
    """
    nested = {} #created b/c output is a dictionary
    for item in list_of_characters:
        for key,value in item.items():
            if key == 'name':
                name = value
                nested[name] = {}
                nested[name][key] = value
            if key == 'birth_year':
                nested[name][key] = value
            if 'species' in key:
                species_name = get_data(value[0])['name']
                nested[name]['species_name'] = species_name
            if 'homeworld' in key:
                planet = get_data(value)['name']
                nested[name]['homeworld_name'] = planet
    return nested


    #ORIGINAL
    # big_dictionary = {}
    # for dictionary in list_of_characters:
    #     first_key = dictionary.get('name') #take first name, make it dictionary key
    #     year = dictionary.get('birth_year')
    #     species_type = eval(requests.get(dictionary.get('species')[0]).text).get('name') #have to index 'species' b/c there's only one list within the key
    #     planet = eval(requests.get(dictionary.get('homeworld')).text).get('name') #homeworld is a URL...but no name.  dictionary.get gets value of homeworld API...have to make it .text  eval converts back to dict 
    #     nested['name'] = first_key #creating profiles nested within big_dictionary
    #     nested['birth_year'] = year
    #     nested['species_name'] = species_type
    #     nested['homeworld_name'] = planet
    #     big_dictionary[first_key] = nested #every time it iterates, there's an error where it runs 
    # return big_dictionary


def write_json(filename, data):
    """
    parameters:
        - filename (str)
        - data (json-able object, e.g. nested dictionary or list)
    description:
        Write <data> to the .json file specified by <filename>
    returns:
        This function doesn't return anything.
    test:
        There is no test for this function provided, although you are free and encouraged to test this
        function however you see fit.

    """
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


def main():
    """
    parameters:
        (there are no parameters for <main>)
    description:
        Use <search_swapi>, <get_information_on_characters>, and <write_json> to produce the following
        .json files:
        "darth_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "darth" in their name.
        "skywalker_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "skywalker" in their name.
        "tatooine_residents_info.json": <-- CHALLENGE
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have are residents of "tatooine".
            - HINT: You may want to use your <search_swapi> function with "planets" as the <resource> and
            "tatooine" as the <query> here...and then you'll need to find the URLs of all the characters that
            reside on Tatooine and save their information to a list for <get_information_on_characters> to use.
    """

file_path = os.path.dirname(os.path.abspath(__file__))

darth_info = get_information_on_characters(search_swapi("people","darth"))['results']
darth_info_filepath = os.path.join('darth_info.json')
write_json(darth_info_filepath,darth_info)

skywalker_info = get_information_on_characters(search_swapi("people","skywalker"))['results']
skywalker_info_filepath = os.path.join('skywalker_info.json')
write_json(skywalker_info_filepath,skywalker_info)

#HELP LOL
tatooine_list = []
# It'll be easier if you break this down step by step as well as use "meta programming" by commenting out the steps you need to take in order to get to the results
# Step 1: Get the info for Tatooine
# Step 2: Parse the JSON and get a list of characters
# Step 3: Append list of characters to the file
# Step 4: Write JSON to the file

#Step 1
tatooine_info = search_swapi("planets", "tatooine")
#Step 1 results
"""
{
  u'diameter': u'10465',
  u'climate': u'arid',
  u'surface_water': u'1',
  u'name': u'Tatooine',
  u'created': u'2014-12-09T13:50:49.641000Z',
  u'url': u'https://swapi.co/api/planets/1/',
  u'rotation_period': u'23',
  u'edited': u'2014-12-21T20:48:04.175778Z',
  u'terrain': u'desert',
  u'gravity': u'1 standard',
  u'orbital_period': u'304',
  u'films': [
    u'https://swapi.co/api/films/5/',
    u'https://swapi.co/api/films/4/',
    u'https://swapi.co/api/films/6/',
    u'https://swapi.co/api/films/3/',
    u'https://swapi.co/api/films/1/'
  ],
  u'residents': [
    u'https://swapi.co/api/people/1/',
    u'https://swapi.co/api/people/2/',
    u'https://swapi.co/api/people/4/',
    u'https://swapi.co/api/people/6/',
    u'https://swapi.co/api/people/7/',
    u'https://swapi.co/api/people/8/',
    u'https://swapi.co/api/people/9/',
    u'https://swapi.co/api/people/11/',
    u'https://swapi.co/api/people/43/',
    u'https://swapi.co/api/people/62/'
  ],
  u'population': u'200000'
}
"""
#Step 2
tatooine_list.append(tatooine_info['results'][0]['residents'])

#Step 3
tatooine_info_filepath = os.path.join('tatooine_residents_info.json')

#Step 4
write_json(tatooine_info_filepath,tatooine_info)


# STOP CODING HERE! DO NOT MODIFY ANYTHING BELOW THIS LINE (except to comment/uncomment tests)!

# The below code will call the <main> function you wrote so long as you are running this
# code directly (as opposed to importing it in another python script).
if __name__ == '__main__':
    main()

    ##### test for <get_data>...uncomment the below two lines when you are ready!
    test1 = get_data('https://swapi.co/api/',resource='people',params={'search':'yoda'})['results'][0]['mass']=='17'
    print(f"\nTest for <get_data>: {test1}")

    ##### tests for <search_swapi>...uncomment the below four lines when you are ready!
    test2 = search_swapi('people','yoda')['results'][0]['mass']=='17'
    test3 = search_swapi('starships','tie')['results'][0]['crew']=='1'
    print(f"\nTest #1 for <search_swapi>: {test2}")
    print(f"Test #2 for <search_swapi>: {test3}")

    ##### test for <get_information_on_characters>...uncomment the below two lines when you are ready!
    test4 = get_information_on_characters(search_swapi('people','skywalker')['results'])['Shmi Skywalker']['birth_year']=='72BBY'
    print(f"\nTest for <get_information_on_characters>: {test4}")

# END PROBLEM SET 10
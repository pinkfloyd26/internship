#!/usr/bin/env python
# coding: utf-8

# # Regression Assignment
# 

# In[1]:


# Answer1


# In[2]:


import re


# In[106]:


def check_characters(string):
  
  allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
  for character in string:
    if character not in allowed_characters:
      return False
  return True


# In[107]:


print (check_characters('Chinmay1996'))


# In[5]:


# Answer 2


# In[6]:


def match_a_followed_by_zero_or_more_b(string):
  
  pattern = 'a*b*'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[15]:


print(match_a_followed_by_zero_or_more_b('aaaabbbbbbbbbbbb'))


# In[7]:


# Answer 3


# In[8]:


def match_a_followed_by_one_or_more_b(string):
 
  pattern = 'a+b+'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[16]:


print(match_a_followed_by_one_or_more_b('aaaaaaaabbbbbbbbbbbb'))


# In[9]:


# Answer 4


# In[10]:


def match_a_followed_by_zero_or_one_b(string):
 
  pattern = 'a?b?'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[21]:


print(match_a_followed_by_zero_or_one_b('abbbbbbbb'))


# In[19]:


# Answer 5


# In[108]:


def match_a_followed_by_three_b(string):
  
  pattern = 'a{1}b{3}'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[22]:


print(match_a_followed_by_three_b('abbbbbbbb'))


# In[23]:


# Answer 6


# In[25]:


def split_string_into_uppercase_letters(string):
 
  pattern = '[A-Z]+'
  matches = re.findall(pattern, string)
  return matches


# In[26]:


print(split_string_into_uppercase_letters('PinkFloydIsTheGreatestBandOfAllTime'))


# In[27]:


# Answer 7


# In[28]:


def match_a_followed_by_two_to_three_b(string):
  
  pattern = 'a{1}b{2,3}'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[29]:



print(match_a_followed_by_two_to_three_b('abbbb'))
print(match_a_followed_by_two_to_three_b('abbbbb'))
print(match_a_followed_by_two_to_three_b('abbbbbbbbb'))


# In[30]:


# Answer 8


# In[31]:


def find_sequences_of_lowercase_letters_joined_with_underscore(string):
 
  pattern = '[a-z]+_[a-z]+'
  matches = re.findall(pattern, string)
  return matches


# In[33]:


print(find_sequences_of_lowercase_letters_joined_with_underscore('east_west_north_south'))


# In[34]:


# Answer 9


# In[35]:


def match_a_followed_by_anything_ending_in_b(string):

  pattern = 'a.*b'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[36]:


print(match_a_followed_by_anything_ending_in_b('a_b'))
print(match_a_followed_by_anything_ending_in_b('a_ba'))
print(match_a_followed_by_anything_ending_in_b('a_bb'))


# In[37]:


def match_a_word_at_the_beginning_of_a_string(string):
 
  pattern = r'\b\w+\b'
  if re.search(pattern, string):
    return True
  else:
    return False


# In[38]:


print(match_a_word_at_the_beginning_of_a_string('A brief history of time'))
print(match_a_word_at_the_beginning_of_a_string('Principles of physics'))
print(match_a_word_at_the_beginning_of_a_string('Lazarus by porcupine tree is an awesome song'))


# In[39]:


# Answer 11
def match_string_with_only_upper_lowercase_letters_and_underscores(string):
 
  pattern = '[a-zA-Z0-9_]+'
  if re.match(pattern, string):
    return True
  else:
    return False


# In[40]:


print(match_string_with_only_upper_lowercase_letters_and_underscores('The_brief_history_of_time'))
print(match_string_with_only_upper_lowercase_letters_and_underscores('123abc_def'))
print(match_string_with_only_upper_lowercase_letters_and_underscores('$%^&*()'))


# In[41]:


# Answer 12


# In[42]:


def match_string_that_starts_with_specific_number(string, number):
 
  pattern = '^\d{1,3}' + number
  if re.match(pattern, string):
    return True
  else:
    return False


# In[43]:


print(match_string_that_starts_with_specific_number('123abc', '123'))
print(match_string_that_starts_with_specific_number('abc123', '123'))
print(match_string_that_starts_with_specific_number('123abc123', '123'))


# In[44]:


# Answer 13


# In[45]:


def remove_leading_zeros_from_ip_address(ip_address):
  
  pattern = '^0{1,3}'
  result = re.sub(pattern, '', ip_address)
  return result


# In[48]:


print(remove_leading_zeros_from_ip_address('012.34.56.78'))
print(remove_leading_zeros_from_ip_address('0012.34.56.78'))


# In[49]:


# Answer 14


# In[50]:


def match_date_string(string):
 
  pattern = '^([a-zA-Z]{3})\s+(\d{1,2})\s+(\d{4})$'
  if re.match(pattern, string):
    return True
  else:
    return False


# In[51]:


print(match_date_string('February 26th 1996'))
print(match_date_string('February 26 1996'))
print(match_date_string('26th February 1996'))


# In[52]:


# Answer 15


# In[53]:


# Answer 16


# In[54]:


def search_literal_in_string_and_get_location(string, literal):
  
  match = re.search(literal, string)
  if match:
    return match.start()
  else:
    return None


# In[55]:


string = 'The quick brown fox jumps over the lazy dog.'
literal = 'fox'

print(search_literal_in_string_and_get_location(string, literal))


# In[56]:


# Answer 17


# In[57]:


def find_substrings_within_string(string, pattern):
 
  matches = re.findall(pattern, string)
  return matches


# In[58]:


string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

print(find_substrings_within_string(string, pattern))


# In[59]:


# Answer 18


# In[109]:


def find_occurrence_and_position_of_substrings_within_string(string, pattern):
  
  matches = re.finditer(pattern, string)
  for match in matches:
    print(f'Occurrence: {match.start()}, Position: {match.end() - 1}')


# In[61]:


string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

find_occurrence_and_position_of_substrings_within_string(string, pattern)


# In[62]:


# Answer 19


# In[63]:


def convert_date_of_yyyy_mm_dd_format_to_dd_mm_yyyy_format(date_string):
 
  pattern = '^(\d{4})-(\d{1,2})-(\d{1,2})$'
  match = re.match(pattern, date_string)
  if match:
    return f'{match.group(2)}-{match.group(1)}-{match.group(3)}'
  else:
    return None


# In[64]:


date_string = '2023-07-16'

print(convert_date_of_yyyy_mm_dd_format_to_dd_mm_yyyy_format(date_string))


# In[65]:


# Answer 20


# In[66]:


def find_all_words_starting_with_a_or_e_in_a_given_string(string):
 
  pattern = '^[ae]\w+'
  matches = re.findall(pattern, string)
  return matches


# In[68]:


string = 'Chester Bennington was a great singer.'

print(find_all_words_starting_with_a_or_e_in_a_given_string(string))


# In[69]:


# Answer 21


# In[71]:


def separate_and_print_numbers_and_their_position_of_a_given_string(string):
  
  pattern = '\d+'
  matches = re.finditer(pattern, string)
  for match in matches:
    print(f'{match.group()} at {match.start()}')


# In[72]:


string = 'The quick brown fox jumps over the lazy dog. 12345 67890'

separate_and_print_numbers_and_their_position_of_a_given_string(string)


# In[73]:


# Answer 22


# In[74]:


def extract_maximum_numeric_value_from_a_string(string):
 
  pattern = '\d+\.?\d*'
  matches = re.findall(pattern, string)
  max_value = max(int(match) for match in matches)
  return max_value


# In[75]:


string = 'The quick brown fox jumps over the lazy dog. 12345 67890'

print(extract_maximum_numeric_value_from_a_string(string))


# In[76]:


# Answer 23


# In[77]:


def put_spaces_between_words_starting_with_capital_letters(string):
  
  pattern = '([A-Z])\w+'
  result = re.sub(pattern, r'\1 \2', string)
  return result


# In[79]:


string = 'The quick Brown Fox jumps over the lazy dog.'

print(string)


# In[80]:


# Answer 24


# In[81]:


def find_sequences_of_one_upper_case_letter_followed_by_lower_case_letters(string):
 
  pattern = '[A-Z]\w+'
  matches = re.findall(pattern, string)
  return matches


# In[82]:


string = 'The quick Brown Fox jumps over the lazy dog.'

print(find_sequences_of_one_upper_case_letter_followed_by_lower_case_letters(string))


# In[83]:


# Answer 25


# In[84]:


def remove_duplicate_words_from_sentence_using_regular_expression(sentence):
 
  pattern = '\b(\w+)(?:\s+\1)+\b'
  result = re.sub(pattern, r'\1', sentence)
  return result


# In[85]:


sentence = 'The quick brown fox jumps over the lazy dog. The quick brown fox.'

print(remove_duplicate_words_from_sentence_using_regular_expression(sentence))


# In[86]:


# Answer 26


# In[87]:


def alphanumeric_string(text):
  pattern = r"\w$"
  if re.search(pattern, text):
    return True
  else:
    return False


# In[88]:


print(alphanumeric_string("This is a string"))


# In[89]:


print(alphanumeric_string("This is not a string"))


# In[90]:


# Answer 27


# In[91]:


def extract_hashtags(text):
  pattern = r"#(\w+)"
  hashtags = re.findall(pattern, text)
  return hashtags


# In[92]:


text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = extract_hashtags(text)


# In[93]:


print (hashtags)


# In[94]:


# Answer 28


# In[95]:


def remove_unicode_symbols(text):
  pattern = r"<U\+.+>"
  text = re.sub(pattern, "", text)
  return text

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

new_text = remove_unicode_symbols(text)


# In[96]:


print (new_text)


# In[ ]:


# Answer 29


# In[100]:


import datetime


# In[101]:


def extract_dates(text):
  pattern = r"\d{2}[-/]\d{2}[-/]\d{4}"
  dates = re.findall(pattern, text)
  for date in dates:
    date = datetime.datetime.strptime(date, "%d-%m-%Y")
    yield date

text = """Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."""

dates = extract_dates(text)
for date in dates:
    print (date)


# In[102]:


# Answer 30


# In[103]:


def replace_special_characters(text):
  pattern = r"[\s,.]"
  replacement = ":"
  new_text = re.sub(pattern, replacement, text)
  return new_text

text = "Python Exercises, PHP exercises."

new_text = replace_special_characters(text)


# In[104]:


print (new_text)


# In[ ]:





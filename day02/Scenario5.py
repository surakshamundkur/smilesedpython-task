text = "This is a sample text for analysis."

#1.	Extract the first three words:
text = "This is a sample text for analysis."
words = text.split()
first_three_words = ''.join(words[:3]) #This joins the first three words back together into a single string separated by spaces using the join() method.
print(f"First three words: {first_three_words}")
#################################
text = "This is a sample text for analysis."
words = text.split()
first_three_words = ' '.join(words[:3]) #This joins the first three words back together into a single string separated by spaces using the join() method.
print(f"First three words: {first_three_words}")

#2.	Extract the substring from "sample" to "analysis" (inclusive):
start_index = text.find("sample")
end_index = text.find("analysis") + len("analysis")
extracted_substring = text[start_index:end_index]
print(f"Extracted substring: {extracted_substring}")
#######################################
start_index = text.find("sample")
end_index = text.find("analysis") 
extracted_substring = text[start_index:end_index]
print(f"Extracted substring: {extracted_substring}")



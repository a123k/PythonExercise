1. To test the program execute 'test.py' file
2. In test.py file
     a) Provide the file name and number of top occurrences while calling 'test_app' function from main.
     b) Provide 'expected_result' value in 'test_app' function as it will be matched with actual value from program
3. 'application.py' file contains actual logic to count and print the top frequent occurring words in a file
    a) The function 'run_application' executes 'find_most_common_words' to get the common words and
    b) Then executes 'output_to_console' to print the value
    Sample output:
    Word - Occurrences
    cat - 5
    rabbit - 2
    apple -1

Following Points have been considered in the program
a) How do you define a word?
   Any character or a group of characters separated by whitespace is considered as Word.
   Also in this program word is considered as case sensitive. for Example cat, Cat, CAT, caT, cAt all are considered as different words

b) What does the standard Python library provide to help with the implementation of function 2? Do you have to write everything yourself, or can you use the standard library for the heavy lifting?
Existing Standard Library function such as 'most_common(n)' does not help as this function returns top n words, but words with same number of occurrences do not appear in sorted order which is required to identify 'TOP' frequent words.
So, another Standard library function 'sorted' is used to sort the List which is efficient for huge number elements as 'sorted' function simply returns the sorted form of the list without actually physically sorting the list.

c) What do we mean by a ‘text’ file? Say the file contains, Japanese, or Finish words how should the program cope?

If first block of file can be read using Unicode coding, its a text file, else its not text file. This logic is implemented in 'isfile_text' function in 'application.py' file
To handle all type of characters Unicode encode is used.

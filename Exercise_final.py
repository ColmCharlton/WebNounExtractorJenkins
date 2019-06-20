from urllib.request import urlopen
from collections import Counter
import re
import os

class Extractor:


    #Fetches words from webpage
    def fetch_content(self, url):
        try:
            with urlopen(url) as content:
                content_words = []
                for line in content:
                    line_words = line.decode('utf-8').split()
                    for word in line_words:
                        content_words.append(word)
            return content_words

        except Exception as e: print(e)

    #This method removes all Html tags
    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        try:
            clean = re.compile('<.*?>')  # Match all occurences of characters inside the bracets
            return re.sub(clean, '', text)
        except Exception as e: print(e)

    # This method removes most javascrtpt tags using the ajax $ as the key word
    def remove_javascript(self, text):
        try:
            content_words = []
            line_words = text.split()
            x = list(line_words)
            for word in x:
                if not word.lstrip().startswith('$'):   #If word in text = character break
                    # if y != "$":
                    content_words.append(word)
                else:
                    break
                
            str1 = ' '.join(content_words)  

            return str1
        except Exception as e: print(e)


    #This method removes all text before word given
    def remove_text_before_this_word(self, text, word):
        try:
            before = re.split('\\b' + word + '\\b', text)[-1]
            return before
        except Exception as e: print(e)

    # This method removes all text after word given
    def remove_text_after_this_word(self, text, word):
        try:
            after = re.split('\\b' + word + '\\b', text)[0]
            return after
        except Exception as e: print(e)

    # This method removes all Non alphabic characters
    def remove_Non_Al_Num(self, text):
        try:
            # pattern = '\w'  #Match all non numerical characters
            pattern = '\W'
            t = re.split(pattern, text) #splits string
            # t = re.findall(pattern, text)
            str1 = ' '.join(t)  #joins string again

            return str1
        except Exception as e: print(e)


    def remove_decimal(self ,text):
        try:
            pattern = '\d'  # Match all decimal digit
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            decimal = ' '.join(t)
            return decimal


        except Exception as e: print(e)


    def remove_whiteSpace(self ,text):

        try:
            pattern = '\s'  # match all white space
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            whiteSpace = ' '.join(t)
            return whiteSpace

        except Exception as e: print(e)


    #print item method
    def print_items(self ,items):
        for word in items:
            print(word)



    #Data to be saved = words, save is the file name
    def save(self,words, save):
        try:
            with open(save, "w") as text_file:
                print(f"{words}", file=text_file)


        except Exception as e:
            print(e)



    def run(self):

        try:
            E = Extractor()

            content = E.fetch_content('https://www.rte.ie/news/')
            # content = fetch_content('https://www.bbc.com/news')

            str1 = ' '.join(content)  # Joins strings otherwise error is produced
            # print(str1)
            htmlRemove = E.remove_html_tags(str1)  # Remmoves html taga
            # print(htmlRemove)

            remove_java = E.remove_javascript(htmlRemove)  # Reomves java script
            # print(remove_java)

            # Varibales to be degsenated throough constructor, removes any unwanted code above and below the words passed into the method
            before = 'Javascript'
            after = 'cookies'

            # To remove text before kyeword
            remove_text_before = E.remove_text_before_this_word(remove_java,
                                                                before)  # Should be a variable passed in through the constructor
            # print(remove_text_before)

            # To remove text before kyeword
            remove_text_after = E.remove_text_after_this_word(remove_text_before,
                                                              after)  # #Should be a variable passed in through the constructor
            # print(remove_text_after)

            # These methods are to ensure only text is outputed
            Al_num_Remove = E.remove_Non_Al_Num(remove_text_after)
            decimal_remove = E.remove_decimal(Al_num_Remove)
            whitespace = E.remove_whiteSpace(decimal_remove)

            final = whitespace  # the final output after all cleaning is done

            E.save(final, 'HTMLRemoved.txt')


        except Exception as e:
            print(e)



class Key_Noun:

    # Open file
    def openFile(self, file):
        try:
            with open(file, "r") as filterlist:
                # print(filterlist.read())
                words = []
                for line in filterlist:
                    line_words = line.split()
                    for word in line_words:
                        words.append(word)
            return words


        except Exception as e:
            print(e)



    # # Data to be saved = words, save is the file name with the current date appended
    def save(self, words, save):
        import time
        try:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            # print(timestr)

            # Check if there is a current file named as above if so create a new one
            with open(save + "%s.txt" % timestr, "w") as text_file:
                print(f"{words}", file=text_file)


        except Exception as e:

            print(e)


    # Search using filterlist/exclusion list
    def search_items(self, words, filterlist):
        try:
            words1 = []
            for word in words:
                if word not in filterlist:
                    words1.append(word)
            return words1


        except Exception as e:

            print(e)


    # print method
    def print_items(self, items):
        for word in items:
            print(word)

    def run(self):
        try:
            K = Key_Noun()  # instatiate class
            inputText = K.openFile("HTMLRemoved.txt")  # Open and store the htmlRemoved content
            words1 = [x.lower() for x in inputText]  # Ensure all the text is in lower case

            # Using an exclusion list, find only the action words in the page
            Exclusion_list_Keywords = K.openFile("ExclusionList_Keywords.txt")
            result_Action_Words = K.search_items(words1, Exclusion_list_Keywords)
            # print(Counter(result_Action_Words))                                     #To count occurances of words for keyword analysis

            # Using an exclusion list, find only the nouns in the page
            Exclusion_list = K.openFile("ExclusionList.txt")
            result_Nouns = K.search_items(words1, Exclusion_list)
            result_Nouns_Count = Counter(result_Nouns)
            # print(Counter(result_Nouns_Count))
            # print(result_Nouns)
            K.save(result_Nouns, "Noun_List")

            # Using results from nouns as an exclusion list, to find only the action words in the page
            result_Action_Words_Final = K.search_items(result_Action_Words, result_Nouns)
            # print(Counter(result_Action_Words_Final))


        except Exception as e:

            print(e)



#This class retrieves files from the directory, sorts and compares them
class retrieve_sort_compare:


    mypath = 'C:\\pyfund\\Exercise1'

    # Lists files in this directory and searches for specific files
    def retrieve_sort(self):

        try:
            files = os.listdir(retrieve_sort_compare.mypath)
            mylist = []
            for file in files:
                if file.lstrip().startswith('Noun'):  # Search for only the keywrd Noun
                    mylist.append(file)
                mylist.sort(reverse=True)
            # print(mylist)
            # print(mylist[0])
            # print(mylist[1])

            a = mylist[0]
            b = mylist[1]

            return mylist   #Return a the last two entries in the list


        except Exception as e:

            print(e)


    #This method takes in two files an compares them, if there is no change then it returns same
    def compare(self, file1, file2):
        try:
            with open(file1, "r") as f1:
                f1_text = f1.read()
            with open(file2, "r") as f2:
                f2_text = f2.read()
            # Find and print the diff:

            # Cast to a set
            A = {f1_text}
            B = {f2_text}

            # print(A.difference(B))
            # print(B.difference(A))

            compare_result = A.difference(B)

            if len(compare_result) == 0:
                print("No change")
            else:
                print(compare_result)
                # compare_result_Count = [Counter(compare_result)]
                # print(Counter(compare_result_Count))

            return


        except Exception as e:

            print(e)



    #This method is used to run the class
    def run(self):
        try:
            CC = retrieve_sort_compare()
            CC.retrieve_sort()
            # print(CC.retrieve_sort())

            # List of the last two elements has been returned
            list = CC.retrieve_sort()
            # print(list)
            # Passing releveant files to check content
            CC.compare(list[0], list[1])
            # CC.compare('Noun_List.txt', 'Noun_List20190619-153127.txt')


        except Exception as e:

            print(e)




# main method
def main():

        E = Extractor()
        E.run()

        K = Key_Noun()
        K.run()

        C = retrieve_sort_compare()
        C.run()



    # Runs script in shell
if __name__ == '__main__':
        main()





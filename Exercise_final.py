import os
import re
from collections import Counter
from urllib.request import urlopen


import os
import re
from collections import Counter
from urllib.request import urlopen


class Extractor:

    # Fetches words from webpage
    def fetch_content(self, url):
        try:
            with urlopen(url) as content:
                content_words = []
                for line in content:
                    line_words = line.decode('utf-8').split()
                    for word in line_words:
                        content_words.append(word)
            return content_words

        except Exception as e:
            print(e)

    # class SubTextRemove:
    # This method removes all Html tags
    import re
    from urllib.request import urlopen
    def remove_script_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<script.*?>?</script>'
            clean = re.compile(pattern)
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_noscript_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<noscript.*? >?</noscript>'
            clean = re.compile(pattern)
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_iframe_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<iframe.*?>?</iframe>'
            clean = re.compile(pattern)
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_a_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<a.*?>?</a>'
            clean = re.compile(pattern)
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_input_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<input.*?>'
            clean = re.compile(pattern)
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        try:
            pattern = '<.*?>'
            clean = re.compile(pattern)  # Match all occurences of characters inside the bracets
            f = ''.join(re.sub(clean, '', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeAllNumericalCharacters(self, text):
        """Remove html tags from a string"""
        try:
            pattern = r'[^A-Za-z0-9]+'
            clean = re.compile(pattern)  # Match all occurences of characters inside the bracets
            f = ''.join(re.sub(clean, ' ', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    # class SplitTextRemove:
    # These methods split text after a certain point
    def remove_text_before_this_word(self, text, word):
        try:
            before = re.split('\\b' + word + '\\b', text)[-1]
            return before

        except Exception as e:
            print(e)

    def remove_text_after_this_word(self, text, word):
        try:
            after = re.split('\\b' + word + '\\b', text)[0]
            return after
        except Exception as e:
            print(e)

    def remove_Non_Al_Num(self, text):
        try:
            # pattern = '\w'  #Match all non numerical characters
            pattern = '\W'
            t = re.split(pattern, text)  # splits string
            str1 = ' '.join(t)  # joins string again

            return str1
        except Exception as e:
            print(e)

    def remove_decimal(self, text):
        try:
            pattern = '\d'  # Match all decimal digit
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            decimal = ' '.join(t)
            return decimal

        except Exception as e:
            print(e)

    def remove_whiteSpace(self, text):
        try:
            pattern = '\s'  # match all white space
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            whiteSpace = ' '.join(t)
            return whiteSpace
        except Exception as e:
            print(e)

    #
    # def removeTo(self,text):
    #     """Remove html tags from a string"""
    #     pattern = re.compile('<span.*></span>')  # Match all occurences of characters inside the bracets
    #     # pattern = re.compile('<h3.*></h3>')
    #     pattern = re.compile('<body.*></body>')
    #     pattern2 = re.compile('<iframe.*></iframe>')
    #
    #     pattern3 = re.compile('<h1.*></h1>')
    #
    #     # pattern.fullmatch(text)
    #     # pattern.search(text)
    #
    #     matches = re.findall(pattern3, text)
    #     f = ''.join(matches)  # Joins strings otherwise error is produced
    #
    #     # t = re.sub(pattern, ' ', text)
    #
    #     return f
    #

    # class FindallTextRemove:
    # All these methods are used to find the text in between the tags and return it, abstract?

    def removeTo(self, text, pattern):
        """Remove all but the body, from a string"""
        try:
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeToBody(self, text):
        """Remove all but the body, from a string"""
        try:
            pattern = re.compile('<body.*>?</body>')
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeToDiv(self, text):
        """Remove all divs from a string and return"""
        try:
            pattern = re.compile('<div.*')
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeToHead(self, text):
        """Remove all but the head, from a string"""
        try:
            pattern = re.compile('<head.*?>?</head>')
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    # def run(self):
    #     try:
    #         f = FindallTextRemove()
    #         f.removeTo('<body.*>?</body>')
    #         f.removeTo('<div.*')
    #         f.removeTo('<head.*?>?</head>')
    #
    #
    #     except Exception as e:
    #         print(e)

    # Data to be saved = words, save is the file name

    def save(self, words, save):

        try:
            with open(save, "w") as text_file:
                print(f"{words}", file=text_file)
        except Exception as e:
            print(e)

    # def run(self, url):

    def run(self, url):

        try:
            E = Extractor()

            # content = E.fetch_content('https://edition.cnn.com') #  very odd, has the content in the header, in a script tag
            # content = E.fetch_content('https://www.rte.ie/news/')
            # content = E.fetch_content('https://www.bbc.com/news')
            # content = E.fetch_content('https://www.thefreedictionary.com/')
            # content = E.fetch_content('https://www.euronews.com')

            content = E.fetch_content(url)

            # print(content)

            str1 = ' '.join(content)  # Joins strings otherwise error is produced
            # print(str1)

            body = E.removeToBody(str1)
            # print(body)

            # head = removeToHead(str1)
            # print(head)

            saveDivs = E.removeToDiv(body)

            # print(saveDivs)
            scripts = E.remove_script_tags(saveDivs)

            noscripts = E.remove_noscript_tags(scripts)
            # print(noscripts)

            noiframes = E.remove_iframe_tags(noscripts)
            # print(noiframes)

            # Can't do this
            # noatag = remove_a_tags(noiframes)
            # print(noatag)

            noinput = E.remove_input_tags(noiframes)
            # print(noinput)

            no_html = E.remove_html_tags(noiframes)
            # print(no_html)

            num_char = E.removeAllNumericalCharacters(no_html)
            # print(num_char)

            removeNon_Al_Num = E.remove_Non_Al_Num(num_char)
            # print(removeNon_Al_Num)

            clean = E.remove_decimal(removeNon_Al_Num)

            # print(clean)
            #
            print(E.remove_whiteSpace(clean))
            final = clean

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


    #method to count instance of each word
    def word_count(self, str):
        counts = dict()
        words = str.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts


    # Remove duplicate members
    def unique_list(self, list):
        ulist = []
        [ulist.append(x) for x in list if x not in ulist]
        return ulist


    def run(self, url):
        try:
            K = Key_Noun()  # instatiate class
            inputText = K.openFile("HTMLRemoved.txt")  # Open and store the htmlRemoved content
            words1 = [x.lower() for x in inputText]  # Ensure all the text is in lower case


            #Create an abstract class

            #Create a Noun method
            # Using an exclusion list, find only the nouns in the page
            Exclusion_list = K.openFile("ExclusionList.txt")
            result_Nouns = K.search_items(words1, Exclusion_list)
            result_Nouns_Count = Counter(result_Nouns)
            # print(Counter(result_Nouns_Count))
            # print(result_Nouns)
            Nounstr1 = ' '.join(result_Nouns)
            # print(K.word_count(str1))

            CountNouns = K.word_count(Nounstr1)    #Counts the number of instances of a word
            # print(sorted([(value, key) for (key, value) in CountNouns.items()], reverse=True))   #Sorts the list and prints
            CountNounsSort = sorted([(value, key) for (key, value) in CountNouns.items()], reverse=True)
            print("\nNouns list sorted \n", CountNounsSort)

            # print(str1) #Prints the joined list
            Nounfinal = ' '.join(K.unique_list(Nounstr1.split()))   #Method to remove duplicte words
            print("\nNouns list \n",Nounfinal)
            K.save(Nounfinal, "Noun_List_")# + url + "_")





            # Create a Verb method
            # Using an exclusion list, find only the action words in the page
            Exclusion_list_Keywords = K.openFile("ExclusionList_Keywords.txt")
            result_Action_Words = K.search_items(words1, Exclusion_list_Keywords)
            # print(Counter(result_Action_Words))  # To count occurances of words for keyword analysis

            # Using results from nouns as an exclusion list, to find only the action words in the page
            result_Action_Words_Final = K.search_items(result_Action_Words, Nounfinal)
            # print(Counter(result_Action_Words_Final))

            Verbstr1 = ' '.join(result_Action_Words_Final)
            CountVerbs = K.word_count(Verbstr1)    #Counts the number of instances of a word
            # print(sorted([(value, key) for (key, value) in CountVerbs.items()], reverse=True))   #Sorts the list and prints
            CountVerbSort = sorted([(value, key) for (key, value) in CountVerbs.items()], reverse=True)  # Sorts the list and prints

            print("\nKey list sorted \n", CountVerbSort)

            Keystrl = ' '.join(result_Action_Words_Final)
            KeyFinal = ' '.join(K.unique_list(Keystrl.split()))  # Method to remove duplicte words

            print("\nKey list \n", KeyFinal)
            K.save(KeyFinal, "Verb_List_")
        except Exception as e:
            print(e)



#This class retrieves files from the directory, sorts and compares them
class retrieve_sort_compare:


    mypath = 'C:\\pyfund\\Exercise1'

    # Lists files in this directory and searches for specific files
    def retrieve_sort(self, filename):

        try:
            files = os.listdir(retrieve_sort_compare.mypath)
            mylist = []
            for file in files:
                if file.lstrip().startswith(filename):  # Search for only the keywrd Noun
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
    def compare(self, file1, file2, str):
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
                print("\n No change")
            else:
                # print(compare_result)
                print("\n The " + str + " that have changed are: \n")
                str1 = ' '.join(compare_result)  # Joins strings otherwise error is produced
                print(str1)
                # str2 = ''.join(str1)  # Joins strings otherwise error is produced
                # compare_result_Count = Counter({str1})
                # print(str2)
                # print(compare_result_Count)

            return


        except Exception as e:

            print(e)



    #This method is used to run the class
    def run(self):
        try:
            CN = retrieve_sort_compare()    #Create instance of object
            # CC.retrieve_sort('Noun') #Searches for files with the key word 'Noun'
            # print(CC.retrieve_sort())

            # List of the last two elements has been returned
            list = CN.retrieve_sort('Noun')
            # print(list)
            # Passing releveant files to check content
            CN.compare(list[0], list[1], 'Noun')
            # CC.compare('Noun_List.txt', 'Noun_List20190620-131122.txt')


            CV = retrieve_sort_compare()
            list = CV.retrieve_sort('Verb')
            # Passing releveant files to check content
            CV.compare(list[0], list[1], 'Verb' )




        except Exception as e:

            print(e)




# main method
def main(url):

        E = Extractor()
        E.run(url)

        K = Key_Noun()
        K.run(url)

        C = retrieve_sort_compare()
        C.run()



    # Runs script in shell
if __name__ == '__main__':
        main('https://www.bbc.com/news')





# # main method
# def main(url):
#
#         E = Extractor()
#         E.run(url)
#
#
#
#     # Runs script in shell
# if __name__ == '__main__':
#         main('https://www.bbc.com/news')
#

import pyttsx3
import PyPDF2
mybook = open('DLML.pdf', 'rb') #directory to open the pdf file
pdfReader = PyPDF2.PdfFileReader(mybook) #reading the pdf file by using the book
readingpages = pdfReader.numPages #printing how many pages exist in the pdf
# print (pages) #printing how many pages exist in the pdf
speaker = pyttsx3.init() #speech assist
speaker.setProperty("rate", 150) #changing the default speech rate
startoffpage = pdfReader.getPage(16) #start off page to read
text = startoffpage.extractText() #extracting the text from the page
speaker.say(text) #speaking the text

# uncomment the following line to save the audio file
# speaker.save_to_file(text, 'DLML.mp3')

speaker.runAndWait() #running the text
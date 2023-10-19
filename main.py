#Import required packages
import glob
import PyPDF2
import pandas as pd

path = "" #Enter pathname here with all .pdf files

#Query all MRI reports
pdf_lists = sorted(glob.glob(path))

#Create empty list to store subject_id and MRI impressions

data = []

for i in range(len(pdf_lists)):
    #Extract subject_id for PDF file path
    sub_id = pdf_lists[i].split('\\')[-1].split('.pdf')[0]
    
    # creating a pdf file object
    pdfFileObj = open(pdf_lists[i], 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pageObj = pdfReader.pages[0]
    page = pageObj.extract_text()
    page = page.replace('\n \n',', ').replace('\n','')
    
    #Custom extraction of texts from MRI files
    impression = page[page.find("IMPRESSION"):page.find("DR M L")].replace("R E","RE").replace("  ,  ","").replace("ION","ION:")
    fazekas_score = page[page.find("FAZ"):page.find("FAZ")+11]
    if len(impression) == 0:
        impression = page[page.find("IMPR ESSION"):page.find("DR M L")].replace("R E","RE").replace("  ,  ","").replace("ION","ION:")
    
    if len(fazekas_score) == 0:  
        data.append([sub_id,impression,'NO SCORE'])
    else:
        data.append([sub_id,impression,fazekas_score])
        
    print(sub_id,':DONE')

#Save the extracted data
destination_path = ""
save_data_to_csv = pd.DataFrame(data,columns=['SubID','Comments','Fazekas']).to_csv(destination_path)
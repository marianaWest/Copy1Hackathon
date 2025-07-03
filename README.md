# Dataset overview

## Historical background

In the 1860s photography as a medium and industry was coming under scrutiny due to its rapid development. Issues of ownership and copyright were becoming impossible to ignore and so debates ensued around how photography should be defined and protected under the law. This culminated in the 1862 Fine Arts Copyright Act, which in turn required the registration of photographs, paintings and drawings with the Stationers’ Company, a system which continued for almost 50 years. 
Those registering a work were instructed to enter a description of the work being registered, along with the name and place of abode of the copyright owner (or proprietor of copyright) and the name and place of abode of the copyright author (the artist or photographer). The forms were then dated and signed by the owner and in many cases a copy of the work (in the form or a print or sketch) was attached to the form.
These registration forms and attached artwork, along with related registers and indexes were eventually transferred to the Public Record Office, now The National Archives (TNA). This collection (COPY 1) now comprises potentially over 400,000 individual entry forms. 

![image](https://github.com/user-attachments/assets/461f961e-efea-421d-93a4-5a3c3b01c15b)

![image](https://github.com/user-attachments/assets/4f7bb20a-f7f0-4f5c-827d-e8dd3aa157d3)

Fig. 1 and 2. Examples of a deposited image and its associated registration form.


## Catalogue records

The individual entry forms registering photographs (COPY 1 – Photographs) have been fully transcribed and catalogued by volunteers and metadata is openly available and downloadable from TNA’s online catalogue Discovery. The metadata includes each document classification and the full transcription of the description of the photograph, as well as the key stakeholders (copyright depositor and owner) and the location of the registration. However these are conflated in the “Description” field, making the downloaded metadata only semi-structured.


![image](https://github.com/user-attachments/assets/2f93df8e-2eee-4c0f-8bf2-a84b1efc2621)

Fig. 3. Example of a catalogue record at The National Archives.



# Guide to the data

_to be edited_

## RAW Catalogue files

The COPY 1 Photography collection can be downloaded from [The National Archives catalogue](https://discovery.nationalarchives.gov.uk/)
To do so:
* Go to "Advanced search"
* Search for "Photographs" and restrict the references field to "COPY 1" (see screenshot below)
* Filter the results by:
    * *Held by*: The National Archives
    * *Collection*: COPY
    * *Catalogue level*: Piece
* Once filtered the results, click "Export results" on the ribbon and choose the preferred format

<img width="500" alt="image" src="https://github.com/user-attachments/assets/70d37ae2-7c70-48cb-84bd-cdb1356ccab6" /><br />

<img width="500" alt="image" src="https://github.com/user-attachments/assets/ce166cd5-bada-42b3-8038-397d996a20b1" /><br />


## Processed metadata
The catalogue entries in Discovery are formatted for presentation on the web and therefore contain HTML tags. In addition, the information in the catalogue is captured in a semi-structured format with field names (e.g. Copyright owner of work). As an added convenience we have used regular expressions to parse the catalogue entries and separate them into field-value pairs which have been added to the json files.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/16aeebb9-d89e-45cf-a57d-3f8809f511ef" />

The **Metadata** folder contains two versions of the processed data:
* [Processed metadata JSON][Metadata](Metadata/Processed metadata/COPY 1 processed json.zip)
* [Processed metadata TSV][Metadata](Metadata/Processed metadata/COPY 1 processed tsv.zip)


## Split metadata
Despite the convenience of processed metadata, the dataset retains quite a lot of inconsistencies that can limit its use. 
One such examples are the copyright owners and authors addresses:

![image](https://github.com/user-attachments/assets/91d0ddf3-2d5f-4b6b-835a-457ac7d724d9)


There are two folders, one for Images and one for Metadata. The images are all extracted from the PDFs available to download at: https://discovery.nationalarchives.gov.uk/details/r/C325807

The images are digitised versions of forms submitted to the Stationer's Company in the first quarter of 1883 to register the copyright of photographs or other artworks. Generally, a form is filled in with a description of the photography/art and details of the Author and Owner of the Copyright. A copy of the copyrighted image is attached to the form. In most cases, therefore, there are two digitised versions of each form - one with the image visible, and another with it folded out the way so that the details of the form are visible. This is not always the case.

The metadata folder contains three files. The larger copy1_catalogue.zip file contains 275 json files derived from the The National Archives' Discovery catalogue. A tabular (tab separated) version of this data is also available in the copy1_catalogue_tsv.zip file.

The COPY 1 collection can be viewed in its entirety at this link: https://discovery.nationalarchives.gov.uk/results/r?_q=copy+1&_hb=tna&_d=COPY&Refine+departments=Refine

An example of a single catalogue record can be found here: https://discovery.nationalarchives.gov.uk/details/r/C9082740

Each of the json records represents a box of forms. The reference number (C32.....) at the beginning of each json file name is the Discovery reference number which can be appended to the following URL to find it in the catalogue: https://discovery.nationalarchives.gov.uk/details/r/

You can also browse the contents of a box by appending the same reference number to: https://discovery.nationalarchives.gov.uk/browse/r/h/

The images in the Images folder are from box 60 (reference COPY 1/60, see: https://discovery.nationalarchives.gov.uk/browse/r/h/C325807). Each individual form has a number stamped on it (usually in the top right hand corner, but sometimes further down). That number completes the catalogue reference for that specific form. So the form with number 22 on it has reference COPY 1/60/22. The file names of the images in the Image folder do not match those reference numbers (since there is not a 1:1 relationship between images and forms), so the image file names have been added into the json file for this box only. As it is a special case the file C325807_catalogue_structure.json has been copied into the Metadata folder outside of the zip file for convenience.

Finally, for COPY 1/60 we have experimented with the Llama 3.2 LLM to further process the catalogue entries so that names and addresses are separated into the individual fields within the json.

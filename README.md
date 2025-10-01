# Dataset overview


## Historical background

In the 1860s photography as a medium and industry was coming under scrutiny in Britain due to its rapid development. Issues of ownership and copyright were becoming impossible to ignore and so debates ensued around how photography should be defined and protected under the law. This culminated in the 1862 Fine Arts Copyright Act, which in turn required a system of registration of photographs, paintings and drawings with the Stationers’ Company, a system which continued for almost 50 years. 
Those registering a work were instructed to complete a form entering a description of the work being registered, along with the name and address of the copyright owner (or proprietor of copyright) and the name and address of the copyright author (the artist or photographer). The forms were then dated and signed by the owner and in many cases a copy of the work (in the form or a print or sketch) was attached to the form.
These registration forms and attached artwork, along with related registers and indexes were eventually transferred to the Public Record Office, now The National Archives (TNA). This collection (COPY 1) now comprises potentially over 400,000 individual entry forms. 

<kbd><img src="https://github.com/user-attachments/assets/461f961e-efea-421d-93a4-5a3c3b01c15b" width="600" border="2px"></kbd><br />

<kbd><img src="https://github.com/user-attachments/assets/4f7bb20a-f7f0-4f5c-827d-e8dd3aa157d3" width="600" border="2px"></kbd><br />

Fig. 1 and 2. Examples of a deposited image and its associated registration form.



## Catalogue records

The individual entry forms registering photographs (COPY 1 – Photographs) have been fully transcribed and catalogued by volunteers and metadata is openly available and downloadable from TNA’s online catalogue Discovery. The metadata includes each document classification and the full transcription of the description of the photograph, as well as the key stakeholders (copyright depositor and owner) and their addresss. However these individual pieces of information are conflated in the “Description” field, making the downloaded metadata only semi-structured.

<kbd><img src="https://github.com/user-attachments/assets/2f93df8e-2eee-4c0f-8bf2-a84b1efc2621" width="600" border="2px"></kbd><br />

Fig. 3. Example of a catalogue record at The National Archives.



# Guide to the data

The **Metadata** folder contains two sets of metadata and some data cleaning instruction:

* COPY 1 Processed data
* COPY 1 Split data

We haven't included raw data, as this can easily be downloaded from Discovery following the instruction below. 



## RAW Catalogue files

Metadata for the COPY 1 Photography collection can be downloaded from [The National Archives catalogue](https://discovery.nationalarchives.gov.uk/). When using the catalogue, an *item* is an individual entry form and attached photograph. A *piece* is a box of entry forms with attached photographs.

To download metadata from the catalogue:

* Go to "Advanced search"
* Use the following options
    * *Any of these words*: Photographs
    * *Any of these references*: COPY 1
    * *Date range*: Select a date range
    * *Held by*: The National Archives
    * *Catalogue level*: Item

<kbd><img src="https://github.com/user-attachments/assets/70d37ae2-7c70-48cb-84bd-cdb1356ccab6" width="600" border="2px"></kbd><br />

* Click "Search"
* Click "Export results" on the ribbon and choose the preferred format.

<kbd><img width="644" height="344" alt="image" src="https://github.com/user-attachments/assets/cd4a5701-1af1-4f8a-9a06-fbc6038fdb39" />

Exporting all of your results is only possible when there are fewer than 10,000 results. If you wish to export more, read the guidance on using our Discovery API [here](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/).

An example of a catalogue record for an individual entry form and photograph can be found at https://discovery.nationalarchives.gov.uk/details/r/C9082740
You can also browse the contents of a piece by appending the same reference number found at the end of the URL (e.g. C9082740) to: https://discovery.nationalarchives.gov.uk/browse/r/h/

Pieces **COPY 1/1 - COPY 1/60** and **COPY 1/364 - COPY 1/566** have all been individually catalogued to item level by volunteers. Other pieces in the collection include drawings and other copyrighted material. These are in the process of being catalogued to item level and the full metadata will be available in the future. 

## COPY 1 processed metadata

The catalogue entries in Discovery are formatted for presentation on the web and therefore contain HTML tags. In addition, the information in the catalogue is captured in a semi-structured format with field names (e.g. Copyright owner of work). As an added convenience we have used regular expressions to parse the catalogue entries and separate them into field-value pairs which have been added to the json files.

<kbd><img src="https://github.com/user-attachments/assets/16aeebb9-d89e-45cf-a57d-3f8809f511ef" width="600" border="2px"></kbd><br />

The **COPY 1 processed data** folder contains two versions of the processed data:
* [Processed metadata JSON](Metadata/COPY 1 processed data/COPY 1 processed json.zip)
* [Processed metadata TSV](Metadata/COPY 1 processed data/COPY 1 processed tsv.zip)

Each of the json records represents a box of forms. 
The reference number (C32.....) at the beginning of each json file name is the Discovery reference number which can be appended to the following URL to find it in the catalogue: https://discovery.nationalarchives.gov.uk/details/r/

For COPY 1/60 we have experimented with the Llama 3.2 LLM to further process the catalogue entries so that names and addresses are separated into the individual fields within the json.



## COPY 1 split metadata

To improve the usability of the dataset, the data from the JSON files was then processed further using a python script.

The script downloads the JSON files, combines them into a single pandas dataframe and performs the following additional processing:
* Splits 'CopyrightOwner' and 'CopyrightAuthor' columns by the first comma into name and address components, and cleans up whitespace and trailing characters.
   * "Copyright owner"  -> "Copyright owner name" AND "Copyright owner address"
   * "Copyright author" -> "Copyright author name" AND "Copyright author address"
* Removes unecessary columns and reoerders columns.
* Allows the user to filter the dataframe by year.
* Saves the filtered DataFrame to a CSV file with a filename that includes the selected year range and downloads the generated CSV file.

The generated CSV file containing the metadata is now ready for further experimentation. A zip file containing a csv of the entire processed and split dataset can be found in the **COPY 1 split data** folder, along with a Jupyter notebook containing the code.

Despite the convenience of processed metadata, the dataset retains quite a lot of inconsistencies that can limit its use. 
One such examples are the copyright owners and authors addresses, which can be inconsistent and are not easily reconcilable:

<kbd><img src="https://github.com/user-attachments/assets/91d0ddf3-2d5f-4b6b-835a-457ac7d724d9" width="600" border="2px"></kbd><br />

This variation is caused by a range of factors: changes in names and addresses over time, different people filling in forms at different times and, most importantly the fact that these historical inconsistencies had been preserved through a transcription process which prioritises precision to guarantee historical accuracy as per best cataloguing practices. Eventually, after some internal experimentation and debate, we opted to preserve these variations rather than standardise them. It was preferable to keep fuzzy but historically authentic data, rather than potentially introduce inaccuracies by editing them.  

The **COPY 1 split data** folder contains :
* [COPY 1 split data](Metadata/COPY 1 split data/COPY 1_json_combined_split.csv)
* [Jupyter notebook](Metadata/COPY 1 split data/COPY1_split_metadata.ipynb)



# Experimentation

The Experimentation folder includes examples of experiments attempted using COPY 1 data. 
Some experiments required extra data, like images of records or examples of stereographic photographs. 
We are keen to hear about other examples of experiments and code, so if you have anything to share, please to get in touch with [katherine.howells@nationalarchives.gov.uk](mailto:katherine.howells@nationalarchives.gov.uk) or [giorgia.tolfo@nationalarchives.gov.uk](mailto:giorgia.tolfo@nationalarchives.gov.uk).



## Collaborative hackathon

In January 2025 a hybrid collaborative hackathon was held at The National Archives. Participants have experimented with the _COPY processed data_ 
Additional material was made available, this included:
* COPY 1/60 images
* Selection of stereoscopic images from different boxes

The outcome of the hackathon and a report of the experiments run by the teams can be accessed reading the co-authored [Collaborative hackathon experimentation report](Collaborative hackathon/Collaborative hackathon experimentation.md)
The hackathon was generously supported by The National Archives strategic research fund 2024/2025.



### Images (COPY 1/60)

The images are digitised versions of forms submitted to the Stationer's Company. A copy of the copyrighted image is attached to the form. In most cases, therefore, there are two digitised versions of each form - one with the image visible, and another with it folded out the way so that the details of the form are visible. This is not always the case.

The images are all extracted from the PDFs available to download at: https://discovery.nationalarchives.gov.uk/details/r/C325807
The images in the Images folder are from box 60 (reference COPY 1/60, see: https://discovery.nationalarchives.gov.uk/browse/r/h/C325807). Each individual form has a number stamped on it (usually in the top right hand corner, but sometimes further down). That number completes the catalogue reference for that specific form. So the form with number 22 on it has reference COPY 1/60/22. The file names of the images in the Image folder do not match those reference numbers (since there is not a 1:1 relationship between images and forms), so the image file names have been added into the json file for this box only. As it is a special case the file C325807_catalogue_structure.json has been copied into the Metadata folder outside of the zip file for convenience.

For COPY 1/60 we have experimented with the Llama 3.2 LLM to further process the catalogue entries so that names and addresses are separated into the individual fields within the json.

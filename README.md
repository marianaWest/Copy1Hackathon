# COPY 1 Hackathon

## Guide to the data
There are two folders, one for Images and one for Metadata. The images are all extracted from the PDFs available to download at: https://discovery.nationalarchives.gov.uk/details/r/C325807

The images are digitised versions of forms submitted to the Stationer's Company in the first quarter of 1883 to register the copyright of photographs or other artworks. Generally, a form is filled in with a description of the photography/art and details of the Author and Owner of the Copyright. A copy of the copyrighted image is attached to the form. In most cases, therefore, there are two digitised versions of each form - one with the image visible, and another with it folded out the way so that the details of the form are visible. This is not always the case.

The metadata folder contains three files. The larger copy1_catalogue.zip file contains 275 json files derived from the The National Archives' Discovery catalogue. A tabular (tab separated) version of this data is also available in the copy1_catalogue_tsv.zip file.

The COPY 1 collection can be viewed in its entirety at this link: https://discovery.nationalarchives.gov.uk/results/r?_q=copy+1&_hb=tna&_d=COPY&Refine+departments=Refine

An example of a single catalogue record can be found here: https://discovery.nationalarchives.gov.uk/details/r/C9082740

Each of the json records represents a box of forms. The reference number (C32.....) at the beginning of each json file name is the Discovery reference number which can be appended to the following URL to find it in the catalogue: https://discovery.nationalarchives.gov.uk/details/r/

You can also browse the contents of a box by appending the same reference number to: https://discovery.nationalarchives.gov.uk/browse/r/h/

The images in the Images folder are from box 60 (reference COPY 1/60, see: https://discovery.nationalarchives.gov.uk/browse/r/h/C325807). Each individual form has a number stamped on it (usually in the top right hand corner, but sometimes further down). That number completes the catalogue reference for that specific form. So the form with number 22 on it has reference COPY 1/60/22. The file names of the images in the Image folder do not match those reference numbers (since there is not a 1:1 relationship between images and forms), so the image file names have been added into the json file for this box only. As it is a special case the file C325807_catalogue_structure.json has been copied into the Metadata folder outside of the zip file for convenience.

## Processed metadata

The catalogue entries in Discovery are formatted for presentation on the web and therefore contain HTML tags. In addition, the information in the catalogue is captured in a semi-structured format with field names (e.g. Copyright owner of work). As an added convenience we have used regular expressions to parse the catalogue entries and separate them into field-value pairs which have been added to the json files.

Finally, for COPY 1/60 we have experimented with the Llama 3.2 LLM to further process the catalogue entries so that names and addresses are separated into the individual fields within the json.

# Collaborative Digital Exploration: exploring the copyright world of early photography

On 27-28th January 2025, The National Archives organised the hybrid “Collaborative Digital Exploration: exploring the copyright world of early photography” hackathon.
As we outlined in [this blog](https://blog.nationalarchives.gov.uk/exploring-early-photography-through-collaborative-digital-experimentation/), the idea of the hackathon was born out of the desire to work collaboratively with the COPY 1 metadata. We were interested in identifying potential new ways of processing, enriching and/or visualizing the metadata, but also to try to test new hybrid collaborative ways of working.
To this end we borrowed the format of the hackathon from the world of software development, and we adapted it to the research context. Since we wanted to approach the collection interdisciplinarily, intersecting for example expertise in copyright law and history with digital humanities, we sent out a call to attract participants with different backgrounds. We kept the technical requirements to the minimum and asked applicants to articulate their interest in the hackathon as well as the reason why it resonated or was relevant to past or present work and research experience.
What follows is a brief outline of ideas explored during the hackathon, compiled with the help of the participants themselves.
 
## Named Entity Recognition and Semantic Classification: connecting people to WikiData, and classification of word tokens

**Team**: 
5 people onsite (Katherine Howell, Colette Townend, Erik, Jonno, Arianna Milighetti)

**Experiments**:
Our team worked on three different tasks.

### Connecting people to WikiData
Using a mix of natural language processing (NLP) techniques, regular expressions, semantic web, and web interfaces our team explored ways to markup and enrich the collection metadata. In particular, we tried to pull out personal names from different metadata fields (photographer, copyright owner, description) and to retrieve their Wikidata QID.
The open linked data database of WikiData opens up possibilities as it connects with other GLAM institutions authority control identifiers, having potential to make subjects and objects in this collection more discoverable to researchers and the general public worldwide, while also providing a potential way for reparative metadata enrichment.
We saw evidence that off-the-shelf large language models (LLM) perform impressively on the WikiData QID matching task, suggesting that they may replace dedicated NLP tools in the near future. 


<kbd ><img src="https://github.com/user-attachments/assets/137d9603-e5f7-4ec7-82a7-0a09fae76f8b" width="600" border="2px"></kbd><br />
_Figure 1. COPY 1/1/34 Metadata_

As an example, the description of COPY 1/2/34 reads as “Photograph of African Princess”. While the Python packages were unable to suggest the correct WikiData ID, ChatGPT had no problem identifying this historical figure as Sara Forbes Bonetta, likely incorporating the contextual semantic information of ‘African Princess’.
As an attempt towards reparative metadata approaches, we uncovered the identities of numerous other prominent figures from African and Asian regions depicted in the archive, such as Ethiopian royal Dejatch Alamayou, and Chung Mow, a Chinese circus performer.


### Prototyping a web interface
Building on the work done extracting personal names and connecting to WikiData IDs, we developed the prototype of a web based interface to view and search results from WikiData using the gathered Wiki IDs. 
This is available to view at: https://tna-named-persons-2.glitch.me/ 

<kbd><img src="https://github.com/user-attachments/assets/7cf61f04-5f77-4a5e-a300-417cbd79089e" width="600" border="2px"></kbd><br />
_Figure 2. Screenshot of web interface_

### Semantic Classification
Finally, we tried to investigate the semantic categories of general word tokens in the descriptions using the rule-based PyMUSAS semantic tagger. PyMUSAS identified the following words in its ‘Drinks’ category, and perhaps unsurprisingly for a largely Victorian archive, the most frequently mentioned drink is tea.

<kbd><img src="https://github.com/user-attachments/assets/4e42abf5-ed5f-4816-ada3-32cb504f63d3" width="600" border="2px"></kbd><br />
_Figure 3. Drinks named in 131,563 Stationer's Company copyright registration forms, as classified by PyMUSAS._

**Methods**: 
Name Entity Extraction:  Python NLP package spaCy, regular expressions;
People WikiData QID retrieval: dedicated Python packages (pymediawiki and wikidata), and OpenRefine, Chat GPT-4o
Semantic classification: spaCy, PyMUSAS
Web interface: Glitch.com running a Fastify/Node.js application 

**Obstacles**: 
A significant obstacle was the accuracy in the identification of named persons in the catalogue data: while SpaCy was able to recognise the most prominent names in the dataset, the NLP package also returned a number of geographical names, company names and string of words misinterpreted as names. Thorough data cleaning would need to take place to ensure the accuracy of the dataset.
Moreover, while the most prominent named persons could be mapped with ease to WikiData by automated tools, less notable names posed more of an issue. In many cases, the names extracted did not have a WikiData entry, but tools such as OpenRefine recognised the name in a homonymous person. The linked data would need to be checked manually to ensure the correct WikiData entry is associated with each name.
The WikiData API does limit the amount of requests that can be done in one go. As a result further work would be needed to do requests in batches and bring back more data. Handling errors caused by empty values within the data. For instance, not every person has a date of birth attached.

**Research potential**:
•	Extract named persons from the archive using named entity recognition in Python/spaCy or LLM
•	Further investigation of semantic classification of words in the archival texts using e.g. PyMUSAS
•	Evaluate the GUI platform OpenRefine as an alternative method to code-based methods
•	Metadata enrichment and linkage to GLAM institutions authority control identifiers to make subjects and objects in this collection more discoverable to researchers and the general public worldwide, as well as to open up new opportunities of digital storytelling
•	Discover lesser known and marginalised or silenced people in descriptions as a form of reparative metadata enrichment 
 

## Data enrichment: identifying, visualizing, and linking place names

**Team**: 
3 people onsite (Simon Wilson, Laurisa Sastoque, George Jukes)

**Experiments**: 
As a group, we aimed to experiment with different tools to enable a geospatial analysis of the dataset. We explored three main pathways: 
I.	Linking to Wikidata Gazetteers: We experimented with extracting place names from the dataset’s description field using Python’s spaCy for named entity recognition (NER) with the goal of linking them to WikiData gazetteers.
II.	Tracking Photograph Movement: Using R for data cleaning and ArcGIS for visualization, we explored the copyright owner and author fields to identify movement patterns of photographs from of creation to registration. 
III.	Country Identification in Descriptions: With OpenRefine, we worked on cleaning description fields to accurately extract country-level locations for improved geocoding.

<kbd><img src="https://github.com/user-attachments/assets/5e82567c-c1e8-4a09-8c1b-1842d3bbf4b8" width="600" border="2px"></kbd><br />
_Fig 4. Preliminary map of copyright owners vs. authors from COPY 1._ [Link to resource](https://www.arcgis.com/apps/mapviewer/index.html?webmap=629efa22176344ac920ee336c08d97df_)

**Methods**:
Name Entity Extraction: Python (spacy);
Data Cleaning and Geolocation: R (tidygeocoder), OpenRefine, ArcGIS

**Obstacles**: 
We encountered challenges with the accuracy and scalability of automated geocoding and text analysis tools like Nominatim and spaCy. Linking description fields to Wikidata gazetteers proved difficult due to inconsistent text formats. Additionally, batch-cleaning data for geocoding required refining regex strategies to meet algorithmic standards.

**Research potential**: 
* enhanced metadata linking in archival datasets;
* improved geocoding and entity recognition could enable richer historical mapping, tracing the movement of copyrighted photographs across time and space;
* future research could refine NER models for historical text, integrate additional gazetteers, and explore machine learning approaches for more precise place-name extraction.


## A photograph, an artwork, or a photograph of an artwork? Separating artforms in copyright descriptions

**Team**: 
4 people onsite, 1 online (Christian Fernandez Perotti, Holly Mangu, Yun Ling, Paula Westenberg)

**Experiment**:
Our team experimented with leveraging Natural Language Processing to analyse the archive's descriptions. The experiment aimed to discover hidden patterns and connections within the archives, which can potentially enhance accessibility to the art collection for researchers, curators, and the public. 


<kbd><img src="https://github.com/user-attachments/assets/ab75b001-564d-4cf2-abeb-1b428174fb81" width="600" border="2px"></kbd><br />

<kbd><img src="https://github.com/user-attachments/assets/c4a8019d-d1b8-4010-9ecc-28b13eec7472" width="600" border="2px"></kbd><br />
_Figure 5 and 6. Examples of queries using Google NotebookLM_
 
**Methods**: 
Thematic classification: Google NotebookLM; 
Metadata enrichment: NotebookLM was able to enrich the dataset with details on the original work referenced and the socio-cultural significance of the particular rendition.

**Obstacles**: 
The main challenge in this experiment concerns the limitations of NLP algorithms in handling ambiguity and context. Interpretation of the analysis' findings requires domain expertise in art history.

**Research potential**: 
* Collection Interconnections: This method could potentially help uncover interconnections within the archives for digital curation. 
* Dataset Enhancement: NotebookLM's ability to summarize and extract key information could be used to enrich the collection with additional contextual information.


## From description to images and from images to description: exploring generative AI

**Team**: 
1 person onsite, 2 online (Valentina Vavassori, Alea Cook, Tamara Tubb)

**Experiment**: 
Our team wanted to test if it is possible to  generate rich descriptive information from images at scale, using off-the-shelf ML/AI tools. The resulting enhanced data will aid pattern finding and inspire further research. We also tested the creation of keywords, asking the tools to create keywords from the generated descriptions.

<kbd><img src="https://github.com/user-attachments/assets/25c2f9db-8cd2-4d77-aa6e-2545b68bac80" width="600" border="2px"></kbd><br />
_Figure 7: COPY 1/60/57 with description generated by Gemini. Original description: 'Photograph of frost scene - trees with railings from foreground to back'._

**Methods**: 
We trialled a range of off-the-shelf AI tools on four different images to identify the most promising and accessible ones. We created a Miro board taking notes of which ones were accessible and which ones did not provide answers at all.

**Obstacles**:
The tools which provided the richest and most accurate results were Claude, ChatGPT, and Gemini. 
However, while testing we realised that most free tools have a limit of the dimensions or number of images that can be used as well as a limited number of prompts. For this reason our sample comprised a set of 13 images and we had to design strategically our prompts, without much scope for refinement.
Despite some promising results, there were striking inaccuracies, hallucinations and assumptions made by the AI.
Some descriptions gave useful added context, but needed to be cross referenced and fact checked against existing data – eg for names of depicted individuals.
The tools were most successful in providing keywords as it removed the more “creative” level of the generated answers.

**Research potential**:
* If applied to the collection images at scale, the enhanced descriptions generated could be used to create visualisations around commonly occurring key words and help identify themes, patterns and narratives within the collection;
help with image detection in records and to make them available for discovery for users.;
* explore the potential of metadata generation through AI and the role of the human in the loop;
* employ techniques such as Retrieval Augmented Generation (RAG) to have more tailored results.
 
 
## Accessing the collection through open standards: a IIIF viewer

**Team**: 
1 person onsite (John Moore)

**Additional data**
For this experiment we used images. Only two boxes COPY 1/60-61 are available digitally. 
These can be downloaded as a pdf from Discovery or as a single images in the related folder.

**Experiment**: 
In an era where digital collections are expanding rapidly, institutions face the challenge of making vast archives accessible, interoperable, and interactive. The International Image Interoperability Framework (IIIF) provides a solution, enabling seamless access to high-resolution images, metadata, and annotations across institutions.
A IIIF viewer is a powerful tool that allows researchers, educators, and the public to engage with digitised collections in ways that were previously impossible. Through open standards, users can zoom, compare, annotate, and search within historical documents, artworks, and manuscripts—all without being confined to a single platform.
Figure 1 shows the result of rendering the COPY 1 data within a IIIF viewer. Functionality includes being able to navigate through the images and zoom into specific regions of each image. The description of each image is displayed on the right-hand side as an annotation.

<kbd><img src="https://github.com/user-attachments/assets/731a0f77-1231-462e-acfa-5f4ba98441a4" width="600" border="2px"></kbd><br />
_Figure 8. Tamerlane IIIF viewer_
 
**Methods**: 
To enable access to the COPY 1 data through a IIIF viewer requires the data provided in the hackathon to be converted to the IIIF Presentation standard. The output of writing code to carry out this process is available here. This included extracting the description from the JSON provided and converting it to the W3C web annotation standard. This enables IIIF Content Search functionality, allowing keyword searches to quickly locate and navigate to relevant images. Both the annotation standard and content search standard are supported by software and infrastructure developed at TNA available on our GitHub repository at https://github.com/nationalarchives/miiify and https://github.com/nationalarchives/annosearch respectively.

**Obstacles**: 
The IIIF Presentation standard has a rich set of properties for representing metadata, attribution and rights. More work is required to map the catalogue entries to these properties, so they are correctly displayed as links back to the catalogue by the IIIF viewer. Currently only a description label is being displayed. Likewise, more processing could be done to better render the text descriptions with neatly formatted HTML within the annotations.

**Research potential**:
Integrating content search into our digital documents would significantly enhance catalogue navigation by allowing users to search beyond metadata and directly within the full text of digitised materials. This capability, especially when combined with existing search tools, enables more precise and efficient discovery of relevant content. Rather than relying solely on predefined tags or descriptions, users can locate specific terms, phrases, or references within documents, making research and exploration more intuitive. By leveraging technologies such as OCR to extract text from digitised collections, content search unlocks a deeper level of accessibility, transforming how users engage with archival materials. IIIF provides an open standard to enable this, unlocking the potential of vast amounts of content generated through digitisation pipelines, including OCR text. Further work is needed to refine the user experience and facilitate seamless searching across our collections and those of other institutions. The Tamerlane IIIF viewer is currently being developed to examine these questions.


## Stereoscopic photographs viewer

**Team**: 
1 person onsite (Alex Nelson)

**Additional data**
In order to carry on this experiment, additional stereoscopic images where provided. These can be accessed in the related folder.

**Experiment**: 
Part of the COPY 1 archive contains ‘Stereoscopic’ Images. These were pairs of images that were slightly offset, in some cases with one brighter/more exposed than the other. These photos were printed side-by-side on a ‘stereocard’ which was slid into the stereoscope, a viewer with a frame to hold the stereocard and two eyepieces to view it. Viewing the images would give a 3D effect, a sort of precursor to modern 3D glasses. 
The idea was to create a tool to generate repeating GIFs from pairs of stereoscopic images to give a sense of the three-dimensional effect that would be seen when viewing them through a stereoscope.


<kbd><img src="https://github.com/user-attachments/assets/3b9f364e-8341-4e3d-bf8b-3c5649ed6805" width="600" border="2px"></kbd><br />

<kbd><img src="https://github.com/user-attachments/assets/d861124e-2844-4482-be33-0870877991bf" width="600" border="2px"></kbd><br />

<kbd><img src="https://github.com/user-attachments/assets/8d907ef4-6574-43ab-b252-db25c98fd9cc" width="600" border="2px"></kbd><br />
_Figures 9-11: Example of Stereoscopic images and reconstriction through GIF animation_
 
**Methods**: 
Used existing Gif tools for Gif generation. Crossfaded original 2 images with intermediate frames to produce smoother transition. Also explored using generative AI to improve quality of original images (e.g. straightening, removing flaws) but with limited results
Obstacles: 
The images were reproductions of the original stereoscopic photos for the purposes of record-keeping so often had flaws compared to the originals. E.g. Images of different sizes, images at angles/skewed, dog ears, creases. Also the more similar the pair of images are, the better the results and when images were too offset it was difficult to create a smooth transition.

**Research potential**: 
Shorter-term Ideas:
* Generate Gifs for COPY 1 Stereoscopic images and convert to IIIF standard. Potentially incorporate into the National Archives collection.
* Improve Gif generation tool and process with UI and better gif generation code.
* Making the images available to view using Google cardboard viewer https://arvr.google.com/cardboard/ 
* Potentially use generative AI to improve quality of initial stereoscopic images
* Improve quality of photos of stereoscopic images

Longer-term/Stretch Ideas: 
* Research paper exploring Gif generation methods from stereoscopic images in greater depth.
* Incorporating other historic collections of stereoscopic images into the National Archives and generate corresponding Gifs. E.g. the collection of Thomas Richard Williams https://www.londonstereo.com/trwilliams/first_series1.html 
* Incorporate stereoscopic images into National Archives’ public displays E.g. Allowing members of the public to view reproductions of stereoscopic images through a stereoscopic viewer or displaying stereoscopic image Gifs on screens.

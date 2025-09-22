# Network analysis with Neo4j

Experiments by: _Natasha Kitcher_

To understand if and how the copy 1 catalogue could be brought together, and queried as a connected collection, I built a ‘Neo4J’ relational graph interface and fed in a subset of 1000 entries. 
Neo4J is a graph database consisting of a series of nodes and relationships that the user defines. I used a program called ‘arrows’ to create my own schema for how I would like each individual row of the copy 1 spreadsheet to be presented in Neo4J. 

IMAGE 1

Each node (in the circles) represents an individual column in the spreadsheet. While the schema shows how just one row would be presented, it’s possible to see where connections between individual entries would start to be made. Photograph ID would always be unique to a specific row, but entries could be connected if they had the same Copyright Owner, Copyright Author, Location, Registration Date, or ‘AuthorOwner.’ AuthorOwner was a new column I created which merged the Copyright Owner and Copyright Author column in instances where they were the same. This made it easier to read the graph, as there would only be an Owner and Author node if they were different people.

IMAGE 2

When loading the first 200 rows of the graph database, you get to see the shape of the collection. Green circles represent the Photograph ID nodes, orange represent Copyright AuthorOwners, blue represent Copyright Owners and purple represent Copyright Authors. We can see small clusters forming where a photographer was active, an orange or purple node surrounded by multiple green ones. We can see small triangles form where owners and authors have worked together on a particular photo, or a more unusual spider-like-shape when they have collaborated on several photos. 
This is interesting for visualising the collection, but does not show the real power of Neo4J. The real advantage of using Neo4J comes when you begin to query the database.
Take the below image of all AuthorOwners based in Yorkshire in the period. We can see the dominance of the prolific Benjamin Hepworth, the orange circle with the most green nodes surrounding him. Judging by the description of his photos, he focused on drawing images of animals. Looking at the handful of images copyrighted by the other AuthorOwners in the region, he was a lone-wolf in drawing animals, while each of the other image owners focused on creating logos or designs for their own specific companies. We start to get an idea of the arts scene in Yorkshire at the time. 

IMAGE 3

The graph is also useful for viewing relationships. A very simple example is the change of ownership relating to oil painting C16265498. The graph shows us that the painting was by George Frederick Hughes for Bejamin Brooks, who later transferred the ownership back to the original artist.  

IMAGE 4

A Neo4J graph is only ever as good as your data, though. As the above screenshot shows, transcription errors such as the addition of “1)” before George’s name are still present in work like this. This is why cleaning the data is so important!
When searching for any catalogue entry that includes the text ‘Image of Westminster,’ we see an inconsistency in the way a name has been recorded majorly impacts the graph itself:


IMAGE 5

It is reasonable to assume that O’Bryen Lomax is the same as both James O’Bryan and James O’Bryen Lomax, but they have been listed as separate entries due to the difference in spelling. It may be possible in the future to unite nodes with similar text using Levenshtein distance (a metric that determines how similar two nodes are and can merge within a certain level of confidence) – but this would not help with the core issue of the data being wrong in the original sheet. While the relational graph database can help us understand and query our data, it doesn’t produce any exportable relational data itself. 
This is only a small, random, selection of 1000 rows from the copy 1 collection but there’s certainly scope to scrutinise more relationships between the data with a larger subset. Graph databases are one of the best ways to understand historic networks and professional relationships that exist throughout archival collections. 

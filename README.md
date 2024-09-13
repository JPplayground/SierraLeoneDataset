# Sierra Leone Dataset (Schools in Sierra Leone)
## The Data
The raw data for this project comes from here
- https://mbsse.gov.sl/wp-content/uploads/2020/03/2017-School-List.pdf

## Process
The scripts in this project are labled in the order that they were created/executed. Small amounts of
processing were done manually using find-and-replace features, however none of these would make a major difference
to the outcome.  To summarize the process:

- The raw data was simply copy and pasted to a txt file
- Many sections of the text file were fragmented with line breaks and had to be fixed
- The raw txt data was converted to a csv file

The main challenge in part of the process is that there was no highly reliable way to separate school names from
town and city names (partly because they were grouped directly together in the raw data), at least one that I could come up with. 
Therefore, I decided to use the OpenAI API to recognize school names and town names in the raw data. There are 9258 schools in this dataset,
and ended up costing me about $1.00 in total. Not bad!

- Utilized the OpenAI API to recognize school names and town names in the raw data
- Converted the inferred names (responses from the OpenAI API) to json format
- Re-merged the data back together in the form of a SQLite database

## Results
The results are, for the most part,a well formatted database that can be utilized in future projects.
There are still mistakes within the data that can be corrected over time. Feel free to use the dataset 
or any of the scripts in this project in your own projects.

[Download the Database File (.db extension)](./database/schools.db) \
[Download as CSV](./database/schools.csv)


# Top 5 data analysis tool fails

We've compiled a list of ten occassions where our analysis tools have behaved unexpectedly. Avoid the blood, sweat, tears and swearing by learning from our experience. We mainly look at Excel, but many of the problems turn out to be deep rooted in computer science and the way our machines handle and process data.

# 1 - Excel Vlookup
One of the most powerful functions in excel is being able to match and merge data from one source into another. To recap, the vlookup function takes four commands.
*  Which bit of data item am I looking for? (data item from a single cell) 
*  In which data 'area' (a 2 dimensional array of rows and columns) do I focus on? (Note, the function only looks up the data item from the first column)
*  If I find the data item, which column offset should I return?
*  Do I have to match exactly or generally? (Always exactly, use False)

But here are some common ways which vlookup can behave strangely.
*  Check your data for duplicates, at least one of your data sets needs to be unique. To explain further, common use cases for vlookup include..
  - one-to-one match (both columns of data have no duplicates, for example survey IDs)
  - one-to-many or many-to-one (of the data sources has duplicates, such as State, and we want to match in additional information based on state)
  - many-to-many <- Vlookup is not the right tool! If both of your data sources have duplicates, then vlookup will only match the first value it finds.
*  Vlookup interprets blank cells as '0'. This is not the same thing as blank and can cause all sorts of problems when merging numeric data, where there is a difference between 0 and missing. To avoid this, you may need an if statement that tests if the length of the matched result is 0 or not

# 2 - Excel's handling of CSV files

CSV or comma seperated values is one of the most common and open ways to share data between different sources. You can open CSV files in text editers such as Windows Notepad and easily edit.

It can be tempting to load CSV files into Excel, but be aware that *excel may change the format* of CSV files, such that when you save the files, they are different!

This has burnt us before in a few ways;
*  Mobile numbers preceeded with '0' (0401001001), get the 0 dropped and excel treats the vaue as a number! When we attempted to load this into our surveying platform, no valid mobile numbers were found, which delayed survey sends until the next day when we resolved the issue.

*  Excel will often change the format of dates. Excel may make a small change such as changing a date format from 20-5-17 to 20/5/2017. This has caused us downstream issues where we end up with two versions of dates in our analysis files, and no single way to clean/treat the data.

*  Excel may interpret dates as US dates. This can depend on your computer's localisation options (does your word processor default to US spelling?). If your dates data doesn't imply that it's day/month/year (for instance, maybe your data file contains only dates early in the month before the 13th), be on the lookout for excel playing funny buggers with your data.

*  If you have a CSV file with 'ID' as cell A1, excel does not recognise it as a CSV file, and instead as another type of document called a SYLK. This will throw several errors upon trying to load the file, and may cause frustration.

# 3 - Excel's filtering options

With a well formed data set, the excel filtering options can be great to help quickly sort columns and filter out options. We noticed that with large data files, sometimes excel does not display an exhaustive list of options available in a column. Don't rely on filter information to inform you about included values!

When using excel filtering, be sure that you've squarely-selected all of the data in your workbook. If you miss some rows, they will not be included in any filtered operations such as sorting and filtering! Including too many rows may result in blanks being included as well.

Tip: If you want to delete rows of data in an excel workbook with filters, try sorting the column, unselecting the filter values you want to retain, then delete. You'll find it's faster to delete when the rows are contigious/sorted.

# 4 - Excel hidden information

There are all kinds of ways to hide data in Excel files such as hiding tabs. Many data analysis downstream processes may look for the first sheet of an excel file; and you may not realise that the process is using the first sheet if it's hidden. There are other ways of hiding data such as with formatting. When cleaning sample files from unknown sources, start with removing all formats and checking for hidden tabs. 

# 5 - Quirks with Q and statistical analysis

Q is a data analysis program which specialises in survey data, crosstabulation and statistical testing. We use it widely at Evolve Research as part of our insights generation and replicable research process. Q works best with SPSS data files, but when using alternative sources such as CSV or Excel data we should pay close attention to how the data is being interpreted in Q.  

Inspecting market research data in Excel we have one sheet of data. This may be rows for respondents and columns for questions asked, with each cell containing a single value. SPSS files can actually contain two types of information per cell; the cell value and the cell label. A label may be 'Strongly Agree - 10' and the associated value of 10, reflecting the way information was presented in surveying.  

When loading Excel or CSV information, be careful that the data you are loading is intended to be treated numerically or as text. Q may interpret columns of data as 'labels', and apply a 'value' to each label in the order it entered the data file. This can be disasterous, as you may have a label of 'Strongly Agree - 10', interpreted as a value of 3!

Take care when interpreting the base sizes of tables which use multiple questions. The base size, when taken over multiple questions, implies 'how many respondents answered all of the questions'. This can be problematic when adding a *new* question to a survey - thus no respondent answered the question in the past resulting in a 0 column base. It can also be problematic when recoding answers of 'don't know' into missing data. The solution here is to analyse base sizes within cells (rather than on aggregate for the table).

Very occassionally in statistical analysis we encounter Simpson's paradox. This is a unique circumstance where a trend appears to be increasing for two groups, but when the two groups are combined the trend decreases. You can read further about Simpson's paradox here;
https://en.wikipedia.org/wiki/Simpson%27s_paradox

Conclusion

Solid data analysis starts from the ground up. Having trust in the data collection, data management, aggregation and statistic testing allows us to report insights with confidence to our clients. Seeing inconsistant results or behaviour in our primary tools can be unsettling. Understanding some of the shortcomings and problems means we can adapt and continue to report with confidence.


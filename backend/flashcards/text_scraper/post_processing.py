""" This is the post-processing module for the text scraper. It contains a class that performs post-processing on the extracted text data. The post-processing class is responsible for cleaning up the extracted text data and extracting paragraphs from the page content. The extracted paragraphs are then stored in a data class object for further processing."""
from dataclasses import dataclass


@dataclass
class Data:
    text: str
    page_num: int
    pdf_name: str
    
    
class PostProcessor:
    
    def __init__(self):
        pass
    
        

    def page_post_processing(self, page_data,  pdf_name):
        data = []
        i = 0
        for page in page_data:
            
            paragraphs = self.extract_paragraphs(page)
            for paragraph in paragraphs:
                data.append(Data(text = paragraph, page_num=i, pdf_name=pdf_name) )
            
            i += 1
            
        return data
        
        
        
        
            
          
    
    def extract_paragraphs(self, page):
        """
        Extract paragraphs from a list of strings, where each string represents page content from a PDF.
        
        Parameters:
        - page_data: list of strings, where each string represents the content of a page.
        
        Returns:
        - A list of paragraphs extracted from the page content.
        """
        paragraphs = []
        
        # Split the page into segments based on double newline characters
        segments = page.split('\n\n')
            
        # Further process each segment
        for segment in segments:
            # Clean up the segment by stripping leading/trailing whitespace and replacing multiple newlines with a single space
            cleaned_segment = ' '.join(segment.strip().split('\n'))
            cleaned_segment = self.simple_clean(cleaned_segment)
                
            # Ignore empty segments
            if cleaned_segment:
                paragraphs.append(cleaned_segment)
        
        return paragraphs
    
    
    
    def simple_clean(self, text, replace_with='?'):
        return ''.join(char if ord(char) < 128 else replace_with for char in text)
        
    
        
    


if __name__=="__main__":
    
    
            
    text = """
    700 4
    600 +
    500 ~
    400 -

    300 ~

    No. of Employees

    200 -

    100 4 [|

    19.3 Use of Selectivities in Cost-Based Optimization

    30k-�40k 40k-70k  70k-120k 120k-200k 200k-500k
    Salary

    714 Chapter 19 Query Optimization

    19.4 Cost Functions for SELECT Operation

    We now provide cost functions for the selection algorithms $1 to S8 discussed in
    Section 18.3.1 in terms of number of block transfers between memory and disk.
    Algorithm S9 involves an intersection of record pointers after they have been
    retrieved by some other means, such as algorithm S6, and so the cost function will
    be based on the cost for S6. These cost functions are estimates that ignore computa-
    tion time, storage cost, and other factors. To reiterate, the following notation is
    used in the formulas hereafter:

    Cs;: Cost for method Si in block accesses

    ry: Number of records (tuples) in a relation X

    by: Number of blocks occupied by relation X (also referred to as b)
    bfrx: Blocking factor (i.e., number of records per block) in relation X
    sly: Selectivity of an attribute A for a given condition

    sA: Selection cardinality of the attribute being selected (= s/, +r)

    xA: Number of levels of the index for attribute A

    by, A: Number of first-level blocks of the index on attribute A

    NDV (A, X): Number of distinct values of attribute A in relation X

    Note: In using the above notation in formulas, we have omitted the relation name
    or attribute name when it is obvious.

    $1�Linear search (brute force) approach. We search all the file blocks to
    retrieve all records satisfying the selection condition; hence, Cs,, = b. For an
    equality condition on a key attribute, only half the file blocks are searched on
    the average before finding the record, so a rough estimate for Cs), = (b/2) if
    the record is found; if no record is found that satisfies the condition, Cs1, = b.

    $2�Binary search. This search accesses approximately Cs, =
    logyb +I (s/bfr) |� 1 file blocks. This reduces to logyb if the equality condition
    is on a unique (key) attribute, because s = 1 in this case.

    $3a�Using a primary index to retrieve a single record. For a primary
    index, retrieve one disk block at each index level, plus one disk block from
    the data file. Hence, the cost is one more disk block than the number of
    index levels: Co3, =x + 1.

    $3b�Using a hash key to retrieve a single record. For hashing, only one
    disk block needs to be accessed in most cases. The cost function is approxi-
    mately Cs3, = 1 for static hashing or linear hashing, and it is 2 disk block
    accesses for extendible hashing (see Section 16.8).

    $4� Using an ordering index to retrieve multiple records. If the compari-
    son condition is >, >=, <, or <=on a key field with an ordering index, roughly
    half the file records will satisfy the condition. This gives a cost function of
    Cs4 =x + (b/2). This is a very rough estimate, and although it may be correct
    on the average, it may be inaccurate in individual cases. A more accurate
    estimate is possible if the distribution of records is stored in a histogram.

    S5�Using a clustering index to retrieve multiple records. One disk block
    is accessed at each index level, which gives the address of the first file disk

    block in
    records
    indexin
    of file b.
    S6�-Us
    (unique
    tion, the
    (nonun
    the se�.
    index :
    block, +
    to accor
    is seare]
    is >, >=,
    then (v�
    file recc
    Crop = -
    estimate
    very cus
    ity s mu
    distribu
    or not /
    exercise

    S7�Co
    to S6 di
    records
    record

    indexes
    (record

    record
    then th.

    $8�Ce
    S6a, de:
    $9�Sei
    nature �
    tions, �:
    a bit v
    numbe
    are acc
    $10�:
    similai
    if that
    may be"""

    
    
    page_data = [text]
    processor = Post_processor()
    
    paragraphs = (processor.extract_paragraphs(page_data))
        
    for element in paragraphs:
        print("==============================================================")
        try:
            cleaned_text = simple_clean(element)
            print(cleaned_text)
        except:
            pass
        
    















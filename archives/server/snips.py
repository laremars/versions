'''                                            CREATE DB                                              '''

#Create a database called "mydatabase":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

'''
    
    To create a collection in MongoDB, use database object and specify the name of the colelction you want to create.
    
    MongoDB will create the collection if it does not exist.
    
    Create a collection called "customers":
        
'''
mycol = mydb["customers"]

#In MongoDB, a collection is not created until it gets content!

'''                                            INSERT DB                                              '''

'''

    To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
    
    The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

'''

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

#The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.

print(x.inserted_id)

'''
    
    If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
    
    In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).
    
'''
    
'''
    
    To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
    
    The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:

'''

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids of the inserted documents.
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

'''
    
    If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).
    
    Remember that the values has to be unique. Two documents cannot have the same _id:
    
    mylist = [
      { "_id": 1, "name": "John", "address": "Highway 37"},
      { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
      { "_id": 3, "name": "Amy", "address": "Apple st 652"},
      { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
      { "_id": 5, "name": "Michael", "address": "Valley 345"},
      { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
      { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
      { "_id": 8, "name": "Richard", "address": "Sky st 331"},
      { "_id": 9, "name": "Susan", "address": "One way 98"},
      { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
      { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
      { "_id": 12, "name": "William", "address": "Central st 954"},
      { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
      { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]
    
    x = mycol.insert_many(mylist)
    
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)

'''

'''                                            FIND                                              '''

'''
    
    To select data from a collection in MongoDB, we can use the find_one() method.
    
    The find_one() method returns the first occurrence in the selection.
    
    To select data from a table in MongoDB, we can also use the find() method.
    
    The find() method returns all occurrences in the selection.
    
    The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

'''

x = mycol.find_one()

print(x)

for x in mycol.find():
  print(x)

'''
    
    The second parameter of the find() method is an object describing which fields to include in the result.
    
    This parameter is optional, and if omitted, all fields will be included in the result.
    
    You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
    
    If you specify a field with the value 0, all other fields get the value 1, and vice versa:

'''

#Return only the names and addresses, not the _ids:
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
  
#This example will exclude "address" from the result:
for x in mycol.find({},{ "address": 0 }):
  print(x)

#This example will produce an error
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)

'''                                            QUERY                                              '''

'''
    
    When finding documents in a collection, you can filter the result by using a query object.
    
    The first argument of the find() method is a query object, and is used to limit the search.

'''

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
'''
    
    To make advanced queries you can use modifiers as values in the query object.
    
    E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

'''

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

'''
    
    You can also use regular expressions to narrow your results:

'''

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

'''                                            SORT                                              '''

'''
    
    Use the sort() method to sort the result in ascending or descending order.
    
    The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

'''
#sort("name", 1) #ascending
#sort("name", -1) #descending
mydoc = mycol.find().sort("name", -1)#descending

for x in mydoc:
  print(x)
  
'''                                            UPDATE                                              '''

'''
    
    You can update a record, or document as it is called in MongoDB, by using the update_one() method.
    
    The first parameter of the update_one() method is a query object defining which document to update.
    
      Note: If the query finds more than one record, only the first occurrence is updated.
    
    The second parameter is an object defining the new values of the document.

'''

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

'''

    To update all documents that meets the criteria of the query, use the update_many() method.
    
    Update all documents were the name starts with the letter "S":

'''

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

'''                                            UPDATE                                                                 '''

'''

    To limit the result in MongoDB, we use the limit() method.
    
    The limit() method takes one parameter, a number defining how many documents to return.
    
    Consider you have a "customers" collection:
        
        {'_id': 1, 'name': 'John', 'address': 'Highway37'}
        {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
        {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
        {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
        {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
        {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
        {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
        {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
        {'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
        {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
        {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
        {'_id': 12, 'name': 'William', 'address': 'Central st 954'}
        {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
        {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}

'''

#Limit to only 5 documents returned
myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)

'''                                              SUCCESSFUL QUERIES                                                   '''

'''

    for doc in CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST": 0, "DATE": 0, "LINE": 0, "PROCESS": 0, "TESTER_NAME": 0, "LOWER_LIMIT": 0, "UPPER_LIMIT": 0, "UNIT": 0, "STEP_NUMBER": 0, "PASS_COUNT": 0 }).limit(100):
        flash(doc,'info')
        
    for doc in CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST": 0 }).limit(100):
        flash(doc,'info')
        
    for doc in CLIENT.TX.IOFF.find({},{ "_id": 0, "TEST": 0 }).limit(10):
        flash(doc,'info')
        
    myquery = { "$and": [
            { "FAIL_COUNT": { "$gt": 1500 }},
            { "LINE": "TX2" },
            { "FAIL_COUNT": { "$lt": 1550 }}
            ]
    }
    
    myquery = { 
             "FAIL_COUNT": { "$gt": 1500 , "$lt": 1550 },
             "LINE": "TX2" 
    }
    
    myquery = { "FAIL_COUNT": { "$gt": 1500 }, "LINE":"TX2" }


    for doc in CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST": 0, "DATE": 0, "LINE": 0, "PROCESS": 0, "TESTER_NAME": 0, "LOWER_LIMIT": 0, "UPPER_LIMIT": 0, "UNIT": 0, "STEP_NUMBER": 0, "PASS_COUNT": 0 }).limit(100):
        flash(doc,'info')
        
    #Only shows FAIL_COUNT
    for doc in CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "FAIL_COUNT": 1 }).limit(100):
        flash(doc,'info')
        
    #To return just the value associated with the passed in key
        #Note: if appending a string to the statement, val (if a number) number but be converted to a string
    for val in doc:
        flash( 'Fail Count: '+str(val['FAIL_COUNT']), 'info' )
        
    for val in doc:
        flash( 'Fail Count: ' + str(val['FAIL_COUNT']) + '----- Line: ' + str(val['LINE']), 'info' )
    
    #To Time a Query
    start=time.time()
    doc = list(CLIENT.TX.IOFF.find(myquery,{ "_id": 0 }))
    flash(time.time()-start,'info')
        

'''

'''                                            BUILT IN PYTHON FUNCTIONS                                              '''

'''

    abs()	Returns the absolute value of a number
    all()	Returns True if all items in an iterable object are true
    any()	Returns True if any item in an iterable object is true
    ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
    bin()	Returns the binary version of a number
    bool()	Returns the boolean value of the specified object
    bytearray()	Returns an array of bytes
    bytes()	Returns a bytes object
    callable()	Returns True if the specified object is callable, otherwise False
    chr()	Returns a character from the specified Unicode code.
    classmethod()	Converts a method into a class method
    compile()	Returns the specified source as an object, ready to be executed
    complex()	Returns a complex number
    delattr()	Deletes the specified attribute (property or method) from the specified object
    dict()	Returns a dictionary (Array)
    dir()	Returns a list of the specified object's properties and methods
    divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
    enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
    eval()	Evaluates and executes an expression
    exec()	Executes the specified code (or object)
    filter()	Use a filter function to exclude items in an iterable object
    float()	Returns a floating point number
    format()	Formats a specified value
    frozenset()	Returns a frozenset object
    getattr()	Returns the value of the specified attribute (property or method)
    globals()	Returns the current global symbol table as a dictionary
    hasattr()	Returns True if the specified object has the specified attribute (property/method)
    hash()	Returns the hash value of a specified object
    help()	Executes the built-in help system
    hex()	Converts a number into a hexadecimal value
    id()	Returns the id of an object
    input()	Allowing user input
    int()	Returns an integer number
    isinstance()	Returns True if a specified object is an instance of a specified object
    issubclass()	Returns True if a specified class is a subclass of a specified object
    iter()	Returns an iterator object
    len()	Returns the length of an object
    list()	Returns a list
    locals()	Returns an updated dictionary of the current local symbol table
    map()	Returns the specified iterator with the specified function applied to each item
    max()	Returns the largest item in an iterable
    memoryview()	Returns a memory view object
    min()	Returns the smallest item in an iterable
    next()	Returns the next item in an iterable
    object()	Returns a new object
    oct()	Converts a number into an octal
    open()	Opens a file and returns a file object
    ord()	Convert an integer representing the Unicode of the specified character
    pow()	Returns the value of x to the power of y
    print()	Prints to the standard output device
    property()	Gets, sets, deletes a property
    range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
    repr()	Returns a readable version of an object
    reversed()	Returns a reversed iterator
    round()	Rounds a numbers
    set()	Returns a new set object
    setattr()	Sets an attribute (property/method) of an object
    slice()	Returns a slice object
    sorted()	Returns a sorted list
    @staticmethod()	Converts a method into a static method
    str()	Returns a string object
    sum()	Sums the items of an iterator
    tuple()	Returns a tuple
    type()	Returns the type of an object
    vars()	Returns the __dict__ property of an object
    zip()	Returns an iterator, from two or more iterators

'''


'''                                            PYTHON STRING METHODS                                              '''

'''
    Note: All string methods returns new values. They do not change the original string.
    
    capitalize()	Converts the first character to upper case
    casefold()	Converts string into lower case
    center()	Returns a centered string
    count()	Returns the number of times a specified value occurs in a string
    encode()	Returns an encoded version of the string
    endswith()	Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	Searches the string for a specified value and returns the position of where it was found
    format()	Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	Searches the string for a specified value and returns the position of where it was found
    isalnum()	Returns True if all characters in the string are alphanumeric
    isalpha()	Returns True if all characters in the string are in the alphabet
    isdecimal()	Returns True if all characters in the string are decimals
    isdigit()	Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	Returns True if all characters in the string are whitespaces
    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case
    join()	Joins the elements of an iterable to the end of the string
    ljust()	Returns a left justified version of the string
    lower()	Converts a string into lower case
    lstrip()	Returns a left trim version of the string
    maketrans()	Returns a translation table to be used in translations
    partition()	Returns a tuple where the string is parted into three parts
    replace()	Returns a string where a specified value is replaced with a specified value
    rfind()	Searches the string for a specified value and returns the last position of where it was found
    rindex()	Searches the string for a specified value and returns the last position of where it was found
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	Splits the string at the specified separator, and returns a list
    rstrip()	Returns a right trim version of the string
    split()	Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    swapcase()	Swaps cases, lower case becomes upper case and vice versa
    title()	Converts the first character of each word to upper case
    translate()	Returns a translated string
    upper()	Converts a string into upper case
    zfill()	Fills the string with a specified number of 0 values at the beginning
    
    Note: All string methods returns new values. They do not change the original string.

'''

'''                                            PYTHON LIST/ARRAY METHODS                                              '''

'''

    Python has a set of built-in methods that you can use on lists/arrays.
    
    append()	Adds an element at the end of the list
    clear()	Removes all the elements from the list
    copy()	Returns a copy of the list
    count()	Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	Removes the element at the specified position
    remove()	Removes the first item with the specified value
    reverse()	Reverses the order of the list
    sort()	Sorts the list
    
    Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

'''

'''                                            PYTHON DICTIONARY PRIMER                                              '''

'''

    #A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
    
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(thisdict)

                                                #MUTABLE
                                                
    #Example of changing a value in the above dictionary:

thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
thisdict["apple"] = "red"
print(thisdict)

                                                #USING CONSTRUCTOR

    #It is also possible to use the dict() constructor to make a dictionary:
        # note that keywords are not string literals
        # note the use of equals rather than colon for the assignment
        
thisdict =	dict(apple="green", banana="yellow", cherry="red")

print(thisdict)

                                                #APPENDING ITEM
                                                
    #Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)

                                                #REMOVING ITEM
                                                
    #Removing a dictionary item must be done using the del() function in python:

thisdict =	dict(apple="green", banana="yellow", cherry="red")
del(thisdict["banana"])
print(thisdict)

                                                #SIZE OF DICTIONARY
                                                
    #The len() function returns the size of the dictionary:
    
thisdict =	dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))



'''

'''

                                                #Helpful Links and Descriptions
                                                
Collision aware tooltip: http://jsfiddle.net/tj_vantoll/587n9/
Header, aside and footer declarations in HTML: http://jsfiddle.net/tj_vantoll/59eZq/
Flight data retrieval via API and JSON: http://jsfiddle.net/tj_vantoll/ujwWL/
Table data entry, access and edit via JQuery: http://jsfiddle.net/tj_vantoll/tAp93/
Position utility example demonstrating increased control of DOM items: http://jsfiddle.net/tj_vantoll/LgGQH/



'''







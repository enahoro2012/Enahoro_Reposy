 #nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in nums:
#     if (num%2 == 0):
#         print(f"this is even {num}")
#     else:
#         print(f"this is either odd or prime {num}")


# for num in range(1, 10, 2):
#     print(num)

# num = 7
# while num>=7:
    # num += 1
    # print(num)

# nums = [1,2,3,4,5,6]

# for num in nums:
    # if(num%2 == 0):
        # print(f"{num} is even")
    # else:
        # print(f"{num} is an odd number")


# nums =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for num in nums: 
#     if(num%2 == 1):
#         print(f"{num} is an odd number")
#     else:
#         print(f"{num} is even")

# for num in range (1, 10, 2):
#     print(num)

# num = 1
# while num < 100:
#     print (num)
#     num +=1


 # create a while loop from 1-100, to print out 5 times table within the range of 100

# num = 5
# while num < 100:
#     print (num)
#     num +=5

# my_data = open('sample.txt', 'w')

# writer = """
#             i am a boy
#          """

#  my_data.write(writer)
#  my_data.close()

# read_data = open("sample.txt", "r")
# read_data.read()



# What is  functions? Functions are reusable codes that can be called at will(anytime u need them), there are two types of functions, the function signature which includes the name of the function and the parameter , the second is the body of the function, every function  behaves like a computer. To use a function there are two steps to follow, first is, to create a function or define it. Second is function invocation(calling of function) in the right order.(In python .pop is used to remove items from mutable data types , e.g(lists...) and insert to add items)

# def greetuser(name):
#     id = 2
#     id = str(id)
#     print("welcome" + name +"! How are you?" + "your ID is:" + id)


#     # function call
    # greetuser("James")




    # def format_name(name, index, min_size ): # <- Parameters (function definition)
    #     if len(name) > min_size :

    # # convert the name into a list(type cast)
    #     name = list (name)

    #     # pop the last item (pop means remove the last item)
    #     Removed = name.pop(index)

    #     # create an empty string
    #     final_name = ""

    #     # loop through the name list to populate the final_name string variable
    #     for item in name :
    #         final_name += item

    #         # return the final result
    #     return final_name


    #     names_to_analyze =["Ade", "Jacob", "jane", "Mary"]

    #     # create an empty list
    # result_;ist[]
    # for name in names_to_analyze:
    #     result = format_name(name, 1, 3)

    #     if result != None:
    #         result_list.append(result)

    # print(result_list)

        # format_name("james" , 4) # <= arguments (function called)


        # Arguments is what is passed to the function called, while parameters is passed to function definition


    # username.pop(len(username)-1) (how to calculate the amount indexes we have)

    # Different types of parameters and arguments , and types of functions.
    # We have diff types of parameters, first type is called positional parameters or positional arguments, it is called positional because they must all match, second type is default arguments/parameters

    # Types of functions 

    # There are two types of functions, named functions and anonymous functions , Named functions are those functions that have names, in  their signature there is a name there, they're easily identified'. The anonympous function means the function doesnt have a name in the signature another name for anonmyous function  is LAMBDA functions . 

    # Keyworded parameters 
# return statements allows u to access a variable outside a function, it also helps to write a modula
# age ="21yrs"
# def sayhi(fname, lname):
#     print (f"my name is {fname} and lastname is {lname} and i am {age}")
    

# sayhi("mary", lname="john")

# Lambda function
# A LAMBDA function is also known as a nameless function or an anonymous function, it takes in many arguments and returns only one expression.


# x = lambda a,b : print (a+b)
# x (2, 3)


# write a program to introduce yourself 


def introduce(num1, num2):
    fname = input(" enter your name: ")
    gender = input("enter your gender:")
    if(fname == "james"):
        print(f"my name is {fname}, I am a {gender} :{num1+num2}" )
    elif(fname == "mary"):
        print(f"my name is {fname} and i am {gender}")
    else:
        print("Unknown person")
    
   


# gender = input("enter your gender :")

intro = lambda num1, num2: introduce(num1, num2)

intro(1, 2)



pass in a condition for odd and even and prime numbers
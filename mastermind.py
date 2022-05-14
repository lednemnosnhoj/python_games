def response(code,guess):
    response=[]
    for i,peg in enumerate(guess):
        if code[i]==peg:
            response.append(2)
    return response
        
def get_a_guess():
    return [1,3,2,4,5]

code=[1,2,3,4,5]
guess=get_a_guess()
print(response(code,guess))

#comment









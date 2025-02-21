#  Access the value of key ‘history’

dictionary1 = {
   "class":{
      "student":{
                    "name":"ABC",
                    "marks":{ 
                              "physics":70,
                              "history":80
                            }
                }     
           }
}

marks = dictionary1['class']['student']['marks']['history']
print(marks)
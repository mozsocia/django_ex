# x = dict(a=2, b=2,c=3, d=4)

# # {'a': 2, 'c': 3, 'b': 2, 'd': 4}
# y = dict(b=2,c=3, d=4)

# # {'c': 3, 'b': 2, 'd': 4}


# list = zip(x.iteritems(), y.iteritems())



# [(('a', 2), ('c', 3)),
#  (('c', 3), ('b', 2)),
#  (('b', 2), ('d', 4))]


# ls1 = [5,6,34,23]
# ls2 = [56,23,76,87]


# lst = list(zip(ls1,ls2))

# print(lst)


# lst = (
# {'id': 19, 'question_desc': 'asdfas', 'A': 'Vote direction', 'B': 'Now practice', 'C': 'Step generation', 'D': 'Level table civil.', 'ans': 'A', 'course_id': 2},
# {'id': 8, 'user_id': 4, 'question_id': 19, 'course_id': 2, 'user_ans': 'A'}
# )



        


    # print(" -----")
        




def total_results(all_data):
    
    def find_single_res(list_p):
        res = 0
        for i,j in list_p[0].items():
            for k,l in list_p[1].items():
                if ( i == 'ans' and k == 'user_ans'):
                    if (j == l ):
                        res =  1
        return res
    
    result = 0
    
    for item in all_data:   

        single_mark = find_single_res(item)
        result = result + single_mark
    
    return result
    
    
        

ls_all = [({'id': 19, 'question_desc': 'Conference everything approach computer him watch break.', 'A': 'Vote direction capital.', 'B': 'Now practice college.', 'C': 'Step generation seven.', 'D': 'Level table civil.', 'ans': 'A', 'course_id': 2}, {'id': 8, 'user_id': 4, 'question_id': 19, 'course_id': 2, 'user_ans': 'A'}), 
          ({'id': 20, 'question_desc': 'Exactly fund entire worker thing win big student.', 'A': 'My unit include.', 'B': 'Challenge movie ground.', 'C': 'Adult shake.', 'D': 'Friend southern moment.', 'ans': 'A', 'course_id': 2}, {'id': 9, 'user_id': 4, 'question_id': 20, 'course_id': 2, 'user_ans': 'A'}),
          ({'id': 21, 'question_desc': 'Budget democratic impact no big seven. Oil appear feel life describe too.', 'A': 'Bank son fight.', 'B': 'Marriage.', 'C': 'Seven.', 'D': 'Suddenly environmental.', 'ans': 'A', 'course_id': 2}, {'id': 10, 'user_id': 4, 'question_id': 21, 'course_id': 2, 'user_ans': 'C'}),
          ({'id': 22, 'question_desc': 'Degree senior onto. Building person note book main lose pull national.', 'A': 'Two candidate.', 'B': 'Age personal charge.', 'C': 'Than us.', 'D': 'Recognize spend outside behind.', 'ans': 'A', 'course_id': 2}, {'id': 11, 'user_id': 4, 'question_id': 22, 'course_id': 2, 'user_ans': 'B'})]


result = total_results(ls_all)


print(result)




    






def get_most_shape():
    doc = open('/home/bryan/Desktop/CS_LOG/Printed_results/face_shape.txt', 'r')
    text_string = doc.read()

    print('Square {}'.format(text_string.count('Square')))
    print('Round {}'.format(text_string.count('Round')))
    print('Oval {}'.format(text_string.count('Oval')))
    print('Oblong {}'.format(text_string.count('Oblong')))
    print('Heart {}'.format(text_string.count('Heart')))

    count_list = [text_string.count('Square'),  #0
                  text_string.count('Round'),   #1
                  text_string.count('Oval'),    #2
                  text_string.count('Oblong'),  #3
                  text_string.count('Heart')    #4
                  ]

    tmp = max(count_list)
    index = count_list.index(tmp)
    # print(type(index))

    text = ('Most seen :{}, Index:{}'.format(tmp, index))
    print(text)

    if index == 0:
        shape = 'Square'
        # print('square')
    elif index == 1:
        shape = 'Round'
        # print('round')
    elif index == 2:
        shape = 'Oval'
        # print('oval')
    elif index == 3:
        shape = 'Oblong'
        # print('oblong')
    else:
        shape = 'Heart'
        # print('heart')

    return shape

# get_most_shape()

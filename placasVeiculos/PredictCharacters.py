import SegmentCharacters
import pickle
print("Carregando modelo")
filename = './finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

print('Lendo caracteres da placa')
classification_result = []
for each_character in SegmentCharacters.characters:
    
    each_character = each_character.reshape(1, -1);
    result = model.predict(each_character)
    classification_result.append(result)

print('Resultado: ')
print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]

print('Placa: ')
print(plate_string)



column_list_copy = SegmentCharacters.column_list[:]
SegmentCharacters.column_list.sort()
rightplate_string = ''
for each in SegmentCharacters.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]

print('Placa: ')
print(rightplate_string)
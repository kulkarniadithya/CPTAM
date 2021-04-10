##################################################
#This block contains code for clusters_from_parsed_sentence class in resources.py

# parsed_sentence = "(S (INTJ (UH Well)) (, ,) (ADVP (RB finally)) (, ,) (VP (VB let) (S (NP (PRP 's)) (VP (VB turn) (NP (PRP$ our) (NN attention)) (PP (IN to) (NP (NP (NP (NN handling)) (PP (IN of) (NP (DT the) (NN situation)))) (, ,) (INTJ (UH ah)) (, ,) (PP (IN during) (NP (NP (DT the) (JJ latter) (NNS stages)) (PP (IN of) (NP (DT the) (NN cave))) (HYPH -) (RP in) (NP (NP (NN accident)) (PP (IN in) (NP (NNP Beijing))))))))))) (. .))"
#
# character_array = [char for char in parsed_sentence]
#
# print(character_array)
#
# brackets_array = []
# brackets_index_array = []
# for i in range(0, len(character_array)):
#     if character_array[i] in ['(', ')']:
#         brackets_array.append(character_array[i])
#         brackets_index_array.append(i)
#
# #print(brackets_array)
#
# cluster_bracket_index = []
#
# current_length_bracket_array = len(brackets_array)
# previous_length_bracket_array = 0
# while len(brackets_array) > 0:
#     previous_length_bracket_array = current_length_bracket_array
#     for i in range(0, len(brackets_array)-1):
#         if brackets_array[i] == '(' and brackets_array[i+1] == ')':
#             cluster_bracket = []
#             cluster_bracket.append(brackets_index_array[i])
#             cluster_bracket.append(brackets_index_array[i+1])
#             cluster_bracket_index.append(cluster_bracket)
#             brackets_array.pop(i)
#             brackets_array.pop(i)
#             brackets_index_array.pop(i)
#             brackets_index_array.pop(i)
#             break
#         else:
#             continue
#     current_length_bracket_array = len(brackets_array)
#     if previous_length_bracket_array == current_length_bracket_array:
#         if len(brackets_array) > 0:
#             raise Exception("Invalid number of brackets")
#         break
#
# # print(cluster_bracket_index)
# # print(brackets_array)
# # print(brackets_index_array)
#
# start_index = []
# end_index = []
# counter_index = []
#
# for i in range(0, len(cluster_bracket_index)):
#     counter_index.append(i)
#     start_index.append(cluster_bracket_index[i][0])
#     end_index.append(cluster_bracket_index[i][1])
#
# # print(start_index)
# # print(end_index)
# # print(counter_index)
#
# start_index_sorted = [index for index,counter in sorted(zip(start_index,counter_index))]
# counter_index_sorted = [counter for index,counter in sorted(zip(start_index,counter_index))]
#
# # print(start_index_sorted)
# # print(counter_index_sorted)
#
# cluster_bracket_index_sorted = []
# for i in range(0, len(counter_index_sorted)):
#     cluster_bracket_index_sorted.append(cluster_bracket_index[counter_index_sorted[i]])
#
# # print(cluster_bracket_index_sorted)
#
# character_clusters = []
# cluster_pos = []
#
# for i in range(0, len(cluster_bracket_index_sorted)):
#     clusters = []
#     for j in range(cluster_bracket_index_sorted[i][0], cluster_bracket_index_sorted[i][1] + 1):
#         clusters.append(character_array[j])
#     pos = []
#     for k in range(1, len(clusters)):
#         if clusters[k] != ' ':
#             pos.append(clusters[k])
#         elif clusters[k] == ' ':
#             break
#     cluster_pos.append(''.join(pos))
#     character_clusters.append(''.join(clusters))
#
# print(character_clusters)
# print(cluster_pos)
# print(len(cluster_pos))

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for character_indexing.format_parsed_sentence method in resources.py
############################################################################

# from resources import character_indexing
#
# parsed_sentence = "(S (INTJ (UH Well)) (, ,) (ADVP (RB finally)) (, ,) (VP (VB let) (S (NP (PRP 's)) (VP (VB turn) (NP (PRP$ our) (NN attention)) (PP (IN to) (NP (NP (NP (NN handling)) (PP (IN of) (NP (DT the) (NN situation)))) (, ,) (INTJ (UH ah)) (, ,) (PP (IN during) (NP (NP (DT the) (JJ latter) (NNS stages)) (PP (IN of) (NP (DT the) (NN cave))) (HYPH -) (RP in) (NP (NP (NN accident)) (PP (IN in) (NP (NNP Beijing))))))))))) (. .))"
#
# character_indexing_object = character_indexing(parsed_sentence=parsed_sentence, language='English')
# tokens = character_indexing_object.get_tokens(parsed_sentence=parsed_sentence)
# pos = character_indexing_object.get_pos(parsed_sentence=parsed_sentence)
#
# for i in range(0, len(pos)):
#     parsed_sentence = parsed_sentence.replace('(' + pos[i], '(', 1)
#
# print(parsed_sentence)
# sentence_without_space = ''.join(tokens)
# characters = [char for char in sentence_without_space]
# character_index = []
# for i in range(0, len(characters)):
#     character_index.append(i+1)
# character_appended_index = []
# # for i in range(0, len(characters)):
# #     character_appended_index.append(str(characters[i]) + '_' + str(character_index[i]))
# # print(character_appended_index)
#
# formatted_characters = [char for char in parsed_sentence]
# covered = 0
# for i in range(0, len(formatted_characters)):
#     for j in range(covered, len(characters)):
#         if characters[j] == formatted_characters[i]:
#             formatted_characters[i] = str(character_index[j])
#             covered = j+1
#             break
#
# parsed_sentence = ''.join(formatted_characters)
# print(parsed_sentence)
#
# formatted_tokens = parsed_sentence.split(' ')
# print(formatted_tokens)
# covered = 0
# for i in range(0, len(formatted_tokens)):
#     if formatted_tokens[i] == '(':
#         formatted_tokens[i] = formatted_tokens[i] + str(pos[covered])
#         covered = covered + 1
# parsed_sentence = ' '.join(formatted_tokens)
# print(parsed_sentence)
#
# # for i in range(0, len(character_appended_index)):
# #     parsed_sentence = parsed_sentence.replace(str(characters[i]), str(character_appended_index[i]), 1)
# #
# # print(parsed_sentence)
# #
# # for i in range(0, len(pos)):
# #     parsed_sentence = parsed_sentence.replace('( ', '(' + pos[i] + ' ')
# #
# # print(parsed_sentence)

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for copying files
############################################################################

# import shutil
# def copy_files(from_directory, to_directory, sentence_count):
#     for i in range(1, sentence_count+1):
#         source = str(from_directory) + 'sentence_' + str(i) + '.txt'
#         destination = str(to_directory) + 'sentence_' + str(i) + '.txt'
#         try:
#             status = shutil.copyfile(source, destination)
#         except:
#             write_file = open(destination, "w")
#             write_file.close()
#     return True

# # Penn Tree Bank English
# berkeley = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset_ptb/berkeley/', '/Users/adithya/PycharmProjects/medcpt/dataset/penntreebank_english/berkeley/', 49208)
# corenlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset_ptb/corenlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/penntreebank_english/corenlp/', 49208)
# allennlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset_ptb/allennlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/penntreebank_english/allennlp/', 49208)
# hanlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset_ptb/hanlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/penntreebank_english/hanlp/', 49208)
# ground_truth = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/SAPAR/SAPar-master/penntreebank/english/dataset/', '/Users/adithya/PycharmProjects/medcpt/dataset/penntreebank_english/ground_truth/', 49208)

# Onto notes English
# berkeley = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset/berkeley/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_english/berkeley/', 143709)
# corenlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset/corenlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_english/corenlp/', 143709)
# allennlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset/allennlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_english/allennlp/', 143709)
# hanlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/Dataset/hanlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_english/hanlp/', 143709)
# ground_truth = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/SAPAR/SAPar-master/ontonotes/english/dataset/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_english/ground_truth/', 143709)


# # Onto notes Chinese
# berkeley = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/chinese/Dataset/berkeley/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_chinese/berkeley/', 51230)
# corenlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/chinese/Dataset/corenlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_chinese/corenlp/', 51230)
# sapar = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/SAPAR/SAPar-master/chinese_data/chinese_prediction/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_chinese/sapar/', 51230)
# hanlp = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/chinese/Dataset/hanlp/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_chinese/hanlp/', 51230)
# ground_truth = copy_files('/Users/adithya/PycharmProjects/constituency_median_tree/updated_plan/SAPAR/SAPar-master/chinese_data/chinese_dataset/', '/Users/adithya/PycharmProjects/medcpt/dataset/ontonotes_chinese/ground_truth/', 51230)

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for main function in resources.py
############################################################################

# character_indexing_object = character_indexing(parsed_sentence=parsed_sentence, language='English')
# formatted_parsed_sentence, characters, character_index = character_indexing_object.format_parsed_sentence(parsed_sentence=parsed_sentence)
# clusters_from_parsed_sentence_object = clusters_from_parsed_sentence(parsed_sentence=formatted_parsed_sentence, language='English')
# character_clusters, cluster_span, cluster_pos = clusters_from_parsed_sentence_object.get_clusters()
# sentence_dictionary = {}
# sentence_dictionary[0] = {}
# sentence_dictionary[0]['parsed_sentence'] = parsed_sentence
# sentence_dictionary[0]['formatted_parsed_sentence'] = formatted_parsed_sentence
# sentence_dictionary[0]['characters'] = characters
# sentence_dictionary[0]['character_index'] = character_index
# print(sentence_dictionary)
# sentence_cluster_dictionary = {}
# sentence_cluster_dictionary[0] = {}
# sentence_cluster_dictionary[0]['formatted_parsed_sentence'] = formatted_parsed_sentence
# sentence_cluster_dictionary[0]['character_clusters'] = character_clusters
# sentence_cluster_dictionary[0]['cluster_span'] = cluster_span
# sentence_cluster_dictionary[0]['cluster_pos'] = cluster_pos
# print(sentence_cluster_dictionary)

# with open('../dictionary_pickle_files/test/sentence_dictionary.pickle', 'wb') as handle:
#     pickle.dump(sentence_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
# with open('../dictionary_pickle_files/test/sentence_cluster_dictionary.pickle', 'wb') as handle:
#     pickle.dump(sentence_cluster_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('../dictionary_pickle_files/test/sentence_dictionary.pickle', 'rb') as handle:
#     sentence_dictionary_pickle = pickle.load(handle)
#
# with open('../dictionary_pickle_files/test/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     sentence_cluster_dictionary_pickle = pickle.load(handle)
#
# print(sentence_dictionary_pickle == sentence_dictionary)
# print(sentence_cluster_dictionary_pickle == sentence_cluster_dictionary)

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for creating dictionary
############################################################################

# import os
#
# pickle_dump_directory = "../dictionary_pickle_files/"
#
# if not os.path.exists(pickle_dump_directory + 'test1'):
#     os.mkdir(pickle_dump_directory + 'test1')

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for reading pickle file
############################################################################

# import pickle
#
# pickle_path = "../dictionary_pickle_files/penntreebank_english/allennlp"
#
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     sentence_dictionary_pickle = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     sentence_cluster_dictionary_pickle = pickle.load(handle)
#
# print(sentence_dictionary_pickle.get(1))
# print(sentence_cluster_dictionary_pickle.get(1))

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for pre formatting hanlp file
############################################################################

#hanlp_sentence = "[['TOP', [['IP', [['NP', [['NP', [['DP', [['DT', ['The']]]], ['NP', [['NN', ['president']]]]]], ['VP', [['VP', [['VC', ['said']], ['NP', [['PN', ['that']], ['NN', ['he']], ['CC', ['and']], ['NP', [['DP', [['DT', ['the']]]], ['NP', [['NN', ['Kremlin']], ['NP', [['NN', ['leader']]]]]]]]]]]], ['NP', [['NN', ['would']], ['NN', ['meet']], ['NR', ['Dec']]]]]], ['PU', ['.']]]], ['IP', [['QP', [['CD', ['2']], ['PU', ['-']], ['CD', ['3']]]], ['NN', ['aboard']], ['NN', ['U']], ['PU', ['.']], ['IP', [['NN', ['S']], ['PU', ['.']], ['IP', [['CC', ['and']], ['VP', [['NN', ['Soviet']], ['NN', ['naval']], ['VP', [['NN', ['vessels']], ['PP', [['P', ['in']], ['NP', [['NP', [['DP', [['DT', ['the']]]], ['NN', ['Mediterranean']]]], ['PP', [['P', ['to']], ['NP', [['NP', [['NN', ['discuss']]]], ['QP', [['CD', ['a']], ['NP', [['NP', [['NN', ['wide']], ['NN', ['range']]]], ['PP', [['P', ['of']], ['NP', [['NP', [['NN', ['issues']]]], ['PP', [['P', ['without']], ['NP', [['CD', ['a']], ['NP', [['NN', ['formal']], ['NP', [['NN', ['agenda']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], ['PU', ['.']]]]]]]"
# hanlp_directory = "../dataset/penntreebank_english/hanlp/"
# error_sentence_index = []
# error_sentence_brackets_left = []
# for count in range(1, 49209):
#     file_path = str(hanlp_directory) + 'sentence_' + str(count) + '.txt'
#     read_file = open(file_path, "r")
#     read_line = read_file.readline()
#     hanlp_sentence = read_line.rstrip()
#
#     hanlp_characters = [char for char in hanlp_sentence]
#     hanlp_brackets = []
#     hanlp_brackets_index = []
#
#     for j in range(0, len(hanlp_characters)):
#         if hanlp_characters[j] in ['[', ']']:
#             hanlp_brackets.append(hanlp_characters[j])
#             hanlp_brackets_index.append(j)
#
#     cluster_bracket_index = []
#
#     brackets_array = hanlp_brackets
#     brackets_index_array = hanlp_brackets_index
#
#     try:
#         current_length_bracket_array = len(brackets_array)
#         previous_length_bracket_array = 0
#         while len(brackets_array) > 0:
#             previous_length_bracket_array = current_length_bracket_array
#             for i in range(0, len(brackets_array)-1):
#                 if brackets_array[i] == '[' and brackets_array[i+1] == ']':
#                     cluster_bracket = []
#                     cluster_bracket.append(brackets_index_array[i])
#                     cluster_bracket.append(brackets_index_array[i+1])
#                     cluster_bracket_index.append(cluster_bracket)
#                     brackets_array.pop(i)
#                     brackets_array.pop(i)
#                     brackets_index_array.pop(i)
#                     brackets_index_array.pop(i)
#                     break
#                 else:
#                     continue
#             current_length_bracket_array = len(brackets_array)
#             if previous_length_bracket_array == current_length_bracket_array:
#                 if len(brackets_array) > 0:
#                     # print("Length of brackets left: " + str(len(brackets_array)))
#                     # print("brackets left: " + str(brackets_array))
#                     error_sentence_index.append(count)
#                     error_sentence_brackets_left.append(brackets_array)
#                     raise Exception("Invalid number of brackets")
#                 break
#     except:
#         continue
#
# print(error_sentence_index)
# print(error_sentence_brackets_left)
# print(brackets_index_array)

#hanlp_sentence = "[['TOP', [['IP', [['NP', [['NP', [['DP', [['DT', ['The']]]], ['NP', [['NN', ['president']]]]]], ['VP', [['VP', [['VC', ['said']], ['NP', [['PN', ['that']], ['NN', ['he']], ['CC', ['and']], ['NP', [['DP', [['DT', ['the']]]], ['NP', [['NN', ['Kremlin']], ['NP', [['NN', ['leader']]]]]]]]]]]], ['NP', [['NN', ['would']], ['NN', ['meet']], ['NR', ['Dec']]]]]], ['PU', ['.']]]], ['IP', [['QP', [['CD', ['2']], ['PU', ['-']], ['CD', ['3']]]], ['NN', ['aboard']], ['NN', ['U']], ['PU', ['.']], ['IP', [['NN', ['S']], ['PU', ['.']], ['IP', [['CC', ['and']], ['VP', [['NN', ['Soviet']], ['NN', ['naval']], ['VP', [['NN', ['vessels']], ['PP', [['P', ['in']], ['NP', [['NP', [['DP', [['DT', ['the']]]], ['NN', ['Mediterranean']]]], ['PP', [['P', ['to']], ['NP', [['NP', [['NN', ['discuss']]]], ['QP', [['CD', ['a']], ['NP', [['NP', [['NN', ['wide']], ['NN', ['range']]]], ['PP', [['P', ['of']], ['NP', [['NP', [['NN', ['issues']]]], ['PP', [['P', ['without']], ['NP', [['CD', ['a']], ['NP', [['NN', ['formal']], ['NP', [['NN', ['agenda']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], ['PU', ['.']]]]]]]"
#hanlp_sentence_try = "[['TOP', [['IP', [['NP', [['NP', [['DP', [['DT', ['The']]]], ['NP', [['NN', ['president']]]]]], ['VP', [['VP', [['VC', ['said']], ['NP', [['PN', ['that']], ['NN', ['he']], ['CC', ['and']], ['NP', [['DP', [['DT', ['the']]]], ['NP', [['NN', ['Kremlin']], ['NP', [['NN', ['leader']]]]]]]]]]]], ['NP', [['NN', ['would']], ['NN', ['meet']], ['NR', ['Dec']]]]]], ['PU', ['.']]]], ['IP', [['QP', [['CD', ['2']], ['PU', ['-']], ['CD', ['3']]]], ['NN', ['aboard']], ['NN', ['U']], ['PU', ['.']], ['IP', [['NN', ['S']], ['PU', ['.']], ['IP', [['CC', ['and']], ['VP', [['NN', ['Soviet']], ['NN', ['naval']], ['VP', [['NN', ['vessels']], ['PP', [['P', ['in']], ['NP', [['NP', [['DP', [['DT', ['the']]]], ['NN', ['Mediterranean']]]], ['PP', [['P', ['to']], ['NP', [['NP', [['NN', ['discuss']]]], ['QP', [['CD', ['a']], ['NP', [['NP', [['NN', ['wide']], ['NN', ['range']]]], ['PP', [['P', ['of']], ['NP', [['NP', [['NN', ['issues']]]], ['PP', [['P', ['without']], ['NP', [['CD', ['a']], ['NP', [['NN', ['formal']], ['NP', [['NN', ['agenda']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], ['PU', ['.']]]]]]]"

# [['DP', [['DT', The]]], ['NP', [['NN', ['president']]]]]
# (S (NP (DT The) (NN president)) (VP (VBD said) (SBAR (IN that) (S (NP (NP (PRP he)) (CC and) (NP (DT the) (NNP Kremlin) (NN leader))) (VP (MD would) (VP (VB meet) (NP (NNP Dec.) (CD 2) (SYM -) (CD 3)) (PP (IN aboard) (NP (NP (NNP U.S.) (CC and) (JJ Soviet) (JJ naval) (NNS vessels)) (PP (IN in) (NP (DT the) (NNP Mediterranean))))) (S (VP (TO to) (VP (VB discuss) (NP (NP (DT a) (JJ wide) (NN range)) (PP (IN of) (NP (NNS issues)))) (PP (IN without) (NP (DT a) (JJ formal) (NN agenda))))))))))) (. .))

# hanlp_characters = [char for char in hanlp_sentence]
# hanlp_brackets = []
# hanlp_brackets_index = []
#
# for j in range(0, len(hanlp_characters)):
#     if hanlp_characters[j] in ['[', ']']:
#         hanlp_brackets.append(hanlp_characters[j])
#         hanlp_brackets_index.append(j)
#
# cluster_bracket_index = []
#
# brackets_array = hanlp_brackets
# brackets_index_array = hanlp_brackets_index
#
#
# current_length_bracket_array = len(brackets_array)
# previous_length_bracket_array = 0
# while len(brackets_array) > 0:
#     previous_length_bracket_array = current_length_bracket_array
#     for i in range(0, len(brackets_array)-1):
#         if brackets_array[i] == '[' and brackets_array[i+1] == ']':
#             cluster_bracket = []
#             cluster_bracket.append(brackets_index_array[i])
#             cluster_bracket.append(brackets_index_array[i+1])
#             cluster_bracket_index.append(cluster_bracket)
#             brackets_array.pop(i)
#             brackets_array.pop(i)
#             brackets_index_array.pop(i)
#             brackets_index_array.pop(i)
#             break
#         else:
#             continue
#     current_length_bracket_array = len(brackets_array)
#     if previous_length_bracket_array == current_length_bracket_array:
#         if len(brackets_array) > 0:
#             print("Length of brackets left: " + str(len(brackets_array)))
#             print("brackets left: " + str(brackets_array))
#             raise Exception("Invalid number of brackets")
#         break
#
# hanlp_characters_try = hanlp_characters
#
# change = 1
# index = 0
# while change > 0:
#     change = 0
#     for i in range(index, len(hanlp_characters_try)):
#         if hanlp_characters_try[i] == "\'":
#             hanlp_characters_try.pop(i)
#             change = 1
#             index = i
#             break
#
# # print(hanlp_characters_try)
#
# change = 1
# index = 0
# while change > 0:
#     change = 0
#     for i in range(index, len(hanlp_characters_try)-1):
#         if (hanlp_characters_try[i] == ",") and (hanlp_characters_try[i+1] == " "):
#             hanlp_characters_try.pop(i)
#             change = 1
#             index = i
#             break
#
# print(''.join(hanlp_characters_try))

# import re
# import string
# import random
# letters = string.ascii_lowercase
# formatted_sentence = "[[TOP [[IP [[NP [[NP [[DP [[DT [The]]]] [NP [[NN [president]]]]]] [VP [[VP [[VC [said]] [NP [[PN [that]] [NN [he]] [CC [and]] [NP [[DP [[DT [the]]]] [NP [[NN [Kremlin]] [NP [[NN [leader]]]]]]]]]]]] [NP [[NN [would]] [NN [meet]] [NR [Dec]]]]]] [PU [.]]]] [IP [[QP [[CD [2]] [PU [-]] [CD [3]]]] [NN [aboard]] [NN [U]] [PU [.]] [IP [[NN [S]] [PU [.]] [IP [[CC [and]] [VP [[NN [Soviet]] [NN [naval]] [VP [[NN [vessels]] [PP [[P [in]] [NP [[NP [[DP [[DT [the]]]] [NN [Mediterranean]]]] [PP [[P [to]] [NP [[NP [[NN [discuss]]]] [QP [[CD [a]] [NP [[NP [[NN [wide]] [NN [range]]]] [PP [[P [of]] [NP [[NP [[NN [issues]]]] [PP [[P [without]] [NP [[CD [a]] [NP [[NN [formal]] [NP [[NN [agenda]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] [PU [.]]]]]]]"
#
# formatted_characters = [char for char in formatted_sentence]
# special_characters = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '{', '}', '\"', "\'", ';', ':', '?', '/', '`', '~']
# for i in range(0, len(formatted_characters)):
#     if formatted_characters[i] in special_characters:
#         formatted_characters[i] = random.choice(letters)
#
# formatted_sentence = ''.join(formatted_characters)
#
# pos = re.findall("\[\w+ ", formatted_sentence)
# tokens = re.findall("\[\w+.\]", formatted_sentence)
#
# print(pos)
# print(tokens)
#
# formatted_tokens = ['']*len(tokens)
# for i in range(0, len(tokens)):
#     formatted_tokens[i] = str(tokens[i]).replace('[', '')
#     formatted_tokens[i] = str(formatted_tokens[i]).replace(']]', ']')
#
# # print(formatted_tokens)
#
# for i in range(0, len(tokens)):
#     formatted_sentence = formatted_sentence.replace(tokens[i], formatted_tokens[i], 1)
#
# print(formatted_sentence)
#
# hanlp_characters = [char for char in formatted_sentence]
# hanlp_brackets = []
# hanlp_brackets_index = []
#
# for j in range(0, len(hanlp_characters)):
#     if hanlp_characters[j] in ['[', ']']:
#         hanlp_brackets.append(hanlp_characters[j])
#         hanlp_brackets_index.append(j)
#
# cluster_bracket_index = []
#
# brackets_array = hanlp_brackets
# brackets_index_array = hanlp_brackets_index
#
#
# current_length_bracket_array = len(brackets_array)
# previous_length_bracket_array = 0
# while len(brackets_array) > 0:
#     previous_length_bracket_array = current_length_bracket_array
#     for i in range(0, len(brackets_array)-1):
#         if brackets_array[i] == '[' and brackets_array[i+1] == ']':
#             cluster_bracket = []
#             cluster_bracket.append(brackets_index_array[i])
#             cluster_bracket.append(brackets_index_array[i+1])
#             cluster_bracket_index.append(cluster_bracket)
#             brackets_array.pop(i)
#             brackets_array.pop(i)
#             brackets_index_array.pop(i)
#             brackets_index_array.pop(i)
#             break
#         else:
#             continue
#     current_length_bracket_array = len(brackets_array)
#     if previous_length_bracket_array == current_length_bracket_array:
#         if len(brackets_array) > 0:
#             print("Length of brackets left: " + str(len(brackets_array)))
#             print("brackets left: " + str(brackets_array))
#             raise Exception("Invalid number of brackets")
#         break
#
# print(cluster_bracket_index)
# index_to_remove = []
# for i in range(0, len(hanlp_characters) -2):
#     if (hanlp_characters[i] == " ") and (hanlp_characters[i+1] == "[") and (hanlp_characters[i+2] == "["):
#         index_to_remove.append(i+1)
#
# print(index_to_remove)
# brackets_to_remove = []
#
# change = 1
# index = 0
# while change > 0:
#     change = 0
#     for i in range(index, len(cluster_bracket_index)):
#         if cluster_bracket_index[i][0] in index_to_remove:
#             brackets_to_remove.append(cluster_bracket_index[i])
#             change = 1
#             index = i + 1
#             break
#
# print(brackets_to_remove)
# print(len(pos))
# print(len(brackets_to_remove))
# brackets_to_remove_bkp = brackets_to_remove
# hanlp_characters_bkp = hanlp_characters
# counter = 0
# while (counter != len(brackets_to_remove)):
#     hanlp_characters_bkp.pop(brackets_to_remove[counter][0] - 2* counter)
#     hanlp_characters_bkp.pop((brackets_to_remove[counter][1] - 2 * counter) - 1)
#     counter = counter + 1
#
# print(''.join(hanlp_characters_bkp))

# character_index_to_remove = []
# for i in range(0, len(brackets_to_remove)):
#     character_index_to_remove.append(brackets_to_remove[i][0])
#     character_index_to_remove.append(brackets_to_remove[i][1])
#
# character_index_to_remove.append(0)
# character_index_to_remove.append(len(hanlp_characters)-1)
#
# after_removal_characters = []
# for i in range(0, len(hanlp_characters)):
#     if i not in character_index_to_remove:
#         after_removal_characters.append(hanlp_characters[i])
#
# print(''.join(after_removal_characters))

#[TOP [IP [NP [NP [DP [DT The]] [NP [NN president]]] [VP [VP [VC said] [NP [PN that] [NN he] [CC and] [NP [DP [DT the]] [NP [NN Kremlin] [NP [NN leader]]]]]] [NP [NN would] [NN meet] [NR Dec]]] [PU t]] [IP [QP [CD 2] [PU x] [CD 3]] [NN aboard] [NN U] [PU s] [IP [NN S] [PU x] [IP [CC and] [VP [NN Soviet] [NN naval] [VP [NN vessels] [PP [P in] [NP [NP [DP [DT the]] [NN Mediterranean]] [PP [P to] [NP [NP [NN discuss]] [QP [CD a] [NP [NP [NN wide] [NN range]] [PP [P of] [NP [NP [NN issues]] [PP [P without] [NP [CD a] [NP [NN formal] [NP [NN agenda]]]]]]]]]]]]]]]]]] [PU c]]]

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for testing hanlp_resources.pre_format_hanlp_parsed_sentence class
############################################################################

# from hanlp_resources import pre_format_hanlp_parsed_sentence
#
# hanlp_sentence = "[['TOP', [['IP', [['NP', [['NP', [['DP', [['DT', ['The']]]], ['NP', [['NN', ['president']]]]]], ['VP', [['VP', [['VC', ['said']], ['NP', [['PN', ['that']], ['NN', ['he']], ['CC', ['and']], ['NP', [['DP', [['DT', ['the']]]], ['NP', [['NN', ['Kremlin']], ['NP', [['NN', ['leader']]]]]]]]]]]], ['NP', [['NN', ['would']], ['NN', ['meet']], ['NR', ['Dec']]]]]], ['PU', ['.']]]], ['IP', [['QP', [['CD', ['2']], ['PU', ['-']], ['CD', ['3']]]], ['NN', ['aboard']], ['NN', ['U']], ['PU', ['.']], ['IP', [['NN', ['S']], ['PU', ['.']], ['IP', [['CC', ['and']], ['VP', [['NN', ['Soviet']], ['NN', ['naval']], ['VP', [['NN', ['vessels']], ['PP', [['P', ['in']], ['NP', [['NP', [['DP', [['DT', ['the']]]], ['NN', ['Mediterranean']]]], ['PP', [['P', ['to']], ['NP', [['NP', [['NN', ['discuss']]]], ['QP', [['CD', ['a']], ['NP', [['NP', [['NN', ['wide']], ['NN', ['range']]]], ['PP', [['P', ['of']], ['NP', [['NP', [['NN', ['issues']]]], ['PP', [['P', ['without']], ['NP', [['CD', ['a']], ['NP', [['NN', ['formal']], ['NP', [['NN', ['agenda']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], ['PU', ['.']]]]]]]"
#
# pre_format_hanlp_parsed_sentence_object = pre_format_hanlp_parsed_sentence(hanlp_sentence, language='English')
# pre_formatted_sentence = pre_format_hanlp_parsed_sentence_object.pre_format_sentence(hanlp_parsed_sentence=hanlp_sentence)
# print(pre_formatted_sentence)

#############################################################################
#End Block
############################################################################


############################################################################
#This block contains code for obtaining unique clusters
############################################################################
# import pickle
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset = "penntreebank_english/"
# folders = ["allennlp", "berkeley", "hanlp", "corenlp", "ground_truth"]


# pickle_path = str(pickle_dump_directory) + str(dataset) + str('allennlp')
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     allennlp_sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     allennlp_sentence_cluster_dictionary = pickle.load(handle)
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('berkeley')
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     berkeley_sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     berkeley_sentence_cluster_dictionary = pickle.load(handle)
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('hanlp')
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     hanlp_sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     hanlp_sentence_cluster_dictionary = pickle.load(handle)

# pickle_path = str(pickle_dump_directory) + str(dataset) + str('corenlp')
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     corenlp_sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     corenlp_sentence_cluster_dictionary = pickle.load(handle)

# pickle_path = str(pickle_dump_directory) + str(dataset) + str('ground_truth')
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     ground_truth_sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     ground_truth_sentence_cluster_dictionary = pickle.load(handle)

# print(hanlp_sentence_cluster_dictionary[1])
# print(corenlp_sentence_cluster_dictionary[1])

# unique_sentence_cluster_dictionary = {}

# for i in range(1, 2):
#     cluster_span = hanlp_sentence_cluster_dictionary[i]['cluster_span']
#     cluster_pos = hanlp_sentence_cluster_dictionary[i]['cluster_pos']
#     unique_cluster_span = []
#     for j in range(0, len(cluster_span)):
#         if cluster_span[j] not in unique_cluster_span:
#             unique_cluster_span.append(cluster_span[j])
#     print(unique_cluster_span)
#     unique_pos_span = []
#     for k in range(0, len(unique_cluster_span)):
#         single_cluster_pos = []
#         for j in range(0, len(cluster_span)):
#             if cluster_span[j] == unique_cluster_span[k]:
#                  single_cluster_pos.append(cluster_pos[j])
#         unique_pos_span.append(single_cluster_pos)
#     print(unique_pos_span)


#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for obtaining support for unique clusters
############################################################################
# import pickle
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset = "penntreebank_english/"
# folders = ["allennlp", "berkeley", "hanlp", "corenlp", "ground_truth"]
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('allennlp')
# with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#     allennlp_unique_sentence_cluster_dictionary = pickle.load(handle)
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('berkeley')
# with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#     berkeley_unique_sentence_cluster_dictionary = pickle.load(handle)
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('hanlp')
# with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#     hanlp_unique_sentence_cluster_dictionary = pickle.load(handle)
#
# pickle_path = str(pickle_dump_directory) + str(dataset) + str('corenlp')
# with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#     corenlp_unique_sentence_cluster_dictionary = pickle.load(handle)
#
# for k in range(1,2):
#     allennlp_unique_cluster_span = allennlp_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
#     allennlp_unique_pos_span = allennlp_unique_sentence_cluster_dictionary[k]['unique_pos_span']
#     allennlp_error = allennlp_unique_sentence_cluster_dictionary[k]['error']
#
#     berkeley_unique_cluster_span = berkeley_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
#     berkeley_unique_pos_span = berkeley_unique_sentence_cluster_dictionary[k]['unique_pos_span']
#     berkeley_error = berkeley_unique_sentence_cluster_dictionary[k]['error']
#
#     hanlp_unique_cluster_span = hanlp_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
#     hanlp_unique_pos_span = hanlp_unique_sentence_cluster_dictionary[k]['unique_pos_span']
#     hanlp_error = hanlp_unique_sentence_cluster_dictionary[k]['error']
#
#     corenlp_unique_cluster_span = corenlp_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
#     corenlp_unique_pos_span = corenlp_unique_sentence_cluster_dictionary[k]['unique_pos_span']
#     corenlp_error = corenlp_unique_sentence_cluster_dictionary[k]['error']
#
#     total_cluster_span = allennlp_unique_cluster_span + berkeley_unique_cluster_span + hanlp_unique_cluster_span + corenlp_unique_cluster_span
#
#     total_unique_cluster_span = []
#
#     for i in range(0, len(total_cluster_span)):
#         if total_cluster_span[i] not in total_unique_cluster_span:
#             total_unique_cluster_span.append(total_cluster_span[i])
#     print(total_unique_cluster_span)
#     total_unique_cluster_support = []
#     total_unique_cluster_pos = []
#
#     for i in range(0, len(total_unique_cluster_span)):
#         support = []
#         pos = []
#         boolean = False
#         for j in range(0, len(allennlp_unique_cluster_span)):
#             boolean = False
#             if allennlp_unique_cluster_span[j] == total_unique_cluster_span[i]:
#                 support.append(1)
#                 pos.append(allennlp_unique_pos_span[j])
#                 boolean = True
#                 break
#         if boolean == False:
#             support.append(0)
#             empty_array = []
#             pos.append(empty_array)
#
#         for j in range(0, len(berkeley_unique_cluster_span)):
#             boolean = False
#             if berkeley_unique_cluster_span[j] == total_unique_cluster_span[i]:
#                 support.append(1)
#                 pos.append(berkeley_unique_pos_span[j])
#                 boolean = True
#                 break
#         if boolean == False:
#             support.append(0)
#             empty_array = []
#             pos.append(empty_array)
#
#         for j in range(0, len(hanlp_unique_cluster_span)):
#             boolean = False
#             if hanlp_unique_cluster_span[j] == total_unique_cluster_span[i]:
#                 support.append(1)
#                 pos.append(hanlp_unique_pos_span[j])
#                 boolean = True
#                 break
#         if boolean == False:
#             support.append(0)
#             empty_array = []
#             pos.append(empty_array)
#
#         for j in range(0, len(corenlp_unique_cluster_span)):
#             boolean = False
#             if corenlp_unique_cluster_span[j] == total_unique_cluster_span[i]:
#                 support.append(1)
#                 pos.append(corenlp_unique_pos_span[j])
#                 boolean = True
#                 break
#         if boolean == False:
#             support.append(0)
#             empty_array = []
#             pos.append(empty_array)
#
#         total_unique_cluster_support.append(support)
#         total_unique_cluster_pos.append(pos)
#
#
# print(total_unique_cluster_span)
# print(total_unique_cluster_support)
# print(total_unique_cluster_pos)

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for obtaining support for unique clusters
############################################################################

# import pickle
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset = "penntreebank_english/"
# folders = ["allennlp", "berkeley", "hanlp", "corenlp"]
#
# loop_dictionary = {}
#
# for i in range(0, len(folders)):
#     loop_dictionary[i] = {}
#     pickle_path = str(pickle_dump_directory) + str(dataset) + str(folders[i])
#     with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#         unique_sentence_cluster_dictionary = pickle.load(handle)
#     loop_dictionary[i]['dictionary'] = unique_sentence_cluster_dictionary
#
# #print(loop_dictionary[0]['dictionary'][1]['unique_cluster_span'])
#
# input_cluster_support_dictionary = {}
#
# for k in range(1,2):
#     total_cluster_span = []
#     length = 0
#     for f in range(0, len(folders)):
#         unique_cluster_span = loop_dictionary[f]['dictionary'][k]['unique_cluster_span']
#         # unique_pos_span = loop_dictionary[f]['dictionary'][k]['unique_pos_span']
#         # error = loop_dictionary[f]['dictionary'][k]['error']
#         total_cluster_span = total_cluster_span + unique_cluster_span
#         length = length + len(unique_cluster_span)
#     # print(total_cluster_span)
#     # print(len(total_cluster_span))
#     # print(length)
#
#     total_unique_cluster_span = []
#
#     for i in range(0, len(total_cluster_span)):
#         if total_cluster_span[i] not in total_unique_cluster_span:
#             total_unique_cluster_span.append(total_cluster_span[i])
#     print(total_unique_cluster_span)
#     total_unique_cluster_support = []
#     total_unique_cluster_pos = []
#
#     for i in range(0, len(total_unique_cluster_span)):
#         support = []
#         pos = []
#         boolean = False
#         for f in range(0, len(folders)):
#             unique_cluster_span = loop_dictionary[f]['dictionary'][k]['unique_cluster_span']
#             unique_pos_span = loop_dictionary[f]['dictionary'][k]['unique_pos_span']
#             for j in range(0, len(unique_cluster_span)):
#                 boolean = False
#                 if unique_cluster_span[j] == total_unique_cluster_span[i]:
#                     support.append(1)
#                     pos.append(unique_pos_span[j])
#                     boolean = True
#                     break
#             if boolean == False:
#                 support.append(0)
#                 empty_array = []
#                 pos.append(empty_array)
#         total_unique_cluster_support.append(support)
#         total_unique_cluster_pos.append(pos)
#
#     input_cluster_support_dictionary[k] = {}
#     input_cluster_support_dictionary[k]['total_unique_cluster_span'] = total_unique_cluster_span
#     input_cluster_support_dictionary[k]['total_unique_cluster_support'] = total_unique_cluster_support
#     input_cluster_support_dictionary[k]['total_unique_cluster_pos'] = total_unique_cluster_pos
#     error_boolean = False
#     for f in range(0, len(folders)):
#         error = loop_dictionary[f]['dictionary'][k]['error']
#         if (error_boolean or error):
#             error_boolean = True
#     input_cluster_support_dictionary[k]['error'] = error_boolean
#
#     print(error_boolean)
#     print(total_unique_cluster_span)
#     print(total_unique_cluster_support)
#     print(total_unique_cluster_pos)


#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for medcpt optimal solution
############################################################################

# import pickle
# import numpy as np

# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset = "penntreebank_english/"
# medcpt_directory = str(pickle_dump_directory) + str(dataset) + 'medcpt'
#
# with open(str(medcpt_directory) + '/input_cluster_support_dictionary.pickle', 'rb') as handle:
#     input_cluster_support_dictionary = pickle.load(handle)
#
# for k in range(1,2):
#     total_unique_cluster_span = input_cluster_support_dictionary[k]['total_unique_cluster_span']
#     total_unique_cluster_support = input_cluster_support_dictionary[k]['total_unique_cluster_support']
#     total_unique_cluster_pos = input_cluster_support_dictionary[k]['total_unique_cluster_pos']
#     error = input_cluster_support_dictionary[k]['error']
#     if error == False:
#         input_parser_count = len(input_cluster_support_dictionary[k]['total_unique_cluster_support'][0])
#         print(input_parser_count)
#         input_parser_weight = [1]*input_parser_count
#         weighted_support = []
#         sum_parser_weight = np.sum(input_parser_weight)
#         print(sum_parser_weight)
#         for i in range(0, len(total_unique_cluster_support)):
#             cluster_weight = 0
#             for j in range(0, len(total_unique_cluster_support[i])):
#                 cluster_weight = cluster_weight + total_unique_cluster_support[i][j] * input_parser_weight[j]
#             cluster_support = cluster_weight/sum_parser_weight
#             weighted_support.append(cluster_support)
#
#         medcpt_clusters = []
#         medcpt_pos = []
#         temp_cluster_array = []
#         temp_cluster_pos = []
#         for i in range(0, len(weighted_support)):
#             if weighted_support[i] > 0.5:
#                 medcpt_clusters.append(total_unique_cluster_span[i])
#                 medcpt_pos.append(total_unique_cluster_pos[i])
#             elif weighted_support[i] == 0.5:
#                 temp_cluster_array.append(total_unique_cluster_span[i])
#                 temp_cluster_pos.append(total_unique_cluster_pos[i])
#
#         print(temp_cluster_array)
#
#         print(medcpt_clusters)

        # def check_cluster_compatibility(temp_cluster_array):
        #     compatible_boolean = []
        #     appended_cluster_array = ['']*len(temp_cluster_array)
        #     for i in range(0, len(temp_cluster_array)):
        #         appended_cluster_array[i] = str(temp_cluster_array[i]).replace(' ', '')
        #
        #     for i in range(0, len(appended_cluster_array)):
        #         compatible_boolean_cluster = True
        #         for j in range(0, len(appended_cluster_array)):


        #def isindependent(cluster1, cluster2):
# cluster1 = '3435363738394041'
# cluster1 = '9899100101102'
# cluster2 = '40414243'
# # print(cluster1)
# # print(cluster2)
# characters_cluster1 = [char for char in cluster1]
# characters_cluster2 = [char for char in cluster2]

# digit_span = 1
# difference_array = []
# for i in range(0, len(characters_cluster1)-1):
#     difference_array.append(int(characters_cluster1[i+1]) - int(characters_cluster1[i]))
# for i in range(0, len(difference_array)):
#     if difference_array[i] != 1:
#         digit_span = digit_span + 1
# digit_span = 2
# updated_character_cluster = []
# counter = 0
# while (counter +digit_span) <= len(characters_cluster1):
#     for i in range(counter, len(characters_cluster1)):
#         updated_character = ''
#         for j in range(0, digit_span):
#             updated_character = updated_character + characters_cluster1[i+j]
#         updated_character_cluster.append(updated_character)
#         counter = counter + digit_span
#         if updated_character in ['9', '99', '999', '9999']:
#             digit_span = digit_span + 1
#         break
#
# print(updated_character_cluster)


# def get_character_cluster(cluster):
#     characters_cluster = [char for char in cluster]
#     boolean = False
#     digit_span = 1
#     formatted_character_cluster = []
#     while boolean == False:
#         updated_character_cluster = []
#         counter = 0
#         while (counter + digit_span) <= len(characters_cluster):
#             for i in range(counter, len(characters_cluster)):
#                 previous_character = ''
#                 if counter != 0:
#                     for j in range(counter-digit_span, counter):
#                         previous_character = previous_character + characters_cluster[j]
#
#                 updated_character = ''
#                 for j in range(0, digit_span):
#                     updated_character = updated_character + characters_cluster[i + j]
#                 updated_character_cluster.append(updated_character)
#                 counter = counter + digit_span
#
#                 if (counter + digit_span + 1) <= len(characters_cluster):
#                     next_character = ''
#                     for j in range(0, digit_span+1):
#                         next_character = next_character + characters_cluster[counter + j]
#
#                     if (digit_span == 1) and (updated_character == '9') and (next_character == '10') and (previous_character == '8'):
#                         digit_span = digit_span + 1
#                     elif (digit_span == 2) and (updated_character == '99') and (next_character == '100') and (previous_character == '98'):
#                         digit_span = digit_span + 1
#                     elif (digit_span == 3) and (updated_character == '999') and (next_character == '1000') and (previous_character == '998'):
#                         digit_span = digit_span + 1
#                     elif (digit_span == 4) and (updated_character == '9999'):
#                         digit_span = digit_span + 1
#
#                 break
#
#         #print(updated_character_cluster)
#
#         difference_array = []
#         for i in range(0, len(updated_character_cluster)-1):
#             difference_array.append(int(updated_character_cluster[i+1]) - int(updated_character_cluster[i]))
#         for i in range(0, len(difference_array)):
#             if difference_array[i] != 1:
#                 digit_span = digit_span + 1
#                 boolean = False
#                 break
#             else:
#                 boolean = True
#
#         if boolean == True:
#             formatted_character_cluster = updated_character_cluster
#
#     return formatted_character_cluster
#
# temp_cluster_array = ['123456 78910 111213', '78910','101112']
#
# def check_cluster_compatibility(temp_cluster_array):
#     compatible_boolean = []
#     appended_cluster_array = ['']*len(temp_cluster_array)
#     for i in range(0, len(temp_cluster_array)):
#         appended_cluster_array[i] = str(temp_cluster_array[i]).replace(' ', '')
#
#     for i in range(0, len(appended_cluster_array)):
#         compatible_boolean_cluster = []
#         for j in range(0, len(appended_cluster_array)):
#             characters = [char for char in appended_cluster_array[j]]
#             if (appended_cluster_array[j] in appended_cluster_array[i]) or (appended_cluster_array[i] in appended_cluster_array[j]):
#                 compatible_boolean_cluster.append(True)
#
#             elif len(characters) <= 3:
#                 compatible_boolean_cluster.append(True)
#             else:
#                 first_array = get_character_cluster(appended_cluster_array[i])
#                 second_array = get_character_cluster(appended_cluster_array[j])
#
#                 print(first_array)
#                 print(second_array)
#
#                 independent_boolean = True
#
#                 for a in range(0, len(second_array)):
#                     if second_array[a] in first_array:
#                         independent_boolean = False
#                         break
#                 compatible_boolean_cluster.append(independent_boolean)
#         compatible_boolean.append(compatible_boolean_cluster)
#
#     return compatible_boolean

# compatible_boolean = check_cluster_compatibility(temp_cluster_array)
# print(compatible_boolean)

# cluster = '72'
# print(get_character_cluster(cluster))
# cluster1 = '78910111213'
# print(get_character_cluster(cluster1))
# cluster2 = '1213141516'
# print(get_character_cluster(cluster2))
# cluster3 = '9899100'
# print(get_character_cluster(cluster3))
# cluster4 = '101102103104105'
# print(get_character_cluster(cluster4))


    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for igraph maximal independent set
############################################################################

# compatibility_matrix = [[True, True, True], [True, True, False], [True, False, True]]
#
# incompatible_clusters_count = []
#
# for i in range(0, len(compatibility_matrix)):
#     if False not in compatibility_matrix[i]:
#         incompatible_clusters_count.append(0)
#     else:
#         count_false = 0
#         for j in range(0, len(compatibility_matrix[i])):
#             if compatibility_matrix[i][j] == False:
#                 count_false = count_false + 1
#         incompatible_clusters_count.append(count_false)
#
# print(incompatible_clusters_count)
#
# compatible_cluster_index = []
#
# incompatible_count = 0
# max_incompatible_count = np.max(incompatible_clusters_count)
#
# while incompatible_count <= max_incompatible_count:
#     for i in range(0, len(incompatible_clusters_count)):
#         if incompatible_clusters_count[i] == incompatible_count:
#             if incompatible_count == 0:
#                 if i not in compatible_cluster_index:
#                     compatible_cluster_index.append(i)
#             else:
#                 for j in range(0, len(compatibility_matrix[i])):
#                     if compatibility_matrix[i][j] == False:
#                         if (j not in compatible_cluster_index) and (i not in compatible_cluster_index):
#                             compatible_cluster_index.append(i)
#
#     incompatible_count = incompatible_count + 1
#
# print(compatible_cluster_index)

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for evaluation metrics
############################################################################

# import pickle
# import numpy as np
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset = "penntreebank_english/"
# medcpt_directory = str(pickle_dump_directory) + str(dataset) + 'medcpt'
# ground_truth_directory = str(pickle_dump_directory) + str(dataset) + 'ground_truth'
#
# with open(str(medcpt_directory) + '/medcpt_aggregate_clusters_dictionary.pickle', 'rb') as handle:
#     medcpt_aggregate_clusters_dictionary = pickle.load(handle)
#
# with open(str(ground_truth_directory) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#     unique_sentence_cluster_dictionary = pickle.load(handle)
#
# # print(medcpt_aggregate_clusters_dictionary[2])
# # print(unique_sentence_cluster_dictionary[2])
#
# def robinson_foulds_distance(cluster1, cluster2):
#     cluster1 = set(cluster1)
#     cluster2 = set(cluster2)
#     difference = cluster1.symmetric_difference(cluster2)
#     print(difference)
#     list_difference = list(difference)
#     print(list_difference)
#     robinsonfould_distance = len(list_difference)
#     return robinsonfould_distance
#
# #print(robinson_foulds_distance(medcpt_aggregate_clusters_dictionary[2]['medcpt_clusters'], unique_sentence_cluster_dictionary[2]['unique_cluster_span']))
#
# def precision_score(true_cluster, predict_cluster):
#     TP = 0
#     for i in range(0, len(predict_cluster)):
#         if predict_cluster[i] in true_cluster:
#             TP = TP + 1
#     if len(predict_cluster) != 0:
#         precision = TP/len(predict_cluster)
#     else:
#         precision = 0
#
#     return precision
#
# def recall_score(true_cluster, predict_cluster):
#     TP = 0
#     for i in range(0, len(true_cluster)):
#         if true_cluster[i] in predict_cluster:
#             TP = TP + 1
#     if len(true_cluster) != 0:
#         recall = TP/len(true_cluster)
#     else:
#         recall = 0
#
#     return recall
#
# def f1_score(true_cluster, predict_cluster):
#     precision = precision_score(true_cluster=true_cluster, predict_cluster=predict_cluster)
#     recall = recall_score(true_cluster=true_cluster, predict_cluster=predict_cluster)
#
#     if (precision+recall) == 0:
#         f1 = 0
#     else:
#         f1 = (2*precision*recall)/(precision+recall)
#
#     return f1
#
# def accuracy_score(true_cluster, predict_cluster):
#     correct = 0
#     for i in range(0, len(predict_cluster)):
#         if predict_cluster[i] in true_cluster:
#             correct = correct + 1
#     if len(predict_cluster) != 0:
#         accuracy = correct / len(predict_cluster)
#     else:
#         accuracy = 0
#
#     return accuracy
#
# def precision_score_label(true_cluster, true_label, predict_cluster, predict_label):
#     TP = 0
#     FP = 0
#     for i in range(0, len(predict_cluster)):
#         prediction_boolean = False
#         for j in range(0, len(true_cluster)):
#             if true_cluster[j] == predict_cluster[i]:
#                 prediction_boolean = True
#                 for a in range(0, len(true_label[j])):
#                     ground_truth_label = str(true_label[j][a]).split('-')[0]
#                     boolean = False
#                     for k in range(0, len(predict_label[i])):
#                         prediction_label = str(predict_label[i][k]).split('-')[0]
#                         if prediction_label == ground_truth_label:
#                             TP = TP + 1
#                             boolean = True
#                             break
#                     if boolean == False:
#                         FP = FP + 1
#                 break
#         if prediction_boolean == False:
#             FP = FP + len(predict_label[i])
#
#     if (TP+FP) == 0:
#         precision = 0
#     else:
#         precision = (TP/(TP+FP))
#     return precision
#
# def recall_score_label(true_cluster, true_label, predict_cluster, predict_label):
#     TP = 0
#     FN = 0
#     for i in range(0, len(true_cluster)):
#         true_boolean = False
#         for j in range(0, len(predict_cluster)):
#             if predict_cluster[j] == true_cluster[i]:
#                 true_boolean = True
#                 for a in range(0, len(true_label[i])):
#                     ground_truth_label = str(true_label[i][a]).split('-')[0]
#                     boolean = False
#                     for k in range(0, len(predict_label[j])):
#                         prediction_label = str(predict_label[j][k]).split('-')[0]
#                         if prediction_label == ground_truth_label:
#                             TP = TP + 1
#                             boolean = True
#                             break
#                     if boolean == False:
#                         FN = FN + 1
#                 break
#         if true_boolean == False:
#             FN = FN + len(true_label[i])
#     if (TP+FN) == 0:
#         recall = 0
#     else:
#         recall = (TP/(TP+FN))
#     return recall
#
# def f1_score_label(true_cluster, true_label, predict_cluster, predict_label):
#     precision = precision_score_label(true_cluster=true_cluster, true_label= true_label, predict_cluster=predict_cluster, predict_label=predict_label)
#     recall = recall_score_label(true_cluster=true_cluster, true_label= true_label, predict_cluster=predict_cluster, predict_label=predict_label)
#
#     if (precision+recall) == 0:
#         f1 = 0
#     else:
#         f1 = (2*precision*recall)/(precision+recall)
#
#     return f1
#
# true_cluster = unique_sentence_cluster_dictionary[1]['unique_cluster_span']
# predict_cluster = medcpt_aggregate_clusters_dictionary[1]['medcpt_clusters']
# true_label = unique_sentence_cluster_dictionary[1]['unique_pos_span']
# predict_label = medcpt_aggregate_clusters_dictionary[1]['medcpt_pos']
#
# print(precision_score(true_cluster, predict_cluster))
# print(recall_score(true_cluster, predict_cluster))
# print(f1_score(true_cluster, predict_cluster))

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for validating evaluation results
############################################################################
#
# import pickle
# pickle_dump_directory = "../dictionary_pickle_files/"
# #directories = ["penntreebank_english/", "ontonotes_english/"]
# directories = [ "ontonotes_chinese/"]
# #folders = ["allennlp", "berkeley", "hanlp", "corenlp"]
# folders = ["sapar", "berkeley", "hanlp", "corenlp"]
#
# for d in range(0, len(directories)):
#     results_directory = str(pickle_dump_directory) + str(directories[d]) + 'results'
#     with open(str(results_directory) + '/results_dictionary.pickle', 'rb') as handle:
#         results_dictionary = pickle.load(handle)
#     print("Dataset: " + str(str(directories[d]).split('/')[0]))
#     for f in range(0, len(folders)):
#         folder = folders[f]
#         print("Baseline: " + str(folder))
#         print("robinson_foulds_distance: " + str(results_dictionary[folder]['robinson_foulds_distance']))
#         print("precision_score: " + str(results_dictionary[folder]['precision_score']))
#         print("recall_score: " + str(results_dictionary[folder]['recall_score']))
#         print("f1_score: " + str(results_dictionary[folder]['f1_score']))
#         print("accuracy_score: " + str(results_dictionary[folder]['accuracy_score']))
#         print("precision_score_label: " + str(results_dictionary[folder]['precision_score_label']))
#         print("recall_score_label: " + str(results_dictionary[folder]['recall_score_label']))
#         print("f1_score_label: " + str(results_dictionary[folder]['f1_score_label']))
#         print("accuracy_score_label: " + str(results_dictionary[folder]['accuracy_score_label']))
#         print("count: " + str(results_dictionary[folder]['count']))

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for correcting errors in support calculation
############################################################################

# sentence = "8_9_10_11_12_13_14_15_16_"
#
# tokens = sentence.split("_")
# print(tokens)
# tokens.remove('')
# print(tokens)

# import os
# import pickle
#
#
# def get_support(loop_dictionary, input_parser_count, current_sentence_count):
#     total_cluster_span = []
#     for f in range(0, input_parser_count):
#         unique_cluster_span = loop_dictionary[f]['dictionary'][current_sentence_count]['unique_cluster_span']
#         total_cluster_span = total_cluster_span + unique_cluster_span
#
#     total_unique_cluster_span = []
#     for i in range(0, len(total_cluster_span)):
#         if total_cluster_span[i] not in total_unique_cluster_span:
#             total_unique_cluster_span.append(total_cluster_span[i])
#
#     total_unique_cluster_support = []
#     total_unique_cluster_pos = []
#     for i in range(0, len(total_unique_cluster_span)):
#         support = []
#         pos = []
#         boolean = False
#         for f in range(0, input_parser_count):
#             unique_cluster_span = loop_dictionary[f]['dictionary'][current_sentence_count]['unique_cluster_span']
#             unique_pos_span = loop_dictionary[f]['dictionary'][current_sentence_count]['unique_pos_span']
#             for j in range(0, len(unique_cluster_span)):
#                 boolean = False
#                 if unique_cluster_span[j] == total_unique_cluster_span[i]:
#                     support.append(1)
#                     pos.append(unique_pos_span[j])
#                     boolean = True
#                     break
#             if boolean == False:
#                 support.append(0)
#                 empty_array = []
#                 pos.append(empty_array)
#         if len(support) == input_parser_count:
#             total_unique_cluster_support.append(support)
#             total_unique_cluster_pos.append(pos)
#         else:
#             difference = input_parser_count - len(support)
#             for i in range(0, difference):
#                 support.append(0)
#                 empty_array = []
#                 pos.append(empty_array)
#             total_unique_cluster_support.append(support)
#             total_unique_cluster_pos.append(pos)
#
#     return total_unique_cluster_span, total_unique_cluster_support, total_unique_cluster_pos
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# directories = ["penntreebank_english/"]
# folders = ["allennlp", "berkeley", "hanlp", "corenlp"]
# sentences = [49208]
#
# for d in range(0, len(directories)):
#     directory = str(pickle_dump_directory) + str(directories[d])
#     sentence_count = sentences[d]
#
#     loop_dictionary = {}
#     for f in range(0, len(folders)):
#         loop_dictionary[f] = {}
#         pickle_path = str(directory) + str(folders[f])
#         with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
#             unique_sentence_cluster_dictionary = pickle.load(handle)
#         loop_dictionary[f]['dictionary'] = unique_sentence_cluster_dictionary
#
#     #input_cluster_support_dictionary = {}
#     input_parser_count = len(folders)
#     #for k in range(1, sentence_count+1):
#     for k in range(65, 66):
#         current_sentence_count = k
#         #input_cluster_support_dictionary[current_sentence_count] = {}
#         print(loop_dictionary[0]['dictionary'][current_sentence_count]['unique_cluster_span'])
#         print(loop_dictionary[1]['dictionary'][current_sentence_count]['unique_cluster_span'])
#         print(loop_dictionary[2]['dictionary'][current_sentence_count]['unique_cluster_span'])
#         print(loop_dictionary[3]['dictionary'][current_sentence_count]['error'])
#         print(input_parser_count)
#         print(current_sentence_count)
#         total_unique_cluster_span, total_unique_cluster_support, total_unique_cluster_pos = get_support(loop_dictionary=loop_dictionary, input_parser_count=input_parser_count, current_sentence_count=current_sentence_count)
#
#         #print(total_unique_cluster_span)
#         print(total_unique_cluster_support)
#         #print(total_unique_cluster_pos)
#
#         # input_cluster_support_dictionary[current_sentence_count]['total_unique_cluster_span'] = total_unique_cluster_span
#         # input_cluster_support_dictionary[current_sentence_count]['total_unique_cluster_support'] = total_unique_cluster_support
#         # input_cluster_support_dictionary[current_sentence_count]['total_unique_cluster_pos'] = total_unique_cluster_pos
#         # error_boolean = False
#         # for f in range(0, input_parser_count):
#         #     error = loop_dictionary[f]['dictionary'][current_sentence_count]['error']
#         #     if (error_boolean or error):
#         #         error_boolean = True
#         # input_cluster_support_dictionary[current_sentence_count]['error'] = error_boolean

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for calculating accuracy score for labels
############################################################################

# def accuracy_score_label(self, true_cluster, true_label, predict_cluster, predict_label):
#     TP = 0
#     FP = 0
#     for i in range(0, len(predict_cluster)):
#         prediction_boolean = False
#         for j in range(0, len(true_cluster)):
#             if true_cluster[j] == predict_cluster[i]:
#                 prediction_boolean = True
#                 for a in range(0, len(true_label[j])):
#                     ground_truth_label = str(true_label[j][a]).split('-')[0]
#                     boolean = False
#                     for k in range(0, len(predict_label[i])):
#                         prediction_label = str(predict_label[i][k]).split('-')[0]
#                         if prediction_label == ground_truth_label:
#                             TP = TP + 1
#                             boolean = True
#                             break
#                     if boolean == False:
#                         FP = FP + 1
#                 break
#
#     if (TP + FP) == 0:
#         accuracy = 0
#     else:
#         accuracy = (TP / (TP + FP))
#     return accuracy

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for medcpt POS aggregation
############################################################################

# import pickle
# import numpy as np
# pickle_dump_directory = "../dictionary_pickle_files_bkp/"
# dataset = "penntreebank_english/"
# medcpt_directory = str(pickle_dump_directory) + str(dataset) + 'medcpt'
#
# with open(str(medcpt_directory) + '/medcpt_aggregate_clusters_dictionary.pickle', 'rb') as handle:
#     medcpt_aggregate_clusters_dictionary = pickle.load(handle)
#
# # print(medcpt_aggregate_clusters_dictionary[1])
#
# medcpt_pos = medcpt_aggregate_clusters_dictionary[1]['medcpt_pos']
# print(medcpt_pos)
# weight = [1,1,1,1]
# mv = []
# for i in range(0, len(medcpt_pos)):
#     support = []
#     pos_labels = []
#     weight_pos = []
#     for j in range(0, len(medcpt_pos[i])):
#         for k in range(0, len(medcpt_pos[i][j])):
#             pos_labels.append(medcpt_pos[i][j][k])
#             weight_pos.append(weight[j])
#     unique_pos_labels = []
#     for a in range(0, len(pos_labels)):
#         if pos_labels[a] not in unique_pos_labels:
#             unique_pos_labels.append(pos_labels[a])
#             support.append(weight_pos[a])
#         else:
#             for b in range(0, len(unique_pos_labels)):
#                 if unique_pos_labels[b] == pos_labels[a]:
#                     support[b] = support[b] + weight_pos[a]
#
#     print(unique_pos_labels)
#     print(support)
#     print(pos_labels)
#     print(weight_pos)
#
#     max_support_index = np.argmax(support)
#     mv.append(unique_pos_labels[max_support_index])
#
# print(mv)
#
# print(len(mv))
# print(len(medcpt_aggregate_clusters_dictionary[1]['medcpt_clusters']))

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for testing resources.py
############################################################################

# import pickle
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset_directory = "../dataset/"
# directories = ["penntreebank_english/", "ontonotes_english/"]
# folders = ["allennlp", "berkeley", "hanlp", "corenlp", "ground_truth"]
#
# pickle_directory = str(pickle_dump_directory) + str(directories[0])
# pickle_path = str(pickle_directory) + str(folders[0]) + '/'
#
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     sentence_dictionary_pickle = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     sentence_cluster_dictionary_pickle = pickle.load(handle)
#
# with open(str(pickle_path) + '/parser_input_dictionary.pickle', 'rb') as handle:
#     parser_input_dictionary_pickle = pickle.load(handle)
#
# print(sentence_dictionary_pickle[1])
#
# print(sentence_cluster_dictionary_pickle[1])
#
# print(parser_input_dictionary_pickle[1])


    #############################################################################
#End Block
############################################################################


############################################################################
#This block contains code for testing resources.py
############################################################################

# import pickle
# pickle_dump_directory = "../dictionary_pickle_files/"
# dataset_directory = "../dataset/"
# directories = ["penntreebank_english/", "ontonotes_english/"]
# #directories = ["ontonotes_chinese/"]
# # directories = ["penntreebank_english/"]
# # folders = ["allennlp", "berkeley", "hanlp", "corenlp", "ground_truth"]
#
#
#
# # with open(str(pickle_path) + '/results_dictionary.pickle', 'rb') as handle:
# #     unique_sentence_cluster_dictionary_pickle = pickle.load(handle)
# #
# # print(unique_sentence_cluster_dictionary_pickle['allennlp']['robinson_foulds_distance'])
# # print(unique_sentence_cluster_dictionary_pickle['berkeley']['robinson_foulds_distance'])
# # print(unique_sentence_cluster_dictionary_pickle['hanlp']['robinson_foulds_distance'])
# # print(unique_sentence_cluster_dictionary_pickle['corenlp']['robinson_foulds_distance'])
#
#
# for d in range(0, len(directories)):
#     print("Dataset: " + str(str(directories[d]).split('/')[0]))
#     pickle_directory = str(pickle_dump_directory) + str(directories[d])
#     medcpt_directory = str(pickle_directory) + 'medcpt'
#     with open(str(medcpt_directory) + '/medcpt_aggregate_clusters_dictionary_log.pickle', 'rb') as handle:
#         medcpt_aggregate_clusters_dictionary = pickle.load(handle)
#
#     print("Weights: ")
#
#     weight_iterations = len(medcpt_aggregate_clusters_dictionary)
#     for j in range(0, weight_iterations):
#         iteration = j+1
#         print("Iteration: " + str(iteration))
#         print("MedCPT weight: " + str(medcpt_aggregate_clusters_dictionary[iteration]['input_parser_weight']))
#
#     pickle_path = str(pickle_directory) + str('results') + '/'
#     with open(str(pickle_path) + '/medcpt_results_dictionary_log.pickle', 'rb') as handle:
#         medcpt_results_dictionary = pickle.load(handle)
#
#     number_of_iterations = len(medcpt_results_dictionary)
#
#     for i in range(0, number_of_iterations):
#         iteration = i+1
#         print("Iteration: " + str(iteration))
#         print("robinson_foulds_distance: " + str(medcpt_results_dictionary[iteration]['robinson_foulds_distance']))
#         print("precision_score: " + str(medcpt_results_dictionary[iteration]['precision_score']))
#         print("recall_score: " + str(medcpt_results_dictionary[iteration]['recall_score']))
#         print("f1_score: " + str(medcpt_results_dictionary[iteration]['f1_score']))
#         print("accuracy_score: " + str(medcpt_results_dictionary[iteration]['accuracy_score']))
#         print("precision_score_label_mv: " + str(medcpt_results_dictionary[iteration]['precision_score_label_mv']))
#         print("recall_score_label_mv: " + str(medcpt_results_dictionary[iteration]['recall_score_label_mv']))
#         print("f1_score_label_mv: " + str(medcpt_results_dictionary[iteration]['f1_score_label_mv']))
#         print("accuracy_score_label_mv: " + str(medcpt_results_dictionary[iteration]['accuracy_score_label_mv']))
#         print("precision_score_label_weight: " + str(medcpt_results_dictionary[iteration]['precision_score_label_weight']))
#         print("recall_score_label_weight: " + str(medcpt_results_dictionary[iteration]['recall_score_label_weight']))
#         print("f1_score_label_weight: " + str(medcpt_results_dictionary[iteration]['f1_score_label_weight']))
#         print("accuracy_score_label_weight: " + str(medcpt_results_dictionary[iteration]['accuracy_score_label_weight']))
#         print("count: " + str(medcpt_results_dictionary[iteration]['count']))

# print(medcpt_results_dictionary_pickle[1]['robinson_foulds_distance'])
# print(medcpt_results_dictionary_pickle[2]['robinson_foulds_distance'])
# print(medcpt_results_dictionary_pickle[3]['robinson_foulds_distance'])
#
# print(medcpt_results_dictionary_pickle[1]['accuracy_score_label_mv'])
# print(medcpt_results_dictionary_pickle[2]['accuracy_score_label_mv'])
# print(medcpt_results_dictionary_pickle[3]['accuracy_score_label_mv'])
#
# print(unique_sentence_cluster_dictionary_pickle[1])


    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for testing max and sum weights
############################################################################

# import numpy as np
#
# # array = [0.2, 0.3, 0.4, 0.1]
# an_array = np.random.rand(10)*10
# print(an_array)
# norm = np.linalg.norm(an_array)
# print(norm)
# normal_array = an_array/norm
# print(normal_array)
# print(list(normal_array))
# max_index = np.argmax(array)
# print(max_index)
# max_value = array[max_index]
# print(max_value)

# sum = np.sum(array)
#
# for a in range(0, len(array)):
#     array[a] = array[a]/sum
#
# print(array)

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for updating POS aggegation
############################################################################
# import pickle
# import numpy as np
# from collections import Counter
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# directory = "penntreebank_english/"
# pickle_dataset_dump_directory = str(pickle_dump_directory) + str(directory)
# medcpt_directory = str(pickle_dump_directory) + str(directory) + 'medcpt'
# with open(str(medcpt_directory) + '/input_cluster_support_dictionary.pickle', 'rb') as handle:
#     input_cluster_support_dictionary = pickle.load(handle)
#
# total_unique_cluster_span = input_cluster_support_dictionary[2]['total_unique_cluster_span']
# total_unique_cluster_support = input_cluster_support_dictionary[2]['total_unique_cluster_support']
# total_unique_cluster_pos = input_cluster_support_dictionary[2]['total_unique_cluster_pos']
# error = input_cluster_support_dictionary[2]['error']
#
# print(total_unique_cluster_pos)

# array = []
# for i in range(0, len(total_unique_cluster_pos)):
#     internal_array = []
#     for j in range(0, len(total_unique_cluster_pos[i])):
#         internal_array.append(len(total_unique_cluster_pos[i][j]))
#     array.append(internal_array)
#
# print(array)

# c = Counter(array[0])
# print(c.most_common(1)[0][0])
# pos_labels_number = []
# for i in range(0, len(array)):
#     c = Counter(array[i])
#     pos_labels_number.append(c.most_common(1)[0][0])
#
# print(pos_labels_number)

# print(array[0][:0])

# def aggregate_pos_labels(medcpt_pos, input_parser_weight):
#     pos_aggregation = []
#     for i in range(0, len(medcpt_pos)):
#         support = []
#         pos_labels = []
#         weight_pos = []
#         internal_count_array = []
#         for j in range(0, len(medcpt_pos[i])):
#             internal_count_array.append(len(medcpt_pos[i][j]))
#             for k in range(0, len(medcpt_pos[i][j])):
#                 pos_labels.append(medcpt_pos[i][j][k])
#                 weight_pos.append(input_parser_weight[j])
#         unique_pos_labels = []
#         for a in range(0, len(pos_labels)):
#             if pos_labels[a] not in unique_pos_labels:
#                 unique_pos_labels.append(pos_labels[a])
#                 support.append(weight_pos[a])
#             else:
#                 for b in range(0, len(unique_pos_labels)):
#                     if unique_pos_labels[b] == pos_labels[a]:
#                         support[b] = support[b] + weight_pos[a]
#
#         c = Counter(internal_count_array)
#         pos_labels_number = c.most_common(1)[0][0]
#         if pos_labels_number == 0:
#             pos_labels_number = 1
#         #print(support)
#         sorted_unique_pos_labels = [x for _, x in sorted(zip(support, unique_pos_labels), reverse=True)]
#         print(support)
#         print(sorted_unique_pos_labels)
#         aggregate_pos = sorted_unique_pos_labels[:pos_labels_number]
#         # max_support_index = np.argmax(support)
#         # aggregate_pos = []
#         # aggregate_pos.append(unique_pos_labels[max_support_index])
#         pos_aggregation.append(aggregate_pos)
#
#     return pos_aggregation
#
# input_parser_weight = [1,1,1,1]
#
# print(aggregate_pos_labels(total_unique_cluster_pos, input_parser_weight))

    #############################################################################
#End Block
############################################################################

# import pickle
#
# from resources import character_indexing, clusters_from_parsed_sentence
#
# pickle_dump_directory = "../dictionary_pickle_files/"
# directories = ["ontonotes_chinese/"]
# folder = "hanlp"
# sentence_count = 51230
#
# pickle_directory = str(pickle_dump_directory) + str(directories[0])
# pickle_path = str(pickle_directory) + str(folder) + '/'
#
# berkeley_path = str(pickle_directory) + str("berkeley") + '/'
#
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     sentence_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     sentence_cluster_dictionary = pickle.load(handle)
#
# with open(str(pickle_path) + '/parser_input_dictionary.pickle', 'rb') as handle:
#     parser_input_dictionary = pickle.load(handle)
#
#
# with open(str(berkeley_path) + '/sentence_dictionary.pickle', 'rb') as handle:
#     sentence_dictionary_berkeley = pickle.load(handle)
#
# with open(str(berkeley_path) + '/sentence_cluster_dictionary.pickle', 'rb') as handle:
#     sentence_cluster_dictionary_berkeley = pickle.load(handle)
#
#
# #
# error_sentences = []
# for k in range(1, sentence_count+1):
#     if sentence_dictionary[k]['error'] == True:
#         error_sentences.append(k)
#
# print(len(error_sentences))
#
# for i in range(0, len(error_sentences)):
#     k = error_sentences[i]
#     sentence_dictionary[k]['formatted_parsed_sentence'] = sentence_dictionary_berkeley[k]['formatted_parsed_sentence']
#     sentence_dictionary[k]['characters'] = sentence_dictionary_berkeley[k]['characters']
#     sentence_dictionary[k]['character_index'] = sentence_dictionary_berkeley[k]['character_index']
#     sentence_dictionary[k]['character_index_size'] = sentence_dictionary_berkeley[k]['character_index_size']
#     sentence_dictionary[k]['error'] = False
#
#     sentence_cluster_dictionary[k]['formatted_parsed_sentence'] = sentence_cluster_dictionary_berkeley[k]['formatted_parsed_sentence']
#     sentence_cluster_dictionary[k]['character_clusters'] = sentence_cluster_dictionary_berkeley[k]['character_clusters']
#     sentence_cluster_dictionary[k]['cluster_span'] = sentence_cluster_dictionary_berkeley[k]['cluster_span']
#     sentence_cluster_dictionary[k]['cluster_pos'] = sentence_cluster_dictionary_berkeley[k]['cluster_pos']
#     sentence_cluster_dictionary[k]['error'] = False
#
# with open(str(pickle_path) + '/sentence_dictionary.pickle', 'wb') as handle:
#     pickle.dump(sentence_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
# with open(str(pickle_path) + '/sentence_cluster_dictionary.pickle', 'wb') as handle:
#     pickle.dump(sentence_cluster_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)


# number = 0
# print(error_sentences[number])
# print(parser_input_dictionary[error_sentences[number]]['parsed_input_sentence'])
# #print(parser_input_dictionary[error_sentences[0]]['pre_formatted_sentence'])
#
# from hanlp_resources import pre_format_hanlp_parsed_sentence
# parsed_sentence = parser_input_dictionary[error_sentences[number]]['parsed_input_sentence']
# pre_format_hanlp_parsed_sentence_object = pre_format_hanlp_parsed_sentence(parsed_sentence, language='English')
# pre_formatted_sentence = pre_format_hanlp_parsed_sentence_object.pre_format_sentence(hanlp_parsed_sentence=parsed_sentence)

#[['TOP', [['IP', [['NP', [['NN', ['ㄅㄆㄇ']]]], ['VP', [['VV', ['加']], ['NP', [['NN', ['ABC']]]]]], ['PRN', [['PU', ['——']], ['IP', [['NP', [['NN', ['小学']], ['NN', ['英语']]]], ['VP', [['ADVP', [['AD', ['全面']]]], ['VP', [['VV', ['开讲']]]]]]]]]]]]]]]

#(TOP (IP (NP (NN ㄅㄆㄇ)) (VP (VV 加) (NP (NN ABC))) (PRN (PU (——)) (IP (NP (NN 小学) (NN 英语)) (VP (ADVP (AD 全面)) (VP (VV 开讲)))))))

#parsed_sentence = parser_input_dictionary[error_sentences[7]]['pre_formatted_sentence']
# parsed_sentence = pre_formatted_sentence
# #parsed_sentence = parser_input_dictionary[148]['parsed_input_sentence']
# character_indexing_object = character_indexing(parsed_sentence=parsed_sentence, language='English')
# formatted_parsed_sentence, characters, character_index = character_indexing_object.format_parsed_sentence(
#     parsed_sentence=parsed_sentence)
# print(formatted_parsed_sentence)
# print(characters)
# print(character_index)
# clusters_from_parsed_sentence_object = clusters_from_parsed_sentence(
#     parsed_sentence=formatted_parsed_sentence, language='English')
# character_clusters, cluster_span, cluster_pos = clusters_from_parsed_sentence_object.get_clusters()


#[['TOP', [['IP', [['PP', [['P', ['针对']], ['NP', [['CP', [['CP', [['IP', [['VP', [['LCP', [['IP', [['NP', [['PU', ['「']], ['NT', ['五二○']], ['PU', ['」']]]], ['NP', [['ADJP', [['JJ', ['新']]]], ['NP', [['NN', ['政府']]]]]], ['VP', [['VV', ['就职']', ['以来']]]], ['PU', ['，']], ['VP', [['VV', ['导致']], ['IP', [['NP', [['NN', ['朝野']]]], ['VP', [['ADVP', [['AD', ['尖锐']]]], ['VP', [['VV', ['对立']]]]]]]]]]]]]], ['DEC', ['的']]]]]], ['IP', [['NP', [['NN', ['核四']]]], ['VP', [['VV', ['停建']'NN', ['问题']]]]]]]], ['PU', ['，']], ['NP', [['NP', [['NP', [['DP', [['DT', ['上']]]], ['NP', [['NN', ['月']]]]]], ['NP', [['NN', ['司法院']]]], ['NP', [['NN', ['大法官']], ['NN', ['会议']]]]]], ['ADJP', [['JJ', ['释字']]]], ['QP', [['OD', ['第五二', ['号']]]]]], ['NP', [['NN', ['解释文']]]]]], ['VP', [['VV', ['做出']], ['NP', [['DNP', [['NP', [['PU', ['「']], ['NN', ['程序']], ['NN', ['瑕疵']], ['PU', ['」']]]], ['DEG', ['的']]]], ['NP', [['NN', ['结论']]]]]]]], ['PU', ['。']]]]]]]

#[['TOP', [['IP', [['PP', [['P', ['针对']], ['NP', [['CP', [['CP', [['IP', [['VP', [['LCP', [['IP', [['NP', [['PU', ['「']], ['NT', ['五二○']], ['PU', ['」']]]], ['NP', [['ADJP', [['JJ', ['新']]]], ['NP', [['NN', ['政府']]]]]], ['VP', [['VV', ['就职'], 'NN', ['以来']]]], ['PU', ['，']], ['VP', [['VV', ['导致']], ['IP', [['NP', [['NN', ['朝野']]]], ['VP', [['ADVP', [['AD', ['尖锐']]]], ['VP', [['VV', ['对立']]]]]]]]]]]]]], ['DEC', ['的']]]]]], ['IP', [['NP', [['NN', ['核四']]]], ['VP', [['VV', ['停建']'NN', ['问题']]]]]]]], ['PU', ['，']], ['NP', [['NP', [['NP', [['DP', [['DT', ['上']]]], ['NP', [['NN', ['月']]]]]], ['NP', [['NN', ['司法院']]]], ['NP', [['NN', ['大法官']], ['NN', ['会议']]]]]], ['ADJP', [['JJ', ['释字']]]], ['QP', [['OD', ['第五二', ['号']]]]]], ['NP', [['NN', ['解释文']]]]]], ['VP', [['VV', ['做出']], ['NP', [['DNP', [['NP', [['PU', ['「']], ['NN', ['程序']], ['NN', ['瑕疵']], ['PU', ['」']]]], ['DEG', ['的']]]], ['NP', [['NN', ['结论']]]]]]]], ['PU', ['。']]]]]]]




#################

#sentence = "[[TOP [[IP [[IP [[NP [[NP [[PU [s]] [NR [CHINA]] [PU [c]]]] [PU [q]] [NP [[PU [g]] [NP [[NR [庾澄庆]]]] [CC [＆]] [NP [[ADJP [[JJ [顶尖]]]] [NP [[NN [拍档]]]]]] [PU [c]]]] [PU [o]] [NP [[PU [y]] [NR [BABOO]] [PU [m]]]] [PU [n]] [NP [[NP [[NR [伍佰]]] [NP [[NP [[PN [其]]]] [NP [[NN [乐团]]]]]]]] [ETC [等]]]] [PU [m]] [VP [[ADVP [[AD [都]]]] [VP [[VV [集中]] [IP [[VP [[PP [[P [在]] [QP [[OD [八十一]] [CLP [[M [年]]]]]]]] [VP [[VV [发行]]]]]]]]]]]]]] [PU [k]] [IP [[NP [[PN [这]]]] [VP [[ADVP [[AD [[让]] [NP [[NN [乐坛]]]] [IP [[VP [[QP [[CD [一]] [CLP [[M [阵]]]]]] [VP [[VV [振奋]]]]]]]]]]]]]] [PU [h]] [IP [[ADVP [[AD [于是]]]] [IP [[PU [o]] [NP [[NN [乐团]] [NN [时代]]]] [VP [[ADVP [[AD [已经]]]] [VP [[VV [来临]]]]]] [PU [x]]]] [VP [[ADVP [[AAD [再度]]]] [VP [[SB [被]] [VP [[VV [提出]]]]]]]]]] [PU [b]]]]]]]"


############################################################################
#This block contains code for testing log values
############################################################################

# import math
# import numpy as np
#
# array = [2,4,6,8]
# sum_value = np.sum(array)
#
# weights = []
# for a in range(0, len(array)):
#     weight = - math.log(array[a]/8 + 1e-7)
#     weights.append(weight)
#
# print(weights)

    #############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for histogram plots
############################################################################

import matplotlib.pyplot as plt
# sentences = [49208, 133300, 51230]
# datasets = ['PTB English', 'Ontonotes English', 'Ontonotes Chinese']
# avg_tokens_sentence = [23.83, 17.90, 9.43]
#
# # n, bins, patches = plt.hist(x=sentences, bins='auto', color="brown", alpha = 0.7, rwidth = 0.85)
# # plt.grid(axis='y', alpha=0.75)
# # plt.xlabel()
#
# plt.bar(datasets, sentences, align='center', color='brown')
# plt.xlabel('Datasets', size= 30)
# plt.ylabel('Sentence Count', size=30)
# plt.title("Sentence Count in Datasets", fontsize = 35 )
# plt.xticks(size=30)
# plt.yticks(size=30)
#
# plt.show()

# import numpy as np
#
# datasets = ['PTB English', 'Ontonotes English', 'Ontonotes Chinese']
#
# all_parsers_same = [18.79, 24.58, 3.39]
# two_parsers_same = [4.31, 6.9, 32.52]
# all_parsers_different = [76.9, 68.52, 64.07]
#
# x = np.arange(len(datasets))
# width = 0.35
#
# fig, ax = plt.subplots()
# fig.suptitle("Conflict percentage among the input constituency parse trees", fontsize = 35)
# rects1 = ax.bar(x - width/2, all_parsers_same, width, label="All Parser Outputs Same")
# #rects2 = ax.bar(x + width/3, two_parsers_same, width, label="Two Parser Outputs Same")
# rects3 = ax.bar(x + width/2, all_parsers_different, width, label="All Parser Outputs Different")
#
# ax.set_ylabel('Percentage', size=30)
# ax.set_xticks(x)
# ax.set_xticklabels(datasets, size=30)
# ax.legend(prop={'size': 20})
#
# ax.bar_label(rects1, padding=3)
# # ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
#
# fig.tight_layout()
# plt.show()


import numpy as np

iteration = [1,2,3,4]

ontonotes_eng_allennlp = [1, 3.34, 3.50, 3.50]
ontonotes_eng_berkeley = [1, 2.889, 3.07, 3.07]
ontonotes_eng_hanlp = [1, 0.309, 0.29, 0.29]
ontonotes_eng_corenlp = [1, 1.74, 1.73, 1.73]

ptb_eng_allennlp = [1, 3.4706, 3.5490, 3.5490]
ptb_eng_berkeley = [1, 2.201, 2.27013, 2.27013]
ptb_eng_hanlp = [1, 0.39076, 0.378308, 0.378308]
ptb_eng_corenlp = [1, 1.7053, 1.6986, 1.6986]

ontonotes_chi_sapar = [1, 2.2535, 2.13, 2.13]
ontonotes_chi_berkeley = [1, 0.68540, 0.5764, 0.5764]
ontonotes_chi_hanlp = [1, 1.46793, 1.55972, 1.55972]
ontonotes_chi_corenlp = [1, 1.8282, 2.21435, 2.21435]

# plt.plot(iteration, ontonotes_eng_allennlp, label='Allennlp')
# plt.plot(iteration, ontonotes_eng_berkeley, label='Berkeley')
# plt.plot(iteration, ontonotes_eng_hanlp, label='Hanlp')
# plt.plot(iteration, ontonotes_eng_corenlp, label='Corenlp')
#
# plt.xlabel('Iteration', size= 30)
# plt.ylabel('Source Weight', size=30)
#
# plt.xticks(size=30)
# plt.yticks(size=30)
#
# plt.legend(prop={'size': 20})
# plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle("Source Weight Convergence", fontsize = 40)

ax1.plot(iteration, ptb_eng_allennlp, label='Allennlp')
ax1.plot(iteration, ptb_eng_berkeley, label='Berkeley')
ax1.plot(iteration, ptb_eng_hanlp, label='Hanlp')
ax1.plot(iteration, ptb_eng_corenlp, label='Corenlp')
ax1.set_title("PTB English", fontsize = 25)
#ax1.set(xlabel='Iteration', ylabel='Source Weight', labelsize=25)
ax1.set_xlabel('Iteration', fontsize = 25)
ax1.set_ylabel('Source Weight', fontsize = 25)
# ax1.set_xticklabels(labels='Iteration', fontsize=25)
# ax1.set_yticklabels(labels='Source Weight', fontsize=25)
# ax1.xaxis.set_tick_params(labelsize=35)
# ax1.yaxis.set_tick_params(labelsize=35)

# ax1.xlabel('Iteration', size= 30)
# ax1.ylabel('Source Weight', size=30)

# ax1.xticks(size=30)
# ax1.yticks(size=30)

ax1.legend(prop={'size': 20})

ax2.plot(iteration, ontonotes_eng_allennlp, label='Allennlp')
ax2.plot(iteration, ontonotes_eng_berkeley, label='Berkeley')
ax2.plot(iteration, ontonotes_eng_hanlp, label='Hanlp')
ax2.plot(iteration, ontonotes_eng_corenlp, label='Corenlp')
ax2.set_title("Ontonotes English", fontsize = 25)
# ax2.xlabel('Iteration', size= 30)
# ax2.ylabel('Source Weight', size=30)
# ax2.set(xlabel='Iteration', ylabel='Source Weight')
ax2.set_xlabel('Iteration', fontsize = 25)
ax2.set_ylabel('Source Weight', fontsize = 25)
# ax2.set_xticklabels(fontsize=15)
# ax2.set_yticklabels(fontsize=15)
# ax2.xticks(size=30)
# ax2.yticks(size=30)

ax2.legend(prop={'size': 20})

ax3.plot(iteration, ontonotes_chi_sapar, label='Sapar')
ax3.plot(iteration, ontonotes_chi_berkeley, label='Berkeley')
ax3.plot(iteration, ontonotes_chi_hanlp, label='Hanlp')
ax3.plot(iteration, ontonotes_chi_corenlp, label='Corenlp')
ax3.set_title("Ontonotes Chinese", fontsize = 25)
# ax3.xlabel('Iteration', size= 30)
# ax3.ylabel('Source Weight', size=30)
# ax3.set(xlabel='Iteration', ylabel='Source Weight')

ax3.set_xlabel('Iteration', fontsize = 25)
ax3.set_ylabel('Source Weight', fontsize = 25)

# ax3.set_xticklabels(fontsize=15)
# ax3.set_yticklabels(fontsize=15)
# ax3.xticks(size=30)
# ax3.yticks(size=30)

ax3.legend(prop={'size': 20})

plt.show()

    #############################################################################
#End Block
############################################################################
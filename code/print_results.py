############################################################################
#This block contains code for baseline_evaluation
############################################################################
import pickle
pickle_dump_directory = "../dictionary_pickle_files/"
directories = ["penntreebank_english/"]
folders = ["allennlp", "berkeley", "hanlp", "corenlp"]

for d in range(0, len(directories)):
    results_directory = str(pickle_dump_directory) + str(directories[d]) + 'results'
    with open(str(results_directory) + '/results_dictionary.pickle', 'rb') as handle:
        results_dictionary = pickle.load(handle)
    print("Dataset: " + str(str(directories[d]).split('/')[0]))
    for f in range(0, len(folders)):
        folder = folders[f]
        print("Baseline: " + str(folder))
        print("robinson_foulds_distance: " + str(results_dictionary[folder]['robinson_foulds_distance']))
        print("precision_score: " + str(results_dictionary[folder]['precision_score']))
        print("recall_score: " + str(results_dictionary[folder]['recall_score']))
        print("f1_score: " + str(results_dictionary[folder]['f1_score']))
        print("precision_score_label: " + str(results_dictionary[folder]['precision_score_label']))
        print("recall_score_label: " + str(results_dictionary[folder]['recall_score_label']))
        print("f1_score_label: " + str(results_dictionary[folder]['f1_score_label']))
        print("accuracy_score_label: " + str(results_dictionary[folder]['accuracy_score_label']))
        print("count: " + str(results_dictionary[folder]['count']))

#############################################################################
#End Block
############################################################################

############################################################################
#This block contains code for medcpt_evaluation
############################################################################

import pickle
pickle_dump_directory = "../dictionary_pickle_files/"
dataset_directory = "../sample_dataset/"
directories = ["penntreebank_english/"]


for d in range(0, len(directories)):
    print("Dataset: " + str(str(directories[d]).split('/')[0]))
    pickle_directory = str(pickle_dump_directory) + str(directories[d])
    medcpt_directory = str(pickle_directory) + 'medcpt'
    with open(str(medcpt_directory) + '/medcpt_aggregate_clusters_dictionary_log.pickle', 'rb') as handle:
        medcpt_aggregate_clusters_dictionary = pickle.load(handle)

    print("Weights: ")

    weight_iterations = len(medcpt_aggregate_clusters_dictionary)
    for j in range(0, weight_iterations):
        iteration = j+1
        print("Iteration: " + str(iteration))
        print("MedCPT weight: " + str(medcpt_aggregate_clusters_dictionary[iteration]['input_parser_weight']))

    pickle_path = str(pickle_directory) + str('results') + '/'
    with open(str(pickle_path) + '/medcpt_results_dictionary_log.pickle', 'rb') as handle:
        medcpt_results_dictionary = pickle.load(handle)

    number_of_iterations = len(medcpt_results_dictionary)

    for i in range(0, number_of_iterations):
        iteration = i+1
        print("Iteration: " + str(iteration))
        print("robinson_foulds_distance: " + str(medcpt_results_dictionary[iteration]['robinson_foulds_distance']))
        print("precision_score: " + str(medcpt_results_dictionary[iteration]['precision_score']))
        print("recall_score: " + str(medcpt_results_dictionary[iteration]['recall_score']))
        print("f1_score: " + str(medcpt_results_dictionary[iteration]['f1_score']))
        print("accuracy_score: " + str(medcpt_results_dictionary[iteration]['accuracy_score']))
        print("precision_score_label_mv: " + str(medcpt_results_dictionary[iteration]['precision_score_label_mv']))
        print("recall_score_label_mv: " + str(medcpt_results_dictionary[iteration]['recall_score_label_mv']))
        print("f1_score_label_mv: " + str(medcpt_results_dictionary[iteration]['f1_score_label_mv']))
        print("accuracy_score_label_mv: " + str(medcpt_results_dictionary[iteration]['accuracy_score_label_mv']))
        print("precision_score_label_weight: " + str(medcpt_results_dictionary[iteration]['precision_score_label_weight']))
        print("recall_score_label_weight: " + str(medcpt_results_dictionary[iteration]['recall_score_label_weight']))
        print("f1_score_label_weight: " + str(medcpt_results_dictionary[iteration]['f1_score_label_weight']))
        print("accuracy_score_label_weight: " + str(medcpt_results_dictionary[iteration]['accuracy_score_label_weight']))
        print("count: " + str(medcpt_results_dictionary[iteration]['count']))

#############################################################################
#End Block
############################################################################
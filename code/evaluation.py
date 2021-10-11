import pickle
import numpy as np
import os

class evaluation:
    def __init__(self, true_cluster, predict_cluster):
        self.true_cluster = true_cluster
        self.predict_cluster = predict_cluster

    def robinson_foulds_distance(self, cluster1, cluster2):
        cluster1 = set(cluster1)
        cluster2 = set(cluster2)
        difference = cluster1.symmetric_difference(cluster2)
        list_difference = list(difference)
        robinsonfould_distance = len(list_difference)
        return robinsonfould_distance

    def precision_score(self, true_cluster, predict_cluster):
        TP = 0
        for i in range(0, len(predict_cluster)):
            if predict_cluster[i] in true_cluster:
                TP = TP + 1
        if len(predict_cluster) != 0:
            precision = TP / len(predict_cluster)
        else:
            precision = 0

        precision = round(precision, 2)

        return precision

    def recall_score(self, true_cluster, predict_cluster):
        TP = 0
        for i in range(0, len(true_cluster)):
            if true_cluster[i] in predict_cluster:
                TP = TP + 1
        if len(true_cluster) != 0:
            recall = TP / len(true_cluster)
        else:
            recall = 0
        recall = round(recall, 2)
        return recall

    def f1_score(self, true_cluster, predict_cluster):
        precision = self.precision_score(true_cluster=true_cluster, predict_cluster=predict_cluster)
        recall = self.recall_score(true_cluster=true_cluster, predict_cluster=predict_cluster)

        if (precision + recall) == 0:
            f1 = 0
        else:
            f1 = (2 * precision * recall) / (precision + recall)
        f1 = round(f1, 2)
        return f1

    def accuracy_score(self, true_cluster, predict_cluster):
        correct = 0
        for i in range(0, len(predict_cluster)):
            if predict_cluster[i] in true_cluster:
                correct = correct + 1
        if len(predict_cluster) != 0:
            accuracy = correct / len(predict_cluster)
        else:
            accuracy = 0
        accuracy = round(accuracy, 2)
        return accuracy

    def precision_score_label(self, true_cluster, true_label, predict_cluster, predict_label):
        TP = 0
        FP = 0
        for i in range(0, len(predict_cluster)):
            prediction_boolean = False
            for j in range(0, len(true_cluster)):
                if true_cluster[j] == predict_cluster[i]:
                    prediction_boolean = True
                    for a in range(0, len(true_label[j])):
                        ground_truth_label = str(true_label[j][a]).split('-')[0]
                        boolean = False
                        for k in range(0, len(predict_label[i])):
                            prediction_label = str(predict_label[i][k]).split('-')[0]
                            if prediction_label == ground_truth_label:
                                TP = TP + 1
                                boolean = True
                                break
                        if boolean == False:
                            FP = FP + 1
                    break
            if prediction_boolean == False:
                FP = FP + len(predict_label[i])

        if (TP + FP) == 0:
            precision = 0
        else:
            precision = (TP / (TP + FP))

        precision = round(precision, 2)
        return precision

    def accuracy_score_label(self, true_cluster, true_label, predict_cluster, predict_label):
        TP = 0
        FP = 0
        for i in range(0, len(predict_cluster)):
            for j in range(0, len(true_cluster)):
                if true_cluster[j] == predict_cluster[i]:
                    for a in range(0, len(true_label[j])):
                        ground_truth_label = str(true_label[j][a]).split('-')[0]
                        boolean = False
                        for k in range(0, len(predict_label[i])):
                            prediction_label = str(predict_label[i][k]).split('-')[0]
                            if prediction_label == ground_truth_label:
                                TP = TP + 1
                                boolean = True
                                break
                        if boolean == False:
                            FP = FP + 1
                    break

        if (TP + FP) == 0:
            accuracy = 0
        else:
            accuracy = (TP / (TP + FP))

        accuracy = round(accuracy, 2)
        return accuracy

    def error_rate_label(self, true_cluster, true_label, predict_cluster, predict_label):
        TP = 0
        FP = 0
        for i in range(0, len(predict_cluster)):
            for j in range(0, len(true_cluster)):
                if true_cluster[j] == predict_cluster[i]:
                    for a in range(0, len(true_label[j])):
                        ground_truth_label = str(true_label[j][a]).split('-')[0]
                        boolean = False
                        for k in range(0, len(predict_label[i])):
                            prediction_label = str(predict_label[i][k]).split('-')[0]
                            if prediction_label == ground_truth_label:
                                TP = TP + 1
                                boolean = True
                                break
                        if boolean == False:
                            FP = FP + 1
                    break

        if (TP + FP) == 0:
            error_rate = 0
        else:
            error_rate = (FP / (TP + FP))

        error_rate = round(error_rate, 2)
        return error_rate

    def recall_score_label(self, true_cluster, true_label, predict_cluster, predict_label):
        TP = 0
        FN = 0
        for i in range(0, len(true_cluster)):
            true_boolean = False
            for j in range(0, len(predict_cluster)):
                if predict_cluster[j] == true_cluster[i]:
                    true_boolean = True
                    for a in range(0, len(true_label[i])):
                        ground_truth_label = str(true_label[i][a]).split('-')[0]
                        boolean = False
                        for k in range(0, len(predict_label[j])):
                            prediction_label = str(predict_label[j][k]).split('-')[0]
                            if prediction_label == ground_truth_label:
                                TP = TP + 1
                                boolean = True
                                break
                        if boolean == False:
                            FN = FN + 1
                    break
            if true_boolean == False:
                FN = FN + len(true_label[i])
        if (TP + FN) == 0:
            recall = 0
        else:
            recall = (TP / (TP + FN))
        recall = round(recall, 2)
        return recall

    def f1_score_label(self, true_cluster, true_label, predict_cluster, predict_label):
        precision = self.precision_score_label(true_cluster=true_cluster, true_label=true_label,
                                          predict_cluster=predict_cluster, predict_label=predict_label)
        recall = self.recall_score_label(true_cluster=true_cluster, true_label=true_label, predict_cluster=predict_cluster,
                                    predict_label=predict_label)

        if (precision + recall) == 0:
            f1 = 0
        else:
            f1 = (2 * precision * recall) / (precision + recall)
        f1 = round(f1, 2)
        return f1

def baseline_evaluation():
    pickle_dump_directory = "../dictionary_pickle_files/"
    directories = ["penntreebank_english/"]
    folders = ["berkeley", "hanlp", "corenlp", "allennlp"]
    sentences = [100]
    for i in range(0, len(directories)):
        directory = str(pickle_dump_directory) + str(directories[i])
        sentence_count = sentences[i]
        results_dictionary = {}
        ground_truth_pickle_path = str(directory) + str("ground_truth") + '/'
        with open(str(ground_truth_pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
            gt_unique_sentence_cluster_dictionary = pickle.load(handle)
        for j in range(0, len(folders)):
            folder = folders[j]
            pickle_path = str(directory) + str(folder) + '/'
            with open(str(pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
                unique_sentence_cluster_dictionary = pickle.load(handle)

            precision_score = []
            recall_score = []
            f1_score = []
            accuracy_score = []
            precision_score_label = []
            recall_score_label = []
            f1_score_label = []
            accuracy_score_label = []
            robinson_foulds_distance = []

            for k in range(1, sentence_count + 1):
                true_cluster = gt_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
                predict_cluster = unique_sentence_cluster_dictionary[k]['unique_cluster_span']
                true_label = gt_unique_sentence_cluster_dictionary[k]['unique_pos_span']
                predict_label = unique_sentence_cluster_dictionary[k]['unique_pos_span']
                true_error = gt_unique_sentence_cluster_dictionary[k]['error']
                predict_error = unique_sentence_cluster_dictionary[k]['error']

                for clu in range(0, len(true_cluster)):
                    string = true_cluster[clu]
                    string = string.replace(" ", "")
                    true_cluster[clu] = string
                for clu in range(0, len(predict_cluster)):
                    string = predict_cluster[clu]
                    string = string.replace(" ", "")
                    predict_cluster[clu] = string

                if (true_error==False) and (predict_error==False):
                    evaluation_object = evaluation(true_cluster=true_cluster, predict_cluster=predict_cluster)
                    robinson_foulds_distance.append(evaluation_object.robinson_foulds_distance(cluster1=true_cluster, cluster2=predict_cluster))
                    precision_score.append(evaluation_object.precision_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    recall_score.append(
                        evaluation_object.recall_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    f1_score.append(
                        evaluation_object.f1_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    accuracy_score.append(
                        evaluation_object.accuracy_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    precision_score_label.append(evaluation_object.precision_score_label(true_cluster=true_cluster, true_label= true_label, predict_cluster=predict_cluster, predict_label=predict_label))
                    recall_score_label.append(
                        evaluation_object.recall_score_label(true_cluster=true_cluster, true_label=true_label,
                                                                predict_cluster=predict_cluster,
                                                                predict_label=predict_label))
                    f1_score_label.append(
                        evaluation_object.f1_score_label(true_cluster=true_cluster, true_label=true_label,
                                                                predict_cluster=predict_cluster,
                                                                predict_label=predict_label))
                    accuracy_score_label.append(
                        evaluation_object.accuracy_score_label(true_cluster=true_cluster, true_label=true_label,
                                                         predict_cluster=predict_cluster,
                                                         predict_label=predict_label))

            results_dictionary[folder] = {}
            results_dictionary[folder]['robinson_foulds_distance'] = np.sum(robinson_foulds_distance)
            results_dictionary[folder]['precision_score'] = np.mean(precision_score)
            results_dictionary[folder]['recall_score'] = np.mean(recall_score)
            results_dictionary[folder]['f1_score'] = np.mean(f1_score)
            results_dictionary[folder]['accuracy_score'] = np.mean(accuracy_score)
            results_dictionary[folder]['precision_score_label'] = np.mean(precision_score_label)
            results_dictionary[folder]['recall_score_label'] = np.mean(recall_score_label)
            results_dictionary[folder]['f1_score_label'] = np.mean(f1_score_label)
            results_dictionary[folder]['accuracy_score_label'] = np.mean(accuracy_score_label)
            results_dictionary[folder]['count'] = len(precision_score)

        if not os.path.exists(directory):
            os.mkdir(directory)
        results_directory = str(directory) + 'results'
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)

        with open(str(results_directory) + '/results_dictionary.pickle', 'wb') as handle:
            pickle.dump(results_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open(str(results_directory) + '/results_dictionary.pickle', 'rb') as handle:
            results_dictionary_pickle = pickle.load(handle)

        print(results_dictionary_pickle == results_dictionary)

    return True

def medcpt_evaluation():
    pickle_dump_directory = "../dictionary_pickle_files/"
    directories = ["penntreebank_english/"]
    folders = ["berkeley", "hanlp", "corenlp", "allennlp"]
    sentences = [100]
    for d in range(0, len(directories)):
        dataset = directories[d]
        sentence_count = sentences[d]
        medcpt_directory = str(pickle_dump_directory) + str(dataset) + 'medcpt'
        with open(str(medcpt_directory) + '/medcpt_aggregate_clusters_dictionary_log.pickle', 'rb') as handle:
            medcpt_aggregate_clusters_dictionary = pickle.load(handle)
        ground_truth_pickle_path = str(pickle_dump_directory) + str(dataset) + str("ground_truth") + '/'
        with open(str(ground_truth_pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
            gt_unique_sentence_cluster_dictionary = pickle.load(handle)
        number_of_iterations = len(medcpt_aggregate_clusters_dictionary)
        medcpt_results_dictionary = {}
        for iteration in range(1, number_of_iterations+1):
            precision_score = []
            recall_score = []
            f1_score = []
            accuracy_score = []
            precision_score_label = []
            recall_score_label = []
            f1_score_label = []
            accuracy_score_label = []
            robinson_foulds_distance = []

            precision_score_label_weight = []
            recall_score_label_weight = []
            f1_score_label_weight = []
            accuracy_score_label_weight = []

            for k in range(1, sentence_count + 1):
                true_cluster = gt_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
                predict_cluster = medcpt_aggregate_clusters_dictionary[iteration][k]['medcpt_clusters']
                true_label = gt_unique_sentence_cluster_dictionary[k]['unique_pos_span']
                predict_label = medcpt_aggregate_clusters_dictionary[iteration][k]['mv_pos_aggregation']
                predict_label_weight = medcpt_aggregate_clusters_dictionary[iteration][k]['weight_pos_aggregation']
                true_error = gt_unique_sentence_cluster_dictionary[k]['error']
                predict_error = medcpt_aggregate_clusters_dictionary[iteration][k]['error']

                for clu in range(0, len(true_cluster)):
                    string = true_cluster[clu]
                    string = string.replace(" ", "")
                    true_cluster[clu] = string
                for clu in range(0, len(predict_cluster)):
                    string = predict_cluster[clu]
                    string = string.replace(" ", "")
                    predict_cluster[clu] = string

                if (true_error == False) and (predict_error == False):
                    evaluation_object = evaluation(true_cluster=true_cluster, predict_cluster=predict_cluster)
                    robinson_foulds_distance.append(
                        evaluation_object.robinson_foulds_distance(cluster1=true_cluster, cluster2=predict_cluster))
                    precision_score.append(
                        evaluation_object.precision_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    recall_score.append(
                        evaluation_object.recall_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    f1_score.append(
                        evaluation_object.f1_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    accuracy_score.append(
                        evaluation_object.accuracy_score(true_cluster=true_cluster, predict_cluster=predict_cluster))
                    precision_score_label.append(
                        evaluation_object.precision_score_label(true_cluster=true_cluster, true_label=true_label,
                                                                predict_cluster=predict_cluster,
                                                                predict_label=predict_label))
                    recall_score_label.append(
                        evaluation_object.recall_score_label(true_cluster=true_cluster, true_label=true_label,
                                                             predict_cluster=predict_cluster,
                                                             predict_label=predict_label))
                    f1_score_label.append(
                        evaluation_object.f1_score_label(true_cluster=true_cluster, true_label=true_label,
                                                         predict_cluster=predict_cluster,
                                                         predict_label=predict_label))
                    accuracy_score_label.append(
                        evaluation_object.accuracy_score_label(true_cluster=true_cluster, true_label=true_label,
                                                               predict_cluster=predict_cluster,
                                                               predict_label=predict_label))

                    precision_score_label_weight.append(
                        evaluation_object.precision_score_label(true_cluster=true_cluster, true_label=true_label,
                                                                predict_cluster=predict_cluster,
                                                                predict_label=predict_label_weight))
                    recall_score_label_weight.append(
                        evaluation_object.recall_score_label(true_cluster=true_cluster, true_label=true_label,
                                                             predict_cluster=predict_cluster,
                                                             predict_label=predict_label_weight))
                    f1_score_label_weight.append(
                        evaluation_object.f1_score_label(true_cluster=true_cluster, true_label=true_label,
                                                         predict_cluster=predict_cluster,
                                                         predict_label=predict_label_weight))
                    accuracy_score_label_weight.append(
                        evaluation_object.accuracy_score_label(true_cluster=true_cluster, true_label=true_label,
                                                               predict_cluster=predict_cluster,
                                                               predict_label=predict_label_weight))

            medcpt_results_dictionary[iteration] = {}
            medcpt_results_dictionary[iteration]['robinson_foulds_distance'] = np.sum(robinson_foulds_distance)
            medcpt_results_dictionary[iteration]['precision_score'] = np.mean(precision_score)
            medcpt_results_dictionary[iteration]['recall_score'] = np.mean(recall_score)
            medcpt_results_dictionary[iteration]['f1_score'] = np.mean(f1_score)
            medcpt_results_dictionary[iteration]['accuracy_score'] = np.mean(accuracy_score)
            medcpt_results_dictionary[iteration]['precision_score_label_mv'] = np.mean(precision_score_label)
            medcpt_results_dictionary[iteration]['recall_score_label_mv'] = np.mean(recall_score_label)
            medcpt_results_dictionary[iteration]['f1_score_label_mv'] = np.mean(f1_score_label)
            medcpt_results_dictionary[iteration]['accuracy_score_label_mv'] = np.mean(accuracy_score_label)
            medcpt_results_dictionary[iteration]['precision_score_label_weight'] = np.mean(precision_score_label_weight)
            medcpt_results_dictionary[iteration]['recall_score_label_weight'] = np.mean(recall_score_label_weight)
            medcpt_results_dictionary[iteration]['f1_score_label_weight'] = np.mean(f1_score_label_weight)
            medcpt_results_dictionary[iteration]['accuracy_score_label_weight'] = np.mean(accuracy_score_label_weight)
            medcpt_results_dictionary[iteration]['count'] = len(precision_score)

        if not os.path.exists(str(pickle_dump_directory) + str(dataset)):
            os.mkdir(str(pickle_dump_directory) + str(dataset))
        results_directory = str(str(pickle_dump_directory) + str(dataset)) + 'results'
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)

        with open(str(results_directory) + '/medcpt_results_dictionary_log.pickle', 'wb') as handle:
            pickle.dump(medcpt_results_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open(str(results_directory) + '/medcpt_results_dictionary_log.pickle', 'rb') as handle:
            medcpt_results_dictionary_pickle = pickle.load(handle)

        print(medcpt_results_dictionary_pickle == medcpt_results_dictionary)

    return True

def medcpt_pos_evaluation():
    pickle_dump_directory = "../dictionary_pickle_files/"
    directories = ["penntreebank_english/"]
    sentences = [100]
    for d in range(0, len(directories)):
        print("Dataset: " + str(directories[d]))
        dataset = directories[d]
        sentence_count = sentences[d]
        medcpt_directory = str(pickle_dump_directory) + str(dataset) + 'medcpt'
        with open(str(medcpt_directory) + '/medcpt_aggregate_labels_dictionary_log.pickle', 'rb') as handle:
            medcpt_aggregate_labels_dictionary = pickle.load(handle)
        ground_truth_pickle_path = str(pickle_dump_directory) + str(dataset) + str("ground_truth") + '/'
        with open(str(ground_truth_pickle_path) + '/unique_sentence_cluster_dictionary.pickle', 'rb') as handle:
            gt_unique_sentence_cluster_dictionary = pickle.load(handle)
        number_of_iterations = len(medcpt_aggregate_labels_dictionary)
        medcpt_pos_results_dictionary = {}
        for iteration in range(1, number_of_iterations+1):
            precision_score_label = []
            recall_score_label = []
            f1_score_label = []
            accuracy_score_label = []
            for k in range(1, sentence_count + 1):
                true_cluster = gt_unique_sentence_cluster_dictionary[k]['unique_cluster_span']
                predict_cluster = medcpt_aggregate_labels_dictionary[iteration][k]['medcpt_clusters']
                true_label = gt_unique_sentence_cluster_dictionary[k]['unique_pos_span']
                predict_label = medcpt_aggregate_labels_dictionary[iteration][k]['pos_aggregation']
                true_error = gt_unique_sentence_cluster_dictionary[k]['error']
                predict_error = medcpt_aggregate_labels_dictionary[iteration][k]['error']

                for clu in range(0, len(true_cluster)):
                    string = true_cluster[clu]
                    string = string.replace(" ", "")
                    true_cluster[clu] = string
                for clu in range(0, len(predict_cluster)):
                    string = predict_cluster[clu]
                    string = string.replace(" ", "")
                    predict_cluster[clu] = string

                if (true_error == False) and (predict_error == False):
                    evaluation_object = evaluation(true_cluster=true_cluster, predict_cluster=predict_cluster)

                    precision_score_label.append(
                        evaluation_object.precision_score_label(true_cluster=true_cluster, true_label=true_label,
                                                                predict_cluster=predict_cluster,
                                                                predict_label=predict_label))
                    recall_score_label.append(
                        evaluation_object.recall_score_label(true_cluster=true_cluster, true_label=true_label,
                                                             predict_cluster=predict_cluster,
                                                             predict_label=predict_label))
                    f1_score_label.append(
                        evaluation_object.f1_score_label(true_cluster=true_cluster, true_label=true_label,
                                                         predict_cluster=predict_cluster,
                                                         predict_label=predict_label))
                    accuracy_score_label.append(
                        evaluation_object.accuracy_score_label(true_cluster=true_cluster, true_label=true_label,
                                                               predict_cluster=predict_cluster,
                                                               predict_label=predict_label))
            medcpt_pos_results_dictionary[iteration] = {}
            medcpt_pos_results_dictionary[iteration]['precision_score'] = np.mean(precision_score_label)
            medcpt_pos_results_dictionary[iteration]['recall_score'] = np.mean(recall_score_label)
            medcpt_pos_results_dictionary[iteration]['f1_score'] = np.mean(f1_score_label)
            medcpt_pos_results_dictionary[iteration]['accuracy_score'] = np.mean(accuracy_score_label)

            print("Iteration: " + str(iteration) + " precision_score: " + str(np.mean(precision_score_label)) + " recall_score: " + str(np.mean(recall_score_label))
                  + " f1_score: " + str(np.mean(f1_score_label)) + " accuracy_score: " + str(np.mean(accuracy_score_label)))

        if not os.path.exists(str(pickle_dump_directory) + str(dataset)):
            os.mkdir(str(pickle_dump_directory) + str(dataset))
        results_directory = str(str(pickle_dump_directory) + str(dataset)) + 'results'
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)

        with open(str(results_directory) + '/medcpt_pos_results_dictionary_log.pickle', 'wb') as handle:
            pickle.dump(medcpt_pos_results_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open(str(results_directory) + '/medcpt_pos_results_dictionary_log.pickle', 'rb') as handle:
            medcpt_pos_results_dictionary_pickle = pickle.load(handle)

        print(medcpt_pos_results_dictionary_pickle == medcpt_pos_results_dictionary)
    return True



if __name__ == '__main__':
    run = baseline_evaluation()
    run1 = medcpt_evaluation()
    run2 = medcpt_pos_evaluation()
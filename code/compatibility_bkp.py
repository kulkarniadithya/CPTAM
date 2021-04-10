import numpy as np

class compatibility:
    def __init__(self, temp_cluster_array):
        self.temp_cluster_array = temp_cluster_array

    def get_character_cluster(self, cluster):
        characters_cluster = [char for char in cluster]
        boolean = False
        digit_span = 1
        formatted_character_cluster = []
        while boolean == False:
            updated_character_cluster = []
            counter = 0
            while (counter + digit_span) <= len(characters_cluster):
                for i in range(counter, len(characters_cluster)):
                    previous_character = ''
                    if counter != 0:
                        for j in range(counter - digit_span, counter):
                            previous_character = previous_character + characters_cluster[j]

                    updated_character = ''
                    for j in range(0, digit_span):
                        updated_character = updated_character + characters_cluster[i + j]
                    updated_character_cluster.append(updated_character)
                    counter = counter + digit_span
                    #print(updated_character)
                    if (counter + digit_span + 1) <= len(characters_cluster):
                        next_character = ''
                        for j in range(0, digit_span + 1):
                            next_character = next_character + characters_cluster[counter + j]

                        if (digit_span == 1) and (updated_character == '9') and (next_character == '10') and (
                                previous_character == '8'):
                            digit_span = digit_span + 1
                        elif (digit_span == 1) and (updated_character == '9') and (next_character == '10') and (
                                previous_character == ''):
                            digit_span = digit_span + 1
                        elif (digit_span == 2) and (updated_character == '99') and (next_character == '100') and (
                                previous_character == '98'):
                            digit_span = digit_span + 1
                        elif (digit_span == 2) and (updated_character == '99') and (next_character == '100') and (
                                previous_character == ''):
                            digit_span = digit_span + 1
                        elif (digit_span == 3) and (updated_character == '999') and (next_character == '1000') and (
                                previous_character == '998'):
                            digit_span = digit_span + 1
                        elif (digit_span == 3) and (updated_character == '999') and (next_character == '1000') and (
                                previous_character == ''):
                            digit_span = digit_span + 1
                        elif (digit_span == 4) and (updated_character == '9999'):
                            digit_span = digit_span + 1

                    break

            difference_array = []
            for i in range(0, len(updated_character_cluster) - 1):
                difference_array.append(int(updated_character_cluster[i + 1]) - int(updated_character_cluster[i]))
            for i in range(0, len(difference_array)):
                if difference_array[i] != 1:
                    digit_span = digit_span + 1
                    boolean = False
                    break
                else:
                    boolean = True

            if boolean == True:
                formatted_character_cluster = updated_character_cluster

        return formatted_character_cluster

    def check_cluster_compatibility(self, temp_cluster_array):
        compatible_boolean = []
        appended_cluster_array = [''] * len(temp_cluster_array)
        for i in range(0, len(temp_cluster_array)):
            appended_cluster_array[i] = str(temp_cluster_array[i]).replace(' ', '')

        for i in range(0, len(appended_cluster_array)):
            compatible_boolean_cluster = []
            for j in range(0, len(appended_cluster_array)):
                characters = [char for char in appended_cluster_array[j]]
                characters_i = [char for char in appended_cluster_array[i]]
                if (appended_cluster_array[j] in appended_cluster_array[i]) or (
                        appended_cluster_array[i] in appended_cluster_array[j]):
                    compatible_boolean_cluster.append(True)
                elif (len(characters_i) <= 3) or (len(characters) <= 3):
                    compatible_boolean_cluster.append(True)
                else:
                    # print("In")
                    # print(appended_cluster_array[i])
                    # print(appended_cluster_array[j])
                    first_array = self.get_character_cluster(appended_cluster_array[i])
                    #print(first_array)
                    second_array = self.get_character_cluster(appended_cluster_array[j])
                    #print(second_array)
                    independent_boolean = True

                    for a in range(0, len(second_array)):
                        if second_array[a] in first_array:
                            independent_boolean = False
                            break
                    compatible_boolean_cluster.append(independent_boolean)
            compatible_boolean.append(compatible_boolean_cluster)

        return compatible_boolean

    def compatible_cluster_index(self, temp_cluster_array):
        compatibility_matrix = self.check_cluster_compatibility(temp_cluster_array=temp_cluster_array)
        #print(compatibility_matrix)
        incompatible_clusters_count = []

        for i in range(0, len(compatibility_matrix)):
            if False not in compatibility_matrix[i]:
                incompatible_clusters_count.append(0)
            else:
                count_false = 0
                for j in range(0, len(compatibility_matrix[i])):
                    if compatibility_matrix[i][j] == False:
                        count_false = count_false + 1
                incompatible_clusters_count.append(count_false)

        compatible_cluster_index = []

        incompatible_count = 0
        max_incompatible_count = np.max(incompatible_clusters_count)

        while incompatible_count <= max_incompatible_count:
            for i in range(0, len(incompatible_clusters_count)):
                if incompatible_clusters_count[i] == incompatible_count:
                    if incompatible_count == 0:
                        if i not in compatible_cluster_index:
                            compatible_cluster_index.append(i)
                    else:
                        for j in range(0, len(compatibility_matrix[i])):
                            if compatibility_matrix[i][j] == False:
                                if (j not in compatible_cluster_index) and (i not in compatible_cluster_index):
                                    compatible_cluster_index.append(i)

            incompatible_count = incompatible_count + 1

        return compatible_cluster_index

# if __name__ == '__main__':
#     temp_cluster_array = ['123 45678 9 1011121314 15161718192021 222324 25262728293031323334 3536373839 4041424344 4546 47484950515253 54 555657 585960 616263646566 6768 69 707172737475 7677 78798081828384 8586 8788 8990919293949596 9798 99100101102103104105 106 107108109 110111112113114 115116117 118', '555657 585960 616263646566 6768 69 707172737475 7677 78798081828384 8586 8788 8990919293949596 9798 99100101102103104105 106 107108109 110111112113114 115116117', '585960 616263646566 6768 69 707172737475 7677 78798081828384 8586 8788 8990919293949596 9798 99100101102103104105 106 107108109 110111112113114 115116117', '6768 69 707172737475 7677 78798081828384', '69 707172737475 7677 78798081828384', '7677 78798081828384', '8586 8788 8990919293949596 9798 99100101102103104105 106 107108109 110111112113114 115116117', '8788 8990919293949596 9798 99100101102103104105 106 107108109 110111112113114 115116117', '99100101102103104105']
#     compatibility_object = compatibility(temp_cluster_array=temp_cluster_array)
#     compatible_cluster_index = compatibility_object.compatible_cluster_index(temp_cluster_array=temp_cluster_array)
#     print(compatible_cluster_index)
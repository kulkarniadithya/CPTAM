import re
import string
import random
letters = string.ascii_lowercase
class pre_format_hanlp_parsed_sentence:
    def __init__(self, hanlp_parsed_sentence, language):
        self.original_hanlp_parsed_sentence = hanlp_parsed_sentence
        self.language = language

    def remove_quotes_comma(self, hanlp_parsed_sentence):
        hanlp_characters = [char for char in hanlp_parsed_sentence]

        change = 1
        index = 0
        while change > 0:
            change = 0
            for i in range(index, len(hanlp_characters)):
                if hanlp_characters[i] == "\'":
                    hanlp_characters.pop(i)
                    change = 1
                    index = i
                    break

        change = 1
        index = 0
        while change > 0:
            change = 0
            for i in range(index, len(hanlp_characters)-1):
                if (hanlp_characters[i] == ",") and (hanlp_characters[i+1] == " "):
                    hanlp_characters.pop(i)
                    change = 1
                    index = i
                    break

        return ''.join(hanlp_characters)

    def remove_brackets_around_tokens(self, hanlp_parsed_sentence):
        hanlp_characters = [char for char in hanlp_parsed_sentence]
        special_characters = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\',
                              '{', '}', '\"', "\'", ';', ':', '?', '/', '`', '~', '—', '．', '／', '、', '，', '。', '「', '」', '！', '；', '？', '、', '二', '《', '》', '：',
                              '（', '）', '…', '三', '○', '『',  '』', '□', '〉', '〈', '∶', '＆', '@ ', '# ', '$ ', '% ', '^ ', '& ', '* ', '- ', '_ ', '+ ', '= ', '| ', '{ ', '} ', '\" ', "\' ",
                              '／ ', '－', '＝', '＞', '＜', '｛', '｝', '［', '］', '｀', '＋', '＂', '＝', '／', '，', '．', '·', '％', '＊', '“', '”', '×', '，', '＄', '【', '】', '｜', '：', '．', '＠',
                              '＿', '－', '‘', '’', '”', '／', '＇', '"', '<', '=', '～', '，', '（', '）', '•', '◆', '．','※', '●', '■', '<', '>', '，', '―', '／', '＾', '＿', '一',
                              '＼', '／', '＃', '，', '。', 'o', '–', ',', '_', '.', '一', '¿½', '¿', '½', '°']

        for i in range(0, len(hanlp_characters)):
            if hanlp_characters[i] in special_characters:
                hanlp_characters[i] = random.choice(letters)

        formatted_sentence = ''.join(hanlp_characters)

        pos = re.findall("\[\w+ ", formatted_sentence)
        tokens = re.findall("\[\w+.\]", formatted_sentence)

        formatted_tokens = [''] * len(tokens)
        for i in range(0, len(tokens)):
            formatted_tokens[i] = str(tokens[i]).replace('[', '')
            formatted_tokens[i] = str(formatted_tokens[i]).replace(']]', ']')

        for i in range(0, len(tokens)):
            formatted_sentence = formatted_sentence.replace(tokens[i], formatted_tokens[i], 1)

        formatted_sentence = formatted_sentence.replace("PU [[]", "PU s")
        formatted_sentence = formatted_sentence.replace("PU []]", "PU s")
        formatted_sentence = formatted_sentence.replace("PU []", "PU s")

        return formatted_sentence

    def pre_format_sentence(self, hanlp_parsed_sentence):
        hanlp_parsed_sentence_wqc = self.remove_quotes_comma(hanlp_parsed_sentence=hanlp_parsed_sentence)
        formatted_sentence = self.remove_brackets_around_tokens(hanlp_parsed_sentence=hanlp_parsed_sentence_wqc)
        hanlp_characters = [char for char in formatted_sentence]
        hanlp_brackets = []
        hanlp_brackets_index = []

        for j in range(0, len(hanlp_characters)):
            if hanlp_characters[j] in ['[', ']']:
                hanlp_brackets.append(hanlp_characters[j])
                hanlp_brackets_index.append(j)

        cluster_bracket_index = []

        brackets_array = hanlp_brackets
        brackets_index_array = hanlp_brackets_index

        current_length_bracket_array = len(brackets_array)
        previous_length_bracket_array = 0
        while len(brackets_array) > 0:
            previous_length_bracket_array = current_length_bracket_array
            for i in range(0, len(brackets_array) - 1):
                if brackets_array[i] == '[' and brackets_array[i + 1] == ']':
                    cluster_bracket = []
                    cluster_bracket.append(brackets_index_array[i])
                    cluster_bracket.append(brackets_index_array[i + 1])
                    cluster_bracket_index.append(cluster_bracket)
                    brackets_array.pop(i)
                    brackets_array.pop(i)
                    brackets_index_array.pop(i)
                    brackets_index_array.pop(i)
                    break
                else:
                    continue
            current_length_bracket_array = len(brackets_array)
            if previous_length_bracket_array == current_length_bracket_array:
                if len(brackets_array) > 0:
                    raise Exception("Invalid number of brackets")
                break

        index_to_remove = []
        for i in range(0, len(hanlp_characters) - 2):
            if (hanlp_characters[i] == " ") and (hanlp_characters[i + 1] == "[") and (hanlp_characters[i + 2] == "["):
                index_to_remove.append(i + 1)

        brackets_to_remove = []

        change = 1
        index = 0
        while change > 0:
            change = 0
            for i in range(index, len(cluster_bracket_index)):
                if cluster_bracket_index[i][0] in index_to_remove:
                    brackets_to_remove.append(cluster_bracket_index[i])
                    change = 1
                    index = i + 1
                    break

        character_index_to_remove = []
        for i in range(0, len(brackets_to_remove)):
            character_index_to_remove.append(brackets_to_remove[i][0])
            character_index_to_remove.append(brackets_to_remove[i][1])

        character_index_to_remove.append(0)
        character_index_to_remove.append(len(hanlp_characters) - 1)

        after_removal_characters = []
        for i in range(0, len(hanlp_characters)):
            if i not in character_index_to_remove:
                after_removal_characters.append(hanlp_characters[i])

        for i in range(0, len(after_removal_characters)):
            if after_removal_characters[i] == '[':
                after_removal_characters[i] = '('
            elif after_removal_characters[i] == ']':
                after_removal_characters[i] = ')'

        return ''.join(after_removal_characters)
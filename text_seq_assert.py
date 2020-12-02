from hparams import hparams
from tacotron.utils.text import text_to_sequence
from tacotron.utils.text import sequence_to_text

cleaner_names = [x.strip() for x in hparams.cleaners.split(',')]
print('strange cleaner_names:', cleaner_names)

def reverse_equal_original(text):
    print('text:', text, 'len:', len(text))
    seq_text = text_to_sequence(text, cleaner_names)
    print('seq text:', seq_text, 'len:', len(seq_text))
    textReverse_seq_text = sequence_to_text(seq_text)
    print('textReverse_seq_txt:', textReverse_seq_text, 'len:', len(textReverse_seq_text))
    if len(textReverse_seq_text) - 1 != len(text) or textReverse_seq_text[-1] != '~':
        return False
    if len(text) != len(seq_text) - 1:
        return False
    return True
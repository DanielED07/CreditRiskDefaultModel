LABEL_CATEGORY = [
    (0, ['Fully Paid', 'Does not meet the credit policy. Status:Fully Paid', 'Current']),
    (1, ['Late (31-120 days)', 'Late (16-30 days)', 'In Grace Period', 'Issued',
         'Charged Off', 'Default', 'Does not meet the credit policy. Status:Charged Off'])
]

def classify_label(text):
    for category, matches in LABEL_CATEGORY:
        if any(match in text for match in matches):
            return category
    return None
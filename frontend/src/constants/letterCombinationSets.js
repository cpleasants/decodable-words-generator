const letterCombinationSets = {
    "Common Digraphs": ['ck', 'sh', 'th', 'ch', 'wh', 'qu'],

    "Blends 1": ['bl-', 'cl-', 'fl-', 'gl-', 'pl-', 'sl-'],
    "Blends 2": ['br-', 'cr-', 'dr-', 'fr-', 'gr-', 'pr-', 'tr-'],
    "Blends 3": ['sc-', 'shr-', 'sk-', 'sm-', 'sn-', 'sp-', 'squ-', 'st-', 'sw-'],
    "Blends 4": ['ay', 'ow', 'oy'],

    "Suffixes 1": ['-lp', '-st', '-ct', '-pt', '-sk', '-lk', '-lf', '-xt', '-ft', '-nd', '-mp', '-lt', '-nch'],
    "Suffixes 2": ['-ing', '-ang', '-ong', '-ung', '-ank', '-ink', '-onk', '-unk'],
    "Suffixes 3": ['-ild', '-old', '-ind', '-olt', '-ost'],

    "Other": ['wr-', 'kn-', 'ph-', 'gh-', 'gn-', '-mb', '-tch', '-dge']
};

export default letterCombinationSets;

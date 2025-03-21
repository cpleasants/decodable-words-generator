// app.js


const letter_sets = [
    ['m', 's', 'r', 't', 'n', 'p', 'o', 'c', 'a', 'd'],
    ['g', 'f', 'b', 'k', 'i', 'l', 'h', 'w'],
    ['e', 'v', 'j', 'u', 'y', 'z', 'x', 'q'],
]

const digraph_sets = [
    ['ck', 'sh', 'th', 'ch', 'wh', 'qu'],
]

const blend_sets = [
    ['bl-', 'cl-', 'fl-', 'gl-', 'pl-', 'sl-'],
    ['br-', 'cr-', 'dr-', 'fr-', 'gr-', 'pr-', 'tr-'],
    ['sc-', 'shr-', 'sk-', 'sm-', 'sn-', 'sp-', 'squ-', 'st-', 'sw-'],
    ['ay', 'ow', 'oy'],
]

const suffix_sets = [
    ['-lp', '-st', '-ct', '-pt', '-sk', '-lk', '-lf', '-xt', '-ft', '-nd', '-mp', '-st', '-lt', '-nch'],
    ['-ing', '-ang', '-ong', '-ung', '-ank', '-ink', '-onk', '-unk'],
    ['-ild', '-old', '-ind', '-olt', '-ost'],
]

const other_sets = [
    ['wr-', 'kn-', 'ph-', 'gh-', 'gn-', '-mb', '-tch', '-dge']
]

const vowel_team_sets = [
    list(utils.vowel_teams.values())
]

// Sample letters list for checkboxes
const letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

// Function to create checkboxes
function createCheckboxes(letterList) {
    const container = document.getElementById('checkbox-container');
    container.innerHTML = ''; // Clear any existing checkboxes

    letterList.forEach(letter => {
        const checkboxDiv = document.createElement('div');
        checkboxDiv.classList.add('checkbox-item');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = letter;
        checkbox.name = 'letters';

        const label = document.createElement('label');
        label.setAttribute('for', letter);
        label.textContent = letter.toUpperCase();

        checkboxDiv.appendChild(checkbox);
        checkboxDiv.appendChild(label);

        container.appendChild(checkboxDiv);
    });
}

// Function to handle form submission or process selected checkboxes
function handleSubmit() {
    const selectedCheckboxes = Array.from(document.querySelectorAll('input[type="checkbox"]:checked')).map(checkbox => checkbox.id);
    alert('Selected letters: ' + selectedCheckboxes.join(', '));
}

// Event listener to handle form submission
document.getElementById('submit-btn').addEventListener('click', handleSubmit);

// Initialize the app by creating checkboxes
function initApp() {
    createCheckboxes(letters);
}

// Call initApp when the page is loaded
window.onload = initApp;
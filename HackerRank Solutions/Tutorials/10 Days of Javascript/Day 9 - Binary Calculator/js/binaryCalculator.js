const handleButtonClick = event => {
    const button = event.target || event.srcElement;
    const action = document.getElementById(button.id).innerHTML;
    const res = document.getElementById('res');
    switch(action) {
        case 'C':
            res.innerHTML = '';
            break;
        case '=':
            var expr = res.innerHTML;
            var nums = /(\d+)/g;
            // Replace all base 2 nums with base 10 equivs
            expr = expr.replace(nums, function(match) {
                return parseInt(match, 2);
            })
            // eval in base 10 and convert to base 2
            res.innerHTML = eval(expr).toString(2);
            break;
        default:
            res.innerHTML += action;
            break;
    }
};
const buttons = document.getElementsByTagName('button');
for (let button of buttons) {
    button.addEventListener('click', handleButtonClick);
}
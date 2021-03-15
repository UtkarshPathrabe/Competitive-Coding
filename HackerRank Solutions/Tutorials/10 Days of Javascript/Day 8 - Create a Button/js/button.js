const btnNode = document.querySelector('#btn');
let count = 0;
btnNode.innerHTML = count;
btnNode.addEventListener('click', (event) => {
    count++;
    btnNode.innerHTML = count;
});
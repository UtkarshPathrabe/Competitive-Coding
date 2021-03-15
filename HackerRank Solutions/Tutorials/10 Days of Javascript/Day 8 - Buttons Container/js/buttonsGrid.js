const nums = [1, 2, 3, 6, 9, 8, 7, 4];
const ids = [1, 2, 3, 6, 9, 8, 7, 4];
const btn5Node = document.querySelector('#btn5');
btn5Node.addEventListener('click', (event) => {
    event.preventDefault();
    nums.unshift(nums.pop());
    for (let i = 0; i < 8; i++) {
        document.getElementById('btn' + ids[i]).innerHTML = nums[i];
    }
});
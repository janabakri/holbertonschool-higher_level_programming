document.addEventListener('DOMContentLoaded', function () {
  const list = document.querySelector('.my_list');

  document.querySelector('#add_item').addEventListener('click', function () {
    const item = document.createElement('li');

    item.textContent = 'Item';
    list.appendChild(item);
  });

  document.querySelector('#remove_item').addEventListener('click', function () {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function () {
    list.innerHTML = '';
  });
});

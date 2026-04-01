document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#btn_translate').addEventListener('click', function () {
    const langCode = document.querySelector('#language_code').value;

    if (!langCode) {
      return;
    }

    fetch('https://hellosalut.stefanbohacek.com/?lang=' + langCode)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        document.querySelector('#hello').textContent = data.hello;
      });
  });
});

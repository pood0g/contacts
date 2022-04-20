// pops the modal for the delete confirmation dialogue
function modalPopup(url) {

  var xhr = new XMLHttpRequest;

  xhr.onload = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.querySelector("#modal_content").innerHTML = xhr.response;
      bootstrap.Modal.getOrCreateInstance(document.querySelector("#modal_div")).show();
      addValidators();
    }
  }

  xhr.open("GET", url);
  xhr.send();
}
// creates a xhr post request, updates modal content if not redirected.
function modalPostRequest(url) {

  var xhr = new XMLHttpRequest;
  var formData = new FormData(document.querySelector('#modal_form'));

  xhr.onload = function () {
    if (this.responseURL.endsWith(url)) {
      document.querySelector('#modal_content').innerHTML = xhr.response;
      addValidators();
      dismissAlerts()
    } else document.location = this.responseURL;
  }

  xhr.open('POST', url);
  xhr.send(formData)
}

// Auto dismiss alerts
function dismissAlerts() {
  setTimeout(function () {
    let alertElement = document.querySelector(".alert");
    if (alertElement)
      bootstrap.Alert.getOrCreateInstance(alertElement).close()
  }, 10000);
}

// validates the form on clicking submit from bootstrap help docs
function addValidators() {
  'use strict'

  var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
}

function passwordsMatch() {
  var password1 = document.querySelector("input[name='password1']")
  var password2 = document.querySelector("input[name='password2']")
  password2.setCustomValidity((password1.value == password2.value && password1.validity.valid) ? "" : "Passwords must match")
}

/* 
this is an overly simplicated search feature, could use some improvements
perhaps in the future I will implement pagination aswell possibly switch to
loading the table as json and rendering with javascript
*/
function searchBar(needle, tableID) {
  let table = document.querySelector(`#${tableID}`);
  var row = table.getElementsByTagName('tr');

  for (let i = 1; i < row.length; i++) {
    let haystack = '';
    let column = row[i].getElementsByTagName('td');

    for (let j = 0; j < column.length; j++) {
      haystack += ` ${column[j].innerText.toLowerCase()}`;
      console.log(haystack);
    }
    row[i].style.display = (haystack.search(needle.toLowerCase()) > -1) ? "" : "none";
  }
}
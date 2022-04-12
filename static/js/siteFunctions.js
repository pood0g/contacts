// pops the modal for the delete confirmation dialogue, check if vulnerable to XSS?
function modalPopup(url, slug) {

    var xhr = new XMLHttpRequest;

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            document.querySelector("#modal_body").innerHTML = xhr.response;
            bootstrap.Modal.getOrCreateInstance(document.querySelector("#modal_div")).show();
            addValidators();
        }
    }

    url = (slug) ? `${url}${slug}` : `${url}`
    xhr.open("GET", url, true);
    xhr.send();
}

// Auto dismiss alerts
setTimeout(function () {
    let alertElement = document.querySelector(".alert");
    if (alertElement)
        bootstrap.Alert.getOrCreateInstance(alertElement).close()
}, 10000);

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
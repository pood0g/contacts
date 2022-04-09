// pops the modal for the delete confirmation dialogue, check if vulnerable to XSS?
function modalPopup(id) {
    id = Number(id);

    var xhr = new XMLHttpRequest;

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            document.querySelector("#modal_body").innerHTML = xhr.response;
        }
    }

    xhr.open("GET", `/delete/${id}/`, true);
    xhr.send();

    bootstrap.Modal.getOrCreateInstance(document.querySelector("#modal_div")).show();

}

// Auto dismiss alerts
setTimeout(function () {
    let alertElement = document.querySelector(".alert");
    if (alertElement)
        bootstrap.Alert.getOrCreateInstance(alertElement).close()
}, 10000);
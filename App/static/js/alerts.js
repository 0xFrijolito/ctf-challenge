function createAlert(type, message, id="alerts_container") {
    const alertContainer = document.getElementById(id);
    const alert = document.createElement('div');
    alert.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('');

    if (alertContainer.childElementCount == 0) {
        alertContainer.append(alert);
    } else {
        alertContainer[0] = alert;
    }
}
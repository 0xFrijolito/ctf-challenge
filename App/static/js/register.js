const form = document.getElementById("form");
const alertContainer = document.getElementById("alerts_container");

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

form.onsubmit = async function (e) {
    e.preventDefault()

    const creds = {
        username: e.target[0].value,
        email: e.target[1].value,
        password: e.target[2].value
    }

    const res  = await fetch ("/api/register",{method: "POST", headers: {"content-type": "application/json"},body: JSON.stringify(creds)});
    const data = await res.json();
    
    if (res.status == 200) {
        createAlert("success", data.message);
    } else {
        createAlert("danger", data.message);
    }
}
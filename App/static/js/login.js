const form = document.getElementById("form");
form.onsubmit = async function (e) {
    e.preventDefault()

    const creds = {
        email: e.target[0].value,
        password: e.target[1].value
    }

    const res  = await fetch ("/api/login",{method: "POST", headers: {"content-type": "application/json"},body: JSON.stringify(creds)});
    const data = await res.json();
    
    if (res.status == 200) {
        document.cookie   = "session=" + data.message.jwt + "; expires=Sun, 1 Jan 2023 00:00:00 UTC; path=/";
        localStorage.setItem("username", data.message.data.username);
        localStorage.setItem("wallet", data.message.data.wallet);
        localStorage.setItem("balance", data.message.data.balance);

        document.location = "/dashboard"
    } else {
        createAlert("danger", data.message);
    }
}
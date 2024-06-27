var get = document.getElementById('get')
var inp = document.getElementById('pieces')
var free = document.getElementById("pcs").innerHTML

if (parseInt(free) < 1){
    window.location.replace('http://localhost:8080/no_tickets')
}

get.onclick =
function sendData() {
    var buy = document.getElementById('pieces').value
    var data = buy;
    if (buy < 7 && buy > 0 && buy <= free) {
    fetch('/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => {
        console.error('Error:', error);
    });
    window.location.replace('http://localhost:8080/success')
    }
    else{
        alert('Adjon meg egy érvényes darabszámot (1-6 közé esőt, max. annyit, amennyi elérhető!)!')
        document.getElementById('pieces').value = ''
    }
}

inp.onchange = 
function changeText(){
    document.getElementById('ossz').innerHTML = document.getElementById('egy').innerHTML * document.getElementById('pieces').value
}

inp.oninput = 
function changeText(){
    document.getElementById('ossz').innerHTML = document.getElementById('egy').innerHTML * document.getElementById('pieces').value
}

localStorage.clear()